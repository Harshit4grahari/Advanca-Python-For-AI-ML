# Using Builtin datetime moduleget current age 

# from datetime import datetime

# # birth_year = int(input("Enter your birth year: "))
# # current_year = datetime.now().year
# # age = current_year - birth_year
# # print(f"You are {age} years old.")


# Age Calculator using datetime module

import datetime #datetime module is used to work with dates and times in Python

birth_date = datetime.date(int(input("Enter your birth year: ")), int(input("Enter your birth month: ")), int(input("Enter your birth day: ")))
current_date = datetime.date.today()
age = current_date.year - birth_date.year - (current_date.month < birth_date.month or (current_date.month == birth_date.month and current_date.day < birth_date.day))
print(f"You are {age} years old.")