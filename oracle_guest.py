#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import re
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


#%%
def find_last_ed(url, version_digit,sub_digit):
#version_digit,sub_digit = 5,3
    html = urlopen(url)
    soup = BeautifulSoup(html.read(), 'lxml')
    maximum = 0
    for link in soup.find_all('a', href=True):
        dlink = link.get('href')
        dlink = re.sub(r'/', r'', dlink)
        vlink = dlink
        dlink=dlink.split('.')
        if len(dlink)==3:
            if int(dlink[0])==version_digit:
                if int(dlink[1])==sub_digit:
                    #print(dlink[2])
                    try:
                        results = list(map(int, dlink))
                        print(vlink)
                        maximum = max(maximum, results[2])
                    except:
                        pass
    print('==')
    url2 = 'https://download.virtualbox.org/virtualbox/'+ str(version_digit) + '.' + str(sub_digit) + '.'+str(maximum)
    html = urlopen(url2)
    soup = BeautifulSoup(html.read(), 'lxml')
    for link in soup.find_all('a', href=True):
        dlink = link.get('href')
        if 'VBoxGuestAdditions' in dlink:
            url3 = url2+'/'+dlink
            link_name = dlink
            print(url3)
    return(url3, link_name)

url = 'https://download.virtualbox.org/virtualbox/'
url3, link_name = find_last_ed(url,6,0) 
#%%
urlretrieve(url3, str(Path.home())+'/Downloads/'+link_name)
