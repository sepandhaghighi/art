# -*- coding: utf-8 -*-
'''
>>> import os
>>> import random
>>> import codecs
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
ՇєรՇ
<BLANKLINE>
fancy12:
tєѕt
<BLANKLINE>
fancy13:
tєรt
<BLANKLINE>
fancy14:
ȶɛֆȶ
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
fancy28:
ƬΣƧƬ
<BLANKLINE>
fancy29:
†ê§†
<BLANKLINE>
fancy3:
ŤĔŚŤ
<BLANKLINE>
fancy30:
ᖶᘿSᖶ
<BLANKLINE>
fancy31:
ནპჰན
<BLANKLINE>
fancy32:
꓄ꏂꑄ꓄
<BLANKLINE>
fancy33:
꓅ꍟꌚ꓅
<BLANKLINE>
fancy34:
ꋖꈼꌚꋖ
<BLANKLINE>
fancy35:
੮૯ς੮
<BLANKLINE>
fancy36:
ԵȝՏԵ
<BLANKLINE>
fancy37:
ꋖꏹꌚꋖ
<BLANKLINE>
fancy38:
ꋖꑀꈜꋖ
<BLANKLINE>
fancy39:
ፕቿነፕ
<BLANKLINE>
fancy4:
ᏆᎬsᏆ
<BLANKLINE>
fancy40:
꓅ꑾꇘ꓅
<BLANKLINE>
fancy41:
ț£§ț
<BLANKLINE>
fancy42:
ţ€$ţ
<BLANKLINE>
fancy43:
ᖶᙍSᖶ
<BLANKLINE>
fancy44:
тεƨт
<BLANKLINE>
fancy45:
тešт
<BLANKLINE>
fancy46:
էεʂէ
<BLANKLINE>
fancy47:
†ε$†
<BLANKLINE>
fancy48:
էεรէ
<BLANKLINE>
fancy49:
τεЅτ
<BLANKLINE>
fancy5:
ᏖᏋᏕᏖ
<BLANKLINE>
fancy50:
ҭἔṩҭ
<BLANKLINE>
fancy51:
7357
<BLANKLINE>
fancy52:
τEŠτ
<BLANKLINE>
fancy53:
ƮęsƮ
<BLANKLINE>
fancy54:
⊥ÈS⊥
<BLANKLINE>
fancy55:
t€$t
<BLANKLINE>
fancy56:
𝐭𝐞𝐬𝐭
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
mirror:
ɈƨǝɈ
<BLANKLINE>
mirror_flip:
ʇsǝʇ
<BLANKLINE>
smallcaps2:
ᴛᴇsᴛ
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
symbols:
☂€ⓢ☂
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
>>> random.seed(24)
>>> Art = text2art("test","mix")
>>> random.seed(45)
>>> Art2 = text2art("test","mix")
>>> Art == Art2
False
>>> tprint("test","fancy1")
тεsт
<BLANKLINE>
>>> Data = tsave("test@34",font="antrophobia",filename="antrophobia.txt")
Saved!
Filename: antrophobia.txt
>>> Data = tsave("test@34",font="fancy37",filename="fancy37.txt")
Saved!
Filename: fancy37.txt
>>> os.remove("antrophobia.txt")
>>> os.remove("fancy37.txt")

'''
