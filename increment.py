#!/usr/bin/env python
# -*- coding: utf-8 -*-
def increment():
    f = open('/home/pi/script/autophototweet/count.txt')
    txt = f.read()
    nowcountint = int(txt)
    nowcountint += 1
    newcount = str(nowcountint)
    f.close()
    fw = open('/home/pi/script/autophototweet/count.txt','w')
    fw.write(newcount)
    fw.close()


