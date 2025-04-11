# -*- coding: utf-8 -*-
"""Art function module."""
from typing import List, Dict, Optional, Union, Any
import os
import random

from .utils import distance_calc, indirect_font, indirect_decoration
from .params import art_dic, standard_dic
from .params import fancy1_dic
from .params import DEFAULT_FONT, MIX_FILTERED_FONTS
from .params import FONT_MAP, DECORATIONS_MAP
from .params import ART_NAMES, DECORATION_NAMES, FONT_NAMES, UPPERCASE_FONTS, NON_ASCII_FONTS, RANDOM_FILTERED_ARTS
from .params import NON_ASCII_ARTS
from .params import DESCRIPTION, CLI_HELP, ART_VERSION
from .params import ART_ENVIRONMENT_WARNING, FONT_ENVIRONMENT_WARNING, FONT_OR_DECOR_ENVIRONMENT_WARNING
from .params import DECORATION_TYPE_ERROR, TEXT_TYPE_ERROR, FONT_TYPE_ERROR, CHR_IGNORE_TYPE_ERROR, FILE_TYPE_ERROR
from .params import PRINT_STATUS_TYPE_ERROR, OVERWRITE_TYPE_ERROR, SEP_TYPE_ERROR, SPACE_TYPE_ERROR
from .params import DETAILED_RETURN_TYPE_ERROR, ART_TYPE_ERROR, NUMBER_TYPE_ERROR, ART_NAME_ERROR
from .params import LINE_LENGTH_ERROR, LINE_HEIGHT_ERROR, CHAR_TYPE_ERROR
from .errors import artError


def __word2art(
        word: str,
        font: str,
        chr_ignore: bool,
        letters: Dict[str, str],
        next_word: bool,
        sep: str = "\n") -> str:
    """
    Return ascii art word.

    :param word: input word
    :param font: input font
    :param chr_ignore: ignore not supported character
    :param letters: font letters table
    :param next_word: next word flag
    :param sep: line separator char
    """
    split_list = []
    result_list = []
    splitter = "\n"
    if isinstance(sep, str):
        splitter = sep
    if not word and next_word:
        return splitter
    for i in word:
        if ord(i) == 9:
            continue
        if i not in letters:
            if (chr_ignore):
                continue
            else:
                raise artError(str(i) + " is invalid.")
        if letters[i]:
            split_list.append(letters[i].split("\n"))
    if font in ["mirror", "mirror_flip"]:
        split_list.reverse()
    if not split_list:
        return ""
    for i in range(len(split_list[0])):
        temp = ""
        for item in split_list:
            temp = temp + item[i]
        result_list.append(temp)
    result = (splitter).join(result_list)
    if result[-1] != "\n" and next_word:
        result += splitter
    return result


def text2art(
        text: str,
        font: str = DEFAULT_FONT,
        chr_ignore: bool = True,
        decoration: str = None,
        sep: str = "\n",
        space: int = 0,
        __detailed_return: bool = False) -> str:
    r"""
    Return ascii art text (support \n).

    :param text: input text
    :param font: input font
    :param chr_ignore: ignore not supported character
    :param decoration: text decoration
    :param sep: line separator char
    :param space: space between characters
    :param __detailed_return: flag for returning the font and the decoration
    """
    letters = standard_dic
    if not isinstance(text, str):
        raise artError(TEXT_TYPE_ERROR)
    if not isinstance(font, str):
        raise artError(FONT_TYPE_ERROR)
    text = (' ' * space).join(text)
    text_temp = text
    font = font.lower()
    if font != "mix":
        font = indirect_font(font, text)
        letters = get_font_dic(font)
        if FONT_MAP[font][1]:
            text_temp = text.lower()
        if font in UPPERCASE_FONTS:
            text_temp = text.upper()
    else:
        letters = mix_letters()
    word_list = text_temp.split("\n")
    result = ""
    next_word_flag = True
    for index, word in enumerate(word_list):
        if index == len(word_list) - 1:
            next_word_flag = False
        result = result + __word2art(word=word,
                                     font=font,
                                     chr_ignore=chr_ignore,
                                     letters=letters,
                                     next_word=next_word_flag,
                                     sep=sep)
    if decoration is not None:
        [decor1, decor2] = decor(decoration, both=True)
        result = decor1 + result + decor2
    if __detailed_return:
        return (result, font, decoration)
    return result


