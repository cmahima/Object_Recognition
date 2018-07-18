from watson import Watson
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from PIL import Image
import os
from watson_developer_cloud import VisualRecognitionV3
import random
import json

if __name__ == '__main__':
   apikey=''
   version='2018-05-23'
   w=Watson(apikey,version)
   for filename in os.listdir("/home/mahima/images"):
        #numberoffiles=len(folder)
        img = random.choice(os.listdir("/home/mahima/images"))
        image="/home/mahima/images"+'/'+img      
        res = w.classify(image)
        #resp=str(res)
        #resp=json.dumps(res)
        #print("hi"+resp)
        print(res)
        #os.remove(image)
        #sending response as an email
        fromaddr = ""
        toaddr = ""
        msg = MIMEMultipart()
        msg['From'] = "Watson"
        msg['To'] = "Mahima"
        msg['Subject'] = "CLASSIFICATION RESULT"
        #body = resp
        msg.attach(MIMEText(res, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
 
 
