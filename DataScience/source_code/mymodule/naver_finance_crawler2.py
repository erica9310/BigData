
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup


# In[7]:
def finance(company_code):        
    url = "https://finance.naver.com/item/main.nhn?code=" + company_code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    print(bs_obj)
    print()
    
    no_today = bs_obj.find("p", {"class":"no_today"})
    print(no_today)
    print()
    
    blind_now = no_today.find("span", {"class":"blind"})
    print(blind_now)
    print()

    return blind_now.text


def finance2(company):        
    url = "https://finance.naver.com/item/main.nhn?code=" + company
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
  
    
    no_today = bs_obj.find("p", {"class":"no_today"})
    

    
    blind_now = no_today.find("span", {"class":"blind"})

    return blind_now.text


