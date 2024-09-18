#!/usr/bin/env python
# coding: utf-8

# # EXPERIMENT 3 - PYTHON DATA ANALYSIS (PANDAS)

# ## Learning Intended Outcomes:

# 1. To identify the codes and functions incorporated in the Pandas library
# 2. To be able to apply and use the different codes and functions in creating a Python program using a Pandas library

# ## Preparation for the Experiment:
# 

# The creator downloaded the csv file named 'cars.csv' for the proper demonstration of data analysis

# # PROBLEM 1: Displaying the First and Last Five Rows of the Resulting Cars

# ## Primary Instruction:

# 1. Load the corresponding csv file into a data frame named cars using pandas
# 
# 2. Display the first five and last 5 rows of the resulting cars.

# ## Procedures:

# ### Import pandas in the code

# •In order to access the functions under 'Pandas', we must import its library using the code 'import pandas as pd'

# In[2]:


#Start of Code
import pandas as pd


# ### Loading the csv file in a Data Frame

# •To access the download file, we load it into a data frame (which can be any name) and use the function 'pd.read_csv('file_name.csv')

# In[6]:


#Loading the cars.csv file
cars = pd.read_csv('cars.csv')
cars


# ### Loading the First and Last Five Rows

# #### First Five Rows

# Primary function used: name_of_dataframe.head()

# In[11]:


#First 5 Rows
First_Five_Rows = cars.head()
First_Five_Rows


# •Placed the first 5 rows in a variable named 'First_Five_Rows' then displayed the value after

# #### Last Five Rows

# Primary function used: name_of_dataframe.tail()

# In[16]:


#Last 5 Rows
Last_Five_Rows = cars.tail()
Last_Five_Rows


# •Placed the last 5 rows in a variable named 'Last_Five_Rows' then displayed the value after

# In[19]:


#End of Code

