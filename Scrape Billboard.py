#!/usr/bin/env python
# coding: utf-8

# In[52]:


from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from urllib.request import Request, urlopen
import pandas as pd

import time

song = []
rank = []
year = []
artist = []


for i in range(1975,2020):
    print(i)
    
#     page = Request("https://www.billboard.com/charts/year-end/2019/hot-100-songs",headers={'User-Agent': 'Mozilla/5.0'})
    page = Request("https://www.billboard.com/charts/year-end/" + str(i) + "/hot-100-songs",headers={'User-Agent': 'Mozilla/5.0'})

    html = urlopen(page).read()
    page_soup = soup(html,"html.parser")

    #splits the page into the 100 artists
    containers = page_soup.main.findAll("div",{"class":"ye-chart-item__primary-row"})
    
    #Sleep because if not denies too many requests
    time.sleep(2)


    #iterates through the 100 artists
    for container in containers:

        rank.append(container.contents[1].text.strip())
        song.append(container.find("div",{"class":"ye-chart-item__title"}).text.strip())
        artist.append(container.find("div",{"class":"ye-chart-item__artist"}).text.strip())
        year.append(int(i))
        
data = pd.DataFrame()

data['song'] = song
data['artist'] = artist
data['rank'] = rank
data['year'] = year


data.astype({'year': 'int32'}).dtypes
data.astype({'rank': 'int32'}).dtypes
data.info()
    
    




# In[ ]:





# In[ ]:




