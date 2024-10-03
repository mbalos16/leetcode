'''
1853. Convert Date Format
Solved
Easy
Topics
SQL Schema
Pandas Schema

Table: Days

+-------------+------+
| Column Name | Type |
+-------------+------+
| day         | date |
+-------------+------+
day is the column with unique values for this table.

 

Write a solution to convert each date in Days into a string formatted as "day_name, month_name day, year".

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Days table:
+------------+
| day        |
+------------+
| 2022-04-12 |
| 2021-08-09 |
| 2020-06-26 |
+------------+
Output: 
+-------------------------+
| day                     |
+-------------------------+
| Tuesday, April 12, 2022 |
| Monday, August 9, 2021  |
| Friday, June 26, 2020   |
+-------------------------+
Explanation: Please note that the output is case-sensitive.


'''

import pandas as pd
import datetime as dt

def convert_date_format(days: pd.DataFrame) -> pd.DataFrame:
     # Convert the column 'day' to the desired format where:
        # %A = day of the week in format "Monday"
        # %B = month in format "January"
        # %-d = day of the month in format "1", 
                #the - in front of the "d" gets rid of the zero-leading
        # %Y = year in format "2024"
    days["day"] = days["day"].dt.strftime('%A, %B %-d, %Y')
    return days