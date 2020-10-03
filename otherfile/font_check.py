# -*- coding: utf-8 -*-
"""Fonts height, duplication and UTF-8 compatibility testing script."""
import sys
import art
from art.art_param import NON_ASCII_FONTS
from font_wizard import is_utf8, is_ascii

Failed1 = 0
Failed2 = 0
Failed3 = 0
Font_List = list(art.art_param.FONT_MAP.keys())
Message1 = "Font height test "
Message2 = "Font duplication test "
Message3 = "Font UTF-8 compatibility test "
Message4 = "{0}-font duplication -- > {1},{2}"


def print_result(flag_list, message_list):
    """
    Print final result.

    :param flag_list: list of test flags
    :type flag_list: list
    :param message_list: list of test messages
    :type message_list: list
    :return: None
    """
    print("art version : {}\n".format(art.__version__))
    for index, flag in enumerate(flag_list):
        if flag == 0:
            print(message_list[index] + "passed!")
        else:
            print(message_list[index] + "failed!")


if __name__ == "__main__":
    for font in Font_List:
        s = []
        l = ""
        for letter in art.get_font_dic(font).keys():
            if len(art.get_font_dic(font)[letter]) != 0:
                s.append(
                    len(art.get_font_dic(font)[letter].split("\n")))
            l += art.get_font_dic(font)[letter]
        ascii_flag = is_ascii(l)
        if len(set(s)) != 1:
            print("Height error in font : " + font)
            Failed1 += 1
        if not is_utf8(l):
            Failed3 += 1
            print("UTF-8 compatibility error in font : " + font)
        if ascii_flag and font in NON_ASCII_FONTS:
            print(
                "Font type warning : {0} is ASCII but imported as NON-ASCII".format(font))
        if not ascii_flag and font not in NON_ASCII_FONTS:
            print(
                "Font type warning : {0} is NON-ASCII but imported as ASCII".format(font))

    for font1 in Font_List:
        for font2 in Font_List:
            if Font_List.index(font1) < Font_List.index(font2):
                if len(
                        art.get_font_dic(font1)) == len(
                        art.get_font_dic(font2)):
                    if art.get_font_dic(font1) == art.get_font_dic(font2):
                        Failed2 += 1
                        print(Message4.format(str(Failed2), font1, font2))
                else:
                    font1_keys = set(art.get_font_dic(font1).keys())
                    font2_keys = set(art.get_font_dic(font2).keys())
                    inter_keys = list(font1_keys.intersection(font2_keys))
                    font1_map = []
                    font2_map = []
                    for letter in inter_keys:
                        font1_map.append(art.get_font_dic(font1)[letter])
                        font2_map.append(art.get_font_dic(font2)[letter])
                    if font1_map == font2_map:
                        Failed2 += 1
                        print(Message4.format(str(Failed2), font1, font2))
    print_result([Failed1, Failed2, Failed3], [Message1, Message2, Message3])
    sys.exit(Failed2 + Failed1 + Failed3)
