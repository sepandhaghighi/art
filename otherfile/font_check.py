# -*- coding: utf-8 -*-
"""Fonts height testing script."""
import sys
from art.art_param import *

Failed = 0

for font in FONT_MAP.keys():
    s = []
    for letter in FONT_MAP[font][0].keys():
        if len(FONT_MAP[font][0][letter]) != 0:
            s.append(len(FONT_MAP[font][0][letter].split("\n")))
    if len(set(s)) != 1:
        print("Height error in font : " + font)
        Failed += 1

Message = "Font height test "
if Failed == 0:
    print(Message + "passed!")
    sys.exit(0)
else:
    print(Message + "failed!")
    sys.exit(1)
