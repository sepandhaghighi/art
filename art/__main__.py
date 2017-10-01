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
        else:
            aprint("glasses", 5)
            print("")
            print("Help : ")
            print("     - list (list of arts)\n")
            print("     - test (run tests)\n")
            aprint("coffee", 5)
    else:
        aprint("glasses",5)
        print("")
        print("Help : ")
        print("     - list (list of arts)\n")
        print("     - test (run tests)\n")
        aprint("coffee",5)


