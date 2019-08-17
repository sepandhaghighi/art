# -*- coding: utf-8 -*-
"""Fonts height testing script."""
import string
import sys
import art

Letters = string.ascii_letters + string.punctuation + string.digits
Font_List = list(art.art_param.FONT_MAP.keys())

Error1 = "[Error] Font data is empty!"
Error2 = "[Error] Font should support 95 printable ASCII characters, please check font data!"
Error3 = "[Error] Font duplication (art version : {}) -- > ".format(art.__version__)


if __name__ == "__main__":
    art.tprint("Font Wizard")
    print("Use this string as input for font resource: ")
    print(Letters)
    print("*"*30)
    font_data = input("Please enter font data: ")
    if len(font_data) == 0:
        print(Error1)
        sys.exit()
    if len(font_data) != len(Letters):
        font_data = eval(font_data)
        if len(font_data) != len(Letters):
            print(Error2)
            sys.exit()
    font_dic = dict(zip(Letters,font_data))
    if " " not in font_dic.keys():
        font_dic[" "] = " "
    for font2 in Font_List:
        if font_dic == art.art_param.FONT_MAP[font2][0]:
            print(Error3 + font2)
            sys.exit()
    if len(font_dic) == 95:
        print("Done!")
        print("Font dictionary: \n")
        print(font_dic)
    else:
        print(Error2)







