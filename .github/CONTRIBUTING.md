# Contribution

**Last Update: 2024-09-14**		

Changes and improvements are more than welcome! ❤️ Feel free to fork and open a pull request.

Please consider the following :

1. Fork it!
2. Create your feature branch (under `dev` branch)
3. Add your new features or fix detected bugs
	- To add a new font visit [here](#font)
	- To add a new 1-line art visit [here](#1-line-art)
	- To add a new decoration visit [here](#decoration)
4. Add standard `docstring` to your functions
5. Add tests for new features (`doctest`)
	- **ASCII** fonts/arts in `tests/test.py`
	- Other in `tests/test2.py`
6. Update `README.md` (if needed)
7. Pass all CI tests
8. Update `CHANGELOG.md`
	- Describe changes under `[Unreleased]` section
9. Update `AUTHORS.md`
	- Add your name under `# Other Contributors #` section
10. Submit a pull request into `dev` (please complete the pull request template)

⚠️ If you want to suggest fonts and arts, visit [this issue](https://github.com/sepandhaghighi/art/issues/59)

## Font

1. Select a non-duplicate name
2. Add new font data as a dictionary to the end of `data/fonts3.py` (support 95 printable **ASCII** characters)
	- You can use `font_wizard.py` in `otherfile` folder (need to install latest version of `art` package)
3. Map font name and data in `FONT_MAP` dictionary
4. Select case sensitive mode in `FONT_MAP` dictionary
	- `False` : If font is case sensitive (Example : ```"eftiwater": [eftiwater_dic, False]```)
	- `True` : If font is not case sensitive (Example : ```"poison": [poison_dic, True]```)
	- This is an *optional* step for memory saving, if you haven't removed capital letters from font data, you can simply select case sensitive mode
5. If font only support capital letters:
	- Add font name to `UPPERCASE_FONTS`
6. If font is **Non-ASCII**:
	- Add font name to `NON_ASCII_FONTS` list
	- Add a test case to `tests/test2.py` (*Alphabetical order*)
	- Add font name to `MIX_FILTERED_FONTS` list to remove it from mix mode (*Optional*)
7. If font is **ASCII**:
	- Add a test case to `tests/test.py` (*Alphabetical order*)  
	- Add font name to `RANDOM_FILTERED_FONTS` list to remove it from random modes (*Optional*)
8. Re-run `FontList.ipynb`
	- Before this step you should re-install `art` package : ```pip install .```
9. Update 2 font counters in `README.md`
	- Badge section
	- Overview section
10. Update `References` section in `README.md`
11. Run `autopep8.bat`/`autopep8.sh` (*Optional*, need to install latest version of `autopep8` package)


## 1-Line art

1. Select a non-duplicate name
2. Add 1-line art to the end of ‍`art_dic` dictionary in `data/arts.py`
	- Add as string (Example : ```"1-line art name": "string"```)
3. If 1-line art is **Non-ASCII**:
	- Add 1-line art name to `NON_ASCII_ARTS` list
	- Add a test case to `tests/test2.py` (*Alphabetical order*)
4. If 1-line art is **ASCII**:
	- Add a test case to `tests/test.py` (*Alphabetical order*)
	- Add 1-line art name to `RANDOM_FILTERED_ARTS` list to remove it from random mode (*Optional*)
5. Re-run `ArtList.ipynb`
	- Before this step you should re-install `art` package : ```pip install .```
6. Update 2 art counters in `README.md`
	- Badge section
	- Overview section
7. Update `References` section in `README.md`

## Decoration

1. Select a non-duplicate name
2. Add new decoration data as a list to the end of `data/decorations.py`
3. Map decoration name and data in `DECORATIONS_MAP` dictionary
4. Add a test case to `tests/test2.py` (*Alphabetical order*)
5. Re-run `DecorList.ipynb`
	- Before this step you should re-install `art` package : ```pip install .```
6. Update 2 decor counters in `README.md`
	- Badge section
	- Overview section
7. Update `References` section in `README.md`
