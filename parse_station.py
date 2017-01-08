#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import requests
from pprint import pprint

#r = requests.get("https://github.com/timeline.json")
r = requests.get("https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8965",verify=False)
#print(r.text)
stations = re.findall(r'([A-Z]+)\|([a-z]+)',r.text)
stations = dict(stations)
stations = dict(zip(stations.values(),stations.keys()))
pprint(stations, indent=4)
