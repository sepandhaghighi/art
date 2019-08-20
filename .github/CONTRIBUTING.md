# Contribution			

Changes and improvements are more than welcome! ❤️ Feel free to fork and open a pull request.

Please consider the following :

1. Fork it!
2. Create your feature branch (under `dev` branch)
3. Add your new features or fix detected bugs
	- To add a new font visit [here](#font)
	- To add a new 1-line art visit [here](#1-line-art)
4. Add standard `docstring` to your functions
5. Add tests for new features (`doctest`)
	- Non-ASCII fonts in `test2.py`
	- Other in `test.py`
6. Update `README.md` (if needed)
7. Pass all CI tests
8. Update `CHANGELOG.md`
	- Describe changes under `[Unreleased]` section
9. Submit a pull request into `dev` (please complete the pull request template)



## Font

1. Select a non-duplicate name
2. Add new font data as a dictionary to the end of `text_dic3.py` (support 95 printable ASCII characters)
	- You can use `font_wizard.py` in `otherfile` folder (need to install latest version of `art` package)
3. Map font name and data in `FONT_MAP` dictionary
4. Select case sensitive mode in `FONT_MAP` dictionary
	- `False` : If font is case sensitive (Example : ```"eftiwater": [eftiwater_dic, False]```)
	- `True` : If font is not case sensitive (Example : ```"poison": [poison_dic, True]```)
5. If font only support capital letters:
	- Add font name to `UPPERCASE_FONTS`
6. If font is Non-ASCII:
	- Add font name to `TEST_FILTERED_FONTS` list
	- Add font name to `RANDOM_FILTERED_FONTS` list
	- Add a test case to `test2.py` (*Alphabetical order*)
7. If font is ASCII:
	- Add a test case to `test.py` (*Alphabetical order*) 
8. Re-run `FontList.ipynb`
9. Update counters in `README.md`
10. Update `Reference` section in `README.md`
11. Run `autopep8.bat` (*Optional*, need to install latest version of `autopep8` package)


## 1-Line art

1. Select a non-duplicate name
2. Add 1-line art to the end of ‍`art_dic` dictionary in `art_dic.py`
3. If 1-line art is not bipartite:
	- Add as string (Example : ```"1-line art name": "string"```)
4. If 1-line art is bipartite:
	- Add as list (Example : ```"1-line art name": ["string1","string1"]```)
	- Add 1-line art name to `RANDOM_FILTERED_ARTS` list
5. Add a test case to `test.py` (*Alphabetical order*)  
6. Re-run `ArtList.ipynb`
7. Update counters in `README.md`
8. Update `Reference` section in `README.md`
