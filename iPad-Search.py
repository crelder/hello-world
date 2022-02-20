### Dedicated to Daniel ###
# -*- coding: utf-8 -*-
import urllib
import smtplib

######## Read website
sock = urllib.urlopen("http://www.apple.com/de/shop/browse/home/specialdeals/ipad/ipad_air_2/")
htmlSource = sock.read()
sock.close()

########## Search website
iPad128 = htmlSource.find("Generalüberholtes iPad Air 2 Wi-Fi 128 GB – Silber”)

########## Send notification e-mail
def send_email():
    message128 = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: iPad 128GB available!

E-Mail Body.
“""
    smtpObj = smtplib.SMTP('mx.freenet.de:587')
    smtpObj.starttls()
    smtpObj.login('***@freenet.de’,’************')
    smtpObj.sendmail('***@freenet.de','***@freenet.de',message128)
    smtpObj.close()

if iPad128 != -1 :
    send_email()
