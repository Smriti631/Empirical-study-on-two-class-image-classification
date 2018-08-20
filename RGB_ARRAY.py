#!/usr/bin/python
from PIL import Image
import os, sys
import glob
import numpy as np

avg=0

   
f = open('/home/smriti/Desktop/project_python/refined_programs/RGB_ARRAY.csv','w')
print >>f,"Path,Red,Green,Blue,Class"
def cal_rgb(img,flag):
        sum=0
       
      #  print img   
                
        for i in range(20):
                for j in range(20):
                        im = Image.open(img)
                        pix = im.load()

                        print >>f,img+","+str(pix[i,j][0])+","+str(pix[i,j][1])+","+str(pix[i,j][2])+","+str(flag)

    
      


path3='/home/smriti/Desktop/project_python/indoor_resized/*.jpg' 
#path4='/home/smriti/Desktop/indoor_resized/'    
files=glob.glob(path3)
for img in files: 
        cal_rgb(img,0)
        
path3='/home/smriti/Desktop/project_python/outdoor_resized/*.jpg' 
#path4='/home/smriti/Desktop/outdoor_resized/'    
files=glob.glob(path3)
for img in files: 
        cal_rgb(img,1)
