#!/usr/bin/env python

import imaplib

class MailReader(object):
	"""for read to last inbox mail"""
	def __init__(self):
		print ("Coded by M41C\nMail Reader Class")

	def read(self):
		
		mail = imaplib.IMAP4_SSL('imap.gmail.com' , 993)
		
		try:
			mail.login('malc.reminder@gmail.com' , 'karaman70')
			count = [3]
			data = None
			datan = None

			typ, self.count = mail.select('Inbox')
			typ, self.data =mail.fetch(count[0], '(UID BODY[TEXT])')
			typ, datan = mail.search(None, 'ALL')

			for num in datan[0].split():
				typ, datan = mail.fetch(num , '(RFC822)')
				print('message %s \n %s\n' %(num , datan[0][1]))

			return self.data


		except Exception as e	:
			print("Error Try Again Later.\nInfo : " +str(e))
			return

		finally:
			mail.close()
			mail.logout()
"""ekrana mail ile ilgili herseyi basiyor 
	bana sadece subject ve icerik lazim

Amaci programa commands lar gonderilecek ona gore write_mail ayarlarini degistirecek
case ler write_mailde yazili

"""