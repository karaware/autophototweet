#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import cv2
import datetime

def takephoto():
    now = datetime.datetime.now()
    fileName = '/home/pi/script/sunnylettuce_autophototweet/pic/' + \
    now.strftime('%Y%m%d_%H%M%S') + '.jpg'
    cmd = 'fswebcam -d /dev/video0 -r 1920x1080 -F 10 -S 100 --no-banner ' + fileName
    subprocess.run(cmd, shell=True)
    img = cv2.imread(fileName)
    img_rotate_90_clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite(fileName, img_rotate_90_clockwise)
    return fileName
