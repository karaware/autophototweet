#!/usr/bin/env python
# -*- coding: utf-8 -*-
import increment
import takephoto
import tweet

increment.increment()
filename = takephoto.takephoto()
tweet.tweet(filename)
