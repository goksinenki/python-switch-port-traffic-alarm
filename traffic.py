#!/usr/bin/python
# -*- coding: UTF-8 -*-
# A script to ssh into a cisco device, set the terminal length
# such that paging is turned off, then run commands.
# the results go into 'resp', then are displayed.
# Tweak to your hearts content!

import paramiko
import cmd
import time
import sys
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
import traceback


#buff = ''
#resp = ''

## our uplink port is Eth1/42 here that we need to check the bandwidth

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
IP = "switchipaddress"
hostname = "switchhostname"
hostname = str(hostname)
file = open('outputfile.txt', 'w')
list = []
try:
    ssh.connect(IP, username='burayasshusernameyazilacak', password='burayasifreyazilacak')
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                # komutcalistir!
    stdin, stdout, stderr = ssh.exec_command('sh int Eth1/42 | i 30')
    list = stdout.readlines()
    output = [line.rstrip() for line in list] 
    #print ('\n'.join(output))
    IP = str(IP)
    file.write('\n'.join(output))
    file.close()
    myfile2 = open("outputfile.txt", "r")
    mylist = myfile2.readlines(1)
    gelentrafik = mylist[1]
    sub1 = "rate"
    sub2 = "bits"
    idx1 = gelentrafik.index(sub1)
    idx2 = gelentrafik.index(sub2)
    gelen = gelentrafik[idx1 + len(sub1) + 1: idx2]
    #print (gelen)
    gelenmegabit = int(gelen)
    gidentrafik = mylist[2]
    sub1 = "rate"
    sub2 = "bits"
    idx1 = gidentrafik.index(sub1)
    idx2 = gidentrafik.index(sub2)
    giden = gidentrafik[idx1 + len(sub1) + 1: idx2]
    #print (giden)
    gidenmegabit = int(giden)
    if gelenmegabit > 1500000000 or gidenmegabit > 1500000000:
        #print ("Alarm")
        fromaddr = "sendermailadress"
        toaddr = "receivermailadress"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Esenyurt Uplink 1.5 Gbps üzeri TRAFİK KULLANIM ALARM!"
        server = smtplib.SMTP('smtpserver', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("mailusername", "mailpassword")
        body = "%s + Saldırı var mı kontrol edin ! + input:%s bits/sec, output:%s bits/sec"%(hostname,gelen,giden)
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
    myfile2.close()
        ###except Exception:
        ###    traceback.print_exc()
        ###    #print('%s, "Error"\n'%(IP))
except paramiko.AuthenticationException:
    file.write('%s, "Authentication Failed"\n'%(IP))
    file.close() 
except paramiko.SSHException as sshException:
    file.write('%s, "Unable to establish SSH connection"\n'%(IP))
    file.close() 
except paramiko.ssh_exception.NoValidConnectionsError as novalidconnection:
    file.write('%s, "Unable to connect Port 22"\n'%(IP))
    file.close() 
except Exception:
    print('%s, "Error"\n'%(IP))
    pass


ssh.close()
