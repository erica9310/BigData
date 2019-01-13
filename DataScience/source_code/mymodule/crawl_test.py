
# coding: utf-8

# In[28]:


import urllib.request


# In[29]:


client_id = "xp0Izs39speJ7LS7TPRh"
client_secret = "o973GVS4WA"


# In[30]:


encType = urllib.parse.quote("여행")


# In[31]:


url = "https://openapi.naver.com/v1/search/blog?query="+encType


# In[32]:


request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
print(rescode)


# In[33]:


if(rescode == 200):
    response_body = response.read()
    print(response_body.decode("utf-8"))
else:
    print("Error code: " + rescode)

