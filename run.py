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
from light import LED
#import watson_developer_cloud
threshold=0.6
if __name__ == '__main__':
   apikey=''
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
        fromaddr = ""
        toaddr = ""
        msg = MIMEMultipart()
        msg['From'] = "Watson"
        msg['To'] = "Mahima"
        msg['Subject'] = "WATSON CLASSIFICATION RESULT"
        #body = resp
        msg.attach(MIMEText(res, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        print(res)
        i+=1
        l=LED()
        LED.lit(l,threshold)
