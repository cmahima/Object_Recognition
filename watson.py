import json
from watson_developer_cloud import VisualRecognitionV3
import time

class Watson:
 def __init__(self,apikey,version):
        self.apikey=apikey
        self.version=version

 def classify(self,image_path):
   visual_recognition = VisualRecognitionV3(
   self.version,
   iam_api_key=self.apikey)
   #start = time.time()

   with open(image_path, 'rb') as images_file:
    start=time.time()
    classes = visual_recognition.classify(
        images_file,
        threshold='0.6',
        classifier_ids="")
    end = time.time()
    print (end-start)
    return(json.dumps(classes, indent=2))
