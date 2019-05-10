# -*- coding: utf-8 -*-
'''
>>> import os
>>> import random
>>> from art import *
>>> from art.art_param import TEST_FILTERED_FONTS
>>> for i in sorted(TEST_FILTERED_FONTS):
...     print(i+":")
...     tprint("test",font=i)
antrophobia:
тєѕт
<BLANKLINE>
currency:
₮Ɇ₴₮
<BLANKLINE>
dirty:
ẗệṩẗ
<BLANKLINE>
fancy1:
тεsт
<BLANKLINE>
fancy10:
ɬɛʂɬ
<BLANKLINE>
fancy11:
тeѕт
<BLANKLINE>
fancy12:
tєѕt
<BLANKLINE>
fancy13:
tєรt
<BLANKLINE>
fancy14:
ᏆᎬsᏆ
<BLANKLINE>
fancy15:
✞ƎƧ✞
<BLANKLINE>
fancy16:
ΓΞSΓ
<BLANKLINE>
fancy17:
ᏆɛֆᏆ
<BLANKLINE>
fancy18:
ԵҽՏԵ
<BLANKLINE>
fancy19:
꓄ꍟꌗ꓄
<BLANKLINE>
fancy2:
ㄒ乇丂ㄒ
<BLANKLINE>
fancy20:
ᵀᴱˢᵀ
<BLANKLINE>
fancy21:
тeѕт
<BLANKLINE>
fancy22:
ŤƐらŤ
<BLANKLINE>
fancy23:
ƬЄƧƬ
<BLANKLINE>
fancy24:
ϮꂅᏕϮ
<BLANKLINE>
fancy25:
ｲ乇丂ｲ
<BLANKLINE>
fancy26:
†εš†
<BLANKLINE>
fancy27:
tēŞt
<BLANKLINE>
fancy3:
ŤĔŚŤ
<BLANKLINE>
fancy4:
ᏆᎬsᏆ
<BLANKLINE>
fancy5:
ᏖᏋᏕᏖ
<BLANKLINE>
fancy6:
ƭεรƭ
<BLANKLINE>
fancy7:
丅ᗴᔕ丅
<BLANKLINE>
fancy8:
tєรt
<BLANKLINE>
fancy9:
тeѕт
<BLANKLINE>
flip:
ϝԍƨϝ
<BLANKLINE>
full_width:
ｔｅｓｔ
<BLANKLINE>
knight:
ṮḕṠṮ
<BLANKLINE>
magical:
ᏆᎬsᏆ
<BLANKLINE>
mirror:
ɈƨǝɈ
<BLANKLINE>
mirror_flip:
ʇsǝʇ
<BLANKLINE>
paranormal:
tєѕt
<BLANKLINE>
smallcaps2:
ᴛᴇsᴛ
<BLANKLINE>
sorcerer:
ᏆɛֆᏆ
<BLANKLINE>
special:
TEᔕT
<BLANKLINE>
subscript:
ₜₑₛₜ
<BLANKLINE>
superscript:
ᵗᵉˢᵗ
<BLANKLINE>
thin2:
ｔｅｓｔ
<BLANKLINE>
tiny:
ᴛᴇᴤᴛ
<BLANKLINE>
white_bubble:
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
