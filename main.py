#!/usr/bin/env python

from write_mail import  MailWriter
import  sys


write = MailWriter()


'''
Given sys.arg[1] = 2
'''

while True:
    my_timer=write.timer(int(sys.argv[1]))
    # int(sys.argv[1] = given the console parameter equals string or float. int() conver to interger)
    if (my_timer):
        write.write(sys.argv[2] , sys.argv[3])
        # sys.argv[2] => who send mail to
        # sys.argv[3] => sending file
