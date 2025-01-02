#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib
import seaborn as sbn
import random


# ## Generating the Data

# In[3]:


categories=['Food','Fashion','Fitness','Health','Travel','Music','Culture','Family','Health']


# In[4]:


n=100 #number of entries to generate
dict1 = {
    'Date': pd.date_range('2024-01-01', periods=n),
    'Category': [random.choice(categories) for _ in range(n)],
    'Likes': np.random.randint(0, 10000, size=n)
}


# In[5]:


#step3: loading the generated data onto a dataframe
data=pd.DataFrame(dict1)
print(data)


# In[6]:


#description of the dataframe
data['Category'].value_counts() #count of category element


# In[7]:


data.head()                     #dataframe head
data.info()                     #dataframe information
data.describe()                 #dataframe description


# ## Cleaning the Data

# In[8]:


#cleaning the data

#step1: removing all the null data & duplicate data
data=data.dropna()
data=data.drop_duplicates()

print(data.head())


# In[9]:


#step2: Convert the 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

print(data.info()) #check


# In[10]:


#step3: converting 'Likes' to integers

data['Likes']=data['Likes'].astype(int)  #using astype method to change datatype of specified column to int

print(data.head())  #check


# ## Visualising and Analysing the Data

# In[11]:


#Visualising and Analysing the Data
#using matplotlib and seaborn libraries

import matplotlib.pyplot as plt

#creating a histogram of 'Likes' column
sbn.histplot(data['Likes'], kde=False, bins=20)

#adding titles and labels
plt.title('Histogram of Likes')
plt.xlabel('Likes')
plt.ylabel('Frequency')

#show the plot
plt.show()


# In[12]:


#creating a boxplot with xaxis as 'Category' and yaxis as 'Likes'

sbn.boxplot(x='Category',y='Likes',data=data)

#adding titles and labels
plt.title('Boxplot of Likes by Category')
plt.xlabel('Category')
plt.ylabel('Likes')

plt.show()


# In[16]:


#statistical analysis

mean_likes=data['Likes'].mean()
print("The Mean Likes is:", mean_likes)

median_likes=data['Likes'].median()
print("The Median Likes is:", median_likes)

standard_dev=data['Likes'].std()
print("The Standard Deviation of Likes is:", standard_dev)

variance=data['Likes'].var()
print("The Variance of Likes is:", variance)

#grouping by category and calculating the mean of Likes
category_mean=data.groupby('Category')['Likes'].mean()
print(category_mean)


# ## Conclusion

# #### From the above data, we can conclude that posts in the Culture category the most number of likes on average, followed closely by Fitness posts. These posts have the most viral or engaging content. Food and Music posts have the lowest average likes, suggesting less engagement. Family, Health, and Travel posts do moderately well.
# 
# #### The histogram shows that the data follows a bimodal distribution, with two peaks or cluster of values. Some posts receive very high likes (viral), while other posts receive very low likes (unpopular). The mean (4768) is slightly higher than the median (4482), suggesting either a right-skewed distribution, or a distrubution that is not strictly unimodal or normal. 
# 
# #### The standard deviation (3096.51) and variance (9588396.58) are quite large compared to the mean, indicating a high variability in Likes. This suggests that Likes differ significantly across categories and posts, with some posts receiving very few likes and others receiving a lot.
# 
# 

# In[ ]:




