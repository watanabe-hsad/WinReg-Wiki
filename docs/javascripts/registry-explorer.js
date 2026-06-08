(function () {
  const escapeHtml = (value) =>
    String(value ?? "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");

  const normalize = (value) => String(value ?? "").toLowerCase().trim();
  const collator = new Intl.Collator(["zh-Hans", "en"], {
    numeric: true,
    sensitivity: "base",
  });

  const SORT_OPTIONS = new Set(["path", "hive", "topic", "status"]);
  const GROUP_OPTIONS = new Set(["", "root", "hive", "topic", "status"]);
  const STATUS_RANK = { stable: 0, reviewed: 1, draft: 2 };
  const GROUP_LABELS = {
    root: "Root hive",
    hive: "Offline hive",
    topic: "Topic",
    status: "Status",
  };

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

  const firstPath = (entry) => (entry.native_paths || [])[0] || entry.title || "";
  const primaryTopic = (entry) => (entry.topics || [])[0] || "未分类";

  const shortPathLabel = (entry) => {
    const parts = String(firstPath(entry))
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

  const groupHeading = (label, items) => `
    <div class="ww-explorer-group__heading">
      <h2>${escapeHtml(label)}</h2>
      <span>${items.length} entries</span>
    </div>
  `;

  const groupKey = (entry, type, selectedTopic = "") => {
    if (type === "root") return entry.root || "Unknown";
    if (type === "hive") return entry.hive || "Unknown";
    if (type === "topic" && selectedTopic && (entry.topics || []).includes(selectedTopic)) {
      return selectedTopic;
    }
    if (type === "topic") return primaryTopic(entry);
    if (type === "status") return entry.status || "draft";
    return "";
  };

  const sortEntries = (entries, sortBy) => {
    const sorted = [...entries];
    const byPath = (a, b) => collator.compare(firstPath(a), firstPath(b));

    sorted.sort((a, b) => {
      if (sortBy === "hive") {
        return collator.compare(a.hive || "", b.hive || "") || byPath(a, b);
      }
      if (sortBy === "topic") {
        return collator.compare(primaryTopic(a), primaryTopic(b)) || byPath(a, b);
      }
      if (sortBy === "status") {
        const rankA = STATUS_RANK[a.status] ?? 99;
        const rankB = STATUS_RANK[b.status] ?? 99;
        return rankA - rankB || byPath(a, b);
      }
      return byPath(a, b);
    });

    return sorted;
  };

  const renderEntries = (entries, groupBy, selectedTopic = "") => {
    if (!entries.length) return emptyState();
    if (!groupBy) return entries.map(card).join("");

    const groups = new Map();
    entries.forEach((entry) => {
      const key = groupKey(entry, groupBy, selectedTopic);
      if (!groups.has(key)) groups.set(key, []);
      groups.get(key).push(entry);
    });

    return [...groups.entries()]
      .sort(([a], [b]) => collator.compare(a, b))
      .map(
        ([label, items]) => `
          <section class="ww-explorer-group">
            ${groupHeading(label, items)}
            <div class="ww-explorer-group__grid">
              ${items.map(card).join("")}
            </div>
          </section>
        `
      )
      .join("");
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
    const sort = root.querySelector("[data-registry-sort]");
    const group = root.querySelector("[data-registry-group]");
    const reset = root.querySelector("[data-registry-reset]");
    const copyLink = root.querySelector("[data-registry-copy-link]");
    const state = { root: "", topic: "", status: "", query: "", sort: "path", group: "" };

    const dataUrl = root.getAttribute("data-registry-json") || "../../assets/registry-index.json";
    let entries = [];

    const setActiveFilter = (type, value) => {
      root.querySelectorAll(`[data-filter-type="${CSS.escape(type)}"]`).forEach((button) => {
        button.classList.toggle("is-active", (button.getAttribute("data-filter-value") || "") === value);
      });
    };

    const readUrlState = () => {
      const params = new URLSearchParams(window.location.search);
      state.query = params.get("q") || "";
      state.root = params.get("root") || "";
      state.topic = params.get("topic") || "";
      state.status = params.get("status") || "";
      state.sort = SORT_OPTIONS.has(params.get("sort")) ? params.get("sort") : "path";
      state.group = GROUP_OPTIONS.has(params.get("group")) ? params.get("group") : "";
    };

    const syncControls = () => {
      if (search) search.value = state.query;
      if (sort) sort.value = state.sort;
      if (group) group.value = state.group;
      setActiveFilter("root", state.root);
      setActiveFilter("topic", state.topic);
      setActiveFilter("status", state.status);
    };

    const writeUrlState = () => {
      const url = new URL(window.location.href);
      const values = {
        q: state.query,
        root: state.root,
        topic: state.topic,
        status: state.status,
        sort: state.sort === "path" ? "" : state.sort,
        group: state.group,
      };

      Object.entries(values).forEach(([key, value]) => {
        if (value) url.searchParams.set(key, value);
        else url.searchParams.delete(key);
      });

      window.history.replaceState({}, "", url);
    };

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
            <a class="ww-card-link" href="../generated-index/">Open structured index →</a>
          </div>
        `;
      }
      return;
    }

    readUrlState();
    syncControls();

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

    const applyFilters = (updateUrl = true) => {
      state.query = search?.value || "";
      state.sort = sort?.value || "path";
      state.group = group?.value || "";

      if (!SORT_OPTIONS.has(state.sort)) state.sort = "path";
      if (!GROUP_OPTIONS.has(state.group)) state.group = "";

      const query = normalize(state.query);
      const filtered = entries.filter((entry) => {
        const rootOk = !state.root || entry.root === state.root;
        const topicOk = !state.topic || (entry.topics || []).includes(state.topic);
        const statusOk = !state.status || entry.status === state.status;
        return rootOk && topicOk && statusOk && matchesQuery(entry, query);
      });
      const sorted = sortEntries(filtered, state.sort);
      const groupLabel = state.group ? ` · grouped by ${GROUP_LABELS[state.group]}` : "";

      if (count) {
        count.textContent = `${sorted.length} of ${entries.length} registry entries${groupLabel}`;
      }
      if (results) {
        results.classList.toggle("ww-explorer-results--grouped", Boolean(state.group));
        results.innerHTML = renderEntries(sorted, state.group, state.topic);
      }

      if (updateUrl) writeUrlState();
    };

    root.querySelectorAll("[data-filter-type]").forEach((button) => {
      button.addEventListener("click", () => {
        const type = button.getAttribute("data-filter-type");
        if (!type) return;

        state[type] = button.getAttribute("data-filter-value") || "";
        setActiveFilter(type, state[type]);
        applyFilters();
      });
    });

    if (search) {
      search.addEventListener("input", applyFilters);
    }

    if (sort) sort.addEventListener("change", applyFilters);
    if (group) group.addEventListener("change", applyFilters);

    if (reset) {
      reset.addEventListener("click", () => {
        state.root = "";
        state.topic = "";
        state.status = "";
        state.query = "";
        state.sort = "path";
        state.group = "";
        syncControls();
        applyFilters();
      });
    }

    if (copyLink) {
      copyLink.addEventListener("click", async () => {
        writeUrlState();
        const originalText = copyLink.textContent;
        try {
          await navigator.clipboard.writeText(window.location.href);
          copyLink.textContent = "Copied";
        } catch (error) {
          copyLink.textContent = "URL updated";
        }
        window.setTimeout(() => {
          copyLink.textContent = originalText;
        }, 1400);
      });
    }

    applyFilters(false);
  };

  document.addEventListener("DOMContentLoaded", () => {
    bindSearchTriggers();
    initExplorer();
  });
})();
