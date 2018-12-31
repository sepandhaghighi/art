# -*- coding: utf-8 -*-
from .art_dic import *
from .text_dic import *
import os
import sys
import random

VERSION = "2.8"

SMALLTHRESHOLD = 60
MEDIUMTHRESHOLD = 250
LARGETHRESHOLD = 500

DESCRIPTION = '''ASCII art is also known as "computer text art".
It involves the smart placement of typed special characters or
letters to make a visual shape that is spread over multiple lines of text.
Art is a Python lib for text converting to ASCII ART fancy.'''


class artError(Exception):
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
        if length <= 80:
            small_font.append(font)
        elif length > SMALLTHRESHOLD and length <= MEDIUMTHRESHOLD:
            medium_font.append(font)
        elif length > MEDIUMTHRESHOLD and length <= LARGETHRESHOLD:
            large_font.append(font)
        else:
            xlarge_font.append(font)
    return {
        "small_list": small_font,
        "medium_list": medium_font,
        "large_list": large_font,
        "xlarge_list": xlarge_font}


font_map = {"block": [block_dic, True], "banner": [banner_dic, False],
            "standard": [standard_dic, False], "avatar": [avatar_dic, True],
            "basic": [basic_dic, True], "bulbhead": [bulbhead_dic, True],
            "chunky": [chunky_dic, False], "coinstak": [coinstak_dic, False],
            "contessa": [contessa_dic, False], "contrast": [contrast_dic, True],
            "cyberlarge": [cyberlarge_dic, True], "cybermedium": [cybermedium_dic, True],
            "doom": [doom_dic, False], "dotmatrix": [dotmatrix_dic, False],
            "drpepper": [drpepper_dic, False],
            "epic": [epic_dic, True], "fuzzy": [fuzzy_dic, False],
            "isometric1": [isometric1_dic, True], "isometric2": [isometric2_dic, True],
            "isometric3": [isometric3_dic, True], "isometric4": [isometric4_dic, True],
            "larry3d": [larry3d_dic, False],
            "nancyj": [nancyj_dic, False], "ogre": [ogre_dic, False],
            "rectangles": [rectangles_dic, False], "roman": [roman_dic, False],
            "rounded": [rounded_dic, False], "rowancap": [rowancap_dic, True],
            "script": [script_dic, False],
            "serifcap": [serifcap_dic, True], "shadow": [shadow_dic, False],
            "slant": [slant_dic, False], "speed": [speed_dic, False],
            "starwars": [starwars_dic, False], "stop": [stop_dic, False],
            "thin": [thin_dic, False], "usaflag": [usaflag_dic, False],
            "3-d": [dic_3d, False], "3x5": [dic_3x5, False], "5lineoblique":
                [dic_5lineoblique, False], "alphabet": [alphabet_dic, False],
            "banner3-d": [banner3d_dic, True],
            "banner3": [banner3_dic, True], "banner4": [banner4_dic, True],
            "bell": [bell_dic, False], "catwalk": [catwalk_dic, False], "colossal": [colossal_dic, False],
            "acrobatic": [acrobatic_dic, True], "alligator": [alligator_dic, False],
            "alligator2": [alligator2_dic, False], "block2": [block2_dic, True],
            "caligraphy": [caligraphy_dic, True],
            "computer": [computer_dic, True], "digital": [digital_dic, True],
            "doh": [doh_dic, True],
            "eftirobot": [eftirobot_dic, True], "graffiti": [graffiti_dic, True],
            "stellar": [stellar_dic, False], "swan": [swan_dic, False], "tanja": [tanja_dic, False],
            "thick": [thick_dic, False], "threepoint": [threepoint_dic, False],
            "tombstone": [tombstone_dic, True], "trek": [trek_dic, True],
            "twopoint": [twopoint_dic, False], "univers": [univers_dic, False],
            "weird": [weird_dic, False], "pebbles": [pebbles_dic, False],
            "puffy": [puffy_dic, False], "tinker-toy": [tinker_toy_dic, False],
            "straight": [straight_dic, False], "stampatello": [stampatello_dic,
                                                               False],
            "smslant": [smslant_dic, False], "smshadow": [smshadow_dic, False],
            "smscript": [smscript_dic, False], "smkeyboard": [smkeyboard_dic,
                                                              False],
            "smisome1": [smisome1_dic, True], "slscript": [slscript_dic, False],
            "slide": [slide_dic, False], "sblood": [sblood_dic, True],
            "rozzo": [rozzo_dic, False], "pyramid": [pyramid_dic, False],
            "maxfour": [maxfour_dic, False], "nipples": [nipples_dic, False],
            "o8": [o8_dic, False], "peaks": [peaks_dic, False],
            "pawp": [pawp_dic, False],
            "barbwire": [barbwire_dic, False], "bigchief": [bigchief_dic, False],
            "binary": [binary_dic, False], "bubble": [bubble_dic, False],
            "calgphy2": [calgphy2_dic, False],
            "cygnet": [cygnet_dic, False], "diamond": [diamond_dic, False],
            "eftifont": [eftifont_dic, False], "eftitalic": [eftitalic_dic,
                                                             False],
            "eftiwater": [eftiwater_dic, False], "fourtops": [fourtops_dic, False],
            "goofy": [goofy_dic, True], "hollywood": [hollywood_dic, False],
            "invita": [invita_dic, False], "italic": [italic_dic, False],
            "jazmine": [jazmine_dic, False], "lcd": [lcd_dic, False],
            "lean": [lean_dic, False], "letters": [letters_dic, False],
            "lockergnome": [lockergnome_dic, False], "madrid": [madrid_dic, False],
            "marquee": [marquee_dic, False], "mike": [mike_dic, True],
            "mini": [mini_dic, False],
            "nancyj-fancy": [nancyj_fancy_dic, False],
            "nancyj-underlined": [nancyj_underlined_dic, False],
            "pepper": [pepper_dic, False], "poison": [poison_dic, True],
            "rot13": [rot13_dic, False], "short": [short_dic, False],
            "small": [small_dic, False], "tengwar": [tengwar_dic, True],
            "big": [big_dic, False], "1row": [dic_1row, True],
            "3d_diagonal": [dic_3d_diagonal, False],
            "4max": [dic_4max, True],
            "amc3line": [amc3line_dic, True],
            "cybersmall": [cybersmall_dic, True],
            "gothic": [gothic_dic, False],
            "rev": [rev_dic, False],
            "smtengwar": [smtengwar_dic, False],
            "term": [term_dic, False],
            "amcrazor": [amcrazor_dic, True],
            "amcaaa01": [amcaaa01_dic, True],
            "amcneko": [amcneko_dic, False],
            "amcrazo2": [amcrazo2_dic, True],
            "amcslash": [amcslash_dic, False],
            "amcthin": [amcthin_dic, True],
            "amctubes": [amctubes_dic, True],
            "amcun1": [amcun1_dic, False],
            "arrows": [arrows_dic, False],
            "bear": [bear_dic, True],
            "benjamin": [benjamin_dic, True],
            "bigfig": [bigfig_dic, False],
            "bolger": [bolger_dic, False],
            "braced": [braced_dic, True],
            "bright": [bright_dic, True],
            "broadway": [broadway_dic, True],
            "cards": [cards_dic, True],
            "chiseled": [chiseled_dic, True],
            "cola": [cola_dic, False],
            "crawford": [crawford_dic, True],
            "cricket": [cricket_dic, False],
            "danc4": [danc4_dic, False],
            "dancingfont": [dancingfont_dic, True],
            "decimal": [decimal_dic, False],
            "defleppard": [defleppard_dic, True],
            "dietcola": [dietcola_dic, False],
            "double": [double_dic, True],
            "doubleshorts": [doubleshorts_dic, True],
            "eftipiti": [eftipiti_dic, False],
            "filter": [filter_dic, True],
            "flipped": [flipped_dic, True],
            "fraktur": [fraktur_dic, False],
            "funface": [funface_dic, True],
            "funfaces": [funfaces_dic, True],
            "georgi16": [georgi16_dic, False],
            "georgia11": [georgia11_dic, False],
            "ghost": [ghost_dic, True],
            "ghoulish": [ghoulish_dic, True],
            "glenyn": [glenyn_dic, True],
            "graceful": [graceful_dic, True],
            "greek": [greek_dic, False],
            "heartleft": [heartleft_dic, False],
            "heartright": [heartright_dic, False],
            "henry3d": [henry3d_dic, False],
            "horizontalleft": [horizontalleft_dic, True],
            "horizontalright": [horizontalright_dic, True],
            "icl-1900": [ICL_1900_dic, True],
            "impossible": [impossible_dic, True],
            "jacky": [jacky_dic, True],
            "katakana": [katakana_dic, False],
            "keyboard": [keyboard_dic, False],
            "knob": [knob_dic, True],
            "lildevil": [lildevil_dic, True],
            "lineblocks": [lineblocks_dic, True],
            "merlin1": [merlin1_dic, True],
            "merlin2": [merlin2_dic, True],
            "modular": [modular_dic, True],
            "morse": [morse_dic, True],
            "morse2": [morse2_dic, True],
            "moscow": [moscow_dic, True],
            "muzzle": [muzzle_dic, True],
            "nancyj-improved": [nancyj_improved_dic, False],
            "nscript": [nscript_dic, False],
            "ntgreek": [ntgreek_dic, False],
            "nvscript": [nvscript_dic, False],
            "octal": [octal_dic, False],
            "oldbanner": [oldbanner_dic, False],
            "os2": [os2_dic, False],
            "peaksslant": [peaksslant_dic, False],
            "puzzle": [puzzle_dic, True],
            "rammstein": [rammstein_dic, False],
            "red_phoenix": [red_phoenix_dic, False],
            "runyc": [runyc_dic, False],
            "santaclara": [santaclara_dic, False],
            "shimrod": [shimrod_dic, False],
            "smallcaps": [smallcaps_dic, True],
            "smpoison": [smpoison_dic, True],
            "soft": [soft_dic, False],
            "spliff": [spliff_dic, True],
            "stacey": [stacey_dic, True],
            "stampate": [stampate_dic, False],
            "stforek": [stforek_dic, True],
            "sub-zero": [sub_zero_dic, True],
            "swampland": [swampland_dic, True],
            "sweet": [sweet_dic, True],
            "ticks": [ticks_dic, False],
            "ticksslant": [ticksslant_dic, False],
            "tiles": [tiles_dic, False],
            "tsalagi": [tsalagi_dic, False],
            "tubular": [tubular_dic, False],
            "twisted": [twisted_dic, True],
            "varsity": [varsity_dic, False],
            "wavy": [wavy_dic, False],
            "wetletter": [wetletter_dic, True],
            "whimsy": [whimsy_dic, True],
            "wow": [wow_dic, True],
            "alligator3": [alligator3_dic, True],
            "alpha": [alpha_dic, True],
            "amc3liv1": [amc3liv1_dic, True],
            "ascii_new_roman": [ascii_new_roman_dic, True],
            "b1ff": [B1FF_dic, True],
            "dwhistled": [dwhistled_dic, False],
            "eftiwall": [eftiwall_dic, False],
            "fire_font-k": [fire_font_k_dic, False],
            "fire_font-s": [fire_font_s_dic, False],
            "gradient": [gradient_dic, True],
            "1943": [dic_1943, False],
            "advenger": [advenger_dic, False],
            "char1": [char1_dic, False],
            "char2": [char2_dic, False],
            "char3": [char3_dic, False],
            "char4": [char4_dic, False],
            "charact1": [charact1_dic, False],
            "charact2": [charact2_dic, False],
            "charact3": [charact3_dic, False],
            "charact4": [charact4_dic, False],
            "charact5": [charact5_dic, False],
            "charact6": [charact6_dic, False],
            "characte": [characte_dic, False],
            "chartr": [chartr_dic, False],
            "chartri": [chartri_dic, False],
            "xbrite": [xbrite_dic, False],
            "xbriteb": [xbriteb_dic, False],
            "xbritebi": [xbritebi_dic, False],
            "xbritei": [xbritei_dic, False],
            "xchartr": [xchartr_dic, False],
            "xchartri": [xchartri_dic, False],
            "xcour": [xcour_dic, False],
            "xcourb": [xcourb_dic, False],
            "xcourbi": [xcourbi_dic, False],
            "xcouri": [xcouri_dic, False],
            "xhelv": [xhelv_dic, False],
            "xhelvb": [xhelvb_dic, False],
            "xhelvbi": [xhelvbi_dic, False],
            "xhelvi": [xhelvi_dic, False],
            "xsans": [xsans_dic, False],
            "xsansb": [xsansb_dic, False],
            "xsansbi": [xsansbi_dic, False],
            "xsansi": [xsansi_dic, False],
            "xtimes": [xtimes_dic, False],
            "xttyb": [xttyb_dic, False],
            "heroboti": [heroboti_dic, False],
            "high_noo": [high_noo_dic, False],
            "hills": [hills_dic, False],
            "home_pak": [home_pak_dic, False],
            "house_of": [house_of_dic, False],
            "hypa_bal": [hypa_bal_dic, False],
            "hyper": [hyper_dic, False],
            "inc_raw": [inc_raw_dic, False],
            "italics": [italics_dic, False],
            "kgames_i": [kgames_i_dic, False],
            "4x4_offr": [dic_4x4_offr, False],
            "5x7": [dic_5x7, False],
            "5x8": [dic_5x8, False],
            "6x9": [dic_6x9, False],
            "6x10": [dic_6x10, False],
            "64f1": [dic_64f1, False],
            "a_zooloo": [a_zooloo_dic, False],
            "asc": [asc_dic, False],
            "assalt_m": [assalt_m_dic, False],
            "asslt_m": [asslt__m_dic, False],
            "atc": [atc_dic, False],
            "atc_gran": [atc_gran_dic, False],
            "battle_s": [battle_s_dic, False],
            "battlesh": [battlesh_dic, False],
            "baz_bil": [baz_bil_dic, False],
            "beer_pub": [beer_pub_dic, False],
            "c1": [c1_dic, False],
            "c2": [c2_dic, False],
            "kik_star": [kik_star_dic, False],
            "krak_out": [krak_out_dic, False],
            "tsn_base": [tsn_base_dic, False],
            "twin_cob": [twin_cob_dic, False],
            "type_set": [type_set_dic, False],
            "ucf_fan": [ucf_fan_dic, False],
            "ugalympi": [ugalympi_dic, False],
            "unarmed": [unarmed__dic, False],
            "usa": [usa_dic, False],
            "usa_pq": [usa_pq_dic, False],
            "utopia": [utopia_dic, False],
            "utopiab": [utopiab_dic, False],
            "utopiabi": [utopiabi_dic, False],
            "utopiai": [utopiai_dic, False],
            "vortron": [vortron_dic, False],
            "war_of_w": [war_of_w_dic, False],
            "xtty": [xtty_dic, False],
            "yie_ar_k": [yie_ar_k_dic, False],
            "yie-ar": [yie_ar_dic, False],
            "zig_zag": [zig_zag_dic, False],
            "zone7": [zone7_dic, False],
            "z-pilot": [z_pilot_dic, False]
            }
