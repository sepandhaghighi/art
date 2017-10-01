# -*- coding: utf-8 -*-

art_dic={"fish1":"><(((('>","fish2":"><>","house":"__̴ı̴̴̡̡̡ ̡͌l̡̡̡ ̡͌l̡*̡̡ ̴̡ı̴̴̡ ̡̡͡|̲̲̲͡͡͡ ̲▫̲͡ ̲̲̲͡͡π̲̲͡͡ ̲̲͡▫̲̲͡͡ ̲|̡̡̡ ̡ ̴̡ı̴̡̡ ̡͌l̡̡̡̡.___","care_crowd":"(-(-_(-_-)_-)-)","monster":"٩(̾●̮̮̃̾•̃̾)۶",
         "monster2":"٩(- ̮̮̃-̃)۶","boom_box":"♫♪.ılılıll|̲̅̅●̲̅̅|̲̅̅=̲̅̅|̲̅̅●̲̅̅|llılılı.♫♪","butterfly":"Ƹ̵̡Ӝ̵̨̄Ʒ","finger1":"╭∩╮(Ο_Ο)╭∩╮",
         "pistols":"¯¯̿̿¯̿̿'̿̿̿̿̿̿̿'̿̿'̿̿̿̿̿'̿̿̿)͇̿̿)̿̿̿̿ '̿̿̿̿̿̿\̵͇̿̿\=(•̪̀●́)=o/̵͇̿̿/'̿̿ ̿ ̿̿","finger2":"┌∩┐(◣_◢)┌∩┐","heart":"»-(¯`·.·´¯)->","mouse":'----{,_,">',
         "worm":"_/\__/\__0>","koala":"@( * O * )@","monkey":"@('_')@","waves":"°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸",
         "glasses":"-@-@-","rose1":"--------{---(@","rose2":"@}}>-----","star_in_my_eyes":"<*_*>","looking_face":"ô¿ô",
         "sleeping":"(-.-)Zzz...","sleeping_baby":"[{-_-}] ZZZzz zz z...","love_you":["»-(¯`·.·´¯)->","<-(¯`·.·´¯)-«"]}



def aprint(artname,text=""):
    '''
    This function print ascii art
    :param artname: artname
    :type artname : str
    :return: None
    '''
    try:
        art_value=art_dic[artname.lower()]
        if isinstance(art_value,str):
            print(art_value)
        else:
            print(art_value[0]+text+art_value[1])
    except KeyError:
        print("[Error] Invalid Art Name")
    except Exception:
        print("[Error] Print Faild!")


def art(artname,text=""):
    '''
    This function return ascii art
    :param artname: artname
    :type artname : str
    :return: ascii art as str
    '''
    try:
        art_value=art_dic[artname.lower()]
        if isinstance(art_value,str):
            return art_value
        else:
            return art_value[0]+text+art_value[1]
    except KeyError:
        print("[Error] Invalid Art Name")
    except Exception:
        print("[Error] Return Faild!")

