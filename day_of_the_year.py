'''
1154. Day of the Year
Solved
Easy
Topics
Companies
Hint

Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

 
Example 1:
Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.

Example 2:
Input: date = "2019-02-10"
Output: 41


Constraints:
    date.length == 10
    date[4] == date[7] == '-', and all other date[i]'s are digits
    date represents a calendar date between Jan 1st, 1900 and Dec 31th, 2019.


'''

# Dictionary with the month as a number and the number of days in it as a value
month_days = { 
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}

class Solution:
    def dayOfYear(self, date: str) -> int:
        count = 0
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:])

        # Check if the year is leap
        leap = False
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    leap = True
                else:
                    leap = False
            else:
                leap = True

        # Calculate the days for each month
        days_count = 0
        if month != 1:
            for i in range(1,month):
                days_count += month_days[i]
                if leap and i == 2:
                    days_count += 1
        

        return days_count + day