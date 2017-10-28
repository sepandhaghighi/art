# -*- coding: utf-8 -*-
from .art_dic import *
from .text_dic import *
import string
import os

version="0.2"

font_map={"block":[block_dic,True],"banner":[banner_dic,False],"standard":[standard_dic,False],"avatar":[avatar_dic,True],
          "basic":[basic_dic,True],"bulbhead":[bulbhead_dic,True],"chunky":[chunky_dic,False],"coinstak":[coinstak_dic,False],
          "contessa":[contessa_dic,False],"contrast":[contrast_dic,True],"cyberlarge":[cyberlarge_dic,True],"cybermedium":[cybermedium_dic,True],
          "doom":[doom_dic,False],"dotmatrix":[dotmatrix_dic,False],"drpepper":[drpepper_dic,False],
          "epic":[epic_dic,True],"fuzzy":[fuzzy_dic,False],"isometric1":[isometric1_dic,True],"isometric2":[isometric2_dic,True],
          "isometric3":[isometric3_dic,True],"isometric4":[isometric4_dic,True],"larry3d":[larry3d_dic,False],
          "nancyj":[nancyj_dic,False],"ogre":[ogre_dic,False],"rectangles":[rectangles_dic,False],"roman":[roman_dic,False],
          "rounded":[rounded_dic,False],"rowancap":[rowancap_dic,True],"script":[script_dic,False],
          "serifcap":[serifcap_dic,True],"shadow":[shadow_dic,False],"slant":[slant_dic,False],"speed":[speed_dic,False],
          "starwars":[starwars_dic,False],"stop":[stop_dic,False],"thin":[thin_dic,False],"usaflag":[usaflag_dic,False]}

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
    print("     - text 'yourtext' 'font(optional)' --> (text art) Example : 'python -m art text exampletext block'\n")
    print("     - shape 'shapename' --> (shape art) Example : 'python -m art shape butterfly'\n")
    print("     - save 'yourtext  'font(optional)  -->  Example : 'python -m art save exampletext  block")
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

def tprint(text,dic="standard",chr_ignore=False):
    '''
    This function split function by \n then call text2art function
    :param text: input text
    :type text:str
    :param dic: input font
    :type dic:str
    :param chr_ignore: ignore not supported character
    :type chr_ignore:bool
    :return: None
    '''
    try:
        split_list=text.split("\n")
        result=""
        for item in split_list:
            if len(item)!=0:
                result=result+text2art(item,dic=dic,chr_ignore=chr_ignore)
        print(result)
    except Exception:
        pass


def tsave(text,dic="standard",filename="art",chr_ignore=False):
    '''

    :param text: input text
    :param dic: input font
    :type dic:str
    :type text:str
    :param filename: output file name
    :type filename:str
    :param chr_ignore: ignore not supported character
    :type chr_ignore:bool
    :return: None
    '''
    try:
        split_list = text.split("\n")
        files_list=os.listdir()
        splited_filename=filename.split(".")[0]
        index = 2
        test_name = splited_filename
        while(True):
            if test_name+".txt" in files_list:
                test_name=splited_filename+str(index)
                index=index+1
            else:
                break
        file=open(test_name+".txt","w")
        result=""
        for item in split_list:
            if len(item) != 0:
                result=result+text2art(item, dic=dic, chr_ignore=chr_ignore)
        file.write(result)
        file.close()
        print("Saved! \nFilename: "+test_name+".txt")
    except Exception:
        pass

def text2art(text,dic="standard",chr_ignore=True):
    '''
    This function print art text
    :param text: input text
    :type text:str
    :param dic: input font
    :type dic:str
    :param chr_ignore: ignore not supported character
    :type chr_ignore:bool
    :return: artText as str
    '''
    try:
        split_list=[]
        result_list=[]
        letters=standard_dic
        text_temp=text
        if dic.lower() in font_map.keys():
            letters=font_map[dic.lower()][0]
            if font_map[dic.lower()][1]==True:
                text_temp=text.lower()
        for i in text_temp:
            if (ord(i)==9) or (ord(i)==32 and dic=="block"):
                continue
            if (i not in letters.keys()) and (chr_ignore==True):
                continue
            split_list.append(letters[i].split("\n"))
        for i in range(len(split_list[0])):
            temp=""
            for j in range(len(split_list)):
                if j>0 and (i==1 or i==len(split_list[0])-2) and dic=="block":
                    temp=temp+" "
                temp=temp+split_list[j][i]
            result_list.append(temp)
        return(("\n").join(result_list))

    except KeyError:
        print("[Error] Invalid Char!")
    except Exception:
        print("[Error] Print Faild!")

