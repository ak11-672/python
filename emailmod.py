""" First we will import all necessary modules"""
import smtplib
from email.mime.multipart import MIMEMultipart
"""email package containe mime submodule and multipart is submodule of mime and MIMEMultipart is a class in it"""
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.image import MIMEImage
from datetime import *
import time as t

"""Now we will set the email and pass and provide location of our attachment and logo"""

mymail="khanaseef972.0@gmail.com"
mypass="fqur vhlu kxop ppdb"
filename=r"/hdd1/python/medprac.py"
logo=r"/hdd1/python/PA/alnafi-220930-222108.jpg"

"""initializing the mime multipart object and giving the necc inputs"""


msg=MIMEMultipart()  
"""lets add date and time to subject first"""
day=date.today()
time=datetime.now()
cday=day.strftime("%B %d %Y")
ctime=time.strftime("%I:%M:%S %p")
msg['Subject']=f"SMTP SERVER TEST {cday} {ctime}"
msg['From']=mymail
msg['To']="khanaseef97@gmail.com"
msg['Cc']="abdullahmotors70@gmail.com"
"""Now add the text part of the email here,if dont need to send logo add </p></html> after via python."""

body="""
<html><p> <b> Hi Team,<br> This is testing email server via python script. <b> <br> <img src="cid:alogo" width="200" height="100"></p> </html>
"""
msg.attach(MIMEText(body,'html'))

"""Let's attach our file to the email"""
attachment=open(filename,'rb')
part= MIMEBase('application','octet stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment;filename=%s" % filename)
msg.attach(part)

"""Adding the logo"""
filelogo=open(logo,'rb')
msgimage=MIMEImage(filelogo.read())
filelogo.close()
msgimage.add_header('Content-ID','<alogo>')
msg.attach(msgimage)

"""Conn to stmp server and establishing the conn"""
connection=smtplib.SMTP('smtp.gmail.com')
connection.starttls()
connection.login(user=mymail,password=mypass)
connection.send_message(msg)
connection.close()
print('Mail sent')





