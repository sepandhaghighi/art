<div align="center">
<pre>
 ______   ______  _______ 
| |  | | | |  | \   | |   
| |__| | | |__| |   | |   
|_|  |_| |_|  \_\   |_|   
         
</pre>
<a href="https://codecov.io/gh/sepandhaghighi/art">
  <img src="https://codecov.io/gh/sepandhaghighi/art/branch/master/graph/badge.svg" alt="Codecov" />
</a>
<a href="https://badge.fury.io/py/art"><img src="https://badge.fury.io/py/art.svg" alt="PyPI version" height="18"></a>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3" /></a>
<a href="https://github.com/sepandhaghighi/art/blob/master/FontList.ipynb"><img src="https://img.shields.io/badge/Font List-420-blue.svg"></a>
<a href="https://github.com/sepandhaghighi/art/blob/master/ArtList.ipynb"><img src="https://img.shields.io/badge/Art List-350-orange.svg"></a>
<a href="https://t.me/artlib_bot" target="__blank"><img src="https://img.shields.io/badge/Telegram-Bot-red.svg"></a>
<a href="https://anaconda.org/sepandhaghighi/art"><img src="https://anaconda.org/sepandhaghighi/art/badges/version.svg"></a>
</div>
	
----------

## Table of contents					
   * [Overview](https://github.com/sepandhaghighi/art#overview)
   * [Installation](https://github.com/sepandhaghighi/art/blob/master/INSTALL.md)
   * [Usage](https://github.com/sepandhaghighi/art#usage)
   		* [1-Line Art](https://github.com/sepandhaghighi/art#1-line-art)
   		* [ASCII Text](https://github.com/sepandhaghighi/art#ascii-text)
   		* [Font Modes](https://github.com/sepandhaghighi/art#font-modes)
   		* [Typo-Tolerance](https://github.com/sepandhaghighi/art#typo-tolerance)
   		* [Set Defaults](https://github.com/sepandhaghighi/art#set-defaults)
   		* [CLI](https://github.com/sepandhaghighi/art#cli)
   		* [Telegram Bot](https://github.com/sepandhaghighi/art#telegram-bot)
   		* [Try ART In Your Browser](https://github.com/sepandhaghighi/art#try-art-in-your-browser)
   		* [Screen Record](https://github.com/sepandhaghighi/art#screen-record)
   * [Issues & Bug Reports](https://github.com/sepandhaghighi/art#issues--bug-reports)
   * [Contribution](https://github.com/sepandhaghighi/art/blob/master/.github/CONTRIBUTING.md)
   * [Reference](https://github.com/sepandhaghighi/art#reference)
   * [Authors](https://github.com/sepandhaghighi/art/blob/master/AUTHORS.md)
   * [License](https://github.com/sepandhaghighi/art#license)
   * [Donate](https://github.com/sepandhaghighi/art#donate-to-our-project)
   * [Changelog](https://github.com/sepandhaghighi/art/blob/master/CHANGELOG.md)
   * [Code of Conduct](https://github.com/sepandhaghighi/art/blob/master/.github/CODE_OF_CONDUCT.md)

## Overview	
ASCII art is also known as "computer text art". It involves the smart placement of typed special characters or
letters to make a visual shape that is spread over multiple lines of text.
	
ART is a Python lib for text converting to ASCII art fancy. ;-)



<table>
	<tr> 
		<td align="center">Open Hub</td>
		<td align="center"><a href="https://www.openhub.net/p/artlib"><img src="https://www.openhub.net/p/artlib/widgets/project_thin_badge.gif"></a></td>	
	</tr>
	<tr>
		<td align="center">PyPI Counter</td>
		<td align="center"><a href="http://pepy.tech/count/art"><img src="http://pepy.tech/badge/art"></a></td>
	</tr>
	<tr>
		<td align="center">Github Stars</td>
		<td align="center"><a href="https://github.com/sepandhaghighi/art"><img src="https://img.shields.io/github/stars/sepandhaghighi/art.svg?style=social&label=Stars"></a></td>
	</tr>
	<tr>
		<td align="center">Font Counter</td>
		<td align="center">420</td>
	</tr>
	<tr>
		<td align="center">1-Line-Art Counter</td>
		<td align="center">350</td>
	</tr>
</table>



<table>
	<tr> 
		<td align="center">Branch</td>
		<td align="center">master</td>	
		<td align="center">dev</td>	
	</tr>
	<tr>
		<td align="center">Travis</td>
		<td align="center"><a href="https://travis-ci.org/sepandhaghighi/art"><img src="https://travis-ci.org/sepandhaghighi/art.svg?branch=master"></a></td>
		<td align="center"><a href="https://travis-ci.org/sepandhaghighi/art"><img src="https://travis-ci.org/sepandhaghighi/art.svg?branch=dev"></a></td>
	</tr>
	<tr>
		<td align="center">AppVeyor</td>
		<td align="center"><a href="https://ci.appveyor.com/project/sepandhaghighi/art"><img src="https://ci.appveyor.com/api/projects/status/n350ntyjthc2gil3/branch/master?svg=true"></a></td>
		<td align="center"><a href="https://ci.appveyor.com/project/sepandhaghighi/art"><img src="https://ci.appveyor.com/api/projects/status/n350ntyjthc2gil3/branch/dev?svg=true"></a></td>
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

<img src="https://github.com/sepandhaghighi/art/blob/master/otherfile/ART.gif">
<p>Quick Start</p>

</div>				


### 1-Line art

⚠️ Some environments don't support all 1-Line arts


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
>>> art_3=art("love_you",number=1,text="test") # 2-part art
>>> print(art_3)
»-(¯`·.·´¯)->test<-(¯`·.·´¯)-« 
>>> art("random") # random 1-line art mode
'(っ◕‿◕)っ '
>>> art("rand")   # random 1-line art mode
't(-_-t) '
>>> art(22,number=1,text="") # raise artError
Traceback (most recent call last):
        ...
art.art.artError: artname shoud have str type

```
#### 2. aprint				

This function print 1-line art in normal mode (return None) and raise `artError` in exception.
```pycon
>>> aprint("butterfly") # print art
Ƹ̵̡Ӝ̵̨̄Ʒ 
>>> aprint("happy") # print art
 ۜ\(סּںסּَ` )/ۜ
>>> aprint("love_you",number=1,text="test")  # 2-part art
»-(¯`·.·´¯)->test<-(¯`·.·´¯)-« 
>>> aprint("random") # random 1-line art mode
'(っ◕‿◕)っ '
>>> aprint("rand")   # random 1-line art mode
't(-_-t) '
>>> aprint("woman",number="22",text="") # raise artError
Traceback (most recent call last):
        ...
art.art.artError: number should have int type
```

#### 3. randart

`randart` function is added in `Version 2.2` as `art("random")` shortcut.
```pycon
>>> randart()
'ዞᏜ℘℘Ꮍ ℬℹℛʈዞᗬᏜᎽ '
>>> randart()
'✌(◕‿-)✌ '
```		

### ASCII text
	
⚠️ Some fonts don't support all characters		

⚠️ From `Version 3.3` Non-ASCII fonts added (These fonts are not compatible with some environments)

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

>>> text2art("seسسس",font=DEFAULT_FONT,chr_ignore=False) # raise artError in exception
Traceback (most recent call last):
        ...
art.art.artError: س is invalid 
  
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
                  

>>> tprint('testسس',chr_ignore=False) # raise artError in exception 
Traceback (most recent call last):
       ...
art.art.artError: س is invalid
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


```
#### 3. tsave				

This function return `dict` in normal and exception mode.
```pycon
>>> Response=tsave("art",filename="test.txt") # save ASCII text in test.txt file with save message (print_status==True) # return dict
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
                        
```

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
⚠️ Non-ASCII fonts are only available in `Font name` and `Random Non-ASCII` modes	


### Typo-tolerance			
<a href="https://en.wikipedia.org/wiki/Levenshtein_distance">Levenshtein distance</a> used in this project. (`Version` >0.9)

```pycon
>>> Art=art("loveyou",number=1,text="test") # correct --> art("love_you",number=1,text="test"), error < |artname|/2
>>> print(Art)
»-(¯`·.·´¯)->test<-(¯`·.·´¯)-« 
>>> aprint("happi")  # correct --> aprint("happy"), error < |artname|/2
 ۜ\(סּںסּَ` )/ۜ 
>>> Art=art("birds2222222",number=1) # correct --> Art=art("birds",number=1), error >= |artname|/2
Traceback (most recent call last):
	...
art.art.artError: Invalid art name
>>> aprint("happi231")  # correct --> aprint("happy"), error < |artname|/2
⎦˚◡˚⎣ 
>>> aprint("happi2312344") # correct --> aprint("happy"), error >= |artname|/2
Traceback (most recent call last):
	...
art.art.artError: Invalid art name
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

set_default(font='standard', chr_ignore=True, filename='art', print_status=True)
    This fuction change text2art tprint and tsave default values
    :param font: input font
    :type font:str
    :param chr_ignore: ignore not supported character
    :type chr_ignore:bool
    :param filename: output file name (only tsave)
    :type filename:str
    :param print_status : Save message print flag (only tsave)
    :type print_status:bool
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
 
### CLI			
- List of arts :  `python -m art list` or `python -m art arts`
- List of fonts : `python -m art fonts`
- Test : `python -m art test`
- Text : `python -m art text yourtext fontname(optional)`
- Art : `python -m art shape art_name` or `python -m art art art_name`
- Save :  `python -m art save yourtext fontname(optional)`
- All  :  `python -m art all yourtext`

### Telegram bot			

Just send your text to one of these bots. 👇👇👇👇		

<a href="https://t.me/artlib_bot" target="__blank"><img src="https://img.shields.io/badge/Telegram-Bot1-red.svg"></a>			

<a href="https://t.me/textart_robot" target="__blank"><img src="https://img.shields.io/badge/Telegram-Bot2-blue.svg"></a>


### Try ART in your browser

ART can be used online in interactive Jupyter Notebooks via the Binder service! Try it out now! :	

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sepandhaghighi/art/master)

* Open `FontList.ipynb` and `ArtList.ipynb`
* Edit and execute each part of the notes, step by step from the top panel by run button

### Screen record		


<div align="center">
<a href="https://asciinema.org/a/186368" target="_blank"><img src="https://asciinema.org/a/186368.png" /></a>
<p>Screen Record</p>
</div>

* View full font list ([Link1](https://github.com/sepandhaghighi/art/blob/master/FontList.ipynb "Full Font List"),[Link2](http://art.shaghighi.ir/FontList.html "Full Font List"))					
* View full art list ([Link1](https://github.com/sepandhaghighi/art/blob/master/ArtList.ipynb "Full Art List"),[Link2](http://art.shaghighi.ir/ArtList.html "Full Art List"))

## Issues & bug reports			

Just fill an issue and describe it. I'll check it ASAP!							
or send an email to [sepand.haghighi@yahoo.com](mailto:sepand.haghighi@yahoo.com "sepand.haghighi@yahoo.com"). 

* Please complete the issue template 

## License

[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fsepandhaghighi%2Fart.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fsepandhaghighi%2Fart?ref=badge_large)

## Reference    

1. [1 Line Art](http://1lineart.kulaone.com/#/)
2. [Text To ASCII](http://patorjk.com/software/taag/#p=display&f=Blocks&t=ART)
3. [ASCII Generator](http://www.network-science.de/ascii/)
4. [Asky](https://asky.io/)
5. [Flipyourtext](https://www.flipyourtext.com/)
6. [YayText](https://yaytext.com)
7. [Coolletters](http://www.coolletters.net/)

## Donate to our project
								
<h3>Bitcoin :</h3>					

```12Xm1qL4MXYWiY9sRMoa3VpfTfw6su3vNq```			



<h3>Payping (For Iranian citizens)</h3>

<a href="http://www.payping.net/sepandhaghighi" target="__blank"><img src="http://www.qpage.ir/images/payping.png" height=100px width=100px></a>	

<h3>Say Thanks! </h3>


<a href="https://saythanks.io/to/sepandhaghighi"><img src="https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg"></a>
