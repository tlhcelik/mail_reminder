#!/usr/bin/env python

import smtplib
class MailWriter (object):
    """for send to reminders"""
    def __init__(self):
        print("Mail Sender Class")

    def al(self, word):
        return input(self.word).strip()

    def write(self , client):

        try:
            #smtplib.SMTP('smtp.google.com', 587)

            _mail = smtplib.SMTP_SSL('smtp.google.com',587)
            _mail.sendmail('reminder@malc.com', client, "konu")

            _mail.quit()
        except Exception as e:
            print("Error Info : "+str(e))


"""
oncelik sirasi bunda 
kurulu oldugu yerde yapilacaklar dosyasinin icindekini okuyup gonderecek
    case "2 saatte bir"
    case "ayarlanabilir dakika"
    case "gun"
    case ?
"""