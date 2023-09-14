
# Art Release Instructions

#### Last Update: 2023-09-13

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
3. Update `help_func` function output in `test.py`
4. Update all font counters in `README.md` (**If needed**)
	1. `<img src="https://img.shields.io/badge/Font List-{font_counter}-blue.svg" alt="Font List">`
	2. `<td id="font_counter">{font_counter}</td>`
5. Update all art counters in `README.md` (**If needed**)
	1. `<img src="https://img.shields.io/badge/Art List-{art_counter}-orange.svg" alt="Art List">`
	2. `<td id="art_counter">{art_counter}</td>`
6. Update all decor counters in `README.md` (**If needed**)
	1. `<img src="https://img.shields.io/badge/Decor List-{decor_counter}-green.svg" alt="Decor List">`
	2. `<td id="decor_counter">{decor_counter}</td>`
7. Update `CHANGELOG.md`
	1. Add a new header under `Unreleased` section (Example: `## [0.2] - 2022-08-17`)
	2. Add a new compare link to the end of the file (Example: `[0.2]: https://github.com/sepandhaghighi/art/compare/v0.1...v0.2`)
	3. Update `dev` compare link (Example: `[Unreleased]: https://github.com/sepandhaghighi/art/compare/v0.2...dev`)
8. Update Document
	1. Run `otherfile/doc_run.bat`
9. Create a PR from `release` to `dev`
	1. Title: `Version x.x` (Example: `Version 0.1`)
	2. Tag all related issues
	3. Labels: `release`
	4. Set milestone
	5. Set project
	6. Wait for all CI pass
	7. Need review (**1** reviewer)
10. Merge `dev` branch into `master`
	1. Checkout to `master`
	2. `git merge dev`
	3. `git push origin master`
	4. Wait for all CI pass
11. Create a new release
	1. Target branch: `master`
	2. Tag: `vx.x` (Example: `v0.1`)
	3. Title: `Version x.x` (Example: `Version 0.1`)
	4. Copy changelogs
	5. Tag all related issues
12. Bump!!
13. Close this version issues
14. Close milestone
15. Close project
16. Generate HTML files
	1. Run `otherfile/doc_to_html.bat`
	2. Copy `doc_html` folder for the next steps
17. Update website
	1. `git checkout gh-pages`
	2. Update all version tags
		1. `index.html`
	3. Update fonts list
		1. Update `FontList.html` (Step **16.2**)
	4. Update arts list
		1. Update `ArtList.html` (Step **16.2**)
	5. Update decors list
		1. Update `DecorList.html` (Step **16.2**)
	6. Update all font counters in `index.html` (**If needed**)
		1. `<img src="https://img.shields.io/badge/Font List-{font_counter}-blue.svg" alt="Font List">`
		2. `<td id="font_counter">{font_counter}</td>`
	7. Update all art counters in `index.html` (**If needed**)
		1. `<img src="https://img.shields.io/badge/Art List-{art_counter}-orange.svg" alt="Art List">`
		2. `<td id="art_counter">{art_counter}</td>`
	8. Update all decor counters in `index.html` (**If needed**)
		1. `<img src="https://img.shields.io/badge/Decor List-{decor_counter}-green.svg" alt="Decor List">`
		2. `<td id="decor_counter">{decor_counter}</td>`

	9. Update `Reference` section (**If needed**)
	10. Update code examples (**If needed**)
		1. [http://www.hilite.me](http://www.hilite.me)
		2. Python console session
		3. Colorful
		4. Line numbers