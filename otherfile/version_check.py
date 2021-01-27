# -*- coding: utf-8 -*-
"""Version-check script."""
import os
import sys
import codecs
from art.art_param import *

Failed = 0
VERSION = "5.1"

README_ITEMS = ['<td align="center">{0}</td>'.format(str(FONT_COUNTER)),
                '<img src="https://img.shields.io/badge/Art List-{0}-orange.svg">'.format(str(ART_COUNTER)),
                '<img src="https://img.shields.io/badge/Font List-{0}-blue.svg">'.format(str(FONT_COUNTER)),
                '<td align="center">{0}</td>'.format(str(ART_COUNTER)),
                '<td align="center">{0}</td>'.format(str(DECORATION_COUNTER)),
                '<img src="https://img.shields.io/badge/Decor List-{0}-green.svg">'.format(str(DECORATION_COUNTER))]

SETUP_ITEMS = [
    "version='{0}'"]
INSTALL_ITEMS = [
    "[Version {0}](https://github.com/sepandhaghighi/art/archive/v{0}.zip)",
    "pip install art=={0}",
    "pip3 install art=={0}",
    'easy_install "art=={0}"']
CHANGELOG_ITEMS = [
    "## [{0}]",
    "https://github.com/sepandhaghighi/art/compare/v{0}...dev",
    "[{0}]:"]
ART_LIST_ITEMS = ["### Version : {0}"]
FONT_LIST_ITEMS = ["### Version : {0}"]
PARAMS_ITEMS = ['ART_VERSION = "{0}"']
FILES = {
    "setup.py": SETUP_ITEMS,
    "INSTALL.md": INSTALL_ITEMS,
    "CHANGELOG.md": CHANGELOG_ITEMS,
    "FontList.ipynb": FONT_LIST_ITEMS,
    "ArtList.ipynb": ART_LIST_ITEMS,
    os.path.join(
        "art",
        "art_param.py"): PARAMS_ITEMS}

TEST_NUMBER = len(FILES.keys()) + 1


def print_result(failed=False):
    """
    Print final result.

    :param failed: failed flag
    :type failed: bool
    :return: None
    """
    message = "Version/Counter tag tests "
    if not failed:
        print("\n" + message + "passed!")
    else:
        print("\n" + message + "failed!")
    print("Passed : " + str(TEST_NUMBER - Failed) + "/" + str(TEST_NUMBER))


if __name__ == "__main__":
    for file_name in FILES.keys():
        try:
            file_content = codecs.open(
                file_name, "r", "utf-8", "ignore").read()
            for test_item in FILES[file_name]:
                if file_content.find(test_item.format(VERSION)) == -1:
                    print("Incorrect version tag in " + file_name)
                    Failed += 1
                    break
        except Exception as e:
            Failed += 1
            print("Error in " + file_name + "\n" + "Message : " + str(e))

    try:
        readme_file_content = codecs.open(
            "README.md", "r", "utf-8", "ignore").read()
        for test_item in README_ITEMS:
            if readme_file_content.find(
                    test_item) == -1:
                print("Incorrect counter in " + "README.md")
                Failed += 1
                break
    except Exception as e:
        Failed += 1
        print("Error in README.md" + "\n" + "Message : " + str(e))
    if Failed == 0:
        print_result(False)
        sys.exit(0)
    else:
        print_result(True)
        sys.exit(1)
