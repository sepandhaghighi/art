<div align="center">
<pre>
      ___           ___                   
     /\  \         /\  \                  
    /::\  \       /::\  \         ___     
   /:/\:\  \     /:/\:\__\       /\__\    
  /:/ /::\  \   /:/ /:/  /      /:/  /    
 /:/_/:/\:\__\ /:/_/:/__/___   /:/__/     
 \:\/:/  \/__/ \:\/:::::/  /  /::\  \     
  \::/__/       \::/~~/~~~~  /:/\:\  \    
   \:\  \        \:\~~\      \/__\:\  \   
    \:\__\        \:\__\          \:\__\  
     \/__/         \/__/           \/__/  


</pre>
<a class="badge-align" href="https://www.codacy.com/app/sepand-haghighi/art?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sepandhaghighi/art&amp;utm_campaign=Badge_Grade"><img src="https://api.codacy.com/project/badge/Grade/405020450bc94088ad1450461831a587"/></a>


<a href="https://codecov.io/gh/sepandhaghighi/art">
  <img src="https://codecov.io/gh/sepandhaghighi/art/branch/master/graph/badge.svg" alt="Codecov" />
</a>
<a href="https://travis-ci.org/sepandhaghighi/art"><img src="https://travis-ci.org/sepandhaghighi/art.svg?branch=master"></a>
<a href="https://ci.appveyor.com/project/sepandhaghighi/art"><img src="https://ci.appveyor.com/api/projects/status/n350ntyjthc2gil3?svg=true"></a>	
<a href="https://badge.fury.io/py/art"><img src="https://badge.fury.io/py/art.svg" alt="PyPI version" height="18"></a>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3" /></a>
<a href="https://github.com/sepandhaghighi/art/blob/master/FontList.ipynb"><img src="https://img.shields.io/badge/Font List-160-blue.svg"></a>
<a href="https://github.com/sepandhaghighi/art/blob/master/ArtList.ipynb"><img src="https://img.shields.io/badge/Art List-250-orange.svg"></a>
<a href="https://t.me/artlib_bot" target="__blank"><img src="https://img.shields.io/badge/Telegram-Bot-red.svg"></a>
</div>
	
----------

