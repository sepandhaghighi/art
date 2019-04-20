# -*- coding: utf-8 -*-
"""Art module."""
from .art_dic import *
from .art_param import *
import os
import sys
import random
import codecs


class artError(Exception):  # pragma: no cover
    """Art error class."""

    pass


def font_size_splitter(font_map):
    """
    Split fonts to 4 category (small,medium,large,xlarge) by maximum length of letter in each font.

    :param font_map: input fontmap
    :type font_map : dict
    :return: splitted fonts as dict
    """
    small_font = []
    medium_font = []
    large_font = []
    xlarge_font = []
    fonts = set(font_map.keys()) - set(RANDOM_FILTERED_FONTS)
    for font in fonts:
        length = max(map(len, font_map[font][0].values()))
        if length <= FONT_SMALL_THRESHOLD:
            small_font.append(font)
        elif length > FONT_SMALL_THRESHOLD and length <= FONT_MEDIUM_THRESHOLD:
            medium_font.append(font)
        elif length > FONT_MEDIUM_THRESHOLD and length <= FONT_LARGE_THRESHOLD:
            large_font.append(font)
        else:
            xlarge_font.append(font)
    return {
        "small_list": small_font,
        "medium_list": medium_font,
        "large_list": large_font,
        "xlarge_list": xlarge_font}


RND_SIZE_DICT = font_size_splitter(FONT_MAP)  # pragma: no cover


def line(char="*", number=30):
    """
    Print line of chars.

    :param char: input character
    :type char:str
    :param number: number of characters
    :return: None
    """
    print(char * number)


def font_list(text="test", test=False):
    """
    Print all fonts.

    :param text : input text
    :type text : str
    :param test: test flag
    :type test: bool
    :return: None
    """
    fonts = set(FONT_MAP.keys())
    if test:
        fonts = fonts - set(TEST_FILTERED_FONTS)
    for item in sorted(list(fonts)):
        print(str(item) + " : ")
        text_temp = text
        try:
            tprint(text_temp, str(item))
        except Exception:
            print(FONT_ENVIRONMENT_WARNING)


def art_list(test=False):
    """
    Print all 1-Line arts.

    :param test : exception test flag
    :type test : bool
    :return: None
    """
    for i in sorted(list(art_dic.keys())):
        try:
            if test:
                raise Exception
            print(i)
            aprint(i)
            line()
        except Exception:
            print(ART_ENVIRONMENT_WARNING)
            line()
            if test:
                break


def help_func():
    """
    Print help page.

    :return: None
    """
    tprint("art")
    tprint("v" + VERSION)
    print(DESCRIPTION + "\n")
    print("Webpage : http://art.shaghighi.ir\n")
    print("Help : \n")
    print("     - list --> (list of arts)\n")
    print("     - fonts --> (list of fonts)\n")
    print("     - test --> (run tests)\n")
    print("     - text 'yourtext' 'font(optional)' --> (text art) Example : 'python -m art text exampletext block'\n")
    print("     - shape 'shapename' --> (shape art) Example : 'python -m art shape butterfly'\n")
    print("     - save 'yourtext' 'font(optional)'  -->  Example : 'python -m art save exampletext block'\n")
    print("     - all 'yourtext'  -->  Example : 'python -m art all exampletext'")


def aprint(artname, number=1, text=""):
    """
    Print 1-line art.

    :param artname: artname
    :type artname : str
    :return: None
    """
    print(art(artname=artname, number=number, text=text))


