#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import multiprocessing   #利用pool进程池实现多进程并行
from bs4 import BeautifulSoup    #处理抓到的页面
import sys
import requests
# import importlib
# importlib.reload(sys)#编码转换，python3默认utf-8,一般不用加
from requests.exceptions import MissingSchema
import urllib


# In[ ]:


headers = {
    "Host": "www.baidu.com",
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, compress',
    'Accept-Language': 'en-us;q=0.5,en;q=0.3',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
} #定义头文件，伪装成浏览器


# In[ ]:


def get_host(word):
    url = 'http://www.baidu.com/s?wd=' + urllib.parse.quote(word)
    res=requests.get(url, headers=headers)
    soup = BeautifulSoup(res.content, 'lxml')
    tagh3 = soup.find_all('h3')
    if  len(tagh3) > 3:
        tagh3 = tagh3[:3]
    for h3 in tagh3: 
        try:
            href = h3.find('a').get('href')
            baidu_url = requests.get(url=href, headers=headers, allow_redirects=False)
            real_url = baidu_url.headers['Location'] 
            if real_url.startswith('http') and 'baidu' not in real_url:
                print(word, real_url)
        except MissingSchema as e1:
            continue
        except  AttributeError as e2:
            continue
        except KeyError as e3:
            continue


# In[ ]:


with open("d:/Users/admin/Desktop/hotel_name.txt",encoding="utf8") as file:
    content = file.read()
    hotel_name_set = set(name for name in content.split("\n"))
    hotel_name_list = list(hotel_name)
    for name in hotel_name_list:
        get_host(name)


# In[ ]:


with open("d:\\Users\\admin\\Desktop\\hotel_host.txt", encoding='utf-8') as file:
    content = file.read()
    with open("name_host.txt","w+") as file2:
        for line in content.split("\n"):
            name = line.split(" ")[0]
            host = line.split(" ")[1].split("/")[2]
            
            print(name, host.replace("www.",""))
#             host2 = host.split("/")
#             print(host2[2])


# In[ ]:


from collections import defaultdict 
my_dict = defaultdict(list)
with open("d:\\Users\\admin\\Desktop\\hotel_host.txt", encoding='utf-8') as file:
    content = file.read()
    with open("name_host.txt","w+") as file2:
        for line in content.split("\n"):
            name = line.split(" ")[0]
            host = line.split(" ")[1].split("/")[2].replace("www.","")
            my_dict[host].append(name)


# In[ ]:


import pandas as pd
import numpy as np

host = np.array([key for key in my_dict.keys()])
name = np.array([value for value in my_dict.values()])

data = pd.DataFrame({"host":host,
                     "name":name})

data.shape

data.to_csv('d:\\Users\\admin\\Desktop\\Result.csv',index=0)


# In[ ]:




