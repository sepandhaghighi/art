# -*- coding: utf-8 -*-
"""Art utility module."""
import random

from .params import FONT_MAP
from .params import DECORATION_NAMES, FONT_NAMES, NON_ASCII_FONTS
from .params import RANDOM_FILTERED_FONTS
from .params import XLARGE_WIZARD_FONT, LARGE_WIZARD_FONT, MEDIUM_WIZARD_FONT, SMALL_WIZARD_FONT
from .params import FONT_SMALL_THRESHOLD, FONT_MEDIUM_THRESHOLD, FONT_LARGE_THRESHOLD, TEXT_XLARGE_THRESHOLD
from .params import TEXT_LARGE_THRESHOLD, TEXT_MEDIUM_THRESHOLD


def distance_calc(s1, s2):
    """
    Calculate Levenshtein distance between two words.

    :param s1: first word
    :type s1 : str
    :param s2: second word
    :type s2 : str
    :return: distance between two word

    References :
    1- https://stackoverflow.com/questions/2460177/edit-distance-in-python
    2- https://en.wikipedia.org/wiki/Levenshtein_distance
    """
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2 + 1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(
                    1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]


def wizard_font(text):
    """
    Check input text length for wizard mode.

    :param text: input text
    :type text:str
    :return: font as str
    """
    text_length = len(text)
    if text_length <= TEXT_XLARGE_THRESHOLD:
        font = random.choice(XLARGE_WIZARD_FONT)
    elif text_length <= TEXT_LARGE_THRESHOLD:
        font = random.choice(LARGE_WIZARD_FONT)
    elif text_length <= TEXT_MEDIUM_THRESHOLD:
        font = random.choice(MEDIUM_WIZARD_FONT)
    else:
        font = random.choice(SMALL_WIZARD_FONT)
    return font


def indirect_font(font, text):
    """
    Check input font for indirect modes.

    :param font: input font
    :type font : str
    :param text: input text
    :type text:str
    :return: font as str
    """
    fonts = FONT_NAMES
    if font in ["rnd-small", "random-small", "rand-small"]:
        font = random.choice(RND_SIZE_DICT["small_list"])
        return font
    if font in ["rnd-medium", "random-medium", "rand-medium"]:
        font = random.choice(RND_SIZE_DICT["medium_list"])
        return font
    if font in ["rnd-large", "random-large", "rand-large"]:
        font = random.choice(RND_SIZE_DICT["large_list"])
        return font
    if font in ["rnd-xlarge", "random-xlarge", "rand-xlarge"]:
        font = random.choice(RND_SIZE_DICT["xlarge_list"])
        return font
    if font in ["random", "rand", "rnd"]:
        filtered_fonts = list(set(fonts) - set(RANDOM_FILTERED_FONTS))
        font = random.choice(filtered_fonts)
        return font
    if font in ["wizard", "wiz", "magic"]:
        font = wizard_font(text)
        return font
    if font in ["rnd-na", "random-na", "rand-na"]:
        font = random.choice(NON_ASCII_FONTS)
        return font
    if font not in fonts:
        font = min(fonts, key=lambda x: distance_calc(font, x))
    return font


def indirect_decoration(decoration):
    """
    Check input decoration for indirect modes.

    :param decoration: input decoration
    :type decoration : str
    :return: decoration as str
    """
    decorations = DECORATION_NAMES
    if decoration in ["random", "rand", "rnd"]:
        decoration = random.choice(decorations)
        return decoration
    if decoration not in decorations:
        decoration = min(decorations, key=lambda x: distance_calc(decoration, x))
    return decoration


def font_size_splitter(font_map):
    """
    Split fonts to 4 category (small,medium,large,xlarge) by maximum length of letter in each font.

    :param font_map: input fontmap
    :type font_map : dict
    :return: splitted fonts as dict
    """
    small_font, medium_font, large_font, xlarge_font = [], [], [], []
    fonts = set(font_map) - set(RANDOM_FILTERED_FONTS)
    for font in sorted(fonts):
        length = max(len(x) for x in font_map[font][0].values())
        if length <= FONT_SMALL_THRESHOLD:
            small_font.append(font)
        elif length <= FONT_MEDIUM_THRESHOLD:
            medium_font.append(font)
        elif length <= FONT_LARGE_THRESHOLD:
            large_font.append(font)
        else:
            xlarge_font.append(font)
    return {
        "small_list": small_font,
        "medium_list": medium_font,
        "large_list": large_font,
        "xlarge_list": xlarge_font}


RND_SIZE_DICT = font_size_splitter(FONT_MAP)  # pragma: no cover
