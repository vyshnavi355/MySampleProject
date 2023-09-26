#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import the required Libraries.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ## Data Cleaning 

# ### Data Reading & Data Types 

# In[2]:


#Read the data in pandas
inp0= pd.read_csv(r"C:\Users\saras\OneDrive\Desktop\royalvyshu\PYTHON\Attribute+DataSet.csv")
inp1= pd.read_csv(r"C:\Users\saras\OneDrive\Desktop\royalvyshu\PYTHON\Dress+Sales.csv")


# You have “Attribute DataSet” which contains a column named “Price”. Choose the correct statement from the following about its data type and variable type.
# - Integer type and numerical variable
# - Object type and categorical ordinal variable
# - Object type and categorical nominal variable
# - Float type and categorical variable.
# Answer:Object type and categorical ordinal variable
# 

# #### There is another column in “Attribute DataSet” named as “Recommendation”, choose the correct statement about its data type and variable type.
# - Integer type and categorical
# - Object type and categorical
# - Integer type and continuous numerical
# - Object type only.
# (Answer:Integer type and continuous numerical)

# Which of the following column do you think are of no use in “Attribute DataSet”.
# - Dress_ID
# - Price
# - Size and material
# - NeckLine
# - None of the above
# (Answer:None of the above)
# 

# In[3]:


# Print the information about the attributes of inp0 and inp1.
print(inp0)
print(inp1)


# ### Fixing the Rows and Columns 

# As you can see, there is a column in “Attribute Dataset” named as ‘Size’. This column contains the values in abbreviation format. Write a code in Python to convert the followings:
# 
# - M into  “Medium”
# - L into  “Large”
# - XL into “Extra large”
# - free into “Free”
# - S, s & small into “Small”.
# 
# Now once you are done with changes in the dataset, what is the value of the lowest percentage, the highest percentage and the percentage of Small size categories in the column named “Size”?
# 

# In[4]:


# Column fixing, correcting size abbreviation. count the percentage of each size category in "Size" column.
inp0['Size']=inp0['Size'].replace({'M':'Medium','L':'Large','XL':'Extra large','free':'Free','S':'Small','s':'Small','small':'Small'})
count_size=inp0['Size'].value_counts()
totalcount=inp0['Size'].count()
percentage=(count_size/totalcount)*100
percentage


# In[5]:


# Print the value counts of each category in "Size" column.
print(inp0['Size'].value_counts())


# ### Impute/Remove Missing values

# In[6]:


# Print the null count of each variables of inp0 and inp1.
print(inp0.isnull().count())
print(inp1.isnull().sum())


# You are given another dataset named “Dress Sales”. Now if you observe the datatypes of the columns using ‘inp1.info()’ command, you can identify that there are certain columns defined as object data type though they primarily consist of numeric data.
# 
# Now if you try and convert these object data type columns into numeric data type(float), you will come across an error message. Try to correct this error.
# 
# 
# 
# 
# 
# 

# In[7]:


# Print the data types information of inp1 i.e. "Dress Sales" data.
inp1.info()


# In[8]:


# Try to convert the object type into float type of data. YOU GET ERROR MESSAGE.

#inp1['09-12-2013']=inp1['09-12-2013'].astype('float64')


# In[9]:


# Do the required changes in the "Dress Sales" data set to get null values on string values.
inp1.loc[inp1['09-12-2013']=='Removed',"09-12-2013"]==np.NaN
inp1.loc[inp1['14-09-2013']=='removed',"14-09-2013"]==np.NaN 
inp1.loc[inp1['16-09-2013']=='removed',"16-09-2013"]==np.NaN
inp1.loc[inp1['18-09-2013']=='removed',"18-09-2013"]==np.NaN
inp1.loc[inp1['20-09-2013']=='removed',"20-09-2013"]==np.NaN
inp1.loc[inp1['22-09-2013']=='orders',"22-09-2013"] ==np.NaN



# In[10]:


inp1.isnull().sum()


# In[11]:


inp1.dtypes


# In[12]:


# Convert the object type columns in "Dress Sales" into float type of data type.
inp1['09-12-2013'] = pd.to_numeric(inp1['09-12-2013'], errors='coerce',downcast='float')
inp1['14-09-2013'] = pd.to_numeric(inp1['14-09-2013'], errors='coerce',downcast='float')
inp1['16-09-2013'] = pd.to_numeric(inp1['16-09-2013'], errors='coerce',downcast='float')
inp1['18-09-2013'] = pd.to_numeric(inp1['18-09-2013'], errors='coerce',downcast='float')
inp1['20-09-2013'] = pd.to_numeric(inp1['20-09-2013'], errors='coerce',downcast='float')
inp1['22-09-2013'] = pd.to_numeric(inp1['22-09-2013'], errors='coerce',downcast='float')


