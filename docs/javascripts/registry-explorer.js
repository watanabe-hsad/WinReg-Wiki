(function () {
  const escapeHtml = (value) =>
    String(value ?? "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");

  const normalize = (value) => String(value ?? "").toLowerCase().trim();

  const focusSiteSearch = () => {
    const toggle = document.getElementById("__search");
    if (toggle) {
      toggle.checked = true;
    }

    const input =
      document.querySelector('[data-md-component="search-query"]') ||
      document.querySelector(".md-search__input");

    if (input) {
      window.setTimeout(() => input.focus(), 40);
    }
  };

  const bindSearchTriggers = () => {
    document.querySelectorAll("[data-ww-search-trigger]").forEach((trigger) => {
      trigger.addEventListener("click", (event) => {
        event.preventDefault();
        focusSiteSearch();
      });
    });

    document.addEventListener("keydown", (event) => {
      const target = event.target;
      const isEditable =
        target instanceof HTMLInputElement ||
        target instanceof HTMLTextAreaElement ||
        target instanceof HTMLSelectElement ||
        target?.isContentEditable;

      if (!isEditable && event.key === "/") {
        event.preventDefault();
        focusSiteSearch();
      }
    });
  };

  const badge = (value, type = "") => {
    if (!value) return "";
    const klass = type ? ` ww-chip--${type}` : "";
    return `<span class="ww-chip${klass}">${escapeHtml(value)}</span>`;
  };

  const pathPill = (value) =>
    `<span class="ww-path-pill" title="${escapeHtml(value)}">${escapeHtml(value)}</span>`;

  const shortPathLabel = (entry) => {
    const firstPath = (entry.native_paths || [])[0] || entry.title || "";
    const parts = String(firstPath)
      .split("\\")
      .map((part) => part.trim())
      .filter(Boolean);
    if (!parts.length) return entry.title || "Registry Entry";

    const last = parts[parts.length - 1];
    const prev = parts[parts.length - 2];
    const generic = new Set(["Run", "Interfaces", "Parameters", "CurrentVersion"]);
    if (prev && generic.has(last)) return `${prev}\\${last}`;
    return last;
  };

  const card = (entry) => {
    const paths = (entry.native_paths || []).slice(0, 1).map(pathPill).join("");
    const topics = (entry.topics || [])
      .slice(0, 2)
      .map((topic) => badge(topic, "topic"))
      .join("");
    const scenarios = (entry.related_scenarios || [])
      .slice(0, 2)
      .map((scenario) => badge(scenario, "scenario"))
      .join("");
    const href = entry.page_url || "#";

    return `
      <article class="ww-explorer-card">
        <div class="ww-explorer-card__top">
          <div class="ww-explorer-card__title">
            <h2>${escapeHtml(shortPathLabel(entry))}</h2>
            <span>${escapeHtml(entry.hive || "-")}</span>
          </div>
          <div class="ww-explorer-card__badges">
            ${badge(entry.root, "hive")}
            ${badge(entry.status, "status")}
          </div>
        </div>
        <div class="ww-explorer-card__paths">${paths}</div>
        <p>${escapeHtml(entry.summary || "暂无摘要。")}</p>
        <div class="ww-card-chips">${topics}${scenarios}</div>
        <a class="ww-card-link" href="${escapeHtml(href)}">Open →</a>
      </article>
    `;
  };

  const emptyState = () => `
    <div class="ww-empty-state">
      <strong>没有匹配结果</strong>
      <span>调整关键词、Hive、主题或状态筛选。</span>
    </div>
  `;

  const updateStats = (root, data) => {
    const stats = root.querySelector("[data-registry-stats]");
    if (!stats || !data.meta) return;

    const entries = data.entries || [];
    const roots = data.meta.roots || [];
    const topics = data.meta.topics || [];
    const scenarios = data.meta.scenarios || [];

    stats.innerHTML = `
      <div class="ww-stat-card"><strong>${entries.length}</strong><span>entries</span></div>
      <div class="ww-stat-card"><strong>${roots.length}</strong><span>hives</span></div>
      <div class="ww-stat-card"><strong>${topics.length}</strong><span>topics</span></div>
      <div class="ww-stat-card"><strong>${scenarios.length}</strong><span>scenarios</span></div>
    `;
  };

  const initExplorer = async () => {
    const root = document.querySelector("[data-registry-explorer]");
    if (!root) return;

    const results = root.querySelector("[data-registry-results]");
    const count = root.querySelector("[data-registry-count]");
    const search = root.querySelector("[data-registry-search]");
    const filters = { root: "", topic: "", status: "" };

    const dataUrl = root.getAttribute("data-registry-json") || "../../assets/registry-index.json";
    let entries = [];

    try {
      const response = await fetch(dataUrl, { credentials: "same-origin" });
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }
      const data = await response.json();
      entries = data.entries || [];
      updateStats(root, data);
    } catch (error) {
      if (count) count.textContent = "Registry data could not be loaded.";
      if (results) {
        results.innerHTML = `
          <div class="ww-empty-state">
            <strong>无法加载 registry-index.json</strong>
            <span>请使用结构化索引或覆盖矩阵继续浏览。</span>
            <a class="ww-card-link" href="generated-index.md">Open structured index →</a>
          </div>
        `;
      }
      return;
    }

    const matchesQuery = (entry, query) => {
      if (!query) return true;
      const haystack = [
        entry.title,
        entry.summary,
        entry.root,
        entry.hive,
        entry.category,
        entry.status,
        ...(entry.native_paths || []),
        ...(entry.topics || []),
        ...(entry.related_scenarios || []),
        ...(entry.values || []),
        ...(entry.tools || []),
      ]
        .map(normalize)
        .join(" ");
      return haystack.includes(query);
    };

    const applyFilters = () => {
      const query = normalize(search?.value || "");
      const filtered = entries.filter((entry) => {
        const rootOk = !filters.root || entry.root === filters.root;
        const topicOk = !filters.topic || (entry.topics || []).includes(filters.topic);
        const statusOk = !filters.status || entry.status === filters.status;
        return rootOk && topicOk && statusOk && matchesQuery(entry, query);
      });

      if (count) {
        count.textContent = `${filtered.length} of ${entries.length} registry entries`;
      }
      if (results) {
        results.innerHTML = filtered.length ? filtered.map(card).join("") : emptyState();
      }
    };

    root.querySelectorAll("[data-filter-type]").forEach((button) => {
      button.addEventListener("click", () => {
        const type = button.getAttribute("data-filter-type");
        if (!type) return;

        filters[type] = button.getAttribute("data-filter-value") || "";
        root
          .querySelectorAll(`[data-filter-type="${CSS.escape(type)}"]`)
          .forEach((peer) => peer.classList.toggle("is-active", peer === button));
        applyFilters();
      });
    });

    if (search) {
      search.addEventListener("input", applyFilters);
    }

    applyFilters();
  };

  document.addEventListener("DOMContentLoaded", () => {
    bindSearchTriggers();
    initExplorer();
  });
})();