## Table of contents					
   * [Overview](https://github.com/sepandhaghighi/art#overview)
   * [Installation](https://github.com/sepandhaghighi/art/blob/master/INSTALL.md)
   * [Usage](https://github.com/sepandhaghighi/art#usage)
   		* [1-Line Art](https://github.com/sepandhaghighi/art#1-line-art)
   		* [ASCII Text](https://github.com/sepandhaghighi/art#ascii-text)
   		* [Typo-Tolerance](https://github.com/sepandhaghighi/art#typo-tolerance)
   		* [CLI](https://github.com/sepandhaghighi/art#cli)
   		* [Telegram Bot](https://github.com/sepandhaghighi/art#telegram-bot)
   		* [Screen Record](https://github.com/sepandhaghighi/art#screen-record)
   * [Issues & Bug Reports](https://github.com/sepandhaghighi/art#issues--bug-reports)
   * [Contribution](https://github.com/sepandhaghighi/art/blob/master/CONTRIBUTING.md)
   * [Reference](https://github.com/sepandhaghighi/art#reference)
   * [Authors](https://github.com/sepandhaghighi/art/blob/master/AUTHORS.md)
   * [License](https://github.com/sepandhaghighi/art#license)
   * [Donate](https://github.com/sepandhaghighi/art#donate-to-our-project)
   * [Changelog](https://github.com/sepandhaghighi/art/blob/master/CHANGELOG.md)

## Overview	
ASCII art is also known as "computer text art". It involves the smart placement of typed special characters or
letters to make a visual shape that is spread over multiple lines of text.
	
Art is a Python lib for text converting to ASCII ART fancy. ;-)

<html>
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
		<td align="center">160</td>
	</tr>
	<tr>
		<td align="center">1-Line-Art Counter</td>
		<td align="center">250</td>
	</tr>
</table>
</html>
    

## Usage

### 1-Line Art
1. art					

This function return 1-line art as `str` in normal mode and raise `artError` in exception	
<pre>
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

</pre>
2. aprint				

This function print 1-line art in normal mode (return None) and raise `artError` in exception
<pre>
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
</pre>
### ASCII Text
1. text2art				

This function return ascii text as `str` in normal mode and raise `artError` in exception
<pre>	
>>> Art=text2art("art") # Return ascii text (default font) and default chr_ignore=True 
>>> print(Art)
              _   
  __ _  _ __ | |_ 
 / _` || '__|| __|
| (_| || |   | |_ 
 \__,_||_|    \__|
                  
                     
>>> Art=text2art("art",font='block',chr_ignore=True) # Return ascii text with block font
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

>>> text2art("seسسس",font=DEFAULT_FONT,chr_ignore=False) # raise artError in exception
Traceback (most recent call last):
        ...
art.art.artError: س is invalid 
             
</pre>
2. tprint				

This function print ascii text in normal mode (return None) and raise `artError` in exception
<pre>
>>> tprint("art") # print ascii text (default font) 
              _   
  __ _  _ __ | |_ 
 / _` || '__|| __|
| (_| || |   | |_ 
 \__,_||_|    \__|
                  

>>> tprint("art",font="block",chr_ignore=True) # print ascii text (block font)

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
>>> tprint('''Lorem  # Multi-line print
ipsum 
dolor''', font="cybermedium")
_    ____ ____ ____ _  _    
|    |  | |__/ |___ |\/|    
|___ |__| |  \ |___ |  |    
                            
_ ___  ____ _  _ _  _    
| |__] [__  |  | |\/|    
| |    ___] |__| |  |    
                         
___  ____ _    ____ ____ 
|  \ |  | |    |  | |__/ 
|__/ |__| |___ |__| |  \ 


</pre>
3. tsave				

This function return `dict` in normal and exception mode
<pre>
>>> Response=tsave("art",filename="test.txt") # save ascii text in test.txt file with save message (print_status==True) # return dict
Saved! 
Filename: test.txt
>>> Response["Message"]
'OK'
>>> Response=tsave("art",filename="test.txt",print_status=False) # save ascii text in test.txt file without save message (print_status==False)
>>> Response["Message"]
'OK'
>>> Response["Status"]
True
>>> tsave(22,font=DEFAULT_FONT,filename="art",chr_ignore=True,print_status=True)
{'Status': False, 'Message': "'int' object has no attribute 'split'"}
                        
</pre>
* Note : Functions error response updated in `Version 0.8`

<html>
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
</table> 
</html>				

### Typo-Tolerance			
<a href="https://en.wikipedia.org/wiki/Levenshtein_distance">Levenshtein distance</a> used in this project. (>`Version 0.9`)

<pre>
>>> Art=art("loveyou",number=1,text="test") # correct --> art("love_you",number=1,text="test") (distance < 3)
>>> print(Art)
»-(¯`·.·´¯)->test<-(¯`·.·´¯)-« 
>>> aprint("happi")  # correct --> aprint("happy") (distance < 3)
 ۜ\(סּںסּَ` )/ۜ 
>>> Art=art("birds2222",number=1) # correct --> Art=art("birds",number=1) (distance > 3)
>>> print(Art)
Traceback (most recent call last):
	...
art.art.artError: Invalid art name
>>> aprint("happi231")  # correct --> aprint("happy") (distance > 3)
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
                  
   
</pre>

 
### CLI			
- List of arts :  `python -m art list` or `python -m art arts`
- List of fonts : `python -m art fonts`
- Test : `python -m art test`
- Text : `python -m art text yourtext fontname(optional)`
- Art : `python -m art shape art_name` or `python -m art art art_name`
- Save :  `python -m art save yourtext fontname(optional)`
- All  :  `python -m art all yourtext`

### Telegram Bot			

Just send your text to one of these bots. 👇👇👇👇		

<a href="https://t.me/artlib_bot" target="__blank"><img src="https://img.shields.io/badge/Telegram-Bot1-red.svg"></a>			

<a href="https://t.me/textart_robot" target="__blank"><img src="https://img.shields.io/badge/Telegram-Bot2-blue.svg"></a>

### Screen Record		


<div align="center">
<a href="https://asciinema.org/a/186368" target="_blank"><img src="https://asciinema.org/a/186368.png" /></a>
<p>Screen Record</p>
</div>

* View Full Font List ([Link1](https://github.com/sepandhaghighi/art/blob/master/FontList.ipynb "Full Font List"),[Link2](http://art.shaghighi.ir/FontList.html "Full Font List"))					
* View Full Art List ([Link1](https://github.com/sepandhaghighi/art/blob/master/ArtList.ipynb "Full Art List"),[Link2](http://art.shaghighi.ir/ArtList.html "Full Art List"))

## Issues & Bug Reports			

Just fill an issue and describe it. I'll check it ASAP!							
or send an email to [sepand@qpage.ir](mailto:sepand@qpage.ir "sepand@qpage.ir"). 

## License

[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fsepandhaghighi%2Fart.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fsepandhaghighi%2Fart?ref=badge_large)

## Reference    

1. [1 Line Art](http://1lineart.kulaone.com/#/)
2. [Text To ASCII](http://patorjk.com/software/taag/#p=display&f=Blocks&t=ART)

## Donate to our project
								
<h3>Bitcoin :</h3>					

```12Xm1qL4MXYWiY9sRMoa3VpfTfw6su3vNq```			



<h3>Payping (For Iranian citizens)</h3>

<a href="http://www.payping.net/sepandhaghighi" target="__blank"><img src="http://www.qpage.ir/images/payping.png" height=100px width=100px></a>	

<h3>Say Thanks! </h3>


<a href="https://saythanks.io/to/sepandhaghighi"><img src="https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg"></a>
