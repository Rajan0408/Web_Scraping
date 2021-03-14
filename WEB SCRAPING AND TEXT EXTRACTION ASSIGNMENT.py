#!/usr/bin/env python
# coding: utf-8

# In[1]:


#-----------------------------------------------
#  WEB SCRAPING AND TEXT EXTRACTION ASSIGNMENT
#-----------------------------------------------


# In[2]:


# importing required modules
from bs4 import BeautifulSoup 
import requests 
import csv 
import re


# In[3]:


#Accessing the HTML content from webpage
URL = "https://www.marketsandmarkets.com/telecom-and-IT-market-research-113.html"
req = requests.get(URL) 


# In[4]:


soup = BeautifulSoup(req.content, 'html5lib')                    #raw_content
#print(soup.prettify())

#finding that div element using find() method :
content = soup.find('div', attrs = {'id':'publishedreports'})    #content required
#print(content.prettify())


# In[5]:


#dictionaries for storing contents
final = []
report_title = []
link = []
report_description = []
date_published = []
date = []
USD = []


# In[6]:


# FOR DATE PUBLISHED
for i in content.find_all('td', attrs = {'align':'center', 'class':'displaynone', 'valign':'top' }):
        date_published.append(i.text)

for i in range(len(date_published)):
    if i % 3 == 0:
        date.append(date_published[i])


# In[7]:


#FOR TITLE 
for i in content.find_all('a'):
    report_title.append(i.text)


# In[8]:


#FOR LINKS
x3 = "https://www.marketsandmarkets.com"
for i in content.find_all('a'):
    link.append(x3 + i.get('href'))


# In[9]:


#FOR DESCRIPTION
for i in content.find_all('p', attrs = {'align':'justify'}):
       report_description.append(i.text)
       # print(i.text)


# In[10]:


#USD

des1 = []
for i in range(len(report_description)):
    des1.append(report_description[i].split())

usd2 = []
for j in range(len(des1)):
    for i in range(len(des1[j])):
        if(des1[j][i] == 'USD'):
            #print(des1[j][i+1],des1[j][i+2])
            usd2.append(des1[j][i+1]+' '+ des1[j][i+2])
            break
        


# In[11]:


#PERCENT_VALUE
percent = [] 
for i in range(len(report_description)):
    des1 = report_description[i].split()
    
    for i in des1: 
        if '%' in i: 
            #print(i)
            percent.append(i)


# In[12]:


for i in range(49):
    final1 = {}
    final1['REPORT_TITLE'] = report_title[i]
    final1['HERF_LINKS'] = link[i]
    final1['REPORT_DESCRIPTION'] = report_description[i]
    final1['DATE'] = date[i]
    final1['USD_VALUES'] = usd2[i]
    final1['PERCENTAGE VALUES '] = percent[i]
    final.append(final1)


# In[13]:


#writing all the dictionaries in csv file
filename = 'FINAL.csv'

with open(filename, 'w', newline='') as f: 
    w = csv.DictWriter(f,['REPORT_TITLE','HERF_LINKS','REPORT_DESCRIPTION','DATE','USD_VALUES','PERCENTAGE VALUES ']) 
    w.writeheader() 
    for key in final: 
        w.writerow(key) 


# In[14]:


# --------------------------------------------------------------------------------------------------------
# Differnt modules used  used in this assignment to scrape all the results are :
#
#  1. BeautifulSoup 4 - Python library for pulling data out of HTML and XML files.
#  2. Requests -        The requests module allows you to send HTTP requests using Python.
#  3. CSV -             This csv module implements classes to read and write tabular data in CSV format.
#  4. re -              This module provides regular expression matching operations
#
# Different web scraping packages in Python are :
#
#  1. Requests
#  2. lxml
#  3. Beautiful Soup
#  4. Selenium
#  5. Scrapy
#
#  Among these Beautiful Soup is the module that scrapes websites fastest 
#----------------------------------------------------------------------------------------------------------


# In[ ]:




