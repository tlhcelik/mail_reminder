#!/usr/bin/env python

import smtplib
import time

class MailWriter (object):
    '''
    Mail sender Class
    '''
    def __init__(self):
        print("Mail Sender Class")

    def write(self , to):

        '''
        :param to: Where to send mail. ex: my_mail@server.com
        :return: void
        '''

        __server = 'smtp.gmail.com'
        __from = 'reminder@malc.com'
        __to = to
        __subject = "SUBJECT"

        try:
            __mail=smtplib.SMTP(__server, 587)

            #__mail = smtplib.SMTP_SSL(__server,587)
            __mail.ehlo()
            __mail.starttls()
            __mail.login('malc.reminder@gmail.com', 'karaman70')
            __mail.sendmail(__from, __to, __subject)

        except Exception as e:
            print("Error Info : "+str(e))
        finally:
            __mail.close()
            print ("Mail Send. To %s\n" %(__to))

    def timer(self, to, time):
        '''
        :param to: mail from to send
        :param time: Given to hour type
        :return: void
        '''

        print (to)
        print (time)
        self.write(to)





"""
oncelik sirasi bunda 
kurulu oldugu yerde yapilacaklar dosyasinin icindekini okuyup gonderecek
    case "2 saatte bir"
    case "ayarlanabilir dakika"
    case "gun"
    case ?
"""