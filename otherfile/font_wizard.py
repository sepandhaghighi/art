# -*- coding: utf-8 -*-
"""Wizard script for new fonts."""
import string
import sys
import ast
import art

Letters = string.ascii_letters + string.punctuation + string.digits
Font_List = list(art.art_param.FONT_MAP.keys())

Error1 = "[Error] Font data is empty!"
Error2 = "[Error] Font should support 95 printable ASCII characters, please check font data!"
Error3 = "[Error] Font duplication (art version : {}) -- > ".format(
    art.__version__)
Error4 = "[Error] All letters should have same height"
Error5 = "[Error] Font should be compatible with UTF-8"
Error6 = "[Error] This font name is not available"


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
        if font_name in Font_List:
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
    if " " not in font_dic.keys():
        font_dic[" "] = " "
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
    s = []
    for letter in font_dic.keys():
        if len(font_dic[letter]) != 0:
            s.append(len(font_dic[letter].split("\n")))
    if len(set(s)) != 1:
        print(Error4)
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
    else:
        print(Error2)
