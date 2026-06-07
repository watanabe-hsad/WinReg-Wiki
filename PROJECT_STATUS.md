# Project Status

## Current Goal

The project is `WinReg Wiki`: a concise Chinese-first Windows registry key/value lookup wiki with registry-related forensic leads. The current v0.1 direction is registry-path-first, scenario-assisted, and data-backed.

Current information architecture:

- `首页`: search-first registry database landing with a visible search panel, quick path chips, dashboard stats, and popular registry path cards.
- `注册表位置`: primary dictionary-style entry point organized by Windows native registry tree. Pages explain location, hive source, common values, state, caveats, related scenarios, and related registry positions.
- `取证场景`: checklist-style investigation entry point. Scenario pages primarily link to `docs/registry-tree/` pages and then list cross-validation sources.
- `docs/artifacts/`: supplemental/internal artifact detail. Artifact pages are retained for field semantics, collection notes, parsing tools, common misreads, and YAML-backed artifact indexes. They are not a primary navigation model.

## Repository

- Local path: `/Users/hsad/Documents/CodeProject/registry-forensics-handbook-demo`
- Formal project name: `WinReg Wiki`
- GitHub repository: `https://github.com/watanabe-hsad/WinReg-Wiki.git`
- Repository name: `WinReg-Wiki`
- Default branch: `main`
- Current remote: `origin https://github.com/watanabe-hsad/WinReg-Wiki.git`
- Current online site: pending confirmation after repository rename.
- Current `site_url`: `http://hsad.xyz/windows-registry-forensics-handbook/`
- URL status: keep current `site_url` until DNS and GitHub Pages settings are confirmed. Candidate future paths remain `https://hsad.xyz/winreg/` and `https://winreg.hsad.xyz/`; the subdomain option is cleaner but requires maintainer confirmation.
- Local directory note: the local folder still has the older `registry-forensics-handbook-demo` name. Do not rename it unless local tooling and references are checked.

## Current Structure

- `docs/registry-tree/`: Windows native registry tree entry point. Current count is 98 Markdown files, including `explorer.md`, `generated-index.md`, and `coverage.md`.
- `docs/registry-tree/generated-index.md`: generated structured registry index for readers. Output of `scripts/generate-registry-index.py`.
- `docs/registry-tree/coverage.md`: generated registry coverage matrix for maintenance and next-path planning. Output of `scripts/generate-registry-index.py`.
- `docs/questions/`: forensic scenario entry point. Current count is 12 Markdown files.
- `docs/artifacts/`: supplemental artifact layer. Current count is 44 Markdown files total: 42 artifact content pages plus `index.md` and `generated-index.md`.
- `data/registry/`: structured registry-location fact layer. Current pilot count is 10 YAML records.
- `data/artifacts/`: structured artifact YAML records. Current count is 42 YAML records.
- `schemas/registry-entry.schema.yml`: lightweight reference schema for registry YAML fields. It is documentation-oriented and does not add a validation dependency.
- `scripts/generate-registry-index.py`: reads `data/registry/*.yml`, validates required fields and linked Markdown pages, and writes `docs/registry-tree/generated-index.md`, `docs/registry-tree/coverage.md`, and `docs/assets/registry-index.json`.
- `scripts/generate-artifact-index.py`: reads `data/artifacts/*.yml` and writes `docs/artifacts/generated-index.md`.
- `scripts/check-content-style.py`: lightweight standard-library scan for old artifact headings, English artifact-template headings, subjective priority wording, and stale project/repository names.
- `mkdocs.yml`: site configuration and navigation. Top-level nav remains `首页`, `注册表位置`, `取证场景`, `贡献`, `标签`.
- `.github/workflows/pages.yml`: GitHub Actions workflow for MkDocs build and GitHub Pages deployment.

## Last Completed Round

This round completed a high-fidelity `RegSeek / DFIRHub inspired UI rebuild`. It did not expand registry content, did not add artifact pages, and did not change the top-level navigation. The focus was converting the site from a polished MkDocs document landing into a search-first registry database experience.

Visual / UX changes:

- Rebuilt `docs/index.md` as a DFIRHub-like search-first database landing:
  - product-style first screen with `WINDOWS REGISTRY KNOWLEDGE BASE`, command-style search panel, quick filters, dashboard stats, and three primary entry cards;
  - `Popular Registry Paths` cards for Run Keys, Services, USBSTOR, UserAssist, Winlogon, ProfileList, MountedDevices, Defender Policies, RDP-Tcp, and Tcpip Interfaces.
- Added `docs/registry-tree/explorer.md` as the new Registry Explorer page:
  - search input, Hive filters, topic filters, status filters, result count, empty state, and card-based results;
  - interactive behavior is implemented by `docs/javascripts/registry-explorer.js` with vanilla JavaScript.