def tprint(
        text: str,
        font: str = DEFAULT_FONT,
        chr_ignore: bool = True,
        decoration: Optional[str] = None,
        sep: str = "\n",
        space: int = 0) -> None:
    r"""
    Print art text (support \n).

    :param text: input text
    :param font: input font
    :param chr_ignore: ignore not supported character
    :param decoration: text decoration
    :param sep: line separator char
    :param space: space between characters
    """
    try:
        if font == "UnicodeEncodeError":
            raise UnicodeEncodeError(
                'test', u"", 42, 43, 'test unicode-encode-error')
        result, font, decoration = text2art(
            text,
            font=font,
            decoration=decoration,
            chr_ignore=chr_ignore,
            sep=sep,
            space=space,
            __detailed_return=True)
        print(result)
    except UnicodeEncodeError:
        if decoration is not None:
            print(FONT_OR_DECOR_ENVIRONMENT_WARNING.format(font, decoration))
        else:
            print(FONT_ENVIRONMENT_WARNING.format(font))


def art(
        artname: str,
        number: int = 1,
        space: int = 1,
        __detailed_return: bool = False) -> str:
    """
    Return 1-line ascii art.

    :param artname: art name
    :param number: number of repeats
    :param space: space between arts
    :param __detailed_return: flag for returning the art name
    """
    if not isinstance(artname, str):
        raise artError(ART_TYPE_ERROR)
    if not isinstance(number, int):
        raise artError(NUMBER_TYPE_ERROR)
    if not isinstance(space, int):
        raise artError(SPACE_TYPE_ERROR)
    artname = artname.lower()
    arts = ART_NAMES
    if artname in ["random", "rand", "rnd"]:
        filtered_arts = list(set(arts) - set(RANDOM_FILTERED_ARTS))
        artname = random.choice(filtered_arts)
    elif artname not in art_dic:
        selected_art = min(arts, key=lambda x: distance_calc(artname, x))
        min_distance = distance_calc(artname, selected_art)
        threshold = max(len(artname), len(selected_art)) / 2
        if min_distance < threshold:
            artname = selected_art
        else:
            raise artError(ART_NAME_ERROR)
    art_value = art_dic[artname]
    result = (art_value + " " * space) * number
    result = result.strip()
    if __detailed_return:
        return (result, artname)
    return result


def aprint(artname: str, number: int = 1, space: int = 1) -> None:
    """
    Print 1-line art.

    :param artname: art name
    :param number: number of repeats
    :param space: space between arts
    """
    try:
        if artname == "UnicodeEncodeError":
            raise UnicodeEncodeError(
                'test', u"", 42, 43, 'test unicode-encode-error')
        result, artname = art(
            artname=artname, number=number, space=space, __detailed_return=True)
        print(result)
    except UnicodeEncodeError:
        print(ART_ENVIRONMENT_WARNING.format(artname))


def lprint(length: int = 15, height: int = 1, char: str = '#') -> None:
    """
    Print a grid (length X height) of the given character.

    :param length: the grid length
    :param height: the grid height
    :param char: target character
    """
    grid = line(length, height, char)
    print(grid)


def line(length: int = 15, height: int = 1, char: str = '#') -> str:
    """
    Generate a grid (length X height) of the given character.

    :param length: the grid length
    :param height: the grid height
    :param char: target character
    """
    if not isinstance(length, int) or length < 1:
        raise artError(LINE_LENGTH_ERROR)
    if not isinstance(height, int) or height < 1:
        raise artError(LINE_HEIGHT_ERROR)
    if not isinstance(char, str):
        raise artError(CHAR_TYPE_ERROR)

    line_str = char * length
    return "\n".join([line_str] * height)


def decor(decoration: str, reverse: bool = False, both: bool = False) -> Union[str, List[str]]:
    """
    Return given decoration part.

    :param  decoration: decoration's name
    :param reverse: true if second tail of decoration wanted
    :param both: both tails returning flag
    """
    if not isinstance(decoration, str):
        raise artError(DECORATION_TYPE_ERROR)
    decoration = decoration.lower()
    decoration = indirect_decoration(decoration)
    if both:
        return DECORATIONS_MAP[decoration]
    if reverse:
        return DECORATIONS_MAP[decoration][-1]
    return DECORATIONS_MAP[decoration][0]


def randart() -> str:
    """Return random 1-line ascii art."""
    return art("random")


def tsave(
        text: str,
        font: str = DEFAULT_FONT,
        filename: str = "art",
        chr_ignore: bool = True,
        print_status: bool = True,
        overwrite: bool = False,
        decoration: Optional[str] = None,
        sep: str = "\n",
        space: int = 0) -> Dict[str, Any]:
    """
    Save ascii art (support \n).

    :param text: input text
    :param font: input font
    :param filename: output file name
    :param chr_ignore: ignore not supported character
    :param print_status : save message print flag
    :param overwrite : overwrite the saved file if true
    :param decoration: text decoration
    :param sep: line separator char
    :param space: space between characters
    """
    try:
        if not isinstance(text, str):
            raise Exception(TEXT_TYPE_ERROR)
        files_list = os.listdir(os.getcwd())
        splitted_filename = filename.split(".")
        if len(splitted_filename) > 1:
            name = filename[:-1 * filename[::-1].find('.') - 1]
            extension = "." + splitted_filename[-1]
        else:
            name = filename
            extension = ".txt"
        index = 2
        test_name = name
        while not overwrite:
            if test_name + extension in files_list:
                test_name = name + str(index)
                index = index + 1
            else:
                break
        file = open(test_name + extension, "w", encoding='utf-8')
        result = text2art(
            text,
            font=font,
            decoration=decoration,
            chr_ignore=chr_ignore,
            sep=sep,
            space=space)
        file.write(result)
        file.close()
        if print_status:
            print("Saved! \nFilename: " + test_name + extension)
        return {"Status": True, "Message": "OK"}
    except Exception as e:
        return {"Status": False, "Message": str(e)}


