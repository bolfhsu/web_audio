# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 08:35:56 2017
@author: bolf
"""
import os
import sys
import urllib
from bs4 import BeautifulSoup

#专辑下所有音频下载
url = ""#下载音频专辑的地址
apach = ""音频下载位置
albumid = url.split('/')[-1]
reslink = "http://m.ximalaya.com/album/more_tracks?url=%2Falbum%2Fmore_tracks&aid="+albumid+"&page="
for i in range(1,100):
    albumidlink = reslink +str(i)
    resdata = opener.open(albumidlink).read()
    jsondata = json.loads(resdata)
    nextpage = jsondata['next_page']
    soup=BeautifulSoup(jsondata['html'],'html.parser')
    audiolist = soup.find_all("li")
    for audio in audiolist:
        title = audio.find_all("a")[0].text.strip().replace("\"", "")
        audiopath = apach+title+".m4a"
        audiourl = audio.find_all("a")[1]['sound_url']
        urllib.request.urlretrieve(audiourl,audiopath)
        print ("完成下载"+title)
    if not nextpage:
        break
