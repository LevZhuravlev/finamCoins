from django.test import TestCase

# Create your tests here.

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart()

def sendMail(to_email, message):
    try:
        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        from_email = 'fimcoinofficial@gmail.com'
        password = 'fimcoinofficial4life'
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
    except:
        pass
#
# import requests
import datetime
# from bs4 import BeautifulSoup
#
d1 = datetime.datetime.today()
# print(d1)
#
# d1 = d1 + datetime.timedelta(days=1)
# print(d1)
#
#
# URL = 'https://www.finam.ru/quote/moex-akcii/aeroflot/'
# HEADERS = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'}
#
# response = requests.get(URL, headers=HEADERS)
# soup = BeautifulSoup(response.content, 'html.parser')
# item = soup.findAll('span', class_ = 'PriceInformation__price--26G')
# comps=[]
#
# for i in item:
#     print(int(i.get_text().rpartition(',')[0]))
#
#
# print("hello world")