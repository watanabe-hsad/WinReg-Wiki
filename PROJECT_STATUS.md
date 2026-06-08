# Project Status

## Current Goal

The project is `WinReg Wiki`: a concise Chinese-first Windows registry key/value lookup wiki with registry-related forensic leads. The current v0.1 direction is registry-path-first, scenario-assisted, and data-backed.

Current information architecture:

- `首页`: compact search-first registry database entrance with a quiet title block, inline search bar, small filter chips, metric row, and dense popular path cards.
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
- `data/registry/`: structured registry-location fact layer. Current core count is 30 YAML records.
- `data/artifacts/`: structured artifact YAML records. Current count is 42 YAML records.
- `schemas/registry-entry.schema.yml`: lightweight reference schema for registry YAML fields. It is documentation-oriented and does not add a validation dependency.
- `scripts/generate-registry-index.py`: reads `data/registry/*.yml`, validates required fields and linked Markdown pages, and writes `docs/registry-tree/generated-index.md`, `docs/registry-tree/coverage.md`, and `docs/assets/registry-index.json`.
- `scripts/generate-artifact-index.py`: reads `data/artifacts/*.yml` and writes `docs/artifacts/generated-index.md`.
- `scripts/check-content-style.py`: lightweight standard-library scan for old artifact headings, English artifact-template headings, subjective priority wording, and stale project/repository names.
- `mkdocs.yml`: site configuration and navigation. Top-level nav remains `首页`, `注册表位置`, `取证场景`, `贡献`, `标签`.
- `.github/workflows/pages.yml`: GitHub Actions workflow for MkDocs build and GitHub Pages deployment.

## Last Completed Round

This round expanded the Registry Explorer data backbone from the 10-entry MVP to 30 core registry records. It did not add new registry-tree Markdown pages, did not change top-level navigation, and did not move artifact pages back into the primary entry model.

Registry data expansion:

- Added 20 new `data/registry/*.yml` records:
  - `hkcu-userassist`
  - `hkcu-recentdocs`
  - `hkcu-runmru`
  - `hkcu-mountpoints2`
  - `hkcu-terminal-server-client`
  - `hklm-system-rdp-tcp`
  - `hklm-policies-windows-defender`
  - `hklm-policies-windowsfirewall`
  - `hklm-software-policies-system`
  - `hklm-software-ifeo`
  - `hklm-software-active-setup`
  - `hklm-system-eventlog`
  - `hklm-software-networklist-profiles`
  - `hklm-system-firewallpolicy`
  - `hklm-system-enum-usb`
  - `hklm-system-deviceclasses`
  - `hklm-system-swd-wpdbusenum`
  - `hklm-winlogon-specialaccounts-userlist`
  - `hklm-winlogon-cachedlogonscount`
  - `hklm-system-lsa-security-packages`
- Current `data/registry/` coverage is now 30 records:
  - 5 HKCU records;
  - 25 HKLM records;
  - 9 topic labels: 持久化, 用户行为, 程序执行, 策略, 系统配置, 网络, 设备, 账户, 软件.
- Regenerated:
  - `docs/registry-tree/generated-index.md`
  - `docs/registry-tree/coverage.md`
  - `docs/assets/registry-index.json`
- Homepage metric now shows `30 registry data`.
- README now documents current `data/registry/` coverage as 30 core records.

Artifact relationship updates:

- Added clear `registry_entry_ids` links for additional artifact YAML records:
  - UserAssist, RecentDocs, RunMRU, MountPoints2, Terminal Server Client;
  - RDP-Tcp PortNumber and CredSSP / NLA;
  - Defender Policies, Firewall Policies, UAC Policies;
  - IFEO, Active Setup;
  - USB, DeviceClasses, SWD WPDBUSENUM, Portable Devices;
  - SpecialAccounts\UserList;
  - LSA Security Packages and LSA Authentication Packages.
- No old artifact YAML fields were removed.
- Artifact pages remain supplemental/internal and still stay outside the top-level navigation.

Documentation updates:

- Updated `README.md`, `ROADMAP.md`, `CHANGELOG.md`, and this status document for the 30-record registry data milestone.
- `ROADMAP.md` now treats the 30-record data milestone as complete and moves the next target to about 50 registry records plus richer Explorer sort/group controls.

## Previous Completed Round

This round completed a `Quiet RegSeek-style UI Correction`. It did not expand content, did not change the data model, did not change the top-level navigation, and did not move artifact pages back into the primary entry model.

Reason for this round:

- The previous UI was functional but still felt too much like a large landing page.
- Homepage title, hero area, card size, whitespace, and fact cards were too visually heavy for a registry lookup wiki.
- The desired direction is closer to RegSeek / DFIRHub: search first, compact filters, dense data cards, and quiet Microsoft Learn-like reading surfaces.

Quiet UI changes:

- Rebuilt `docs/index.md` from a split hero into a compact database entrance:
  - H1 is now `WinReg Wiki`, with a smaller title scale and no large hero card;
  - search is a 52-60px inline bar below the title block;
  - quick filters now prioritize registry paths and hives: HKLM, HKCU, SYSTEM, SOFTWARE, Run Keys, Services, USBSTOR, UserAssist, Winlogon, ProfileList, RDP, Defender;
  - metric cards are small dashboard items instead of large stat blocks;
  - primary entry cards are compact and under the target desktop height;
  - popular registry path cards now use short path pills and smaller text.
- Reworked `docs/registry-tree/explorer.md` into a quieter RegSeek-like database page:
  - removed duplicate Markdown page title;
  - replaced the large Explorer hero with a compact heading and toolbar;
  - kept JSON-backed rendering and filters;
  - Explorer result cards now use short path labels, single-line path pills, one-line summaries, and capped chip rows.
- Updated `docs/javascripts/registry-explorer.js`:
  - uses short path labels for card titles;
  - keeps full paths in path-pill `title` text;
  - limits visible topic / scenario chips so cards stay compact.
- Reworked `docs/registry-tree/index.md` as a quiet directory entrance:
  - small `Explorer / 结构化索引 / 覆盖矩阵` entry cards;
  - compact root-key cards;
  - common registry areas presented as dense path cards.
- Reworked `docs/questions/index.md` as a compact scenario directory:
  - small header;
  - compact highlighted `常规注册表检查`;
  - scenario cards use short descriptions and path chips;
  - supplemental artifact / generated-data / detection links remain visually weaker at the bottom.
- Updated `docs/questions/registry-checklist.md`:
  - removed the large page-header block;
  - kept checklist cards but made the page start with a compact title and category chips.
- Rebuilt `docs/stylesheets/extra.css` around quiet constraints:
  - removed viewport-width typography scaling;
  - homepage H1 is capped at `2.1rem` desktop and `1.82rem` mobile;
  - search bar is compact, with mobile staying around 59px and hiding shortcut chips at very narrow widths;
  - metric numbers are `1.05rem`, metric rows are about 58px;
  - card padding, gaps, radii, and shadows were reduced;
  - Explorer result cards are about 139px on desktop;
  - fact cards were changed from a table-like block into a compact fact strip.

Current visual notes:

- The site remains MkDocs Material with small project-specific `ww-*` CSS components.
- The UI is intentionally quiet and dense. It avoids large hero cards, large pale-blue surfaces, thick shadows, gradients, decorative blobs, and marketing copy.
- Registry Fact Cards are smaller and no longer table-like. The `HKLM\SYSTEM\Select` card is still taller than the ideal 160px because it preserves multiple scenario and related-data chips; forcing it smaller would hide useful facts.

Follow-up visual token polish:

- Refined `docs/stylesheets/extra.css` without changing content, navigation, data, or generated-page semantics.
- Tightened light and slate mode tokens for borders, muted text, path pills, chips, and focus rings.
- Set Material header / tabs to a quieter Windows-like blue and gave the built-in search box a restrained bordered treatment.
- Added subtle table zebra rows and hover states for reference-page scanability.
- Added clearer keyboard focus styles for search panels, filter chips, path pills, and registry cards.
- Kept the UI within the quiet RegSeek-style constraints: no new hero treatment, no larger typography, no heavy shadows, and no new decorative surfaces.