- Updated `scripts/generate-registry-index.py` to generate `docs/assets/registry-index.json` in addition to `generated-index.md` and `coverage.md`.
- Updated `docs/registry-tree/index.md` into a Registry Explorer portal with a strong `Open Registry Explorer` entry, generated index / coverage entry cards, root-key cards, topic chips, and common registry areas.
- Rebuilt `docs/questions/index.md` as a scenario directory with a highlighted `常规注册表检查` start card, scenario chips, scenario cards, and a weak supplemental section.
- Reworked `docs/questions/registry-checklist.md` into a checklist dashboard with compact cards instead of large tables.
- Updated `scripts/generate-registry-index.py` so generated registry index pages link to the Explorer and use clearer entry cards, summary headers, badges, path pills, and grouped tables.
- Regenerated:
  - `docs/registry-tree/generated-index.md`
  - `docs/registry-tree/coverage.md`
  - `docs/assets/registry-index.json`
- Rebuilt `docs/stylesheets/extra.css` into a product-style `ww-*` component system:
  - design tokens for surfaces, borders, shadows, radii, spacing, and typography;
  - layout classes: `ww-shell`, `ww-hero`, `ww-section`, `ww-dashboard-grid`;
  - components: `ww-search-panel`, `ww-filter-bar`, `ww-chip`, `ww-badge`, `ww-feature-card`, `ww-path-card`, `ww-root-card`, `ww-scenario-card`, `ww-check-card`, `ww-stat-card`, `ww-path-pill`, `ww-empty-state`;
  - generated / interactive components: `ww-registry-explorer`, `ww-explorer-toolbar`, `ww-explorer-results`, `ww-explorer-card`;
  - upgraded fact components: `ww-fact-card`, `ww-fact-grid`, `ww-fact-footer`.
- Upgraded Registry Fact Card structure on 10 common registry-location pages:
  - `HKLM\SYSTEM\Select`
  - `HKLM\SYSTEM\ControlSet00x`
  - `HKLM\SYSTEM\ControlSet00x\Services`
  - `HKLM\SYSTEM\ControlSet00x\Enum\USBSTOR`
  - `HKLM\SYSTEM\MountedDevices`
  - `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList`
  - `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon`
  - `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`
  - `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`
  - `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist`
- Updated `mkdocs.yml` so `注册表位置` includes `Explorer` and the site loads `javascripts/registry-explorer.js`.
- Updated `.github/workflows/pages.yml` so CI checks the generated `docs/assets/registry-index.json`.
- Updated README and registry data schema documentation for the JSON-backed Explorer.

Local browser preview:

- Preview command: `.venv/bin/mkdocs serve -a 127.0.0.1:8000`.
- Checked pages in this round:
  - `/`
  - `/registry-tree/explorer/`
  - `/registry-tree/`
  - `/registry-tree/generated-index/`
  - `/registry-tree/coverage/`
  - `/questions/`
  - `/questions/registry-checklist/`
  - `/registry-tree/hklm/system/select/`
  - `/registry-tree/hklm/system/controlset/enum/usbstor/`
- Checked desktop width, mobile width, and dark mode.
- Result: Explorer JSON cards render, filters work, search panel is visible, chips wrap normally, and no page-level horizontal overflow was observed. Dark mode remains readable for cards, filters, path pills, and fact cards.
- Browser console note: MkDocs Material may emit theme-level label warnings; these are not introduced by project content.

## Previous Completed Round

This previous round completed the first `Visual UX Redesign`.

Visual / UX changes from that round:

- Rebuilt the homepage as a search-first registry database landing page with a visible search panel, quick registry chips, dashboard stats, primary entry cards, and popular path cards.
- Rebuilt `docs/registry-tree/index.md` as a root-key explorer with generated index and coverage links.
- Rebuilt `docs/questions/index.md` as a scenario-card directory and kept artifact / generated-data links in a bottom supplemental section.
- Reworked `docs/questions/registry-checklist.md` into a checklist dashboard with compact tables by investigation area.
- Updated `scripts/generate-registry-index.py` so generated registry index and coverage pages use summary headers, dashboard stats, topic / hive / status badges, path pills, and grouped tables.
- Rebuilt `docs/stylesheets/extra.css` into a larger `ww-*` visual system.
- Added Registry Fact Card presentation on 10 common registry-location pages.

## Earlier Completed Round

This earlier round prepared the v0.1 Data + UX Refactor.

Data model changes:

- Added `data/registry/` as the structured registry-location fact layer.
- Added 10 pilot registry YAML records:
  - `hklm-system-select`
  - `hklm-system-controlset`
  - `hklm-system-controlset-services`
  - `hklm-system-tcpip-interfaces`
  - `hklm-system-enum-usbstor`
  - `hklm-system-mounteddevices`
  - `hklm-software-profilelist`
  - `hklm-software-winlogon`
  - `hklm-software-run`
  - `hkcu-software-run`
- Added `docs/contributing/registry-data-schema.md` and `schemas/registry-entry.schema.yml`.
- Added `scripts/generate-registry-index.py` and generated:
  - `docs/registry-tree/generated-index.md`
  - `docs/registry-tree/coverage.md`
