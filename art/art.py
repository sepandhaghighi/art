# -*- coding: utf-8 -*-
from .art_dic import *
from .art_param import *
import os
import sys
import random


class artError(Exception):  # pragma: no cover
    pass


def font_size_splitter(font_map):
    '''
    This function split fonts to 4 category (small,medium,large,xlarge) by maximum length of letter in each font
    :param font_map: input fontmap
    :type font_map : dict
    :return: splitted fonts as dict
    '''
    small_font = []
    medium_font = []
    large_font = []
    xlarge_font = []
    for font in font_map.keys():
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
    '''
    This function print line of chars
    :param char: input character
    :type char:str
    :param number: number of characters
    :return: None
    '''
    print(char * number)


def font_list(text="test", test_mode=False):
    '''
    This function print all Of fonts
    :param text : input text
    :type text : str
    :param test_mode : test mode activation flag
    :type test_mode : bool
    :return: None
    '''
    for item in sorted(list(FONT_MAP.keys())):
        print(str(item) + " : ")
        text_temp = text
        if test_mode:
            if str(item) in ["char4", "c2", "war_of_w", "coil_cop", "fbr12"]:
                text_temp = text_temp.upper()
        tprint(text_temp, str(item))


def art_list(test=False):
    '''
    This function print all Of 1-Line arts
    :param test : exception test flag
    :type test : bool
    :return: None
    '''
    for i in sorted(list(art_dic.keys())):
        try:
            if test:
                raise Exception
            print(i)
            aprint(i)
            line()
        except Exception:
            print("[Warning] This art is not printable in this environment")
            line()
            if test:
                break


def help_func():
    '''
    Print help page
    :return: None
    '''
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
    '''
    Art print
    This function print ascii art
    :param artname: artname
    :type artname : str
    :return: None
    '''
    print(art(artname=artname, number=number, text=text))


def art(artname, number=1, text=""):
    '''
    This function return ascii art
    :param artname: artname
    :type artname : str
    :return: ascii art as str
    '''
    if isinstance(artname, str) is False:
        raise artError("artname shoud have str type")
    artname = artname.lower()
    arts = sorted(art_dic.keys())
    if artname == "random" or artname == "rand":
        artname = random.choice(arts)
    elif artname not in art_dic.keys():
        distance_list = list(map(lambda x: distance_calc(artname, x),
                                 arts))
        min_distance = min(distance_list)
        if min_distance < (len(artname)/2):
            artname = arts[distance_list.index(min_distance)]
        else:
            raise artError("Invalid art name")
    art_value = art_dic[artname]
    if isinstance(number, int) is False:
        raise artError("number should have int type")
    if isinstance(art_value, str):
        return (art_value + " ") * number
    if isinstance(text, str) is False:
        raise artError("text should have str type")
    return (art_value[0] + text + art_value[1] + " ") * number


def randart():
    '''
    This function return random 1-line art
    :return: ascii art as str
    '''
    return art("random")


def tprint(text, font=DEFAULT_FONT, chr_ignore=True):
    '''
    This function split function by \n then call text2art function
    :param text: input text
    :type text:str
    :param font: input font
    :type font:str
    :param chr_ignore: ignore not supported character
    :type chr_ignore:bool
    :return: None
    '''
    if isinstance(text, str) is False:
        raise artError("text should have str type")
    split_list = text.split("\n")
    result = ""
    for item in split_list:
        if len(item) != 0:
            result = result + text2art(item, font=font, chr_ignore=chr_ignore)
    print(result)


def tsave(
        text,
        font=DEFAULT_FONT,
        filename="art",
        chr_ignore=True,
        print_status=True):
    '''
    This function save ascii art
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
    '''
    try:
        split_list = text.split("\n")
        files_list = os.listdir(os.getcwd())
        extension = ".txt"
        splited_filename = filename.split(".")
        name = splited_filename[0]
        if len(splited_filename) > 1:
            extension = "." + splited_filename[1]
        index = 2
        test_name = name
        while(True):
            if test_name + extension in files_list:
                test_name = name + str(index)
                index = index + 1
            else:
                break
        file = open(test_name + extension, "w")
        result = ""
        for item in split_list:
            if len(item) != 0:
                result = result + \
                    text2art(item, font=font, chr_ignore=chr_ignore)
        file.write(result)
        file.close()
        if print_status:
            print("Saved! \nFilename: " + test_name + extension)
        return {"Status": True, "Message": "OK"}
    except Exception as e:
        return {"Status": False, "Message": str(e)}


def distance_calc(s1, s2):
    '''
    This function calculate Levenshtein distance between two words
    :param s1: first word
    :type s1 : str
    :param s2: second word
    :type s2 : str
    :return: distance between two word

    References :
    1- https://stackoverflow.com/questions/2460177/edit-distance-in-python
    2- https://en.wikipedia.org/wiki/Levenshtein_distance
    '''
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
    '''
    This function check input text length for wizard mode
    :param text: input text
    :type text:str
    :return: font as str
    '''
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
    '''
    This function check input font for indirect modes
    :param font: input font
    :type font : str
    :param fonts: fonts list
    :type fonts : list
    :param text: input text
    :type text:str
    :return: font as str
    '''
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
        font = random.choice(fonts)
        return font
    if font == "wizard" or font == "wiz" or font == "magic":
        font = wizard_font(text)
        return font
    if font not in FONT_MAP.keys():
        distance_list = list(map(lambda x: distance_calc(font, x), fonts))
        font = fonts[distance_list.index(min(distance_list))]
    return font


def text2art(text, font=DEFAULT_FONT, chr_ignore=True):
    '''
    This function print art text
    :param text: input text
    :type text:str
    :param font: input font
    :type font:str
    :param chr_ignore: ignore not supported character
    :type chr_ignore:bool
    :return: ascii art text as str
    '''
    split_list = []
    result_list = []
    letters = standard_dic
    text_temp = text
    spliter = "\n"
    if isinstance(text, str) is False:
        raise artError("text should have str type")
    if isinstance(font, str) is False:
        raise artError("font should have str type")
    font = font.lower()
    fonts = sorted(FONT_MAP.keys())
    font = indirect_font(font, fonts, text)
    letters = FONT_MAP[font][0]
    if FONT_MAP[font][1]:
        text_temp = text.lower()
    for i in text_temp:
        if (ord(i) == 9) or (ord(i) == 32 and font == "block"):
            continue
        if (i not in letters.keys()):
            if (chr_ignore):
                continue
            else:
                raise artError(str(i) + " is invalid")
        if len(letters[i]) == 0:
            continue
        split_list.append(letters[i].split("\n"))
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
        spliter = "\r\n"
    return((spliter).join(result_list))


def set_default(font=DEFAULT_FONT, chr_ignore=True, filename="art",
                print_status=True):
    '''
    This function change text2art, tprint and tsave default values
    :param font: input font
    :type font:str
    :param chr_ignore: ignore not supported character
    :type chr_ignore:bool
    :param filename: output file name (only tsave)
    :type filename:str
    :param print_status : save message print flag (only tsave)
    :type print_status:bool
    :return: None
    '''
    if isinstance(font, str) is False:
        raise artError("font should have str type")
    if isinstance(chr_ignore, bool) is False:
        raise artError("chr_ignore should have bool type")
    if isinstance(filename, str) is False:
        raise artError("filename should have str type")
    if isinstance(print_status, bool) is False:
        raise artError("print_status should have bool type")
    tprint.__defaults__ = (font, chr_ignore)
    tsave.__defaults__ = (font, filename, chr_ignore, print_status)
    text2art.__defaults__ = (font, chr_ignore)
