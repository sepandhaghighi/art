# -*- coding: utf-8 -*-
"""Art modules."""
from .errors import artError
from .functions import aprint, art, randart
from .functions import tprint, tsave, text2art
from .functions import lprint, line
from .functions import decor, help_func
from .functions import get_font_dic, set_default, art_list, font_list, decor_list
from .params import ART_VERSION, FONT_NAMES, ART_NAMES, DECORATION_NAMES, DEFAULT_FONT
from .params import ART_COUNTER, FONT_COUNTER, DECORATION_COUNTER
from .params import NON_ASCII_ARTS, NON_ASCII_FONTS, ASCII_FONTS, ASCII_ARTS
__version__ = ART_VERSION
