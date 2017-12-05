<div align="center">
<pre>
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

</pre>
<a class="badge-align" href="https://www.codacy.com/app/sepand-haghighi/art?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sepandhaghighi/art&amp;utm_campaign=Badge_Grade"><img src="https://api.codacy.com/project/badge/Grade/405020450bc94088ad1450461831a587"/></a>


<a href="https://codecov.io/gh/sepandhaghighi/art">
  <img src="https://codecov.io/gh/sepandhaghighi/art/branch/master/graph/badge.svg" alt="Codecov" />
</a>
<a href="https://travis-ci.org/sepandhaghighi/art"><img src="https://travis-ci.org/sepandhaghighi/art.svg?branch=master"></a>
<a href="https://ci.appveyor.com/project/sepandhaghighi/art"><img src="https://ci.appveyor.com/api/projects/status/n350ntyjthc2gil3?svg=true"></a>	
<a href="https://badge.fury.io/py/art"><img src="https://badge.fury.io/py/art.svg" alt="PyPI version" height="18"></a>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3" /></a>
<a href="list.md#fonts"><img src="https://img.shields.io/badge/Font-List-blue.svg"></a>
<a href="list.md#1-line-art"><img src="https://img.shields.io/badge/Art-List-orange.svg"></a>
<a href="https://t.me/artlib_bot" target="__blank"><img src="https://img.shields.io/badge/Telegram-Bot-red.svg"></a>

</div>
	
----------

## Overview			
Simple ASCII Art Library For Python

## Installation		

### Source Code
- Download [Version 0.5](https://github.com/sepandhaghighi/art/archive/v0.5.zip) or [Latest Source ](https://github.com/sepandhaghighi/art/archive/master.zip)
- `python3 setup.py install` or `python setup.py install` (Need root access)				

### PyPI


- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- `pip install art` or `pip3 install art` (Need root access)

## Usage

### Library			
<pre>
>>> from art import *  #import art library
>>> aprint("butterfly") # print 1-line art
Ƹ̵̡Ӝ̵̨̄Ʒ 
>>> aprint("happy")
 ۜ\(סּںסּَ` )/ۜ 
>>> art_1=art("coffee") # return 1-line art
>>> print(art_1)
c[_] 
>>> tprint("art") # print ascii text (default font) 
              _   
  __ _  _ __ | |_ 
 / _` || '__|| __|
| (_| || |   | |_ 
 \__,_||_|    \__|
                  

>>> tprint("art",font="block") # print ascii text (block font)

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
>>> tsave("art",filename="test.txt") # save ascii text in test.txt file with save message (print_status==True)
Saved!
Filename: test.txt
>>> tsave("art",filename="test.txt",print_status=False) # save ascii text in test.txt file without save message (print_status==False)
>>> tsave("art") # save ascii text in art.txt
Saved!
Filename: art.txt
>>> tprint('testسس')  # chr_ignore flag ==True (Default)
 _               _   
| |_   ___  ___ | |_ 
| __| / _ \/ __|| __|
| |_ |  __/\__ \| |_ 
 \__| \___||___/ \__|
                     

>>> tprint('testسس',chr_ignore=False) # chr_ignore flag == False
[Error] Invalid Char!
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

### CLI			
- List of arts :  `python -m art list`
- List of fonts : `python -m art fonts`
- Test : `python -m art test`
- Text : `python -m art text yourtext fontname(optional)`
- Shape : `python -m art shape art_name`
- Save :  `python -m art save yourtext fontname(optional)`

### Telegram Bot
<a href="https://t.me/artlib_bot" target="__blank"><img src="https://img.shields.io/badge/Telegram-Bot-red.svg"></a>

<div align="center">
<a href="https://asciinema.org/a/144767" target="_blank"><img src="https://asciinema.org/a/144767.png" /></a>
<p>Screen Record</p>
</div>

* [View Full Art List](list.md "Full Art List")					


## Issues & Bug Reports			

Just fill an issue and describe it. I'll check it ASAP!							
or send an email to [sepand@qpage.ir](mailto:sepand@qpage.ir "sepand@qpage.ir"). 


## Contribution			

You can fork the repository, improve or fix some part of it and then send the pull requests back if you want to see them here. I really appreciate that. ❤️			

Remember to write a few tests for your code before sending pull requests. 



## License

<a href="https://github.com/sepandhaghighi/art/blob/master/LICENSE"><img src="https://img.shields.io/github/license/mashape/apistatus.svg"/></a>

## Reference    

1. [1 Line Art](http://1lineart.kulaone.com/#/)
2. [Text To ASCII](http://patorjk.com/software/taag/#p=display&f=Blocks&t=ART)

## Donate to our project
								
<h3>Bitcoin :</h3>					

```12Xm1qL4MXYWiY9sRMoa3VpfTfw6su3vNq```			



<h3>Payping (For Iranian citizens) :</h3>

<a href="http://www.payping.net/sepandhaghighi" target="__blank"><img src="http://www.qpage.ir/images/payping.png" height=100px width=100px></a>	
