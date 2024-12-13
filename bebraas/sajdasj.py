from keybebra import keyboard #line:1
import time #line:2
def block_keys ():#line:4
    O00O0000OO00O00O0 =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','esc','space','enter','shift','ctrl','alt','win','=','backspace','numlock',"F1","F2","F3","F4","F5","F6","F7","F8",'tab',]#line:12
    while True :#line:14
        if keyboard .is_pressed ('insert'):#line:15
            break #line:16
        for OO0OOO0000000O000 in O00O0000OO00O00O0 :#line:18
            if OO0OOO0000000O000 !='insert':#line:19
                keyboard .block_key (OO0OOO0000000O000 )#line:20
        time.sleep (0.1 )#line:21
block_keys ()#line:24
keyboard .unblock_all ()#line:27
