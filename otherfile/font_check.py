# -*- coding: utf-8 -*-
"""Fonts height checking script."""
import sys
from art import *

Failed = 0

for font in FONT_MAP.keys():
    s = []
    for letter in FONT_MAP[font][0].keys():
        if len(FONT_MAP[font][0][letter]) != 0:
            s.append(len(FONT_MAP[font][0][letter].split("\n")))
    if len(set(s)) != 1:
        print("Height error in font : " + font)
        Failed += 1

if Failed == 0:
    sys.exit(0)
else:
    sys.exit(1)