def set_default(
        font: str = DEFAULT_FONT,
        chr_ignore: bool = True,
        filename: str = "art",
        print_status: bool = True,
        overwrite: bool = False,
        decoration: Optional[str] = None,
        sep: str = "\n",
        space: int = 0,
        __detailed_return: bool = False) -> None:
    """
    Change text2art, tprint and tsave default values.

    :param font: input font
    :param chr_ignore: ignore not supported character
    :param filename: output file name (only tsave)
    :param print_status : save message print flag (only tsave)
    :param overwrite : overwrite the saved file if true (only tsave)
    :param decoration: input decoration
    :param sep: line separator char
    :param space: space between characters
    :param __detailed_return: flag for returning the font and the decoration
    """
    if not isinstance(font, str):
        raise artError(FONT_TYPE_ERROR)
    if not isinstance(decoration, str) and decoration is not None:
        raise artError(DECORATION_TYPE_ERROR)
    if not isinstance(chr_ignore, bool):
        raise artError(CHR_IGNORE_TYPE_ERROR)
    if not isinstance(filename, str):
        raise artError(FILE_TYPE_ERROR)
    if not isinstance(print_status, bool):
        raise artError(PRINT_STATUS_TYPE_ERROR)
    if not isinstance(overwrite, bool):
        raise artError(OVERWRITE_TYPE_ERROR)
    if not isinstance(sep, str):
        raise artError(SEP_TYPE_ERROR)
    if not isinstance(space, int):
        raise artError(SPACE_TYPE_ERROR)
    if not isinstance(__detailed_return, bool):
        raise artError(DETAILED_RETURN_TYPE_ERROR)
    tprint.__defaults__ = (font, chr_ignore, decoration, sep, space)
    tsave.__defaults__ = (
        font,
        filename,
        chr_ignore,
        print_status,
        overwrite,
        decoration,
        sep,
        space)
    text2art.__defaults__ = (
        font,
        chr_ignore,
        decoration,
        sep,
        space,
        __detailed_return)


def get_font_dic(font_name: str) -> Dict[str, str]:
    """
    Return given font's dictionary.

    :param  font_name: font's name
    """
    return FONT_MAP[font_name][0]


def decor_list(text: str = "test", font: str = "fancy6") -> None:
    """
    Print all decorations.

    :param text : input text
    :param font: input font
    """
    for decor in DECORATION_NAMES:
        print(decor)
        tprint(text, font=font, decoration=decor)
        lprint(length=30, char="*")


def font_list(text: str = "test", mode: str = "all") -> None:
    """
    Print all fonts.

    :param text : input text
    :param mode: fonts mode (all, ascii, non-ascii)
    """
    fonts = set(FONT_NAMES)
    if mode.lower() == "ascii":
        fonts = fonts - set(NON_ASCII_FONTS)
    if mode.lower() == "non-ascii":
        fonts = set(NON_ASCII_FONTS)
    for item in sorted(fonts):
        print(str(item) + " : ")
        text_temp = text + "\n"
        tprint(text_temp, str(item))


def art_list(mode: str = "all") -> None:
    """
    Print all 1-Line arts.

    :param mode: fonts mode (all, ascii, non-ascii)
    """
    arts = set(ART_NAMES)
    if mode.lower() == "ascii":
        arts = arts - set(NON_ASCII_ARTS)
    if mode.lower() == "non-ascii":
        arts = set(NON_ASCII_ARTS)
    for i in sorted(arts):
        print(i)
        aprint(i)
        lprint(length=30, char="*")


def mix_letters() -> Dict[str, str]:
    """Return letters in mix mode."""
    letters = fancy1_dic.copy()
    fonts = list(set(NON_ASCII_FONTS) - set(MIX_FILTERED_FONTS))
    for i in letters:
        random_font = random.choice(fonts)
        letters[i] = get_font_dic(random_font)[i]
    return letters


def help_func() -> None:
    """Print help page."""
    tprint("art")
    tprint("v" + ART_VERSION)
    print(DESCRIPTION)
    print(CLI_HELP)
