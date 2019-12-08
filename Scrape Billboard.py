#!/usr/bin/env python
# coding: utf-8

# In[17]:


from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from urllib.request import Request, urlopen



page = Request("https://www.billboard.com/charts/year-end/2019/hot-100-songs",headers={'User-Agent': 'Mozilla/5.0'})

html = urlopen(page).read()
page_soup = soup(html,"html.parser")

#splits the page into the 100 artists
containers = page_soup.main.findAll("div",{"class":"ye-chart-item__text"})



#iterates through the 100 artists
for container in containers:

    print(container.contents[1].text.strip())


# In[ ]:





# In[ ]:




