# Lucky Number Fortune
# This program generates a lucky number and provides a fortune based on that number.

name = input("Enter your name: ")
day = int(input("Enter your birth day (1-31): "))

lucky_number = ord(name[0]) + ord(name[-1]) % 100 + day

print(f"Hello {name}, your lucky number is: {lucky_number}")