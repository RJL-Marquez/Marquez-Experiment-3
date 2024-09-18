#!/usr/bin/env python
# coding: utf-8

# # EXPERIMENT 3 - PYTHON DATA ANALYSIS (PANDAS)

# ## Learning Intended Outcomes:

# 1. To identify the codes and functions incorporated in the Pandas library
# 2. To be able to apply and use the different codes and functions in creating a Python program using a Pandas library

# ## Preparation for the Experiment:
# 

# The creator downloaded the csv file named 'cars.csv' for the proper demonstration of data analysis

# # PROBLEM 2: Extracting Data

# ## Primary Instruction: 

# Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and
# indexing operations.
# 
# a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.
# 
# b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.
# 
# c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
# 
# d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4
# Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

# ## Procedures:

# ### Import pandas in the code

# •In order to access the functions under 'Pandas', we must import its library using the code 'import pandas as pd'

# In[2]:


#Start of Code
import pandas as pd


# ### Loading the csv file in a Data Frame

# •To access the csv file, we must load it in a data frame using the function: 'pd.read_csv('file_name.csv')'

# In[4]:


#Loading the cars.csv file
cars = pd.read_csv('cars.csv')
cars


# ### a. Display First Five Rows and Odd-Numbered Columns of cars

# Primary Extracting Tool: SLICING
# 
# Example syntax: name.iloc[LowerRange:HigherRange, StartVal:EndVal:Interval]

# In Slicing, we can set a range for our desired rows and we can set an interval for columns, making it the most appropriate tool for this question.

# In[70]:


#Instruction A
a = cars.iloc[:5, 0::2]
a


# •By leaving a value blank, it automatically gets the minimum and maximum value depending on what is needed.
# 
# •Then, proceed by placing the produced data in a variable named 'a', and then display the value after.

# ### b. Display the row that contains the ‘Model’ of ‘Mazda RX4’

# Primary Extracting Tool: INDEXING.
# 
# Example syntax: name.loc[(name['SpecificColumn']=='Name of Rows under the Column'), ['Column Names']]

# In Indexing, we can filter the row with specific strings (e.g., 'Mazda RX4' in the 'Model' column), making it the best tool to utilize in this question.

# In[74]:


#Instruction B
b = cars.loc[(cars['Model']=='Mazda RX4 Wag'),]
b


# •By removing the second pair of brackets (where the column is commonly identified), it will automatically generate all the columns in a specific row.
# 
# •Then, proceeded by placing the produced data in a variable named 'b' and then displayed the value after.

# ### c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

# Primary Extracting Tool: INDEXING.
# 
# Example syntax: name.loc[(name['SpecificColumn']=='Name of Rows under the Column'), ['Column Names']]

# In[80]:


#Instruction C
c = cars.loc[(cars['Model']=='Camaro Z28'),['Model', 'cyl']]
c


# •Placed the produced data in a variable named 'c' and then displayed the value after.
# 
# •By looking at the table above, we can answer the following question: How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
# 
# ANSWER:
# 
# -Camaro Z28 has 8 Cylinders.

# ### d. Determine how many Cylinders and what Gear type do the given cars have

# Primary Extracting Tool: INDEXING.
# 
# Example syntax: name.loc[(name['SpecificColumn']=='Name of Rows under the Column'), ['Column Names']]

# In Indexing, we can set proper conditions on both rows and columns to extract our desired data.

# In[83]:


#Instruction D
d = cars.loc[(cars['Model']=='Mazda RX4 Wag') | (cars['Model']=='Ford Pantera L')| (cars['Model']=='Honda Civic'), ['Model', 'cyl', 'gear']]
d


# •By using the or ('|') conditional operator, we can find the specific models of each car and help us narrow down the specific rows we need.
# 
# •Then, proceeded by placing the produced data in a variable named 'b' then displayed the value after.

# •Looking at the table, we can answer the question: How many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4
# Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have
# 
# ANSWERS:
# 
# -'Mazda RX4 Wag' has 6  cylinders and 4 gears
# 
# -'Ford Pantera L' has 4 cylinders and 4 gears
# 
# -'Honda Civic' has 8 cylinders and 4 gears.

# In[36]:


#End of Code

