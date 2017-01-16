#!/usr/bin/env python

import smtplib
import time
import os

class MailWriter (object):
    '''
    Mail sender Class
    '''
    def __init__(self):
        print("Mail Sender Class")

    def attachment (self,file):
        path = os.path.join(file)
        if True:
            try:
                f = open(file , 'r')
                reading = f.read()
                return reading
            except Exception as e:
                print 'File IO Error Shutdown Program '
                return
            finally:
                f.close()

    def write(self , to ,file):

        '''
        :param to: Where to send mail. ex: my_mail@server.com
        :return: void
        '''
        __FILEDIR = file
        __server = 'smtp.gmail.com'
        __from = 'reminder@malc.com'
        __to = to
        __title = "Daily Reminders. Good Day Sir."
        __subject2 = self.attachment(__FILEDIR)

        try: # send to mail block

            __mail=smtplib.SMTP(__server, 587)
            #__mail = smtplib.SMTP_SSL(__server,587)
            __mail.ehlo()
            __mail.starttls()
            __mail.login('malc.reminder@gmail.com', 'karaman70')
            __mail.sendmail(__from, __to,__subject2)

        except Exception as e:
            print("Error Info : "+str(e))
        finally:
            __mail.close()
            print ("Mail Send. To %s\n" %(__to))

    def timer(self,ptime): # when sent to mail block
        '''
        :param time: Given to hour
        :return: boolean
        '''
        __time = (ptime * 60 * 60) # time convert to second

        while True:
            print ('Waiting for %d times' %(ptime))
            time.sleep(__time)
            print ('Sending Reminders ')
            return  True

        return False
"""
oncelik sirasi bunda 
kurulu oldugu yerde yapilacaklar dosyasinin icindekini okuyup gonderecek
    case "2 saatte bir"
    case "ayarlanabilir dakika"
    case "gun"
    case ?
"""