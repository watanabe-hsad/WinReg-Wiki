# Registry Explorer

<section class="ww-registry-explorer" data-registry-explorer data-registry-json="../../assets/registry-index.json">
  <div class="ww-explorer-hero">
    <div>
      <p class="ww-hero-eyebrow">Registry Explorer</p>
      <h1>按 Hive、主题、场景筛选注册表路径</h1>
      <p>基于 <code>data/registry</code> 的结构化入口。它适合快速定位 key / value 页面；正文解释仍由人工维护。</p>
    </div>
    <button class="ww-search-panel ww-search-panel--compact" type="button" data-ww-search-trigger>
      <span class="ww-search-label">Site search</span>
      <span class="ww-search-box">
        <span class="ww-search-placeholder">搜索路径、值名、场景，例如 Run Keys / USBSTOR / Winlogon</span>
        <span class="ww-command-group"><kbd class="ww-command-key">/</kbd><kbd class="ww-command-key">Ctrl K</kbd></span>
      </span>
    </button>
  </div>

  <div class="ww-dashboard-grid ww-dashboard-grid--explorer" data-registry-stats>
    <div class="ww-stat-card"><span>entries</span><strong>10</strong><em>结构化记录</em></div>
    <div class="ww-stat-card"><span>hives</span><strong>2</strong><em>当前试点</em></div>
    <div class="ww-stat-card"><span>topics</span><strong>5</strong><em>系统配置 / 持久化等</em></div>
    <div class="ww-stat-card"><span>scenarios</span><strong>7</strong><em>关联场景</em></div>
  </div>

  <div class="ww-explorer-toolbar">
    <label class="ww-explorer-search">
      <span>Search</span>
      <input type="search" data-registry-search placeholder="Search paths, values, topics..." autocomplete="off">
    </label>

    <div class="ww-filter-section">
      <span class="ww-filter-label">Hive filters</span>
      <div class="ww-filter-bar" data-filter-group="root">
        <button type="button" class="ww-filter-chip is-active" data-filter-type="root" data-filter-value="">All</button>
        <button type="button" class="ww-filter-chip" data-filter-type="root" data-filter-value="HKLM">HKLM</button>
        <button type="button" class="ww-filter-chip" data-filter-type="root" data-filter-value="HKCU">HKCU</button>
        <button type="button" class="ww-filter-chip" data-filter-type="root" data-filter-value="HKU">HKU</button>
        <button type="button" class="ww-filter-chip" data-filter-type="root" data-filter-value="HKCR">HKCR</button>
        <button type="button" class="ww-filter-chip" data-filter-type="root" data-filter-value="HKCC">HKCC</button>
      </div>
    </div>

    <div class="ww-filter-section">
      <span class="ww-filter-label">Topic filters</span>
      <div class="ww-filter-bar" data-filter-group="topic">
        <button type="button" class="ww-filter-chip is-active" data-filter-type="topic" data-filter-value="">All</button>
        <button type="button" class="ww-filter-chip" data-filter-type="topic" data-filter-value="系统配置">系统配置</button>
        <button type="button" class="ww-filter-chip" data-filter-type="topic" data-filter-value="用户行为">用户行为</button>
        <button type="button" class="ww-filter-chip" data-filter-type="topic" data-filter-value="持久化">持久化</button>
        <button type="button" class="ww-filter-chip" data-filter-type="topic" data-filter-value="网络">网络</button>
        <button type="button" class="ww-filter-chip" data-filter-type="topic" data-filter-value="账户">账户</button>
        <button type="button" class="ww-filter-chip" data-filter-type="topic" data-filter-value="设备">设备</button>
        <button type="button" class="ww-filter-chip" data-filter-type="topic" data-filter-value="策略">策略</button>
        <button type="button" class="ww-filter-chip" data-filter-type="topic" data-filter-value="软件">软件</button>
      </div>
    </div>

    <div class="ww-filter-section">
      <span class="ww-filter-label">Status filters</span>
      <div class="ww-filter-bar" data-filter-group="status">
        <button type="button" class="ww-filter-chip is-active" data-filter-type="status" data-filter-value="">All</button>
        <button type="button" class="ww-filter-chip" data-filter-type="status" data-filter-value="stable">stable</button>
        <button type="button" class="ww-filter-chip" data-filter-type="status" data-filter-value="reviewed">reviewed</button>
        <button type="button" class="ww-filter-chip" data-filter-type="status" data-filter-value="draft">draft</button>
      </div>
    </div>
  </div>

  <div class="ww-explorer-count" data-registry-count>Loading registry entries...</div>
  <div class="ww-explorer-results" data-registry-results></div>

  <noscript>
    <div class="ww-empty-state">
      <strong>当前浏览器未启用 JavaScript。</strong>
      <span>请使用 <a href="generated-index.md">结构化索引</a> 或 <a href="coverage.md">覆盖矩阵</a> 查看同一批 registry entry。</span>
    </div>
  </noscript>
</section>
