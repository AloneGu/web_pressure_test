#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import requests

def p_info():
    test_data = {'userName':'cnmb','userPhone':'12345678901','userAddress':'nmb'}

    test_data_urlencode = urllib.urlencode(test_data)

    requrl = "http://bfaln.com/goods.do?m=order&phonetag=touch"

    r = requests.post(requrl,test_data)

    #print r.text