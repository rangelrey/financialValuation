#!/usr/bin/env python
# coding: utf-8

# In[1]:


#official original API connection

#import pandas as pd

#import json
#import urllib.request 



# In[209]:


ratiosDf = pd.DataFrame()

for stock in stocks_list:

    webURL = urllib.request.urlopen(f'https://fmpcloud.io/api/v3/financial-ratios/{stock}?period=quarter&apikey={apikey}')
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    data_json = json.loads(data.decode(encoding))
    dataList = []
    df = pd.DataFrame()
    df = json_normalize(data_json["ratios"])
    df["firm"] = stock
    
    ratiosDf = ratiosDf.append(df)




# In[210]:


#reorder columns
columns = rationsDf.columns.tolist()
rationsDf = df1[columns[-1:] +columns[:-1]]


# In[212]:


ratiosDf


# In[ ]:





# In[ ]:





# In[214]:


import ipywidgets as widgets


# In[ ]:





# In[ ]:


#stocks_list = ["AAPL", "FB"]

#apikey = 'e0d7409bfcfa162e155764a86f84d0d2'


#for stock in stocks_list:

# webURL = urllib.request.urlopen(f'https://fmpcloud.io/api/v3/ratios-ttm/{stock}?apikey={apikey}')
# data = webURL.read()
# encoding = webURL.info().get_content_charset('utf-8')
# data_json = json.loads(data.decode(encoding))

# ratio = data_json[0]



# In[ ]:


# define columns

#mns = ["date", "firm"]

#k,v in dataList[0]["ratios"][0].items():
#if k !="date":
#    for kk in v:
#        columns.append(kk)

#List = []

#firm in dataList:
#row=[]
#row.append(firm["symbol"])
#print(firm["symbol"])
#for dateDic in firm["ratios"]:
#    print(" dateDic")
#    row.append(dateDic["date"])
#    for group, ratios in dateDic.items():
#        if group !="date":
#            print("  "+group)
#            for ratioName, figure in ratios.items():                   
#                print("   " +ratioName+"    "+figure)
#                row.append(figure)


            
    #df.append(pd.Series(row,index=df.columns), ignore_index=True)

    #firm["symbol"]
    #date["date"]

    

    

