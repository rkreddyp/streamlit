#from appsmills.streamlit_apps 
import streamlit as st
st.set_page_config(page_title= "Stock Recommendations by GPT Based on News Sentiment", page_icon='.teacher', layout="wide", initial_sidebar_state="expanded")
from helpers import openai_helpers
import numpy as np
from random import randrange
import openai,boto3,urllib, requests
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from PIL import Image
import re, urllib
## 


st.title( 'Stock Recommendations from News Sentiment')


def streamlit_main (url) :


    

    button_name = "Draft it for me !! "
    response_while = "Right on it, it should be around 2-5 seconds ..."
    response_after = "Here you go ...  "
    
    industries = ['metals and mining', 
              'semiconductor', 'software', 
              'biotechnology', 'pharmaceuticals', 'medical devices', 
              'consumer goods', 'retail and stores', 'food and beverage',
              'financial services', 'banking', 'insurance', 
              'real estate', 'construction', 'reit-industrial,medical,hotel'
              'industrial goods', 'transportation', 'automotive', 'trucking and airlines',
              'energy', 'utilities', 'telecommunications', 
              'media', 'entertainment', 'leisure', 'travel', 'hospitality'
              ]
    
   
    
    industries = ['metals and mining', 
              'semiconductor', 'software', 
              'biotechnology', 'pharmaceuticals','medical devices', 
              'consumer goods', 'retail and stores', 'food and beverage',
              'financial services', 'banking', 'insurance', 
              'real estate']

    df_arr = []
    for industry in industries:
        url = 'https://investrecipes.s3.amazonaws.com/newsgpt/' + 'stock_news_' + industry.replace(' ', '_').replace(",", "_").replace("-", "_") + '.json'
        print (url)
        df = pd.read_json(url)
        df = df.reset_index(drop=True)
        df['sentiment_score'] = df['industry'] + "(" + df.sentiment.astype(str).str.split().tolist()[0][0] + ")"
        df_arr.append(df)
    df = pd.concat(df_arr)
    
    #st.dataframe(df)
    # tabs are the industries
    #tab_list = df.tasks.unique().tolist()
    tabs = df['sentiment_score'].unique().tolist()
    ind_list = df['industry'].unique().tolist()

    #tabs = [ str(x) for x in tab_list if x is not np.nan ]

    tabs = st.tabs ( tabs )  



    i=0
    for tab in tabs :

        with tab :
            tab_name = ind_list[i]
            st.write (tab_name)
            url = 'https://investrecipes.s3.amazonaws.com/newsgpt/' + 'stock_news_' + tab_name.replace(' ', '_').replace(",", "_").replace("-", "_") + '.md'
            destination = '/tmp/stock_news_reit___industrial__medical__hotel.md'
            urllib.request.urlretrieve(url, destination)
            file_path = '/tmp/stock_news_reit___industrial__medical__hotel.md'
            with open(file_path, 'r') as file:
                file_content = file.read()
                st.markdown (file_content)
            i+=1
            json_url = url = 'https://investrecipes.s3.amazonaws.com/newsgpt/' + 'stock_news_' + tab_name.replace(' ', '_').replace(",", "_").replace("-", "_") + '.json'
            
            sdf = pd.read_json(json_url)
            
            df = pd.read_csv ('https://investrecipes.s3.amazonaws.com/basic/all_stocks/just-all-custom-finviz.csv')
            stock_arr = []
            
            for slist in sdf.stock_recommendations['buy']:
                stock_arr.append(slist['stock'])

            cols = ['Ticker', 'Company',  'Industry', 'Market Cap','Sales growth quarter over quarter', 'Profit Margin','Forward P/E', 'EPS growth this year','Performance (Week)', 'Performance (Month)','Relative Strength Index (14)', 'Analyst Recom', 'Relative Volume']
            print (df.columns)
            df = df [df.Ticker.isin (stock_arr)][cols]

            st.header ("Fundamental Analysis of Stocks with Buy Recommendations")
            st.dataframe(df)



streamlit_main ("https://worldopen.s3.amazonaws.com/eighth.csv")

