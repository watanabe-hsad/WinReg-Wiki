<section class="ww-registry-explorer" data-registry-explorer data-registry-json="../../assets/registry-index.json">
  <div class="ww-compact-head ww-compact-head--explorer">
    <p class="ww-hero-eyebrow">REGISTRY EXPLORER</p>
    <h1>按注册表路径筛选</h1>
    <p>按 Hive、主题、场景和状态筛选 <code>data/registry</code> 结构化记录；正文说明仍由人工维护。</p>
  </div>

  <div class="ww-explorer-toolbar">
    <label class="ww-explorer-search" for="registry-explorer-search">
      <span>Search</span>
      <input id="registry-explorer-search" name="registry-explorer-search" type="search" data-registry-search placeholder="Search paths, values, topics..." autocomplete="off">
    </label>

    <div class="ww-explorer-controls">
      <label class="ww-explorer-select" for="registry-explorer-sort">
        <span>Sort</span>
        <select id="registry-explorer-sort" name="registry-explorer-sort" data-registry-sort>
          <option value="path">Path A-Z</option>
          <option value="hive">Hive / path</option>
          <option value="topic">Topic / path</option>
          <option value="status">Status / path</option>
        </select>
      </label>

      <label class="ww-explorer-select" for="registry-explorer-group">
        <span>Group</span>
        <select id="registry-explorer-group" name="registry-explorer-group" data-registry-group>
          <option value="">No grouping</option>
          <option value="root">Root hive</option>
          <option value="hive">Offline hive</option>
          <option value="topic">Topic</option>
          <option value="status">Status</option>
        </select>
      </label>

      <div class="ww-explorer-actions">
        <button type="button" class="ww-filter-chip" data-registry-reset>Reset</button>
        <button type="button" class="ww-filter-chip" data-registry-copy-link>Copy view</button>
      </div>
    </div>

    <div class="ww-filter-section">
      <span class="ww-filter-label">Hive</span>
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
      <span class="ww-filter-label">Topic</span>
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
      <span class="ww-filter-label">Status</span>
      <div class="ww-filter-bar" data-filter-group="status">
        <button type="button" class="ww-filter-chip is-active" data-filter-type="status" data-filter-value="">All</button>
        <button type="button" class="ww-filter-chip" data-filter-type="status" data-filter-value="stable">stable</button>
        <button type="button" class="ww-filter-chip" data-filter-type="status" data-filter-value="reviewed">reviewed</button>
        <button type="button" class="ww-filter-chip" data-filter-type="status" data-filter-value="draft">draft</button>
      </div>
    </div>
  </div>

  <div class="ww-dashboard-grid ww-dashboard-grid--explorer" data-registry-stats>
    <div class="ww-stat-card"><strong>30</strong><span>entries</span></div>
    <div class="ww-stat-card"><strong>2</strong><span>hives</span></div>
    <div class="ww-stat-card"><strong>9</strong><span>topics</span></div>
    <div class="ww-stat-card"><strong>11</strong><span>scenarios</span></div>
  </div>

  <div class="ww-explorer-count" data-registry-count aria-live="polite">Loading registry entries...</div>
  <div class="ww-explorer-results" data-registry-results></div>

  <noscript>
    <div class="ww-empty-state">
      <strong>当前浏览器未启用 JavaScript。</strong>
      <span>请使用 <a href="../generated-index/">结构化索引</a> 或 <a href="../coverage/">覆盖矩阵</a> 查看同一批 registry entry。</span>
    </div>
  </noscript>
</section>
