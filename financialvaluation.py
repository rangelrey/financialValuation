#!/usr/bin/env python
# coding: utf-8

# In[154]:


#official original API connection
#https://financialmodelingprep.com/developer/docs/#Company-Financial-Ratios
#https://fmpcloud.io/documentation#financialRatios
from pprint import pprint
import pandas as pd
import json
from pandas.io.json import json_normalize
from io import StringIO

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen


apikey = 'e0d7409bfcfa162e155764a86f84d0d2'


stocks_list = ['MELI','AMS','AAPL']


# In[155]:



def getData(report,info,stocks_list):

    finalDf = pd.DataFrame()

    if report == "financial-ratios":   
        print("\nDownloading financial ratios \n")
        for stock in stocks_list:    
            print(f'Starting with {stock}')
            try:
                
                webURL =urlopen(f'https://fmpcloud.io/api/v3/{report}/{stock}?period=quarter&apikey={apikey}')
                data = webURL.read()

                if str(data)!="b'{ }'":         
                    encoding = webURL.info().get_content_charset('utf-8')
                    data_json = json.loads(data.decode(encoding))
  
                    df = pd.DataFrame()
                    df = json_normalize(data_json[str(info)])
                    df["symbol"] = stock 
                    finalDf = finalDf.append(df)
                else:
                    print("\nSYMBOL NOT FOUND: Check maybe Stock Symbol: "+str(stock)+"\n\n")

 
            except:
                print("--------------------------\nCODE ERROR---------------------------------\n")
            

                
        
        print("\n \n----- Done -----")
        return finalDf[finalDf.columns[::-1]].set_index("date")


    else:
        print("\nDownloading financials \n")
        for stock in stocks_list: 
            print(f'Starting with {stock}')
            webURL = f'https://fmpcloud.io/api/v3/{report}/{stock}?period=quarter&apikey={apikey}'
            try:
                response = urlopen(webURL)
                data = response.read().decode("utf-8")
                if data!="[ ]":
                    df = json_normalize(json.loads(data))
                    finalDf = finalDf.append(df)
                else:
                    print("\nSYMBOL NOT FOUND: Check maybe Stock Symbol: "+str(stock)+"\n\n")

            except:
                print("--------------------------\nCODE ERROR---------------------------------\n")
                


        print("\n \n----- Done -----")
        return finalDf.set_index("date")
    


# In[157]:


dividend_stock_list = []

df_fR =getData("financial-ratios","ratios",dividend_stock_list)

df_cF =getData("cash-flow-statement","financials",dividend_stock_list)

df_bS =getData("balance-sheet-statement","financials",dividend_stock_list)

df_iS =getData("income-statement","financials",dividend_stock_list)


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

    

    

