# -*- coding: utf-8 -*-
from .art_dic import *
from .text_dic import *
import os
import sys

version = "0.9"


class artError(Exception):
    pass


font_map = {"block": [block_dic, True], "banner": [banner_dic, False], "standard": [standard_dic, False], "avatar": [avatar_dic, True],
            "basic": [basic_dic, True], "bulbhead": [bulbhead_dic, True], "chunky": [chunky_dic, False], "coinstak": [coinstak_dic, False],
            "contessa": [contessa_dic, False], "contrast": [contrast_dic, True], "cyberlarge": [cyberlarge_dic, True], "cybermedium": [cybermedium_dic, True],
            "doom": [doom_dic, False], "dotmatrix": [dotmatrix_dic, False], "drpepper": [drpepper_dic, False],
            "epic": [epic_dic, True], "fuzzy": [fuzzy_dic, False], "isometric1": [isometric1_dic, True], "isometric2": [isometric2_dic, True],
            "isometric3": [isometric3_dic, True], "isometric4": [isometric4_dic, True], "larry3d": [larry3d_dic, False],
            "nancyj": [nancyj_dic, False], "ogre": [ogre_dic, False], "rectangles": [rectangles_dic, False], "roman": [roman_dic, False],
            "rounded": [rounded_dic, False], "rowancap": [rowancap_dic, True], "script": [script_dic, False],
            "serifcap": [serifcap_dic, True], "shadow": [shadow_dic, False], "slant": [slant_dic, False], "speed": [speed_dic, False],
            "starwars": [starwars_dic, False], "stop": [stop_dic, False], "thin": [thin_dic, False], "usaflag": [usaflag_dic, False],
            "3-d": [dic_3d, False], "3x5": [dic_3x5, False], "5lineoblique": [dic_5lineoblique, False], "alphabet": [alphabet_dic, False], "banner3-D": [banner3d_dic, True],
            "banner3": [banner3_dic, True], "banner4": [banner4_dic, True], "bell": [bell_dic, False], "catwalk": [catwalk_dic, False], "colossal": [colossal_dic, False],
            "acrobatic": [acrobatic_dic, True], "alligator": [alligator_dic, False], "alligator2": [alligator2_dic, False], "block2": [block2_dic, True],
            "caligraphy": [caligraphy_dic, True], "computer": [computer_dic, True], "digital": [digital_dic, True], "doh": [doh_dic, True],
            "eftirobot": [eftirobot_dic, True], "graffiti": [graffiti_dic,True],
            "stellar":[stellar_dic,False],"swan":[swan_dic,False],"tanja":[tanja_dic,False],
            "thick":[thick_dic,False],"threepoint":[threepoint_dic,False],
            "tombstone":[tombstone_dic,True],"trek":[trek_dic,True],
            "twopoint":[twopoint_dic,False],"univers":[univers_dic,False],"weird":[weird_dic,False]}

DEFAULT_FONT = "standard"


def line(char="*", number=30):
    '''
    This function print line of chars
    :param char: character
    :type char:str
    :param number: number of character
    :return: None
    '''
    print(char * number)


def font_list():
    '''
    This Function Print All Of Fonts
    :return: None
    '''
    for item in sorted(list(font_map.keys())):
        print(str(item) + " : ")
        tprint("test", str(item))


def aprint_test():
    '''
    This Function Print All Of 1Line Arts
    :return: None
    '''
    for i in sorted(list(art_dic.keys())):
        try:
            print(i)
            aprint(i)
            line()
        except Exception:
            print("[Waning] This art is not printable in this environment")
            line()


def help_func():
    '''
    Print Help Page
    :return: None
    '''
    tprint("art")
    tprint("v" + version)
    print("Webpage : http://art.shaghighi.ir")
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
    Art Print
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
    if isinstance(artname, str) == False:
        raise artError("artname shoud have str type")
    if artname.lower() not in art_dic.keys():
        raise artError("Invalid art name")
    art_value = art_dic[artname.lower()]
    if isinstance(number, int) == False:
        raise artError("number should have int type")
    if isinstance(art_value, str):
        return (art_value + " ") * number
    else:
        if isinstance(text, str) == False:
            raise artError("text should have str type")
        return (art_value[0] + text + art_value[1] + " ") * number


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
    if isinstance(text, str) == False:
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

    :param text: input text
    :param font: input font
    :type font:str
    :type text:str
    :param filename: output file name
    :type filename:str
    :param chr_ignore: ignore not supported character
    :type chr_ignore:bool
    :param print_status : Save message print flag
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


def text2art(text, font=DEFAULT_FONT, chr_ignore=True):
    '''
    This function print art text
    :param text: input text
    :type text:str
    :param font: input font
    :type font:str
    :param chr_ignore: ignore not supported character
    :type chr_ignore:bool
    :return: artText as str
    '''
    split_list = []
    result_list = []
    letters = standard_dic
    text_temp = text
    spliter = "\n"
    if isinstance(text, str) == False:
        raise artError("text should have str type")
    if isinstance(font, str) == False:
        raise artError("font should have str type")
    if font.lower() in font_map.keys():
        letters = font_map[font.lower()][0]
        if font_map[font.lower()][1]:
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
    if "win" not in sys.platform:
        spliter = "\r\n"
    return((spliter).join(result_list))
