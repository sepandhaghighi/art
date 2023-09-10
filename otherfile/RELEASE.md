
# Art Release Instructions

#### Last Update: 2023-09-10

1. Create the `release` branch under `dev`
2. Update all version tags
	1. `setup.py`
	2. `INSTALL.md`
	3. `otherfile/version_check.py`
	4. `otherfile/meta.yaml`
	5. `art/art_param.py`
	6. `ArtList.ipynb`
	7. `DecorList.ipynb`
	8. `FontList.ipynb`
3. Update `CHANGELOG.md`
	1. Add a new header under `Unreleased` section (Example: `## [0.2] - 2022-08-17`)
	2. Add a new compare link to the end of the file (Example: `[0.2]: https://github.com/sepandhaghighi/art/compare/v0.1...v0.2`)
	3. Update `dev` compare link (Example: `[Unreleased]: https://github.com/sepandhaghighi/art/compare/v0.2...dev`)
4. Update Document
	1. Run `otherfile/doc_run.bat`
5. Create a PR from `release` to `dev`
	1. Title: `Version x.x` (Example: `Version 0.1`)
	2. Tag all related issues
	3. Labels: `release`
	4. Set milestone
	5. Wait for all CI pass
	6. Need review (**1** reviewers)
6. Merge `dev` branch into `master`
	1. Checkout to `master`
	2. `git merge dev`
	3. `git push origin master`
	4. Wait for all CI pass
7. Create a new release
	1. Target branch: `master`
	2. Tag: `vx.x` (Example: `v0.1`)
	3. Title: `Version x.x` (Example: `Version 0.1`)
	4. Copy changelogs
	5. Tag all related issues
8. Bump!!
9. Close this version issues
10. Close milestone
11. Close project
12. Generate HTML files
	1. Run `otherfile/doc_to_html.bat`
	2. Copy `doc_html` folder for the next steps
13. Update website