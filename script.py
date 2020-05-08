from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import smtplib
import time
count=1
from twilio.rest import Client

url="https://www.gtu.ac.in/result.aspx"
while True:
    try:
        page = urlopen(url)
    except:
        print("Error opening the URL")
    soup = BeautifulSoup(page, 'html.parser')

    content=soup.findAll('h3', {"class": "Content"})
    #print(type(content))
    str="Result of BE SEM 7 - Regular (DEC 2019) Exam Notification".lower()
    flag=False
    for i in content:
        if str in i.text.lower():
            flag=True
            break
    if flag==True:
        print("Sending........")
        s = smtplib.SMTP('smtp.gmail.com', 587) 
  
        # start TLS for security 
        s.starttls() 
        
        # Authentication .YOU HAVE TO SET GOOGLE SECURITY TO LOW TO USE SMTP
        s.login("ENTER YOU EMAIL", "ENTER PASSWORD HERE")  
        
        # message to be sent 
        message = "------------------------Result of BE sem 5 OUT-------------------- \n\n\n\n\n\n\n -------------EMAIL THROUGH PYTHON SCRIPT--------------------"
        
        # sending the mail 
        """s.sendmail("parthshethwala2000@gmail.com", [Enter Email Addresses Here], message)"""
        
        # terminating the session 
        s.quit()
        client=Client('','') # YOU HAVE TO SET ACCESS TOKEN PROVIDED BY TWILO
        from_whatsapp_number='whatsapp:+141--------' # Enter Twilo Number
        to_whatsapp_number='whatsapp:+91----------'  # Enter Whatsapp_number Whom you want to send	

        client.messages.create(body='Hello',
                                from_=from_whatsapp_number,
                                to=to_whatsapp_number)
        break
    #print(count)
    #count=count+1

