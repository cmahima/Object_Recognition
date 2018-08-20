from face import Watson
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from PIL import Image
import os
from watson_developer_cloud import VisualRecognitionV3
import random
import json
import time
#import watson_developer_cloud

if __name__ == '__main__':
   #apikey='vSyMgZWfne3r_7km1VRkIuUyw-P4uc5uwl6xf3CDxi8w'
   #apikey='HQpAO8ny5r-oiPj9e5v_-Qb6Eq75rs21uxLXeC1gr9td'
   apikey="1ZX6szY1jPm8Bw2ubxvVoq0oiFGR8gW7eVFWVwILSakp"
   version='2018-05-22'
   w=Watson(apikey,version)
   imgs=[]
   i=0

    
    #folder="home/turtle/Desktop"
while (1):
    #for filename in os.listdir("/home/turtle/images"):
     # img=random.choice(os.listdir("/home/turtle/images"))
    # for filename in os.listdir("/home/turtle/images/"):
        imgs.append(os.path.join("/home/mahima/images/frame_" + str(i)+ ".jpg"))
       
#      sleep(1)

           
        image="/home/mahima/images"+'/'+imgs[i]
      #end=time.time()
      
        res = w.classify(imgs[i])
        fromaddr = "cmahima848@gmail.com"
        toaddr = "mahimachaudhary966@gmail.com"
        msg = MIMEMultipart()
        msg['From'] = "Watson"
        msg['To'] = "Mahima"
        msg['Subject'] = "CLASSIFICATION RESULT"
        #body = resp
        msg.attach(MIMEText(res, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "7900567892")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        print(res)
 