# In[13]:


inp1.dtypes


# When you see the null counts in “Dress Sales” dataset after performing all the operations that have been mentioned in jupyter notebook, you will find that there are some columns in “Dress Sales” data where there are more than 40% of missing values. Based on your understanding of dealing with missing values do the following steps.

# In[14]:


# Print the null percetange of each column of inp1.
a=inp1.isnull().sum()/len(inp1.index)*100


# In[15]:


#Drop the columns in "Dress Sales" which have more than 40% of missing values.
b=a[a>40].index
inp1=inp1.drop(columns=b)
inp1


# In[16]:


inp1.isnull().sum()


# You should categorise the dates into seasons in “Dress Sales” data to simplify the analysis according to the following criteria:
# - June, July and August: Summer.
# - September, October and November: Autumn.
# - December, January and February: WInter.
# - March, April and May: Spring.
# 
# 
# 

# In[17]:


# Create the four seasons columns in inp1, according to the above criteria.
inp1['Summer']=inp1['29-08-2013']+inp1['31-08-2013']+inp1['09-06-2013']+inp1['09-08-2013']+inp1['10-06-2013']+inp1['10-08-2013']
inp1['Autumn']=inp1['09-10-2013']+inp1['14-09-2013']+inp1['16-09-2013']+inp1['18-09-2013']+inp1['20-09-2013']+inp1['22-09-2013']+inp1['24-09-2013']+inp1['26-09-2013']+inp1['28-09-2013']+inp1['30-09-2013']+inp1['10-10-2013']
inp1['Winter']=inp1['09-02-2013']+inp1['10-02-2013']+inp1['09-12-2013']+inp1['10-12-2013']
inp1['Spring']=inp1['09-04-2013']+inp1['10-04-2013']


# In[18]:


# calculate the sum of sales in each seasons in inp1 i.e. "Dress Sales".
print(inp1['Summer'].sum())
print(inp1['Autumn'].sum())
print(inp1['Winter'].sum())
print(inp1['Spring'].sum())


# Now let's merge inp1 with inp0 with left join manner, so that the information of inp0 should remain intact.

# In[ ]:


# Merge inp0 with inp1 into inp0. this is also called left merge.
inp0 = pd.merge(left=inp0,right=inp1, how='left', left_on='Dress_ID', right_on='Dress_ID')
inp0.head()


# In[ ]:


# Now Drop the Date columns from inp0 as it is already combined into four seasons.
inp0.drop(inp0.loc[:,'29-08-2013':'10-12-2013'].columns, axis= 1, inplace= True)
inp0.isnull().sum()


# Print the null count of inp0 to get the idea about the missing values in data set.

# In[ ]:


# Print the null count of each columns in inp0 dataframe i.e. combined data frame of inp0 and inp1 without date columns.
inp0.isnull().sum()


# In[ ]:


inp0.columns


# You can see that there are two types of variables one with a large number of missing values and another is very less number of missing values. These two columns can be categorized as:
# 
# Type-1: Missing values are very less (around 2 or 3 missing values): Price, Season, NeckLine, SleeveLength, Winter and Autumn. 
# 
# Type-2: Missing values are large in numbers (more than 15%): Material, FabricType, Decoration and Pattern Type.
# 
# 

# In[19]:


# Deal with the missing values of Type-1 columns: Price, Season, NeckLine, SleeveLength, Winter and Autumn.
inp0['Price'].fillna(inp0['Price'].mode(),inplace=True)
inp0['Season'].fillna(inp0['Season'].mode(),inplace=True)
inp0['NeckLine'].fillna(inp0['NeckLine'].mode(),inplace=True)
inp0['SleeveLength'].fillna(inp0['SleeveLength'].mode(),inplace=True)


# In[20]:


# Deal with the missing values for Type-2 columns: Material, FabricType, Decoration and Pattern Type.
inp0.isnull().sum()


# ### Standardise value 

# In the given dataset, there are certain discrepancies with the categorical names such as irregular spellings. Choose the correct option of columns with irregular categories and update them.
#  
# - Season, NeckLine
# - Price, Material
# - fabricType, Decoration
# - Season, SleeveLength
# 

# In[ ]:


inp0.columns


# In[ ]:


#correcting the spellings.
inp0['Season'].unique()
inp0['Season'].replace(['winter','Automn','spring'],['Winter','Autumn','Spring'],inplace=True)


# In[ ]:


