# -*- coding: utf-8 -*-
"""Wizard script for new fonts."""
import string
import sys
import ast
import art

Letters = string.ascii_letters + string.punctuation + string.digits
Font_List = list(art.art_param.FONT_MAP.keys())

INVALID_FONT_NAME = [
    "mix",
    "wizard",
    "wiz",
    "magic",
    "random",
    "random-na",
    "random-xlarge",
    "random-large",
    "random-medium",
    "random-small",
    "rand",
    "rand-na",
    "rand-xlarge",
    "rand-large",
    "rand-medium",
    "rand-small",
    "rnd",
    "rnd-na",
    "rnd-xlarge",
    "rnd-large",
    "rnd-medium",
    "rnd-small"]

Error1 = "[Error] Font data is empty!"
Error2 = "[Error] Font should support 95 printable ASCII characters, please check font data!"
Error3 = "[Error] Font duplication (art version : {}) -- > ".format(
    art.__version__)
Error4 = "[Error] All letters should have same height"
Error5 = "[Error] Font should be compatible with UTF-8"
Error6 = "[Error] This font name is not available"
Error7 = "[Error] All lines in a letter should have same width (letter : {0})"


def is_utf8(s):
    """
    Check input string for UTF-8 compatibility.

    :param s: input string
    :type s: str
    :return: result as bool
    """
    try:
        if sys.version_info.major == 3:
            _ = bytes(s, 'utf-8').decode('utf-8', 'strict')
        else:
            return True
        return True
    except Exception:
        return False


def is_ascii(s):
    """
    Check input string for ASCII compatibility.

    :param s: input string
    :type s: str
    :return: result as bool
    """
    for i in s:
        if ord(i) > 127:
            return False
    return True


if __name__ == "__main__":
    art.tprint("Font Wizard")
    print("Use this string as input for font resource : ")
    print(Letters)
    print("*" * 30)
    while(True):
        font_name = input("Please enter font name : ")
        if font_name in Font_List or font_name.lower() in INVALID_FONT_NAME:
            print(Error6)
        else:
            break
    font_data = input("Please enter font data (string or list) : ")
    if not is_utf8(font_data):
        print(Error5)
        sys.exit()
    ascii_flag = "ASCII" if is_ascii(font_data) else "Non-ASCII"
    if len(font_data) == 0:
        print(Error1)
        sys.exit()
    if len(font_data) != len(Letters):
        try:
            font_data = ast.literal_eval(font_data)
            if len(font_data) != len(Letters):
                print(Error2)
                sys.exit()
        except Exception:
            print(Error2)
            sys.exit()
    font_dic = dict(zip(Letters, font_data))
    font_height_list = list(
        map(lambda x: len(x.split("\n")), font_dic.values()))
    if len(set(font_height_list)) != 1:
        print(Error4)
        sys.exit()
    font_height = font_height_list[0]
    if " " not in font_dic.keys():
        _ = [" "] * font_height
        font_dic[" "] = "\n".join(_)
    for font2 in Font_List:
        if len(font_dic) == len(art.get_font_dic(font2)):
            if font_dic == art.get_font_dic(font2):
                print(Error3 + font2)
                sys.exit()
        else:
            font1_keys = set(font_dic.keys())
            font2_keys = set(art.get_font_dic(font2).keys())
            inter_keys = list(font1_keys.intersection(font2_keys))
            font1_map = []
            font2_map = []
            for letter in inter_keys:
                font1_map.append(font_dic[letter])
                font2_map.append(art.get_font_dic(font2)[letter])
            if font1_map == font2_map:
                print(Error3 + font2)
                sys.exit()
    first_line_list = list(map(lambda x: x.split(
        "\n")[0] in ["", " "], font_dic.values()))
    last_line_list = list(map(lambda x: x.split(
        "\n")[-1] in ["", " "], font_dic.values()))
    for letter in font_dic.keys():
        letter_data = font_dic[letter]
        letter_data_split = letter_data.split("\n")
        width_list = list(map(len, letter_data_split))
        if letter_data_split[-1] in ["", " "] and all(last_line_list):
            width_list = width_list[:-1]
        if len(width_list) > 0 and letter_data_split[0] in [
                "", " "] and all(first_line_list):
            width_list = width_list[1:]
        if len(set(width_list)) > 1:
            print(Error7.format(letter))
            sys.exit()
    if len(font_dic) == 95:
        print("Done!")
        print("Font dictionary : \n")
        print("{}_dic = ".format(font_name), font_dic)
        print("- Add this dictionary to the end of text_dic3.py")
        print("- This font is {0} : ".format(ascii_flag))
        print('\t1. Add "{0}":[{0}_dic,False] to the end of FONT_MAP dictionary in art_param.py'.format(
            font_name))
        if ascii_flag == "ASCII":
            print("\t2. Add a new test case to test.py")
        else:
            print("\t2. Add a new test case to test2.py")
            print('\t3. Add "{0}" to the end of NON_ASCII_FONTS list in art_param.py'.format(
                font_name))
            if font_height > 1:
                print('\t4. Add "{0}" to the end of MIX_FILTERED_FONTS list in art_param.py'.format(
                    font_name))
    else:
        print(Error2)
