
# coding: utf-8

# In[1]:

import yahoo.backyard, requests


# In[2]:

url = 'https://digits3.data.yahoo.com:4443/v1/data/network/day?metrics=pageViews&dateTime=2014/2015'


# In[3]:

yahoo.backyard.installSSO()


# In[4]:

response = requests.get(url)


# In[5]:

results = response.json()['rows']


# In[6]:

print(results)


