# -*- coding: utf-8 -*-
from .art import *
from .art_dic import *
import sys
import doctest
import getopt

if __name__=="__main__":
    args=sys.argv
    if len(args)>1:
        if args[1].upper()=="TEST":
            doctest.testfile("test.py",optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
        elif args[1].upper()=="LIST":
            aprint_test()
        elif args[1].upper()=="FONTS":
            font_list()
        elif len(args)>2:
            if args[1].upper()=="TEXT":
                if len(args)>3:
                    tprint(args[2],font=args[3])
                else:
                    tprint(args[2])
            elif args[1].upper()=="SAVE":
                if len(args)>3:
                    tsave(args[2], font=args[3])
                else:
                    tsave(args[2])
            elif args[1].upper()=="SHAPE":
                aprint(args[2])
            else:
                help_func()
        else:
            help_func()
    else:
        help_func()



