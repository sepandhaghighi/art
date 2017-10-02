# -*- coding: utf-8 -*-
from .art_dic import *
from .text_dic import *
def aprint(artname,number=1,text=""):
    '''
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

def tprint(text):
    try:
        split_list=[]
        result_list=[]
        for i in text.lower():
            split_list.append(text_dic[i].split("\n"))
        for i in range(len(split_list[0])):
            temp=""
            for j in range(len(split_list)):
                if j>0 and (i==1 or i==len(split_list[0])-2):
                    temp=temp+" "
                temp=temp+split_list[j][i]
            result_list.append(temp)
        print(("\n").join(result_list))

    except KeyError:
        print("[Error] Invalid Char!")
    except Exception:
        print("[Error] Print Faild!")

