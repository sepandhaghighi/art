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
>>> Data = tsave("test@34",font="antrophobia",filename="antrophobia.txt")
Saved!
Filename: antrophobia.txt
>>> Data = tsave("test@34",font="magical",filename="magical.txt")
Saved!
Filename: magical.txt
>>> os.remove("antrophobia.txt")
>>> os.remove("magical.txt")

'''
