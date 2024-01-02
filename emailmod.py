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
import schedule
def email():
    """Now we will set the email and pass and provide location of our attachment and logo"""
    mymail="enter your email"
    mypass="enter app pass"
    filename=r"enter path to file "
    logo=r"enter path to logo"

    """initializing the mime multipart object and giving the necc inputs"""


    msg=MIMEMultipart()  
    """lets add date and time to subject first"""
    day=date.today()
    time=datetime.now()
    cday=day.strftime("%B %d %Y")
    ctime=time.strftime("%I:%M:%S %p")
    msg['Subject']=f"SMTP SERVER TEST {cday} {ctime}"
    msg['From']=mymail
    msg['To']="enter recipient address"
    msg['Cc']="enter address of others"
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
    exit()
    #now we will schedule the code to run at 12:00 PM every day
schedule.every().day.at("12:00").do(email)
#control goes straight to while loop.
while True:                     #this is an infinite loop that checks for tasks waiting to be completed.
    schedule.run_pending()
    t.sleep(1)                    #this makes sures the script doesnt consume cpu resources too much and checks after 1 second delay.



###we can also schedule cron job to fulfill our scheduling purpose and batch file in windows.
###need to install schedule lib by <python3 install schedule > first
