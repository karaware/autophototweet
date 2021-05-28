#!/usr/bin/env python
# -*- coding: utf-8 -*-
import takephoto
import tweet

filename = takephoto.takephoto()
tweet.tweet(filename)
