# -*- coding: iso-8859-1, utf-8 -*-
# Created on 04.11.2015 by @author: PeterH 

import json
import urllib

address = raw_input("Please input a search term for your address: ")
base_url = "http://maps.googleapis.com/maps/api/geocode/json?"
search_url = base_url +  urllib.urlencode({'sensor': 'false', 'address': address })
uh = urllib.urlopen(search_url)
data = uh.read()
js = json.loads(data)
print data
print js['results'][0]['place_id']
