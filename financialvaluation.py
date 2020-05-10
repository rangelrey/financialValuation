#!/usr/bin/env python
# coding: utf-8

# In[75]:


#official original API connection
#https://financialmodelingprep.com/developer/docs/#Company-Financial-Ratios
#https://fmpcloud.io/documentation#financialRatios
from pprint import pprint
import pandas as pd
import json
from pandas.io.json import json_normalize
from io import StringIO
import urllib.request 
apikey = 'e0d7409bfcfa162e155764a86f84d0d2'

#stocks_list = ['AAPL','E3X1','PCE1','ZO1']
stocks_list = ['EXPE','AMS','AAPL']


# In[103]:




def getData(report,info,stocks_list):

    finalDf = pd.DataFrame()
    for stock in stocks_list:
        print(f'Starting with {stock}')
        if report == "financial-ratios":
            webURL = urllib.request.urlopen(f'https://fmpcloud.io/api/v3/{report}/{stock}?period=quarter&apikey={apikey}')
            data = webURL.read()
            encoding = webURL.info().get_content_charset('utf-8')
            data_json = json.loads(data.decode(encoding))
            df = pd.DataFrame()
            df = json_normalize(data_json[str(info)])
            df["firm"] = stock
            
        elif report =="income-statement":
            webURL = f'https://fmpcloud.io/api/v3/{report}/{stock}?period=quarter&apikey={apikey}'

            response = urlopen(webURL)
            data = response.read().decode("utf-8")
            
            df = json_normalize(json.loads(data))

        #url = ("https://financialmodelingprep.com/api/v3/financials/income-statement/AAPL")
        #print(get_jsonparsed_data(url))

        finalDf = finalDf.append(df)
    
    
    
    return finalDf.set_index("date")


# In[104]:


df =getData("income-statement","financials",stocks_list)


# In[94]:


df =getData("financial-ratios","ratios",stocks_list)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[214]:


import ipywidgets as widgets

#https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20Basics.html


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

    

    