- Added `registry_entry_ids` relationships to these artifact YAML files:
  - `services.yml` -> `hklm-system-controlset-services`
  - `usbstor.yml` -> `hklm-system-enum-usbstor`
  - `mounteddevices.yml` -> `hklm-system-mounteddevices`
  - `profilelist.yml` -> `hklm-software-profilelist`
  - `run-keys.yml` -> `hklm-software-run`, `hkcu-software-run`
  - `winlogon-shell.yml` -> `hklm-software-winlogon`
  - `winlogon-userinit.yml` -> `hklm-software-winlogon`

Previous UX and content changes:

- Refreshed `docs/index.md` with compact entry cards, current coverage stats, common path chips, registry basics, and a clear boundary between registry locations, scenarios, and artifact supplements.
- Refreshed `docs/registry-tree/index.md` as a Registry Explorer-style root key entry with links to the structured index and coverage matrix.
- Refreshed `docs/questions/index.md` as a scenario query entry with compact scenario cards and supplemental links.
- Reworked `docs/questions/registry-checklist.md` into a four-column checklist: check target, registry location, fields, and cross-validation.
- Added restrained `ww-*` styling in `docs/stylesheets/extra.css` for entry cards, stats, chips, generated-index topic chips, metadata summaries, and table readability.
- Added summary metadata blocks to high-visible registry pages:
  - `HKLM\SYSTEM\Select`
  - `HKLM\SYSTEM\ControlSet00x`
  - `HKLM\SYSTEM\ControlSet00x\Services`
  - `HKLM\SYSTEM\ControlSet00x\Enum\USBSTOR`
  - `HKLM\SYSTEM\MountedDevices`
  - `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList`
  - `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon`
  - `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`
  - `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`
  - `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist`

Contribution and CI changes:

- Updated `docs/contributing/index.md` for registry YAML, generated registry pages, and updated pre-commit commands.
- Updated `docs/contributing/template.md` with a registry YAML example.
- Updated `README.md` to describe `data/registry/`, generated registry indexes, content style checks, CI behavior, and pending site URL.
- Updated `.github/workflows/pages.yml` so CI now runs artifact generation, registry generation, content style check, generated-file diff check, and `mkdocs build --strict`.
- Updated `mkdocs.yml` so `注册表位置` includes `结构化索引` and `覆盖矩阵`, and `贡献` includes `Registry 数据模型`.

## Artifact Layer Status

- Artifact pages remain supplemental/internal. They are reachable from `取证场景` supplemental links and registry-location `补充阅读`, not from a top-level artifact tab.
- Current artifact inventory is 42 content pages and 42 YAML records. `docs/artifacts/index.md` and `docs/artifacts/generated-index.md` are index pages and are not counted as artifact content pages.
- New registry relationships were added with `registry_entry_ids`; no old artifact YAML fields were removed.

## Validation

Latest required validation results:

- `.venv/bin/python scripts/generate-artifact-index.py`: passed; regenerated `docs/artifacts/generated-index.md`.
- `.venv/bin/python scripts/generate-registry-index.py`: passed; generated 10 registry entries into `docs/registry-tree/generated-index.md`, `docs/registry-tree/coverage.md`, and `docs/assets/registry-index.json`.
- `.venv/bin/python scripts/check-content-style.py`: passed.
- `.venv/bin/mkdocs build --strict`: passed. Material for MkDocs showed the upstream MkDocs 2.0 warning; this is not a project failure. MkDocs also lists artifact detail pages outside `nav`, which is expected because artifact pages remain supplemental.
- `.venv/bin/mkdocs serve -a 127.0.0.1:8000`: used for local visual preview after the redesign.
- Browser preview checks: homepage, Registry Explorer, registry-tree portal, generated index, coverage matrix, scenario directory, registry checklist, `HKLM\SYSTEM\Select`, and `HKLM\SYSTEM\ControlSet00x\Enum\USBSTOR`.
- Visual result: desktop, mobile, light mode, and dark mode were checked. Explorer loaded 10 JSON records, keyword filtering for `USBSTOR` reduced results to one card, homepage search panel focused MkDocs search, and no horizontal overflow or console errors were observed.

## License Status

- Current License: `TBD`.
- Recommended option A: documentation under `CC BY 4.0`, scripts and site engineering under `MIT`.
- Recommended option B: repository-wide `MIT` if the maintainer wants a single simple license.
- Do not add a `LICENSE` file until the maintainer confirms the choice.

## Next Round Suggestions

- Expand `data/registry/` from 10 pilot records to about 30 core registry pages.
- Continue adding `registry_entry_ids` to artifact YAML where relationships are clear.
- Add generated registry indexes by Hive, topic, tool support, and ATT&CK mapping only after the data model reaches enough coverage.
- Confirm GitHub Pages and DNS, then decide whether to move from the old path to `https://winreg.hsad.xyz/` or `https://hsad.xyz/winreg/`.
- Decide License and add `LICENSE`.
- Prepare a `v0.1` tag after URL and License decisions are made.
- Continue filling registry paths from the generated coverage candidate list: HKCU Policies System / Attachments / Associations, Explorer Advanced, TypedPaths, ShellBags / BagMRU, `Enum\STORAGE`, and `DeviceContainers`.
