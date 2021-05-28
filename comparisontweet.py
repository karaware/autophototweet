#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, date, timedelta
import glob
import tweepy
import cv2

def tweet():
    CK = 'F9775TKQrUgwws9uJm7qr0bw9'
    CS = 'UDPVHjwVMaOf3HMHJ2U68s2ssPxv5Kf9LAePW3O2x2n3baSV7V'
    AT = '1384009908178198529-g8yEdNsWEhlsxCEsjqIhOaoAdFnLUP'
    AS = 'RLT6juFbVbPcHHe3V9ERbjSvYmeZmc68Ppcrlb3OPUftr'

    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)
    api = tweepy.API(auth)

    today = datetime.today()
    yesterday = today - timedelta(days=1)
    photoList = []

    todayGlob = '/home/pi/script/sunnylettuce_autophototweet/pic/' + today.strftime('%Y%m%d_') + '1200*'
    photoList = glob.glob(todayGlob)

    yesterdayGlob = '/home/pi/script/sunnylettuce_autophototweet/pic/' + yesterday.strftime('%Y%m%d_') + '1200*'
    yesterdayPhotoList = glob.glob(yesterdayGlob)

    photoList = yesterdayPhotoList + photoList

    media_ids = []
    for filename in photoList:
        res = api.media_upload(filename)
        media_ids.append(res.media_id)

    message = "左 " + yesterday.strftime('%Y/%m/%d') + " 昨日"
    message += "\n"
    message += "右 " + today.strftime('%Y/%m/%d') + " 今日"
    message += "\n"
    message += "#家庭菜園 #水耕栽培"
    message += "\n"
    message += "#サニーレタス"

    api.update_status(status=message, media_ids=media_ids)
