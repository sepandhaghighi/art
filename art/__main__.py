# -*- coding: utf-8 -*-
from .art import *
from .art_dic import *
import sys
import doctest

if __name__=="__main__":
    args=sys.argv
    if len(args)>1:
        if args[1].upper()=="TEST":
            doctest.testfile("test.py", verbose=True)
        elif args[1].upper()=="LIST":
            for line in list(art_dic.keys()):
                print(line)
                aprint(line)
        elif len(args)>2:
            if args[1]=="text":
                tprint(args[2])
            else:
                help()
        else:
            help()
    else:
        help()



