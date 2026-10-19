# Password Stength Checker

while True:
    password = input("Enter Your Password: ")

    length = len(password) >= 8
    upper = any(char.isupper() for char in password)
    digit = any(char.isdigit() for char in password)
    special = any(char in "@!#$%^&*?/" for char in password)

    if length and upper and digit and special:
        print("Strong Password")
        break
    elif length and (upper or digit or special):
        print("Moderate Password")
    else:
        print("Weak Password")
    