font_counter = len(font_map)
DEFAULT_FONT = "standard"
RND_SIZE_DICT = font_size_splitter(font_map)


def line(char="*", number=30):
    '''
    This function print line of chars
    :param char: input character
    :type char:str
    :param number: number of characters
    :return: None
    '''
    print(char * number)


def font_list(text="test"):
    '''
    This function print all Of fonts
    :param text : input text
    :type text : str
    :return: None
    '''
    for item in sorted(list(font_map.keys())):
        print(str(item) + " : ")
        if str(item) in ["char4", "c2", "war_of_w"]:
            tprint(text.upper(), str(item))
        else:
            tprint(text, str(item))


def art_list():
    '''
    This function print all Of 1-Line arts
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
        random_index = random.randint(0, len(arts) - 1)
        artname = arts[random_index]
    elif artname not in art_dic.keys():
        distance_list = list(map(lambda x: distance_calc(artname, x),
                                 arts))
        min_distance = min(distance_list)
        if min_distance < 3:
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


def indirect_font(font, fonts):
    '''
    This function check input font for indirect modes
    :param font: input font
    :type font : str
    :param fonts: fonts list
    :type fonts : list
    :return: font as str
    '''
    if font == "rnd-small" or font == "random-small" or font == "rand-small":
        random_index = random.randint(0, len(RND_SIZE_DICT["small_list"]) - 1)
        font = RND_SIZE_DICT["small_list"][random_index]
    elif font == "rnd-medium" or font == "random-medium" or font == "rand-medium":
        random_index = random.randint(0, len(RND_SIZE_DICT["medium_list"]) - 1)
        font = RND_SIZE_DICT["medium_list"][random_index]
    elif font == "rnd-large" or font == "random-large" or font == "rand-large":
        random_index = random.randint(0, len(RND_SIZE_DICT["large_list"]) - 1)
        font = RND_SIZE_DICT["large_list"][random_index]
    elif font == "rnd-xlarge" or font == "random-xlarge" or font == "rand-xlarge":
        random_index = random.randint(0, len(RND_SIZE_DICT["xlarge_list"]) - 1)
        font = RND_SIZE_DICT["xlarge_list"][random_index]
    elif font == "random" or font == "rand" or font == "rnd":
        random_index = random.randint(0, len(fonts) - 1)
        font = fonts[random_index]
    elif font not in font_map.keys():
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
    fonts = sorted(font_map.keys())
    font = indirect_font(font, fonts)
    letters = font_map[font][0]
    if font_map[font][1]:
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
