# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 11:55:49 2021

@author: samru
"""

import requests
from data_in import data_inp

URL = 'http://127.0.0.1:5000/predict'
headers = {'content type':'application/json'}
data = {'input':data_inp}
r = requests.get(URL, headers=headers, json=data)

r.json()