#correcting the Spellings.
inp0['Season'].unique()
inp0['NeckLine'].unique()
inp0['Price'].unique()
inp0['Material'].unique()
inp0['FabricType'].unique()
inp0['Decoration'].unique()
inp0['SleeveLength'].unique()
inp0['SleeveLength'].replace(['thressqatar','sleeveless','sleeevless','sleveless','threequater','capsleeves','urndowncollor','half'],['threequarter','sleevless','sleevless','sleevless','threequarter','cap-sleeves','turndowncollor','halfsleeve'],inplace=True)


# In[ ]:


inp0['SleeveLength'].unique()


# There is a column named ‘Style’ in ‘Attribute Dataset’ which consists of the different style categories of the women apparels. Certain categories whose total sale is less than 50000 across all the seasons is considered under one single category as ‘Others’.
# 

# Which of the following categories in ‘Style’ column can be grouped into ‘Others’ category? and perform the grouping operation in the notebook for further analysis.
# - Flare, fashion
# - Novelty, bohemian
# - OL, fashion, work
# - Novelty, fashion, Flare
# 

# In[21]:


# Group "Style" categories into "Others" which have less than 50000 sales across all the seasons.
inp0['total'] = inp0['Summer'] + inp0['Autumn'] + inp0['Winter'] + inp0['Spring']
style_group = inp0['total'].groupby(inp0['Style']).sum().reset_index()
res = style_group.loc[style_group['total']<50000]
res


# In[ ]:


inp0['Style'].replace(['Flare','Novelty','bohemian','party','party','sexy','vintage','work'], 'Others', inplace=True)
inp0['Style'].unique()


# What is the percentage of “cute” and “Others” category in “Style” column in “Attribute DataSet” respectively?
# - 46%, 5%
# - 9%, 2.1%
# - 2.1%, 5%
# - 13.8%, 9%
# 

# In[1]:


# Calculate the percentage of each categories in the "Style" variable.

inp0['Style'].value_counts(normalize=True)*100


# Similarly Club Neckline, SLeeve length categories into "Others" which have less than 50000 sales across all the seasons.

# In[ ]:


# Group "Neckline" categories into "Others" which have less than 50000 sales across all the seasons.
neck_group = inp0['total'].groupby(inp0['NeckLine']).sum().reset_index()
res = neck_group.loc[neck_group['total']<50000]
res


# In[ ]:


# Group "Sleeve length" categories into "Others" which have less than 50000 sales across all the seasons.
sleeve_group = inp0['total'].groupby(inp0['SleeveLength']).sum().reset_index()
res = sleeve_group.loc[sleeve_group['total']<50000]
res


# Club material, fabrictype, patterntype and decoration categories into "Others" which have less than 25000 sales across all the seasons

# In[ ]:


# Group "material" categories into "Others" which have less than 25000 sales across all the seasons.
mat_group = inp0['total'].groupby(inp0['Material']).sum().reset_index()
res = mat_group.loc[mat_group['total']<25000]
res


# In[ ]:


# Group "fabric type" categories into "Others" which have less than 25000 sales across all the seasons.
fab_group = inp0['total'].groupby(inp0['FabricType']).sum().reset_index()
res = fab_group.loc[fab_group['total']<25000]
res


# In[ ]:


# Group "patern type" categories into "Others" which have less than 25000 sales across all the seasons.
pat_group = inp0['total'].groupby(inp0['Pattern Type']).sum().reset_index()
res = pat_group.loc[pat_group['total']<25000]
res


# In[ ]:


# Group "decoration" categories into "Others" which have less than 25000 sales across all the seasons.
dec_group = inp0['total'].groupby(inp0['Decoration']).sum().reset_index()
res = dec_group.loc[dec_group['total']<25000]
res


# ### Caregorical Ordered Univariate Analysis

# Which of the following is an unordered variable in “Attribute DataSet”.
# - Style
# - Price
# - Season
# - Size
# (Size)
# 

# ### Numerical variable Univariate analysis:

# What is the approximate difference between the maximum value and 75th percentile in “Autumn” column.
# - Approx 54000
# - Approx 55000
# - Approx 52000
# - Approx 50000
# 
# 

# In[26]:


x=inp0['Autumn'].max()-inp0['Autumn'].quantile(0.75)
x


# In[25]:


# Describe the numerical variale: "Autumn".
inp0['Autumn'].describe()


# In[27]:


# plot the boxplot of "Autumn" column.
plt.boxplot(inp0['Autumn'])
plt


# Which of the following season has the highest difference between the maximum value and 99th quantile of sales?
# - Winter
# - Summer
# - Spring
# - Autumn
# 

# In[ ]:





# In[ ]:


# Find the maximum and 50th percentile of Winter season.


# In[ ]:


# Find the maximum and 50th percentile of Summer season.


# In[ ]:


# Find the maximum and 50th percentile of Spring season.


# In[ ]:


# Find the maximum and 50th percentile of Autumn season.

