## Contribution			

Changes and improvements are more than welcome! ❤️ Feel free to fork and open a pull request.

Please consider the following :

1. Fork it!
2. Create your feature branch (under `dev` branch)
3. Add standard `docstring` to your functions
4. Add tests for new features (`doctest`)
	- Non-ASCII fonts in `test2.py`
	- Other in `test.py`
5. Pass all CI tests
6. Update `CHANGELOG.md`
	- Describe changes under `[Unreleased]` section
7. Submit a pull request into `dev` (please complete the pull request template)


### New font notes

1. Add new font data as a dictionary to the end of `text_dic3.py` (support 95 printable ASCII characters)
2. Map font name and data in `FONT_MAP` dictionary
3. Select case sensitive mode in `FONT_MAP` dictionary
	- `False` : If font is case sensitive
	- `True` : If font is not case sensitive
4. If font only support capital letters:
	- Add font name to `UPPERCASE_FONTS`
5. If font is Non-ASCII:
	- Add font name to `TEST_FILTERED_FONTS` list
	- Add font name to `RANDOM_FILTERED_FONTS` list
	- Add test case to `test2.py`
6. If font is ASCII:
	- Add test case to `test.py` 
7. Update `FontList.ipynb`
8. Update counters in `README.md`


