# Comparison & Logical Operators

age = int(input("Enter your age: ")) # Get the user's age as an integer
if age < 18:
    print("You are a minor.") # If age is less than 18, print "You are a minor."
elif age >= 18 and age < 65:
    print("You are an adult.") # If age is between 18 and 64, print "You are an adult."
else:
    print("You are a senior.") # If age is 65 or older, print "You are a senior."

has_license = input("Do you have a driver's license? (yes/no): ").strip().lower() # Get the user's response about having a driver's license
if has_license == "yes" & age >=18:
    print("You are eligible to drive.") # If the user has a license and is 18 or older, print "You are eligible to drive."
elif has_license == "no" & age >=18:
    print("You need a driver's license to drive.") # If the user does not have a license but is 18 or older, print "You need a driver's license to drive."
