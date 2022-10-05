#!/usr/bin/env python
# coding: utf-8

# # Analyzing Historical Stock/Revenue Data and Building a Dashboard

# ## Extracting and Visualizing Stock Data

# ### Description

# Extracting essential data from a dataset and displaying it is a necessary part of data science; therefore I try to make correct decisions based on the data. In this project, I will extract some stock data and then display this data in a graph.

# #### Steps:

# * Installation
# * importing Python libraries
# * Define a Function that Makes a Graph
# * Use yfinance to Extract Stock Data
# * Use Webscraping to Extract Tesla Revenue Data
# * Use yfinance to Extract Stock Data
# * Use Webscraping to Extract GME Revenue Data
# * Plot Tesla Stock Graph
# * Plot GameStop Stock Graph

# ### Installation

# The Python package management system Pip is used to manage packages. Additionally, it is known as “Pip Installs Python” or “Pip Installs Packages.” Pip installs the packages on your system using the Python Package Index (PyPI).
# 
# For this Project, we are going to be using Python and several Python libraries. Some of these libraries might be installed in your lab environment. Others may need to be installed by you. The cells below will install these libraries when executed.

# In[1]:


get_ipython().system('pip install yfinance')
get_ipython().system('pip install bs4')


# ### Importing Python libraries

# **yfinance** is a python package that enables us to fetch historical market data from Yahoo Finance API in a Pythonic way.
# 
# **Pandas** is a python package used in data analysis and manipulation tool.
# 
# **request** module helps us to download a web page.
# 
# **Beautiful Soup** is a Python library for pulling data out of HTML and XML files. This is accomplished by representing the HTML as a set of objects with methods used to parse the HTML. We can navigate the HTML as a tree and/or filter out what we are looking for.
# 
# **Plotly** provides online graphing, analytics, and statistics tools for individuals and collaboration, as well as scientific graphing libraries for Python.

# In[2]:


import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# ### Define Graphing Function

# In this section, we define the function make_graph. We don’t have to know how the function works, we should only care about the inputs. It takes a dataframe with stock data (dataframe must contain Date and Close columns), a dataframe with revenue data (dataframe must contain Date and Revenue columns), and the name of the stock.

# In[21]:


def graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data.Date, infer_datetime_format=True), y=stock_data.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data.Date, infer_datetime_format=True), y=revenue_data.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()


# ### Use yfinance to Extract Stock Data

# Using the Ticker module we can create an object that will allow us to access functions to extract data. To do this we need to provide the ticker symbol for the stock, here the company is Tesla and the ticker symbol is TSLA.

# In[4]:



tesla = yf.Ticker("TSLA")


# A share is the single smallest part of a company’s stock that you can buy, the prices of these shares fluctuate over time. Using the history() method we can get the share price of the stock over a certain period of time. Using the period parameter we can set how far back from the present to get data. The options for period are 1 day (1d), 5d, 1 month (1mo) , 3mo, 6mo, 1 year (1y), 2y, 5y, 10y, ytd, and max.

# In[5]:



tesla_data = tesla.history(period="max")


# Reset the index using the reset_index(inplace=True) function on the tesla_data DataFrame and display the first five rows of the tesla_data dataframe using the head function. Take a screenshot of the results and code from the beginning of Question 1 to the results below.

# In[6]:


tesla_data.reset_index(inplace=True)
tesla_data.head()


# ### Use Webscraping to Extract Tesla Revenue Data

# Here we will use the requests library to download the webpage https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue. Save the text of the response as a variable named html_data.

# In[7]:


url= "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_data=requests.get(url).text


# Then we Parse the html data using beautiful_soup.

# In[8]:



soup = BeautifulSoup(html_data,"html5lib")


# Here we will use beautiful soup extract the table with Tesla Quarterly Revenue and store it into a dataframe named tesla_revenue. The dataframe should have columns Date and Revenue. Here we make sure that the comma and dollar sign is removed from the Revenue column.

# In[9]:


tesla_revenue= pd.read_html(url, match="Tesla Quarterly Revenue", flavor='bs4')[0]
tesla_revenue=tesla_revenue.rename(columns = {'Tesla Quarterly Revenue(Millions of US $)': 'Date', 'Tesla Quarterly Revenue(Millions of US $).1': 'Revenue'}, inplace = False)
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace(",","").str.replace("$","")
tesla_revenue.head()


# In[10]:



tesla_revenue


# Now we will display the last 5 row of the tesla_revenue dataframe using the tail function.

# In[11]:


tesla_revenue.dropna(inplace=True)
tesla_revenue.tail()


# ### Extracting GameStop Stock Data Using yfinance

# Using the **Ticker** module we can create an object that will allow us to access functions to extract data. To do this we need to provide the ticker symbol for the stock, here the company is **GameStop** and the ticker symbol is **GME**.

# In[12]:



gme = yf.Ticker("GME")


# A share is the single smallest part of a company’s stock that you can buy, the prices of these shares fluctuate over time. Using the **history()** method we can get the share price of the stock over a certain period of time. Using the period parameter we can set how far back from the present to get data. The options for period are 1 day (1d), 5d, 1 month (1mo) , 3mo, 6mo, 1 year (1y), 2y, 5y, 10y, ytd, and max.

# In[14]:


gme = gme.history(period = "max")


# **Reset the index** using the reset_index(inplace=True) function on the tesla_data DataFrame and display the first five rows of the tesla_data dataframe using the head function. Take a screenshot of the results and code from the beginning of Question 1 to the results below.

# In[15]:


gme.reset_index(inplace = True)
gme.head()


# ### Extracting GameStop Revenue Data Using Webscraping

# Here we will use the requests library to download the webpage “https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html&#8221;
# 
# Save the text of the response as a variable named html_data.

# In[19]:


url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
 
html_data=requests.get(url).text


# Here we will use beautiful soup extract the table with GameStop Quarterly Revenue and store it into a dataframe named gme_revenue. The dataframe should have columns Date and Revenue. Here we make sure that the comma and dollar sign is removed from the Revenue column.

# In[20]:


soup = BeautifulSoup(html_data, "html5lib")
gme_revenue = pd.read_html(url, match = "GameStop Quarterly Revenue", flavor='bs4')[0]
gme_revenue = gme_revenue.rename(columns = {"GameStop Quarterly Revenue(Millions of US $)": "Date", "GameStop Quarterly Revenue(Millions of US $).1": "Revenue"}, inplace = False)
gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace(",","").str.replace("$","")
gme_revenue.dropna(inplace = True)
 
gme_revenue.tail()


# ### Tesla Stock and Revenue Dashboard

# In[22]:


graph(tesla_data, tesla_revenue, "Tesla Stock Data Graph")


# ### Plot GameStop Stock Graph

# In[23]:


graph(gme, gme_revenue, "GameStop Stock Data graph")


# In[ ]:




