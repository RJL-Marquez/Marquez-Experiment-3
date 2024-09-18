# Marquez Experiment #3
# PYTHON DATA ANALYSIS (PANDAS)
## Learning Intended Outcomes: 
1. To identify the codes and functions incorporated in the Pandas library
2. To be able to apply and use the different codes and functions in creating a Python program using a Pandas library

## Preparation for the Experiment
The creator downloaded the csv file named 'cars.csv' for the proper demonstration of data analysis

# PROBLEM 1: Displaying the First and Last Five Rows of the Cars

## Primary Instruction:
1. Load the corresponding csv file into a data frame named cars using pandas
2. Display the first five and last 5 rows of the resulting cars.

## Procedures:

### Import pandas in the code
•In order to access the functions under 'Pandas', we must import its library using the code 'import pandas as pd'

```python
#Start of Code
import pandas as pd
```

### Loading the csv file in a Data Frame
•To access the download file, we load it into a data frame (which can be any name) and use the function 'pd.read_csv('file_name.csv')

```python
cars = pd.read_csv('cars.csv')
cars
```

| Model               | mpg  | cyl | disp  | hp  | drat | wt    | qsec  | vs | am | gear | carb |
|---------------------|------|-----|-------|-----|------|-------|-------|----|----|------|------|
| Mazda RX4           | 21   | 6   | 160   | 110 | 3.9  | 2.62  | 16.46 | 0  | 1  | 4    | 4    |
| Mazda RX4 Wag       | 21   | 6   | 160   | 110 | 3.9  | 2.875 | 17.02 | 0  | 1  | 4    | 4    |
| Datsun 710          | 22.8 | 4   | 108   | 93  | 3.85 | 2.32  | 18.61 | 1  | 1  | 4    | 1    |
| Hornet 4 Drive      | 21.4 | 6   | 258   | 110 | 3.08 | 3.215 | 19.44 | 1  | 0  | 3    | 1    |
| Hornet Sportabout   | 18.7 | 8   | 360   | 175 | 3.15 | 3.44  | 17.02 | 0  | 0  | 3    | 2    |
| Valiant             | 18.1 | 6   | 225   | 105 | 2.76 | 3.46  | 20.22 | 1  | 0  | 3    | 1    |
| Duster 360          | 14.3 | 8   | 360   | 245 | 3.21 | 3.57  | 15.84 | 0  | 0  | 3    | 4    |
| Merc 240D           | 24.4 | 4   | 146.7 | 62  | 3.69 | 3.19  | 20    | 1  | 0  | 4    | 2    |
| Merc 230            | 22.8 | 4   | 140.8 | 95  | 3.92 | 3.15  | 22.9  | 1  | 0  | 4    | 2    |
| Merc 280            | 19.2 | 6   | 167.6 | 123 | 3.92 | 3.44  | 18.3  | 1  | 0  | 4    | 4    |
| Merc 280C           | 17.8 | 6   | 167.6 | 123 | 3.92 | 3.44  | 18.9  | 1  | 0  | 4    | 4    |
| Merc 450SE          | 16.4 | 8   | 275.8 | 180 | 3.07 | 4.07  | 17.4  | 0  | 0  | 3    | 3    |
| Merc 450SL          | 17.3 | 8   | 275.8 | 180 | 3.07 | 3.73  | 17.6  | 0  | 0  | 3    | 3    |
| Merc 450SLC         | 15.2 | 8   | 275.8 | 180 | 3.07 | 3.78  | 18    | 0  | 0  | 3    | 3    |
| Cadillac Fleetwood  | 10.4 | 8   | 472   | 205 | 2.93 | 5.25  | 17.98 | 0  | 0  | 3    | 4    |
| Lincoln Continental | 10.4 | 8   | 460   | 215 | 3    | 5.424 | 17.82 | 0  | 0  | 3    | 4    |
| Chrysler Imperial   | 14.7 | 8   | 440   | 230 | 3.23 | 5.345 | 17.42 | 0  | 0  | 3    | 4    |
| Fiat 128            | 32.4 | 4   | 78.7  | 66  | 4.08 | 2.2   | 19.47 | 1  | 1  | 4    | 1    |
| Honda Civic         | 30.4 | 4   | 75.7  | 52  | 4.93 | 1.615 | 18.52 | 1  | 1  | 4    | 2    |
| Toyota Corolla      | 33.9 | 4   | 71.1  | 65  | 4.22 | 1.835 | 19.9  | 1  | 1  | 4    | 1    |
| Toyota Corona       | 21.5 | 4   | 120.1 | 97  | 3.7  | 2.465 | 20.01 | 1  | 0  | 3    | 1    |
| Dodge Challenger    | 15.5 | 8   | 318   | 150 | 2.76 | 3.52  | 16.87 | 0  | 0  | 3    | 2    |
| AMC Javelin         | 15.2 | 8   | 304   | 150 | 3.15 | 3.435 | 17.3  | 0  | 0  | 3    | 2    |
| Camaro Z28          | 13.3 | 8   | 350   | 245 | 3.73 | 3.84  | 15.41 | 0  | 0  | 3    | 4    |
| Pontiac Firebird    | 19.2 | 8   | 400   | 175 | 3.08 | 3.845 | 17.05 | 0  | 0  | 3    | 2    |
| Fiat X1-9           | 27.3 | 4   | 79    | 66  | 4.08 | 1.935 | 18.9  | 1  | 1  | 4    | 1    |
| Porsche 914-2       | 26   | 4   | 120.3 | 91  | 4.43 | 2.14  | 16.7  | 0  | 1  | 5    | 2    |
| Lotus Europa        | 30.4 | 4   | 95.1  | 113 | 3.77 | 1.513 | 16.9  | 1  | 1  | 5    | 2    |
| Ford Pantera L      | 15.8 | 8   | 351   | 264 | 4.22 | 3.17  | 14.5  | 0  | 1  | 5    | 4    |
| Ferrari Dino        | 19.7 | 6   | 145   | 175 | 3.62 | 2.77  | 15.5  | 0  | 1  | 5    | 6    |
| Maserati Bora       | 15   | 8   | 301   | 335 | 3.54 | 3.57  | 14.6  | 0  | 1  | 5    | 8    |
| Volvo 142E          | 21.4 | 4   | 121   | 109 | 4.11 | 2.78  | 18.6  | 1  | 1  | 4    | 2    |

### Loading the First Five Rows
Primary function used: name_of_dataframe.head()
```python
#First 5 Rows
First_Five_Rows = cars.head()
First_Five_Rows
```

Resulting Output: 

| Model               | mpg  | cyl | disp  | hp  | drat | wt    | qsec  | vs | am | gear | carb |
|---------------------|------|-----|-------|-----|------|-------|-------|----|----|------|------|
| Mazda RX4           | 21   | 6   | 160   | 110 | 3.9  | 2.62  | 16.46 | 0  | 1  | 4    | 4    |
| Mazda RX4 Wag       | 21   | 6   | 160   | 110 | 3.9  | 2.875 | 17.02 | 0  | 1  | 4    | 4    |
| Datsun 710          | 22.8 | 4   | 108   | 93  | 3.85 | 2.32  | 18.61 | 1  | 1  | 4    | 1    |
| Hornet 4 Drive      | 21.4 | 6   | 258   | 110 | 3.08 | 3.215 | 19.44 | 1  | 0  | 3    | 1    |
| Hornet Sportabout   | 18.7 | 8   | 360   | 175 | 3.15 | 3.44  | 17.02 | 0  | 0  | 3    | 2    |

Placed the first 5 rows in a variable named 'First_Five_Rows' then displayed the value after


### Loading the Last Five Rows
Primary function used: name_of_dataframe.tail()
```python
#Last 5 Rows
Last_Five_Rows = cars.tail()
Last_Five_Rows
```

Resulting Output: 

| Model               | mpg  | cyl | disp  | hp  | drat | wt    | qsec  | vs | am | gear | carb |
|---------------------|------|-----|-------|-----|------|-------|-------|----|----|------|------|
| Lotus Europa        | 30.4 | 4   | 95.1  | 113 | 3.77 | 1.513 | 16.9  | 1  | 1  | 5    | 2    |
| Ford Pantera L      | 15.8 | 8   | 351   | 264 | 4.22 | 3.17  | 14.5  | 0  | 1  | 5    | 4    |
| Ferrari Dino        | 19.7 | 6   | 145   | 175 | 3.62 | 2.77  | 15.5  | 0  | 1  | 5    | 6    |
| Maserati Bora       | 15   | 8   | 301   | 335 | 3.54 | 3.57  | 14.6  | 0  | 1  | 5    | 8    |
| Volvo 142E          | 21.4 | 4   | 121   | 109 | 4.11 | 2.78  | 18.6  | 1  | 1  | 4    | 2    |

Placed the last 5 rows in a variable named 'Last_Five_Rows' then displayed the value after


```python
#End of Code
```


# PROBLEM 2: Extracting Data

## Primary Instruction:
Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.

a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.

b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.

c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ & ‘Honda Civic’ have.

## Procedures:

### Import pandas in the code
•In order to access the functions under 'Pandas', we must import its library using the code 'import pandas as pd'

```python
#Start of Code
import pandas as pd
```

### Loading the csv file in a Data Frame
•To access the download file, we load it into a data frame (which can be any name) and use the function 'pd.read_csv('file_name.csv')

```python
cars = pd.read_csv('cars.csv')
cars
```

| Model               | mpg  | cyl | disp  | hp  | drat | wt    | qsec  | vs | am | gear | carb |
|---------------------|------|-----|-------|-----|------|-------|-------|----|----|------|------|
| Mazda RX4           | 21   | 6   | 160   | 110 | 3.9  | 2.62  | 16.46 | 0  | 1  | 4    | 4    |
| Mazda RX4 Wag       | 21   | 6   | 160   | 110 | 3.9  | 2.875 | 17.02 | 0  | 1  | 4    | 4    |
| Datsun 710          | 22.8 | 4   | 108   | 93  | 3.85 | 2.32  | 18.61 | 1  | 1  | 4    | 1    |
| Hornet 4 Drive      | 21.4 | 6   | 258   | 110 | 3.08 | 3.215 | 19.44 | 1  | 0  | 3    | 1    |
| Hornet Sportabout   | 18.7 | 8   | 360   | 175 | 3.15 | 3.44  | 17.02 | 0  | 0  | 3    | 2    |
| Valiant             | 18.1 | 6   | 225   | 105 | 2.76 | 3.46  | 20.22 | 1  | 0  | 3    | 1    |
| Duster 360          | 14.3 | 8   | 360   | 245 | 3.21 | 3.57  | 15.84 | 0  | 0  | 3    | 4    |
| Merc 240D           | 24.4 | 4   | 146.7 | 62  | 3.69 | 3.19  | 20    | 1  | 0  | 4    | 2    |
| Merc 230            | 22.8 | 4   | 140.8 | 95  | 3.92 | 3.15  | 22.9  | 1  | 0  | 4    | 2    |
| Merc 280            | 19.2 | 6   | 167.6 | 123 | 3.92 | 3.44  | 18.3  | 1  | 0  | 4    | 4    |
| Merc 280C           | 17.8 | 6   | 167.6 | 123 | 3.92 | 3.44  | 18.9  | 1  | 0  | 4    | 4    |
| Merc 450SE          | 16.4 | 8   | 275.8 | 180 | 3.07 | 4.07  | 17.4  | 0  | 0  | 3    | 3    |
| Merc 450SL          | 17.3 | 8   | 275.8 | 180 | 3.07 | 3.73  | 17.6  | 0  | 0  | 3    | 3    |
| Merc 450SLC         | 15.2 | 8   | 275.8 | 180 | 3.07 | 3.78  | 18    | 0  | 0  | 3    | 3    |
| Cadillac Fleetwood  | 10.4 | 8   | 472   | 205 | 2.93 | 5.25  | 17.98 | 0  | 0  | 3    | 4    |
| Lincoln Continental | 10.4 | 8   | 460   | 215 | 3    | 5.424 | 17.82 | 0  | 0  | 3    | 4    |
| Chrysler Imperial   | 14.7 | 8   | 440   | 230 | 3.23 | 5.345 | 17.42 | 0  | 0  | 3    | 4    |
| Fiat 128            | 32.4 | 4   | 78.7  | 66  | 4.08 | 2.2   | 19.47 | 1  | 1  | 4    | 1    |
| Honda Civic         | 30.4 | 4   | 75.7  | 52  | 4.93 | 1.615 | 18.52 | 1  | 1  | 4    | 2    |
| Toyota Corolla      | 33.9 | 4   | 71.1  | 65  | 4.22 | 1.835 | 19.9  | 1  | 1  | 4    | 1    |
| Toyota Corona       | 21.5 | 4   | 120.1 | 97  | 3.7  | 2.465 | 20.01 | 1  | 0  | 3    | 1    |
| Dodge Challenger    | 15.5 | 8   | 318   | 150 | 2.76 | 3.52  | 16.87 | 0  | 0  | 3    | 2    |
| AMC Javelin         | 15.2 | 8   | 304   | 150 | 3.15 | 3.435 | 17.3  | 0  | 0  | 3    | 2    |
| Camaro Z28          | 13.3 | 8   | 350   | 245 | 3.73 | 3.84  | 15.41 | 0  | 0  | 3    | 4    |
| Pontiac Firebird    | 19.2 | 8   | 400   | 175 | 3.08 | 3.845 | 17.05 | 0  | 0  | 3    | 2    |
| Fiat X1-9           | 27.3 | 4   | 79    | 66  | 4.08 | 1.935 | 18.9  | 1  | 1  | 4    | 1    |
| Porsche 914-2       | 26   | 4   | 120.3 | 91  | 4.43 | 2.14  | 16.7  | 0  | 1  | 5    | 2    |
| Lotus Europa        | 30.4 | 4   | 95.1  | 113 | 3.77 | 1.513 | 16.9  | 1  | 1  | 5    | 2    |
| Ford Pantera L      | 15.8 | 8   | 351   | 264 | 4.22 | 3.17  | 14.5  | 0  | 1  | 5    | 4    |
| Ferrari Dino        | 19.7 | 6   | 145   | 175 | 3.62 | 2.77  | 15.5  | 0  | 1  | 5    | 6    |
| Maserati Bora       | 15   | 8   | 301   | 335 | 3.54 | 3.57  | 14.6  | 0  | 1  | 5    | 8    |
| Volvo 142E          | 21.4 | 4   | 121   | 109 | 4.11 | 2.78  | 18.6  | 1  | 1  | 4    | 2    |

### a. Display First Five Rows and Odd-Numbered Columns of cars

Primary Extracting Tool: SLICING

Example syntax:
```python
name.iloc[LowerRange:HigherRange, StartVal:EndVal:Interval]
```

In Slicing, we can set a range for our desired rows and we can set an interval for columns, making it the most appropriate tool for this question.
```python
#Instruction A
a = cars.iloc[:5, 0::2]
a
```

Resulting Output: 
| Model             | cyl | hp  | wt    | vs | gear |
|-------------------|-----|-----|-------|----|------|
| Mazda RX4         | 6   | 110 | 2.62  | 0  | 4    |
| Mazda RX4 Wag     | 6   | 110 | 2.875 | 0  | 4    |
| Datsun 710        | 4   | 93  | 2.32  | 1  | 4    |
| Hornet 4 Drive    | 6   | 110 | 3.215 | 1  | 3    |
| Hornet Sportabout | 8   | 175 | 3.44  | 0  | 3    |


By leaving a value blank, it automatically gets the minimum and maximum value depending on what is needed.

Then, proceeded by placing the produced data in a variable named 'a' then displayed the value after.


### b. Display the row that contains the ‘Model’ of ‘Mazda RX4’

Primary Extracting Tool: INDEXING.

Example syntax:
```python
name.loc[(name['SpecificColumn']=='Name of Rows under the Column'), ['Column Names']]
```

In Indexing, we can filter the row with a specific strings (e.g., 'Mazda RX4' in the 'Model' column), making it the best tool to utilized in this question.

```python
#Instruction B
b = cars.loc[(cars['Model']=='Mazda RX4 Wag'),]
b
```
Resulting Output: 
| Model         | mpg | cyl | disp | hp  | drat | wt    | qsec  | vs | am | gear | carb |
|---------------|-----|-----|------|-----|------|-------|-------|----|----|------|------|
| Mazda RX4 Wag | 21  | 6   | 160  | 110 | 3.9  | 2.875 | 17.02 | 0  | 1  | 4    | 4    |

By removing the second pair of brackets (where the column is commonly identified), it will automatically generate all the columns in a specific row.

Then, proceeded by placing the produced data in a variable named 'b' then displayed the value after.

### c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

Primary Extracting Tool: INDEXING.

Example syntax:
```python
 name.loc[(name['SpecificColumn']=='Name of Rows under the Column'), ['Column Names']]
```

In Indexing, we can filter the row and column with specific strings, making it the best tool to utilized in this question.

```python
#Instruction C
c = cars.loc[(cars['Model']=='Camaro Z28'),['Model', 'cyl']]
c
```
Resulting Output: 
| Model      | cyl |
|------------|-----|
| Camaro Z28 | 8   |

Placed the produced data in a variable named 'c' and then displayed the value after.

By looking at the table above, we can answer the following question: How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

ANSWER:

Camaro Z28 has 8 Cylinders.

### d. Determine how many Cylinders and what Gear type do the given cars have

Primary Extracting Tool: INDEXING.

Example syntax:
```python
 name.loc[(name['SpecificColumn']=='Name of Rows under the Column'), ['Column Names']]
```

In Indexing, we can set proper conditions on both rows and columns to extract our desired data., making it the best tool to utilize in this question.

```python
#Instruction D
d = cars.loc[(cars['Model']=='Mazda RX4 Wag') | (cars['Model']=='Ford Pantera L')| (cars['Model']=='Honda Civic'), ['Model', 'cyl', 'gear']]
d
```
Resulting Output: 
| Model          | cyl | gear |
|----------------|-----|------|
| Mazda RX4 Wag  | 6   | 4    |
| Honda Civic    | 4   | 4    |
| Ford Pantera L | 8   | 5    |

By using the or ('|') conditional operator, we can find the specific models of each car and help us narrow down the specific rows we need.

Then, proceeded by placing the produced data in a variable named 'b' then displayed the value after.

Looking at the table, we can answer the question: How many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have

ANSWERS:

-'Mazda RX4 Wag' has 6 cylinders and 4 gears

-'Ford Pantera L' has 4 cylinders and 4 gears

-'Honda Civic' has 8 cylinders and 4 gears.

```python
#End of Code
```
