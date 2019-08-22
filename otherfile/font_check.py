# -*- coding: utf-8 -*-
"""Fonts height, duplication and UTF-8 compatibility testing script."""
import sys
from art.art_param import *
from art.art_dic import *

Failed1 = 0
Failed2 = 0
Failed3 = 0
Font_List = list(FONT_MAP.keys())
Message1 = "Font height test "
Message2 = "Font duplication test "
Message3 = "Font UTF-8 compatibility test "

def is_utf8(s):
    """
    Check input string for UTF-8 compatibility.

    :param s: input string
    :type s: str
    :return: result as bool
    """
    try:
        x=bytes(s,'utf-8').decode('utf-8', 'strict')
        return True
    except Exception:
        return False

def print_result():
    """
    Print final result.

    :return: None
    """
    message_list = [Message1,Message2,Message3]
    flag_list = [Failed1,Failed1,Failed1]
    for index,flag in enumerate(flag_list):
        if flag == 0:
            print(message_list[index] + "passed!")
        else:
            print(message_list[index] + "failed!")


for font in Font_List:
    s = []
    l = ""
    for letter in FONT_MAP[font][0].keys():
        if len(FONT_MAP[font][0][letter]) != 0:
            s.append(len(FONT_MAP[font][0][letter].split("\n")))
        l += FONT_MAP[font][0][letter]
    if len(set(s)) != 1:
        print("Height error in font : " + font)
        Failed1 += 1
    if not is_utf8(l):
        Failed3 +=1
        print("UTF-8 compatibility error in font : " + font)

for font1 in Font_List:
    for font2 in Font_List:
        if Font_List.index(font1) < Font_List.index(font2):
            if FONT_MAP[font1][0] == FONT_MAP[font2][0]:
                Failed2 += 1
                print(
                    str(Failed2) +
                    "-font duplication -- > " +
                    font1 +
                    "," +
                    font2)

print_result()
sys.exit(Failed2 + Failed1 + Failed3)
