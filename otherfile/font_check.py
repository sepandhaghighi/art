# -*- coding: utf-8 -*-
"""Fonts height and duplication testing script."""
import sys
from art.art_param import *
from art.art_dic import *

Failed1 = 0
Failed2 = 0
Font_List = list(FONT_MAP.keys())
Message1 = "Font height test "
Message2 = "Font duplication test "
for font in Font_List:
    s = []
    for letter in FONT_MAP[font][0].keys():
        if len(FONT_MAP[font][0][letter]) != 0:
            s.append(len(FONT_MAP[font][0][letter].split("\n")))
    if len(set(s)) != 1:
        print("Height error in font : " + font)
        Failed1 += 1


if Failed1 == 0:
    print(Message1 + "passed!")
else:
    print(Message1 + "failed!")

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

if Failed2 == 0:
    print(Message2 + "passed!")
else:
    print(Message2 + "failed!")

sys.exit(Failed2 + Failed1)
