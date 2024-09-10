# -*- coding: utf-8 -*-
"""Version-check script."""
import os
import sys
import codecs
from art.params import *

Failed = 0
VERSION = "6.2"

README_ITEMS = ['<td id="font_counter">{0}</td>'.format(str(FONT_COUNTER)),
                '<img src="https://img.shields.io/badge/Font List-{0}-blue.svg" alt="Font List">'.format(str(FONT_COUNTER)),
                '<td id="art_counter">{0}</td>'.format(str(ART_COUNTER)),
                '<img src="https://img.shields.io/badge/Art List-{0}-orange.svg" alt="Art List">'.format(str(ART_COUNTER)),
                '<td id="decor_counter">{0}</td>'.format(str(DECORATION_COUNTER)),
                '<img src="https://img.shields.io/badge/Decor List-{0}-green.svg" alt="Decor List">'.format(str(DECORATION_COUNTER))]

SETUP_ITEMS = [
    "version='{0}'"]
INSTALL_ITEMS = [
    "[Version {0}](https://github.com/sepandhaghighi/art/archive/v{0}.zip)",
    "pip install art=={0}"]
CHANGELOG_ITEMS = [
    "## [{0}]",
    "https://github.com/sepandhaghighi/art/compare/v{0}...dev",
    "[{0}]:"]
ART_LIST_ITEMS = ["### Version : {0}"]
FONT_LIST_ITEMS = ["### Version : {0}"]
PARAMS_ITEMS = ['ART_VERSION = "{0}"']
META_ITEMS = ['% set version = "{0}" %']
ISSUE_TEMPLATE_ITEMS = ["- Art {0}"]
SECURITY_ITEMS = ["| {0}           | :white_check_mark: |", "| < {0}         | :x:                |"]

FILES = {
    "setup.py": SETUP_ITEMS,
    "INSTALL.md": INSTALL_ITEMS,
    "CHANGELOG.md": CHANGELOG_ITEMS,
    "SECURITY.md": SECURITY_ITEMS,
    "FontList.ipynb": FONT_LIST_ITEMS,
    "ArtList.ipynb": ART_LIST_ITEMS,
    os.path.join(
        "art",
        "params.py"): PARAMS_ITEMS,
    os.path.join("otherfile", "meta.yaml"): META_ITEMS,
    os.path.join(".github", "ISSUE_TEMPLATE", "bug_report.yml"): ISSUE_TEMPLATE_ITEMS,
}

TEST_NUMBER = len(FILES) + 1


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
    for file_name, test_items in FILES.items():
        try:
            file_content = codecs.open(
                file_name, "r", "utf-8", "ignore").read()
            for test_item in test_items:
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
