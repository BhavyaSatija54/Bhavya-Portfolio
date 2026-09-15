# VP-level refinement — Round 2

## What changed
- Removed the scrolling ticker: less gimmick, more institutional.
- Added a static proof ribbon with project / model / validation metadata.
- Added a hiring-lens control: Full library, IB / Valuation, Risk, Quant, Data / AI.
- Added dynamic explanatory copy for each lens.
- Fixed category visibility when a lens is selected.
- Added an explicit evidence standard: Claim → Method → Output → Check → Limitation.
- Added a concise closing section reinforcing inspectability rather than self-promotion.
- Preserved all existing project pages, models, memos, and repositories.

## Design principle
The site should feel like a junior analyst/researcher publishing inspectable work, not like a student collecting technologies.

## Deployment
Replace the root `index.html` with the supplied version and add/replace `home.css`. Keep `style.css`, `script.js`, `projects/`, `models/`, `memos/`, and `assets/` intact.
