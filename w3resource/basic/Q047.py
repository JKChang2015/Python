# -*- coding: UTF-8 -*-
# Q047
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: CPUs
# Description: Write a Python program to find out the number of CPUs using. 
import multiprocessing
import os
#
print multiprocessing.cpu_count()
print os.uname()

# import socket
# import os
# import sys
# import platform
# import psutil
# import uuid
#
# print  "Name: " +socket.gethostname()
# print "FQDN: " +socket.getfqdn()
# print "System Platform: "+sys.platform
# print "Machine: " +platform.machine()
# print "Node " +platform.node()
# print "Platform: "+platform.platform()
# print "Processor: " +platform.processor()
# print "System OS: "+platform.system()
# print "Release: " +platform.release()
# print "Version: " +platform.version()
# print "Number of CPUs: " +str(psutil.cpu_count())
# print "Number of Physical CPUs: " +str(psutil.cpu_count(logical=False))