def art(artname, number=1, text=""):
    """
    Return 1-line art.

    :param artname: artname
    :type artname : str
    :return: ascii art as str
    """
    if isinstance(artname, str) is False:
        raise artError(ART_TYPE_ERROR)
    artname = artname.lower()
    arts = sorted(art_dic.keys())
    if artname == "random" or artname == "rand" or artname == "rnd":
        filtered_arts = list(set(arts) - set(RANDOM_FILTERED_ARTS))
        artname = random.choice(filtered_arts)
    elif artname not in art_dic.keys():
        distance_list = list(map(lambda x: distance_calc(artname, x),
                                 arts))
        min_distance = min(distance_list)
        selected_art = arts[distance_list.index(min_distance)]
        threshold = max(len(artname), len(selected_art)) / 2
        if min_distance < threshold:
            artname = selected_art
        else:
            raise artError(ART_NAME_ERROR)
    art_value = art_dic[artname]
    if isinstance(number, int) is False:
        raise artError(NUMBER_TYPE_ERROR)
    if isinstance(art_value, str):
        return (art_value + " ") * number
    if isinstance(text, str) is False:
        raise artError(TEXT_TYPE_ERROR)
    return (art_value[0] + text + art_value[1] + " ") * number


def randart():
    """
    Return random 1-line art.

    :return: ascii art as str
    """
    return art("random")


def tprint(text, font=DEFAULT_FONT, chr_ignore=True):
    r"""
    Print art text (support \n).

    :param text: input text
    :type text:str
    :param font: input font
    :type font:str
    :param chr_ignore: ignore not supported character
    :type chr_ignore:bool
    :return: None
    """
    result = text2art(text, font=font, chr_ignore=chr_ignore)
    print(result)


def tsave(
        text,
        font=DEFAULT_FONT,
        filename="art",
        chr_ignore=True,
        print_status=True):
    r"""
    Save ascii art (support \n).

    :param text: input text
    :param font: input font
    :type font:str
    :type text:str
    :param filename: output file name
    :type filename:str
    :param chr_ignore: ignore not supported character
    :type chr_ignore:bool
    :param print_status : save message print flag
    :type print_status:bool
    :return: None
    """
    try:
        if isinstance(text, str) is False:
            raise Exception(TEXT_TYPE_ERROR)
        files_list = os.listdir(os.getcwd())
        extension = ".txt"
        splitted_filename = filename.split(".")
        name = splitted_filename[0]
        if len(splitted_filename) > 1:
            extension = "." + splitted_filename[1]
        index = 2
        test_name = name
        while(True):
            if test_name + extension in files_list:
                test_name = name + str(index)
                index = index + 1
            else:
                break
        if font.lower() in TEST_FILTERED_FONTS:
            file = codecs.open(test_name + extension, "w", encoding='utf-8')
        else:
            file = open(test_name + extension, "w")
        result = text2art(text, font=font, chr_ignore=chr_ignore)
        file.write(result)
        file.close()
        if print_status:
            print("Saved! \nFilename: " + test_name + extension)
        return {"Status": True, "Message": "OK"}
    except Exception as e:
        return {"Status": False, "Message": str(e)}


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
    elif text_length > TEXT_XLARGE_THRESHOLD and text_length <= TEXT_LARGE_THRESHOLD:
        font = random.choice(LARGE_WIZARD_FONT)
    elif text_length > TEXT_LARGE_THRESHOLD and text_length <= TEXT_MEDIUM_THRESHOLD:
        font = random.choice(MEDIUM_WIZARD_FONT)
    else:
        font = random.choice(SMALL_WIZARD_FONT)
    return font


def indirect_font(font, fonts, text):
    """
    Check input font for indirect modes.

    :param font: input font
    :type font : str
    :param fonts: fonts list
    :type fonts : list
    :param text: input text
    :type text:str
    :return: font as str
    """
    if font == "rnd-small" or font == "random-small" or font == "rand-small":
        font = random.choice(RND_SIZE_DICT["small_list"])
        return font
    if font == "rnd-medium" or font == "random-medium" or font == "rand-medium":
        font = random.choice(RND_SIZE_DICT["medium_list"])
        return font
    if font == "rnd-large" or font == "random-large" or font == "rand-large":
        font = random.choice(RND_SIZE_DICT["large_list"])
        return font
    if font == "rnd-xlarge" or font == "random-xlarge" or font == "rand-xlarge":
        font = random.choice(RND_SIZE_DICT["xlarge_list"])
        return font
    if font == "random" or font == "rand" or font == "rnd":
        filtered_fonts = list(set(fonts) - set(RANDOM_FILTERED_FONTS))
        font = random.choice(filtered_fonts)
        return font
    if font == "wizard" or font == "wiz" or font == "magic":
        font = wizard_font(text)
        return font
    if font == "rnd-na" or font == "random-na" or font == "rand-na":
        font = random.choice(TEST_FILTERED_FONTS)
        return font
    if font not in FONT_MAP.keys():
        distance_list = list(map(lambda x: distance_calc(font, x), fonts))
        font = fonts[distance_list.index(min(distance_list))]
    return font