Local browser preview for this round:

- Preview command: `.venv/bin/mkdocs serve -a 127.0.0.1:8000`.
- Checked pages:
  - `/`
  - `/registry-tree/explorer/`
  - `/registry-tree/`
  - `/questions/`
  - `/questions/registry-checklist/`
  - `/registry-tree/hklm/system/select/`
- Checked desktop width, mobile width, and dark mode.
- Result: no horizontal overflow, no console errors, mobile search bar stayed compact, Explorer rendered 10 JSON records, and clicking the HKCU Hive filter reduced results to `1 of 10 registry entries`.

## Previous Completed Round

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

## Earlier Completed Round

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
- `.venv/bin/python scripts/generate-registry-index.py`: passed; generated 30 registry entries into `docs/registry-tree/generated-index.md`, `docs/registry-tree/coverage.md`, and `docs/assets/registry-index.json`.
- `.venv/bin/python scripts/check-content-style.py`: passed.
- `.venv/bin/mkdocs build --strict`: passed. Material for MkDocs showed the upstream MkDocs 2.0 warning; this is not a project failure. MkDocs also lists artifact detail pages outside `nav`, which is expected because artifact pages remain supplemental.
- `.venv/bin/mkdocs serve -a 127.0.0.1:8000`: used for local visual preview after the quiet UI correction and the 30-record registry data expansion.
- Browser preview checks: homepage, Registry Explorer, registry-tree portal, scenario directory, registry checklist, and `HKLM\SYSTEM\Select`.
- Visual result:
  - desktop homepage search bar measured about 57px high, metric cards about 58px, and primary entry cards about 104px;
  - desktop Explorer cards measured about 139px after compact rendering;
  - mobile homepage search bar measured about 59px and did not overflow;
  - mobile Explorer rendered the filter-first layout without horizontal overflow, with single-column result cards;
  - mobile `HKLM\SYSTEM\Select` fact card kept path pills inside the viewport;
  - dark mode was checked on homepage, Explorer, and Registry Fact Card pages;
  - dark mode header, cards, table headers, path pills, and fact-card borders remained visually separated;
  - no page-level horizontal overflow or JavaScript console errors were observed;
  - Explorer loaded 30 JSON records; JSON metadata reports 2 root hives, 9 topics, and 30 entries;
  - Explorer filtering was checked after the data expansion: HKCU returned 6 entries, HKCU + 设备 returned 1 entry, and searching `firewall` after reset returned 2 entries;
  - mobile Explorer rendered 30 single-column cards without horizontal overflow.

## License Status

- Current License: `TBD`.
- Recommended option A: documentation under `CC BY 4.0`, scripts and site engineering under `MIT`.
- Recommended option B: repository-wide `MIT` if the maintainer wants a single simple license.
- Do not add a `LICENSE` file until the maintainer confirms the choice.

## Next Round Suggestions

- Expand `data/registry/` from 30 core records to about 50 records, prioritizing ShellBags / BagMRU, AppCompatFlags, StartupApproved, App Paths, BootExecute, KnownDLLs, TypedPaths, Explorer Advanced, and additional device/container paths.
- Continue adding `registry_entry_ids` to artifact YAML where relationships are clear and not yet represented.
- Add richer Registry Explorer sort/group controls now that the JSON dataset is large enough to benefit from them.
- Add generated registry indexes by Hive, topic, tool support, and ATT&CK mapping only after the data model reaches enough coverage.
- Confirm GitHub Pages and DNS, then decide whether to move from the old path to `https://winreg.hsad.xyz/` or `https://hsad.xyz/winreg/`.
- Decide License and add `LICENSE`.
- Prepare a `v0.1` tag after URL and License decisions are made.
- Continue filling registry paths from the generated coverage candidate list: HKCU Policies System / Attachments / Associations, Explorer Advanced, TypedPaths, ShellBags / BagMRU, `Enum\STORAGE`, and `DeviceContainers`.
