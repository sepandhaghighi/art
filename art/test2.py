# -*- coding: utf-8 -*-
'''
>>> import os
>>> import random
>>> from art import *
>>> from art.art_param import TEST_FILTERED_FONTS
>>> for i in sorted(TEST_FILTERED_FONTS):
...	    tprint("test",font=i)
тєѕт
<BLANKLINE>
₮Ɇ₴₮
<BLANKLINE>
ẗệṩẗ
<BLANKLINE>
ϝԍƨϝ
<BLANKLINE>
ｔｅｓｔ
<BLANKLINE>
ᏆᎬsᏆ
<BLANKLINE>
ɈƨǝɈ
<BLANKLINE>
ʇsǝʇ
<BLANKLINE>
tєѕt
<BLANKLINE>
ᴛᴇsᴛ
<BLANKLINE>
ᏆɛֆᏆ
<BLANKLINE>
TEᔕT
<BLANKLINE>
ₜₑₛₜ
<BLANKLINE>
ᵗᵉˢᵗ
<BLANKLINE>
ⓣⓔⓢⓣ
<BLANKLINE>
>>> random.seed(24)
>>> Art = text2art("test","rnd-na")
>>> random.seed(45)
>>> Art2 = text2art("test","rnd-na")
>>> Art == Art2
False
>>> for i in sorted(TEST_FILTERED_FONTS):
...	    Data = tsave("test@34",font=i,filename=i)
Saved!
Filename: antrophobia.txt
Saved!
Filename: currency.txt
Saved!
Filename: dirty.txt
Saved!
Filename: flip.txt
Saved!
Filename: full_width.txt
Saved!
Filename: magical.txt
Saved!
Filename: mirror.txt
Saved!
Filename: mirror_flip.txt
Saved!
Filename: paranormal.txt
Saved!
Filename: smallcaps2.txt
Saved!
Filename: sorcerer.txt
Saved!
Filename: special.txt
Saved!
Filename: subscript.txt
Saved!
Filename: superscript.txt
Saved!
Filename: white_bubble.txt
>>> os.remove("flip.txt")
>>> os.remove("mirror.txt")
>>> os.remove("mirror_flip.txt")
>>> os.remove("white_bubble.txt")
>>> os.remove("smallcaps2.txt")
>>> os.remove("superscript.txt")
>>> os.remove("subscript.txt")
>>> os.remove("full_width.txt")
>>> os.remove("antrophobia.txt")
>>> os.remove("currency.txt")
>>> os.remove("dirty.txt")
>>> os.remove("magical.txt")
>>> os.remove("paranormal.txt")
>>> os.remove("sorcerer.txt")
>>> os.remove("special.txt")

'''
