# -*- coding: utf-8 -*-
from .art_dic import *
from .text_dic import *
import string
version="0.2"
def line(char="*",number=30):
    print(char*number)
def tprint_test(dic="standard"):
    inp=string.ascii_letters+string.digits+'%&\'()*+,-./:;<=>?@[\\]^_`{|}~!"#'
    for i in inp:
        tprint(i,dic=dic)
def aprint_test():
    for i in sorted(list(art_dic.keys())):
        print(i)
        aprint(i)
        line()
def help_func():
    '''
    Print Help Page
    :return: None
    '''
    tprint("art")
    tprint("v"+version)
    print("Help : \n")
    print("     - list --> (list of arts)\n")
    print("     - test --> (run tests)\n")
    print("     - text 'yourtext' 'font(optional)' --> (text art) Example : 'python -m art text exampletext'\n")
    print("     - shape 'shapename' --> (shape art) Example : 'python -m art shape butterfly'\n")
def aprint(artname,number=1,text=""):
    '''
    Art Print
    This function print ascii art
    :param artname: artname
    :type artname : str
    :return: None
    '''
    try:
        art_value=art_dic[artname.lower()]
        if isinstance(art_value,str):
            print((art_value+" ")*number)
        else:
            print((art_value[0]+text+art_value[1]+" ")*number)
    except KeyError:
        print("[Error] Invalid Art Name")
    except Exception:
        print("[Error] Print Faild!")


def art(artname,number=1,text=""):
    '''
    This function return ascii art
    :param artname: artname
    :type artname : str
    :return: ascii art as str
    '''
    try:
        art_value=art_dic[artname.lower()]
        if isinstance(art_value,str):
            return (art_value+" ")*number
        else:
            return (art_value[0]+text+art_value[1]+" ")*number
    except KeyError:
        print("[Error] Invalid Art Name")
    except Exception:
        print("[Error] Return Faild!")
def tprint(text,dic="standard"):
    '''
    This function split function by \n then call text2art function
    :param text: input text
    :type text:str
    :return: None
    '''
    split_list=text.split("\n")
    for item in split_list:
        if len(item)!=0:
            text2art(item,dic=dic)
def text2art(text,dic="standard"):
    '''
    This function print art text
    :param text: input text
    :type text:str
    :return: None
    '''
    try:
        split_list=[]
        result_list=[]
        letters=standard_dic
        text_temp=text
        if dic=="block":
            letters=block_dic
            text_temp=text.lower()
        for i in text_temp:
            split_list.append(letters[i].split("\n"))
        for i in range(len(split_list[0])):
            temp=""
            for j in range(len(split_list)):
                if j>0 and (i==1 or i==len(split_list[0])-2) and dic=="block":
                    temp=temp+" "
                temp=temp+split_list[j][i]
            result_list.append(temp)
        print(("\n").join(result_list))

    except KeyError:
        print("[Error] Invalid Char!")
    except Exception:
        print("[Error] Print Faild!")

