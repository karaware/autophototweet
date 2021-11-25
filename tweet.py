#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import tweepy
import cv2

def tweet(fileName):
    CK = 'XXXXX'
    CS = 'XXXXX'
    AT = 'XXXXX'
    AS = 'XXXXX'

    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)
    api = tweepy.API(auth)

    now = datetime.datetime.now()
    startDay = datetime.datetime(2021,5,13)

    elapseDays = now - startDay

    message = now.strftime('%Y/%m/%d %H:%M:%S')
    message += "\n"
    message += str(elapseDays.days) + "日経過"
    message += "\n"
    message += "#家庭菜園 #水耕栽培"
    message += "\n"
    message += "#サニーレタス"

    #img = cv2.imread(fileName)
    #img_rotate_90_clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    #cv2.imwrite(fileName, img_rotate_90_clockwise)

    photo = open(fileName, 'rb')

    api.update_with_media(filename=fileName,status=message)
