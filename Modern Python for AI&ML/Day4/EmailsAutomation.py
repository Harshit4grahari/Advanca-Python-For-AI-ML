# Automatic Birthday Wish EMail Sender

import smtplib #Module to send emails using SMTP(Simple Mail Transfer Protocol)


from email.mime.text import MIMEText #Module to create email messages with text content.
import datetime #Module to work with dates and times in Python
import time #Module to work with time-related functions in Python


sender_email = "agrahariagrahari406@gmail.com" #Sender's email address
sender_password = "zmyr eyhb cwpz somu" #Sender's email password

reciever_email = input("Enter the reciever's email address: ") #Reciever's email address
name = input("Enter the reciever's name: ") #Reciever's name
reciever_birthdate = input("Enter the reciever's birthdate (YYYY-MM-DD): ") #Reciever's birthdate in YYYY-MM-DD format

# Convert the birthdate string to a datetime object
birthdate = datetime.datetime.strptime(reciever_birthdate, "%Y-%m-%d")

# Get the current date
current_date = datetime.datetime.now()

# Calculate the age
age = current_date.year - birthdate.year

# Check if the birthday has already occurred this year
if (current_date.month, current_date.day) < (birthdate.month, birthdate.day):
    age -= 1

#Set the time to send the email (e.g., 00:01 AM)
send_hour = 20
send_minute = 45
# Loop to check Date and Time
while True:
    current_time = datetime.datetime.now()
    if (current_time.month, current_time.day) == (birthdate.month, birthdate.day) and current_time.hour == send_hour and current_time.minute == send_minute:
        break
    time.sleep(60) #Check every minute

msg = MIMEText(f"Happy Birthday {name}! Wishing you a wonderful day filled with joy and happiness.") #Email message content
msg['Subject'] = "Happy Birthday!" #Email subject line
msg['From'] = sender_email #Sender's email address
msg['To'] = reciever_email #Reciever's email address

server = smtplib.SMTP_SSL("smtp.gmail.com", 465) #Create a secure SSL connection to the Gmail SMTP server

server.login(sender_email, sender_password) #Login to the sender's email account

server.send_message(msg) #Send the email message

server.quit() #Close the connection to the SMTP server

print("Birthday wish email sent successfully!") #Print a success message