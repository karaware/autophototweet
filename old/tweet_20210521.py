#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import tweepy
import cv2

def tweet(fileName):
    CK = 'F9775TKQrUgwws9uJm7qr0bw9'
    CS = 'UDPVHjwVMaOf3HMHJ2U68s2ssPxv5Kf9LAePW3O2x2n3baSV7V'
    AT = '1384009908178198529-g8yEdNsWEhlsxCEsjqIhOaoAdFnLUP'
    AS = 'RLT6juFbVbPcHHe3V9ERbjSvYmeZmc68Ppcrlb3OPUftr'

    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)
    api = tweepy.API(auth)

    now = datetime.datetime.now()

    message = now.strftime('%Y/%m/%d %H:%M:%S')
    message += "\n"
    message += "#家庭菜園 #水耕栽培"
    message += "\n"
    message += "#サニーレタス"

    #img = cv2.imread(fileName)
    #img_rotate_90_clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    #cv2.imwrite(fileName, img_rotate_90_clockwise)

    photo = open(fileName, 'rb')

    api.update_with_media(filename=fileName,status=message)