def __word2art(word, font, chr_ignore, letters):
    """
    Return art word.

    :param word: input word
    :type word: str
    :param font: input font
    :type font: str
    :param chr_ignore: ignore not supported character
    :type chr_ignore: bool
    :param letters: font letters table
    :type letters: dict
    :return: ascii art as str
    """
    split_list = []
    result_list = []
    splitter = "\n"
    for i in word:
        if (ord(i) == 9) or (ord(i) == 32 and font == "block"):
            continue
        if (i not in letters.keys()):
            if (chr_ignore):
                continue
            else:
                raise artError(str(i) + " is invalid.")
        if len(letters[i]) == 0:
            continue
        split_list.append(letters[i].split("\n"))
    if font in ["mirror", "mirror_flip"]:
        split_list.reverse()
    if len(split_list) == 0:
        return ""
    for i in range(len(split_list[0])):
        temp = ""
        for j in range(len(split_list)):
            if j > 0 and (
                    i == 1 or i == len(
                        split_list[0]) -
                    2) and font == "block":
                temp = temp + " "
            temp = temp + split_list[j][i]
        result_list.append(temp)
    if "win32" != sys.platform:
        splitter = "\r\n"
    result = (splitter).join(result_list)
    if result[-1] != "\n":
        result += splitter
    return result


def text2art(text, font=DEFAULT_FONT, chr_ignore=True):
    r"""
    Return art text (support \n).

    :param text: input text
    :type text:str
    :param font: input font
    :type font:str
    :param chr_ignore: ignore not supported character
    :type chr_ignore:bool
    :return: ascii art text as str
    """
    letters = standard_dic
    text_temp = text
    if isinstance(text, str) is False:
        raise artError(TEXT_TYPE_ERROR)
    if isinstance(font, str) is False:
        raise artError(FONT_TYPE_ERROR)
    font = font.lower()
    fonts = sorted(FONT_MAP.keys())
    font = indirect_font(font, fonts, text)
    letters = FONT_MAP[font][0]
    if FONT_MAP[font][1]:
        text_temp = text.lower()
    if font in UPPERCASE_FONTS:
        text_temp = text.upper()
    word_list = text_temp.split("\n")
    result = ""
    for word in word_list:
        if len(word) != 0:
            result = result + __word2art(word=word,
                                         font=font,
                                         chr_ignore=chr_ignore,
                                         letters=letters)
    return result


def set_default(font=DEFAULT_FONT, chr_ignore=True, filename="art",
                print_status=True):
    """
    Change text2art, tprint and tsave default values.

    :param font: input font
    :type font:str
    :param chr_ignore: ignore not supported character
    :type chr_ignore:bool
    :param filename: output file name (only tsave)
    :type filename:str
    :param print_status : save message print flag (only tsave)
    :type print_status:bool
    :return: None
    """
    if isinstance(font, str) is False:
        raise artError(FONT_TYPE_ERROR)
    if isinstance(chr_ignore, bool) is False:
        raise artError(CHR_IGNORE_TYPE_ERROR)
    if isinstance(filename, str) is False:
        raise artError(FILE_TYPE_ERROR)
    if isinstance(print_status, bool) is False:
        raise artError(PRINT_STATUS_TYPE_ERROR)
    tprint.__defaults__ = (font, chr_ignore)
    tsave.__defaults__ = (font, filename, chr_ignore, print_status)
    text2art.__defaults__ = (font, chr_ignore)
