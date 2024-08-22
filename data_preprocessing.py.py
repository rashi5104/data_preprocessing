#!/usr/bin/env python
# coding: utf-8

# # Importing the dependencies

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# # Loading the raw data

# In[2]:


# loading the dataset
df=pd.read_csv(r"C:\\Users\\rashi\\Dropbox\\PC\\Downloads\\archive (13)\\final (1).csv")


# In[3]:


df


# In[4]:


# printing the top 5 rows of the dataset
df.head()


# In[6]:


# printing the last 5 rows of the dataset
df.tail()


# # Statistical Analysis

# In[7]:


# describe
df.describe()


# In[8]:


# info
df.info()


# In[9]:


# finding missing values
df.isnull().sum()


# In[10]:


# showing the types of the columns
df.dtypes


# In[11]:


# shape
df.shape


# In[12]:


# finding duplicates
df.duplicated().sum()


# In[19]:


print(df.columns)


# # Exploratory Data Analysis

# In[13]:


df.describe().T


# In[14]:


df.describe(include="object")


# In[15]:


df.value_counts("match")


# In[16]:


# Plot pychart
match_data = {
    'Format': ['ODI', 'Test', 'T20'],
    'Matches': [252, 173, 91]
}

# Create a pie chart
plt.pie(match_data['Matches'], labels=match_data['Format'], autopct='%1.1f%%', startangle=140)

# Add a title
plt.title('Distribution of Cricket Matches by Format')

# Display the plot
plt.show()


# In[21]:


# Plot histogram
df['match'].hist()


# In[28]:


# Plot bar chart
df['match'].value_counts().plot.bar()


# In[ ]:




