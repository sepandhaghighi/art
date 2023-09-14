<div align="center">
<img src="https://github.com/sepandhaghighi/art/raw/master/otherfile/logo.png" alt="Logo">
<br/>
<br/>
<a href="https://codecov.io/gh/sepandhaghighi/art">
  <img src="https://codecov.io/gh/sepandhaghighi/art/branch/master/graph/badge.svg" alt="Codecov" />
</a>
<a href="https://badge.fury.io/py/art"><img src="https://badge.fury.io/py/art.svg" alt="PyPI" height="18"></a>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3"></a>
<a href="https://github.com/sepandhaghighi/art/blob/master/FontList.ipynb"><img src="https://img.shields.io/badge/Font List-652-blue.svg" alt="Font List"></a>
<a href="https://github.com/sepandhaghighi/art/blob/master/ArtList.ipynb"><img src="https://img.shields.io/badge/Art List-710-orange.svg" alt="Art List"></a>
<a href="https://github.com/sepandhaghighi/art/blob/master/DecorList.ipynb"><img src="https://img.shields.io/badge/Decor List-218-green.svg" alt="Decor List"></a>
<a href="https://t.me/artlib_bot" target="__blank"><img src="https://img.shields.io/badge/Telegram-Bot-red.svg" alt="Telegram Bot"></a>
<a href="https://anaconda.org/sepandhaghighi/art"><img src="https://anaconda.org/sepandhaghighi/art/badges/version.svg" alt="Anaconda"></a>
<a href="https://discord.com/invite/FAAyq3QJqP"><img src="https://img.shields.io/discord/897532566301724722.svg" alt="Discord Channel"></a>
</div>
	
----------

## Table of contents					
   * [Overview](https://github.com/sepandhaghighi/art#overview)
   * [Installation](https://github.com/sepandhaghighi/art/blob/master/INSTALL.md)
   * [Usage](https://github.com/sepandhaghighi/art#usage)
   		* [1-Line Art](https://github.com/sepandhaghighi/art#1-line-art)
   		* [ASCII Text](https://github.com/sepandhaghighi/art#ascii-text)
   		* [Decoration](https://github.com/sepandhaghighi/art#decoration)
   		* [Font Modes](https://github.com/sepandhaghighi/art#font-modes)
   		* [Typo-Tolerance](https://github.com/sepandhaghighi/art#typo-tolerance)
   		* [Set Defaults](https://github.com/sepandhaghighi/art#set-defaults)
   		* [Testing](https://github.com/sepandhaghighi/art#testing)
   		* [CLI](https://github.com/sepandhaghighi/art#cli)
   		* [Telegram Bot](https://github.com/sepandhaghighi/art#telegram-bot)
   		* [Try ART in Your Browser](https://github.com/sepandhaghighi/art#try-art-in-your-browser)
   		* [Screen Record](https://github.com/sepandhaghighi/art#screen-record)
   * [Issues & Bug Reports](https://github.com/sepandhaghighi/art#issues--bug-reports)
   * [Contribution](https://github.com/sepandhaghighi/art/blob/master/.github/CONTRIBUTING.md)
   * [Reference](https://github.com/sepandhaghighi/art#reference)
   * [Authors](https://github.com/sepandhaghighi/art/blob/master/AUTHORS.md)
   * [License](https://github.com/sepandhaghighi/art/blob/master/LICENSE)
   * [Show Your Support](https://github.com/sepandhaghighi/art#show-your-support)
   * [Changelog](https://github.com/sepandhaghighi/art/blob/master/CHANGELOG.md)
   * [Code of Conduct](https://github.com/sepandhaghighi/art/blob/master/.github/CODE_OF_CONDUCT.md)

## Overview	
ASCII art is also known as "computer text art". It involves the smart placement of typed special characters or
letters to make a visual shape that is spread over multiple lines of text.
	
ART is a Python lib for text converting to ASCII art fancy. ;-)



<table>
	<tr align="center"> 
		<td>Open Hub</td>
		<td><a href="https://www.openhub.net/p/artlib"><img src="https://www.openhub.net/p/artlib/widgets/project_thin_badge.gif"></a></td>	
	</tr>
	<tr align="center">
		<td>PyPI Counter</td>
		<td><a href="http://pepy.tech/project/art"><img src="http://pepy.tech/badge/art"></a></td>
	</tr>
	<tr align="center">
		<td>Github Stars</td>
		<td><a href="https://github.com/sepandhaghighi/art"><img src="https://img.shields.io/github/stars/sepandhaghighi/art.svg?style=social&label=Stars"></a></td>
	</tr>
	<tr align="center">
		<td>Font Counter</td>
		<td id="font_counter">652</td>
	</tr>
	<tr align="center">
		<td>1-Line-Art Counter</td>
		<td id="art_counter">710</td>
	</tr>
    <tr align="center">
		<td>Decor Counter</td>
		<td id="decor_counter">218</td>
	</tr>
</table>



<table>
	<tr> 
		<td align="center">Branch</td>
		<td align="center">master</td>	
		<td align="center">dev</td>	
	</tr>
	<tr>
		<td align="center">CI</td>
		<td align="center"><img src="https://github.com/sepandhaghighi/art/workflows/CI/badge.svg?branch=master"></td>
		<td align="center"><img src="https://github.com/sepandhaghighi/art/workflows/CI/badge.svg?branch=dev"></td>
	</tr>
</table>

<table>
	<tr> 
		<td align="center">Code Quality</td>
		<td align="center"><a class="badge-align" href="https://www.codacy.com/app/sepand-haghighi/art?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sepandhaghighi/art&amp;utm_campaign=Badge_Grade"><img src="https://api.codacy.com/project/badge/Grade/405020450bc94088ad1450461831a587"/></a></td>	
		<td align="center"><a href="https://codebeat.co/projects/github-com-sepandhaghighi-art-dev"><img alt="codebeat badge" src="https://codebeat.co/badges/90e77325-a046-4cc5-9c3e-646c011a5b72" /></a></td>	
		<td align="center"><a href="https://www.codefactor.io/repository/github/sepandhaghighi/art"><img src="https://www.codefactor.io/repository/github/sepandhaghighi/art/badge" alt="CodeFactor" /></a></td>
	</tr>
</table>

    

## Usage

<div align="center">

<img src="https://github.com/sepandhaghighi/art/raw/master/otherfile/ART.gif">
<p>Quick Start</p>

</div>				


### 1-Line art

⚠️ Some environments don't support all 1-Line arts

⚠️ **ART 4.6** is the last version to support **Bipartite art**


#### 1. art					

This function return 1-line art as `str` in normal mode and raise `artError` in exception.	
```pycon
>>> from art import *
>>> art_1=art("coffee") # return art as str in normal mode
>>> print(art_1)
c[_]
>>> art_2=art("woman",number=2) # return multiple art as str
>>> print(art_2)
▓⚗_⚗▓ ▓⚗_⚗▓ 
>>> art("coffee", number=3, space=5) 
'c[_]     c[_]     c[_]'
>>> art("random") # random 1-line art mode
'(っ◕‿◕)っ '
>>> art("rand")   # random 1-line art mode
't(-_-t) '
>>> art(22,number=1) # raise artError
Traceback (most recent call last):
        ...
art.art.artError: The 'artname' type must be str.

```
#### 2. aprint				

This function print 1-line art in normal mode (return None) and raise `artError` in exception.
```pycon
>>> aprint("butterfly") # print art
Ƹ̵̡Ӝ̵̨̄Ʒ 
>>> aprint("happy") # print art
 ۜ\(סּںסּَ` )/ۜ
>>> aprint("coffee", number=3, space=5) 
c[_]     c[_]     c[_] 
>>> aprint("random") # random 1-line art mode
'(っ◕‿◕)っ '
>>> aprint("rand")   # random 1-line art mode
't(-_-t) '
>>> aprint("woman",number="22") # raise artError
Traceback (most recent call last):
        ...
art.art.artError: The 'number' type must be int.
```

#### 3. randart

`randart` function is added in `Version 2.2` as `art("random")` shortcut.
```pycon
>>> randart()
'ዞᏜ℘℘Ꮍ ℬℹℛʈዞᗬᏜᎽ '
>>> randart()
'✌(◕‿-)✌ '
```	

* Note1 : Use `ART_NAMES` to access all arts name list (new in `Version 4.2`)
* Note2 : Use `NON_ASCII_ARTS` to access all Non-ASCII arts name list (new in `Version 4.6`)
* Note3 : Use `ASCII_ARTS` to access all ASCII arts name list (new in `Version 5.7`)

### ASCII text
	
⚠️ Some fonts don't support all characters		

⚠️ From `Version 3.3` Non-ASCII fonts added (These fonts are not compatible with some environments)

⚠️ From `Version 5.3` `\n` is used as the default line separator instead of `\r\n` (Use `sep` parameter if needed)

#### 1. text2art				

This function return ASCII text as `str` in normal mode and raise `artError` in exception.
```pycon	
>>> Art=text2art("art") # Return ASCII text (default font) and default chr_ignore=True 
>>> print(Art)
              _   
  __ _  _ __ | |_ 
 / _` || '__|| __|
| (_| || |   | |_ 
 \__,_||_|    \__|
                  
                     
>>> Art=text2art("art",font='block',chr_ignore=True) # Return ASCII text with block font
>>> print(Art)


 .----------------.  .----------------.  .----------------.
| .--------------. || .--------------. || .--------------. |
| |      __      | || |  _______     | || |  _________   | |
| |     /  \     | || | |_   __ \    | || | |  _   _  |  | |
| |    / /\ \    | || |   | |__) |   | || | |_/ | | \_|  | |
| |   / ____ \   | || |   |  __ /    | || |     | |      | |
| | _/ /    \ \_ | || |  _| |  \ \_  | || |    _| |_     | |
| ||____|  |____|| || | |____| |___| | || |   |_____|    | |
| |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'

>>> Art=text2art("test","random") # random font mode
>>> print(Art)
 |       | 
~|~/~/(~~|~
 | \/__) | 
           
>>> Art=text2art("test","rand") # random font mode
>>> print(Art)
___ ____ ____ ___ 
 |  |___ [__   |  
 |  |___ ___]  | 

>>> print(text2art("test", space=10))
 _                                             _   
| |_             ___            ___           | |_ 
| __|           / _ \          / __|          | __|
| |_           |  __/          \__ \          | |_ 
 \__|           \___|          |___/           \__|
                                                   
>>> print(text2art('''Lorem  
ipsum 
dolor''', font="small")) # Multi-line print
 _                            
| |    ___  _ _  ___  _ __    
| |__ / _ \| '_|/ -_)| '  \   
|____|\___/|_|  \___||_|_|_|  
                              
 _                         
(_) _ __  ___ _  _  _ __   
| || '_ \(_-<| || || '  \  
|_|| .__//__/ \_,_||_|_|_| 
   |_|                     
    _       _           
 __| | ___ | | ___  _ _ 
/ _` |/ _ \| |/ _ \| '_|
\__,_|\___/|_|\___/|_|  
                        

>>> print(text2art("test","white_bubble"))  # Non-ASCII font example
ⓣⓔⓢⓣ
>>> text2art("art",font="fancy5",decoration="barcode1") # decoration parameter is added in Version 4.6
'▌│█║▌║▌║ ᏗᏒᏖ ║▌║▌║█│▌'
>>> text2art("seسسس",font=DEFAULT_FONT,chr_ignore=False) # raise artError in exception
Traceback (most recent call last):
        ...
art.art.artError: س is invalid.
  
```
#### 2. tprint				

This function print ASCII text in normal mode (return None) and raise `artError` in exception.
```pycon
>>> tprint("art") # print ASCII text (default font) 
              _   
  __ _  _ __ | |_ 
 / _` || '__|| __|
| (_| || |   | |_ 
 \__,_||_|    \__|
                  

>>> tprint("art",font="block",chr_ignore=True) # print ASCII text (block font)

 .----------------.  .----------------.  .----------------.
| .--------------. || .--------------. || .--------------. |
| |      __      | || |  _______     | || |  _________   | |
| |     /  \     | || | |_   __ \    | || | |  _   _  |  | |
| |    / /\ \    | || |   | |__) |   | || | |_/ | | \_|  | |
| |   / ____ \   | || |   |  __ /    | || |     | |      | |
| | _/ /    \ \_ | || |  _| |  \ \_  | || |    _| |_     | |
| ||____|  |____|| || | |____| |___| | || |   |_____|    | |
| |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'

>>> tprint('testسس')  # chr_ignore flag ==True (Default)
 _               _   
| |_   ___  ___ | |_ 
| __| / _ \/ __|| __|
| |_ |  __/\__ \| |_ 
 \__| \___||___/ \__|
                     
>>> tprint("test","random") # random font mode
 |       | 
~|~/~/(~~|~
 | \/__) | 
           
>>> tprint("test","rand") # random font mode
___ ____ ____ ___ 
 |  |___ [__   |  
 |  |___ ___]  |  
                  
>>> tprint("test", space=10)
 _                                             _   
| |_             ___            ___           | |_ 
| __|           / _ \          / __|          | __|
| |_           |  __/          \__ \          | |_ 
 \__|           \___|          |___/           \__|
                                                   
>>> tprint('testسس',chr_ignore=False) # raise artError in exception 
Traceback (most recent call last):
       ...
art.art.artError: س is invalid.
>>> tprint('''Lorem  
ipsum 
dolor''', font="cybermedium") # Multi-line print
_    ____ ____ ____ _  _    
|    |  | |__/ |___ |\/|    
|___ |__| |  \ |___ |  |    
                            
_ ___  ____ _  _ _  _    
| |__] [__  |  | |\/|    
| |    ___] |__| |  |    
                         
___  ____ _    ____ ____ 
|  \ |  | |    |  | |__/ 
|__/ |__| |___ |__| |  \ 

>>> tprint("art",font="fancy5",decoration="barcode1") # decoration parameter is added in Version 4.6
▌│█║▌║▌║ ᏗᏒᏖ ║▌║▌║█│▌
>>> tprint("art",font="fancy5",decoration="random") # decoration random mode is added in Version 5.0
•]•·✦º✦·»ᏗᏒᏖ«·✦º✦·•[•
```
#### 3. tsave				

This function return `dict` in normal and exception mode.
```pycon
>>> Response=tsave("art",filename="test.txt") # save ASCII text in test.txt file with save message (print_status==True), return dict
Saved! 
Filename: test.txt
>>> Response["Message"]
'OK'
>>> Response=tsave("art",filename="test.txt",print_status=False) # save ASCII text in test.txt file without save message (print_status==False)
>>> Response["Message"]
'OK'
>>> Response["Status"]
True
>>> tsave(22,font=DEFAULT_FONT,filename="art",chr_ignore=True,print_status=True)
{'Status': False, 'Message': "'int' object has no attribute 'split'"}
>>> Response=tsave("art",filename="test.txt",overwrite=True) # overwrite parameter is added in Version 4.0
Saved! 
Filename: test.txt
>>> Response=tsave("art",filename="test.txt",decoration="barcode1") # decoration parameter is added in Version 4.6
Saved! 
Filename: test.txt
>>> Response=tsave("art",filename="test.txt",sep="\r\n") # sep parameter is added in Version 5.3
Saved! 
Filename: test.txt                        
>>> Response=tsave("art",filename="test.txt",space=5) # space parameter is added in Version 6.0
Saved! 
Filename: test.txt                        
```

* Note1 : Use `FONT_NAMES` to access all fonts name list (new in `Version 4.2`)
* Note2 : Use `NON_ASCII_FONTS` to access all Non-ASCII fonts name list (new in `Version 4.4`)
* Note3 : Use `ASCII_FONTS` to access all ASCII fonts name list (new in `Version 5.7`)

### Decoration

⚠️ Some environments don't support all decorations

#### 1. decor

This function return decoration as `str` in normal mode and raise `artError` in exception.
```pycon
>>> decor("barcode1")
'▌│█║▌║▌║ '
>>> decor("barcode1",reverse=True)
' ║▌║▌║█│▌'
>>> decor("barcode1") + text2art("    art   ",font="fancy42") + decor("barcode1",reverse=True)
'▌│█║▌║▌║     ąяţ    ║▌║▌║█│▌'
>>> decor("barcode1",both=True) # both parameter is added in Version 5.0
['▌│█║▌║▌║ ', ' ║▌║▌║█│▌']
>>> decor("random",both=True) # random mode is added in Version 5.0
['｢(◔ω◔「)三', '三三三ʅ(；◔౪◔)ʃ']
>>> decor("rand",both=True) # random mode is added in Version 5.0
['‹–…·´`·…–›', '‹–…·´`·…–›']
>>> decor(None)
Traceback (most recent call last):
	...
art.art.artError: The 'decoration' type must be str.
```

* Note : Use `DECORATION_NAMES` to access all decorations name list (new in `Version 4.6`)

### Font modes

These modes are available for `text2art`, `tprint` & `tsave`.	

#### 1. Font name	

⚠️ Some fonts don't support all characters
			
```pycon

>>> tprint("art",font="block",chr_ignore=True)

 .----------------.  .----------------.  .----------------.
| .--------------. || .--------------. || .--------------. |
| |      __      | || |  _______     | || |  _________   | |
| |     /  \     | || | |_   __ \    | || | |  _   _  |  | |
| |    / /\ \    | || |   | |__) |   | || | |_/ | | \_|  | |
| |   / ____ \   | || |   |  __ /    | || |     | |      | |
| | _/ /    \ \_ | || |  _| |  \ \_  | || |    _| |_     | |
| ||____|  |____|| || | |____| |___| | || |   |_____|    | |
| |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'

>>> tprint("art","white_bubble")
ⓐⓡⓣ

```	

#### 2. Random		

Randomly select from all fonts.	

Keywords : `random`, `rand` & `rnd`

```pycon
>>> tprint("test",font="random")
 |       | 
~|~/~/(~~|~
 | \/__) | 
  

```

#### 3. Random small

Randomly select from small fonts.	

Keywords : `rnd-small`, `random-small` & `rand-small`

* Note : New in `Version 2.8`

```pycon
>>> tprint("test",font="rnd-small")
             
_/  _   _ _/ 
/  (- _)  /  
             
```

#### 4. Random medium

Randomly select from medium fonts.

Keywords : `rnd-medium`, `random-medium` & `rand-medium`

* Note : New in `Version 2.8`

```pycon
>>> tprint("test",font="rnd-medium")
                      
  ,                ,  
 ||               ||  
=||=  _-_   _-_, =||= 
 ||  || \\ ||_.   ||  
 ||  ||/    ~ ||  ||  
 \\, \\,/  ,-_-   \\, 
                      
                      
```

#### 5. Random large

Randomly select from large fonts.

Keywords : `rnd-large`, `random-large` & `rand-large`

* Note : New in `Version 2.8`

```pycon
>>> tprint("test",font="rnd-large")
                                                                    
8888888 8888888888 8 8888888888      d888888o.   8888888 8888888888 
      8 8888       8 8888          .`8888:' `88.       8 8888       
      8 8888       8 8888          8.`8888.   Y8       8 8888       
      8 8888       8 8888          `8.`8888.           8 8888       
      8 8888       8 888888888888   `8.`8888.          8 8888       
      8 8888       8 8888            `8.`8888.         8 8888       
      8 8888       8 8888             `8.`8888.        8 8888       
      8 8888       8 8888         8b   `8.`8888.       8 8888       
      8 8888       8 8888         `8b.  ;8.`8888       8 8888       
      8 8888       8 888888888888  `Y8888P ,88P'       8 8888       


```

#### 6. Random xlarge

Randomly select from xlarge fonts.	

Keywords : `rnd-xlarge`, `random-xlarge` & `rand-xlarge`

* Note : New in `Version 2.8`

```pycon
>>> tprint("test","rnd-xlarge")
      _____                    _____                    _____                _____          
     /\    \                  /\    \                  /\    \              /\    \         
    /::\    \                /::\    \                /::\    \            /::\    \        
    \:::\    \              /::::\    \              /::::\    \           \:::\    \       
     \:::\    \            /::::::\    \            /::::::\    \           \:::\    \      
      \:::\    \          /:::/\:::\    \          /:::/\:::\    \           \:::\    \     
       \:::\    \        /:::/__\:::\    \        /:::/__\:::\    \           \:::\    \    
       /::::\    \      /::::\   \:::\    \       \:::\   \:::\    \          /::::\    \   
      /::::::\    \    /::::::\   \:::\    \    ___\:::\   \:::\    \        /::::::\    \  
     /:::/\:::\    \  /:::/\:::\   \:::\    \  /\   \:::\   \:::\    \      /:::/\:::\    \ 
    /:::/  \:::\____\/:::/__\:::\   \:::\____\/::\   \:::\   \:::\____\    /:::/  \:::\____\
   /:::/    \::/    /\:::\   \:::\   \::/    /\:::\   \:::\   \::/    /   /:::/    \::/    /
  /:::/    / \/____/  \:::\   \:::\   \/____/  \:::\   \:::\   \/____/   /:::/    / \/____/ 
 /:::/    /            \:::\   \:::\    \       \:::\   \:::\    \      /:::/    /          
/:::/    /              \:::\   \:::\____\       \:::\   \:::\____\    /:::/    /           
\::/    /                \:::\   \::/    /        \:::\  /:::/    /    \::/    /            
 \/____/                  \:::\   \/____/          \:::\/:::/    /      \/____/             
                           \:::\    \               \::::::/    /                           
                            \:::\____\               \::::/    /                            
                             \::/    /                \::/    /                             
                              \/____/                  \/____/                              
                                                                                            
```
	
#### 7. Wizard	

This mode consider length of input text to select font

☑️ Support of 95 ASCII characters guaranteed

Keywords : `wizard`, `wiz` & `magic`

* Note : New in `Version 2.9`

```pycon
>>> tprint("1","wizard")
    88 
  ,d88 
888888 
    88 
    88 
    88 
    88 
    88 
    88 
    88 
       
            

>>> tprint("1"*5,"wizard")
d88  d88  d88  d88  d88  
 88   88   88   88   88  
 88   88   88   88   88  
 88   88   88   88   88  
 88   88   88   88   88  
d88P d88P d88P d88P d88P 
                         
                         

>>> tprint("1"*15,"wizard")
                                             
                                             
 #  #  #  #  #  #  #  #  #  #  #  #  #  #  # 
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 
 #  #  #  #  #  #  #  #  #  #  #  #  #  #  # 
 #  #  #  #  #  #  #  #  #  #  #  #  #  #  # 
 #  #  #  #  #  #  #  #  #  #  #  #  #  #  # 
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 
                                             
                                             
```
	


#### 8. Random Non-ASCII

Randomly select from Non-ASCII fonts.	

Keywords : `random-na`, `rand-na` & `rnd-na`

* Note : New in `Version 3.4`

```pycon
>>> tprint("test","random-na")
₮Ɇ₴₮
>>> tprint("test","random-na")
ʇsǝʇ

```

#### 9. Mix Non-ASCII

Randomly mix Non-ASCII fonts.

Keywords : `mix`

* Note : New in `Version 3.7`

```pycon
>>> tprint("test","mix")
†Ɛѕ†
>>> tprint("test","mix")
tᏋѕt
>>> tprint("test","mix")
꓄єร꓄
```

⚠️ Non-ASCII fonts are only available in `Font name`, `Random Non-ASCII` and `Mix` modes	


### Typo-tolerance			
<a href="https://en.wikipedia.org/wiki/Levenshtein_distance">Levenshtein distance</a> used in this project. (`Version` >0.9)

```pycon
>>> aprint("happi")  # correct --> aprint("happy"), error < |artname|/2
 ۜ\(סּںסּَ` )/ۜ 
>>> Art=art("birds2222222",number=1) # correct --> Art=art("birds",number=1), error >= |artname|/2
Traceback (most recent call last):
	...
art.art.artError: Invalid art name.
>>> aprint("happi231")  # correct --> aprint("happy"), error < |artname|/2
⎦˚◡˚⎣ 
>>> aprint("happi2312344") # correct --> aprint("happy"), error >= |artname|/2
Traceback (most recent call last):
	...
art.art.artError: Invalid art name.
>>> Art=text2art("test",font="black") # correct --> Art=text2art("test",font="block")
>>> print(Art)

 .----------------.  .----------------.  .----------------.  .----------------.
| .--------------. || .--------------. || .--------------. || .--------------. |
| |  _________   | || |  _________   | || |    _______   | || |  _________   | |
| | |  _   _  |  | || | |_   ___  |  | || |   /  ___  |  | || | |  _   _  |  | |
| | |_/ | | \_|  | || |   | |_  \_|  | || |  |  (__ \_|  | || | |_/ | | \_|  | |
| |     | |      | || |   |  _|  _   | || |   '.___`-.   | || |     | |      | |
| |    _| |_     | || |  _| |___/ |  | || |  |`\____) |  | || |    _| |_     | |
| |   |_____|    | || | |_________|  | || |  |_______.'  | || |   |_____|    | |
| |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'

>>> tprint("test",font="cybermedum")   # correct --> tprint("test",font="cybermedium")
___ ____ ____ ___ 
 |  |___ [__   |  
 |  |___ ___]  |  
                  
   
```

### Set defaults			
`set_default` function is added in `Version 2.2` in order to change default values.

```pycon
>>> help(set_default)
Help on function set_default in module art.art:

set_default(font='standard', chr_ignore=True, filename='art', print_status=True, overwrite=False, decoration=None, sep='\n')
    Change text2art, tprint and tsave default values.
    
    :param font: input font
    :type font:str
    :param chr_ignore: ignore not supported character
    :type chr_ignore:bool
    :param filename: output file name (only tsave)
    :type filename:str
    :param print_status : save message print flag (only tsave)
    :type print_status:bool
    :param overwrite : overwrite the saved file if true (only tsave)
    :type overwrite:bool
    :param decoration: input decoration
    :type decoration:str
    :param sep: line separator char
    :type sep: str
    :return: None

>>> tprint("test")
 _               _   
| |_   ___  ___ | |_ 
| __| / _ \/ __|| __|
| |_ |  __/\__ \| |_ 
 \__| \___||___/ \__|
                     

>>> set_default(font="italic")
>>> tprint("test")
             
_/  _   _ _/ 
/  (- _)  /  
             

```
* Note : Functions error response updated in `Version 0.8`

	<table>
	<tr>
		<td align="center">Function</td>
		<td align="center">Normal Output</td>
		<td align="center">Error</td>
	</tr>
    <tr>
		<td align="center">decor</td>
		<td align="center">str</td>
		<td align="center">raise artError</td>

	</tr>
	<tr>
		<td align="center">art</td>
		<td align="center">str</td>
		<td align="center">raise artError</td>

	</tr>
	<tr>
		<td align="center">aprint</td>
		<td align="center">None</td>
		<td align="center">raise artError</td>
	</tr>
	<tr>
		<td align="center">tprint</td>
		<td align="center">None</td>
		<td align="center">raise artError</td>
	</tr>
	<tr>
		<td align="center">tsave</td>
		<td align="center">{"Status":bool,"Message":str}</td>
		<td align="center">{"Status":bool,"Message":str}</td>
	</tr>
	<tr>
		<td align="center">text2art</td>
		<td align="center">str</td>
		<td align="center">raise artError</td>
	</tr>	
	<tr>
		<td align="center">set_default</td>
		<td align="center">None</td>
		<td align="center">raise artError</td>
	</tr>	
	</table> 

### Testing
- Only ASCII fonts and arts :
```
art test
```

- All fonts, arts and decorations :
```
art test2
```

### CLI	
⚠️ [Backward Compatibility] **ART 5.9** is the last version to support this **CLI structure** officially

⚠️ You can use `art` or `python -m art` to run this mode
		
- List of arts :  `art list` or `art arts`
- List of fonts : `art fonts`
- Text : `art text [yourtext] [fontname(optional)]`
- Art : `art shape [artname]` or `art art [artname]`
- Save :  `art save [yourtext] [fontname(optional)]`
- All  :  `art all [yourtext]`

### Telegram bot			

Just send your text to one of these bots. 👇👇👇👇		

<a href="https://t.me/artlib_bot" target="__blank"><img src="https://img.shields.io/badge/Telegram-Bot1-red.svg"></a>			

<a href="https://t.me/textart_robot" target="__blank"><img src="https://img.shields.io/badge/Telegram-Bot2-blue.svg"></a>


### Try ART in your browser

1. ART can be used online in interactive Jupyter Notebooks via the Binder service! Try it out now! :	

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sepandhaghighi/art/master)

* Open `FontList.ipynb`, `ArtList.ipynb` and `DecorList.ipynb`
* Edit and execute each part of the notes, step by step from the top panel by run button

2. ART also can be used online in [ascii-generator.site](https://ascii-generator.site/), a Django website by [hermanTenuki](https://github.com/hermanTenuki)	

### Screen record		


<div align="center">
<a href="https://asciinema.org/a/186368" target="_blank"><img src="https://asciinema.org/a/186368.png" /></a>
<p>Screen Record</p>
</div>

* View full font list ([Link1](https://github.com/sepandhaghighi/art/blob/master/FontList.ipynb "Full Font List"),[Link2](https://www.ascii-art.site/FontList.html "Full Font List"))					
* View full art list ([Link1](https://github.com/sepandhaghighi/art/blob/master/ArtList.ipynb "Full Art List"),[Link2](https://www.ascii-art.site/ArtList.html "Full Art List"))
* View full decoration list ([Link1](https://github.com/sepandhaghighi/art/blob/master/DecorList.ipynb "Full Decoration List"),[Link2](https://www.ascii-art.site/DecorList.html "Full Decoration List"))

## Issues & bug reports			

1. Fill an issue and describe it. We'll check it ASAP!
    - Please complete the issue template
2. Discord : [https://discord.com/invite/FAAyq3QJqP](https://discord.com/invite/FAAyq3QJqP)
3. Website : [https://www.ascii-art.site](https://www.ascii-art.site)
4. Email : [info@ascii-art.site](mailto:info@ascii-art.site "info@ascii-art.site")

## Reference    

1. [FIGlet](http://www.figlet.org/)
2. [1 Line Art](http://1lineart.kulaone.com/#/)
3. [Text to ASCII](http://patorjk.com/software/taag/#p=display&f=Blocks&t=ART)
4. [ASCII Generator](http://www.network-science.de/ascii/)
5. [Asky](https://asky.io/)
6. [Flipyourtext](https://www.flipyourtext.com/)
7. [YayText](https://yaytext.com)
8. [Coolletters](http://www.coolletters.net/)
9. [Instagram Fonts](https://igfonts.io/)
10. [Cool Symbol](https://coolsymbol.com/)
11. [ASCII Moji](http://asciimoji.com/)
12. [SMILEY COOL](https://smiley.cool/)
13. [SPREZZ](https://www.sprezzkeyboard.com/)
14. [Textart4u](http://textart4u.blogspot.com/2013/03/one-line-ascii-text-art.html?m=1)
15. [Chat4o](https://en.chat4o.com/ascii/)
16. [Findwebapp](http://www.findwebapp.com/ascii-art-one-liner/)
17. [Hubpages](https://hubpages.com/technology/one-line-ascii-art-for-twitter)
18. [ASCII-ART](http://www.ascii-art.de/ascii/mno/one_line.txt)
19. [Messletters](https://www.messletters.com/en/)
20. [Webestools](http://www.webestools.com/)
21. [ASCII-emoji](https://github.com/dysfunc/ascii-emoji)
22. [Instagram Fonts2](https://www.instagramfonts.com/)
23. [Emotiworld](http://en.emotiworld.com/)
24. [Fancy Text Pro](https://www.fancytextpro.com/)
25. [Playing Cards in Unicode](https://en.m.wikipedia.org/wiki/Playing_cards_in_Unicode)
26. [Text Generator](https://coolfonts.text-generator.org/)
27. [GOGOTEXT](https://instafontsgen.codesdetail.com)
28. [Fsymbols](https://fsymbols.com/)
29. [Font Copy and Paste](https://www.fontcopypaste.com/)
30. [Mega Cool Text](http://megacooltext.com/)
31. [ToolCalculator](https://www.toolcalculator.com/)


* Logo designed by [Arta Khanalizadeh](https://www.linkedin.com/in/artakhanalizadeh)	

## Show your support
								
<h3>Star this repo</h3>					

Give a ⭐️ if this project helped you!

<h3>Donate to our project</h3>	

If you do like our project and we hope that you do, can you please support us? Our project is not and is never going to be working for profit. We need the money just so we can continue doing what we do ;-) .			

<a href="https://www.ascii-art.site/#support" target="_blank"><img src="https://github.com/sepandhaghighi/art/raw/master/otherfile/donate-button.png" height="90px" width="270px" alt="Art Donation"></a>

<h3>Become a sponsor to ART</h3>

* Contact us at the email first	

<h4>Corporate sponsor</h4>

- **$250** a month
- Your company's logo can be featured on **Readme**
- Intended for small companies


<h4>Mega corporate sponsor</h4>

- **$500** a month
- Your company's logo can be featured on **Readme** and **Website**
- Intended for medium-sized companies

