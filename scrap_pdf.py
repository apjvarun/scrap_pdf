# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 09:24:01 2016

@author: Varun Gupta
"""

# To download pdf files from a webpage.

import urllib2
import re

#sample url
url = 'http://www.cse.iitk.ac.in/users/piyush/courses/ml_autumn16/ML.html'

website = urllib2.urlopen(url)
html = website.read()
#links = re.findall('"((http|ftp)s?://.?)"', html)
links=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', html)

#from pattern.web import URL
new_list = []
for l in links:
    if (l[-4:]=='.pdf'):
        new_list.append(l)
        print l
        
for l in new_list:
    response = urllib2.urlopen(l)
    name_file = l.split('/')[-1]
    file = open(name_file, 'wb')
    file.write(response.read())
    file.close()
    print("Completed")
        
