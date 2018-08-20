# -*- coding: utf-8 -*-

#!/usr/bin/python
from PIL import Image
import os, sys
import glob
import numpy as np
   
avg=0
   
f = open('/home/smriti/Desktop/project_python/refined_programs/RGB_CCT_ARRAY.csv','w')
print >>f,"Path,Red,Green,Blue,CCT,Class"
def cal_rgb(img,flag):
        sum=0
        r=[]
        g=[]
        b=[]
        CCT_sum=0.0
        X=0.0
        Y=0.0
        Z=0.0
        x=0.0
        y=0.0
        z=0.0
        n=0.0
        CCT=[]
      #  print img                        
        for i in range(20):
                for j in range(20):
                        im = Image.open(img)
                        pix = im.load()
                    #    print(str(sum)+"R"+str(r_sum)+"="+str(r_sum)+"+"+str(pix[i,j][0])+"="+str(r_sum+pix[i,j][0]))


                     #   print(str(sum)+"G"+str(g_sum)+"="+str(g_sum)+"+"+str(pix[i,j][1])+"="+str(g_sum+pix[i,j][1]))
                     #   print(str(sum)+"B"+str(b_sum)+"="+str(b_sum)+"+"+str(pix[i,j][2])+"="+str(b_sum+pix[i,j][2]))
                        r=pix[i,j][0]
                                           
                        g=pix[i,j][1]
                       
                        
                        b=pix[i,j][2]
                     #Convert the RGB values to CIE tristimulus values (XYZ) as follows:


                        X=(-0.14282)*pix[i,j][0]+(1.54924)*pix[i,j][1]+(-0.95641)*pix[i,j][2]

                        Y=(-0.32466)*pix[i,j][0]+(1.57837)*pix[i,j][1]+(-0.73191)*pix[i,j][2] #=Illuminance

                        Z=(-0.68202)*pix[i,j][0]+(0.77073)*pix[i,j][1]+(0.56332)*pix[i,j][2]
                       # Calculate the normalized chromaticity values:

                        try:
                                x=X/(X+Y+Z)
                                y=Y/(X+Y+Z)
                                n=(((0.23881)*pix[i,j][0])+((0.25499)*pix[i,j][1])+((-0.58291)*pix[i,j][2]))/(((0.11109)*pix[i,j][0])+((-0.85406)*pix[i,j][1])+((0.52289)*pix[i,j][2]))
                        except ZeroDivisionError as error:
                                x=0
                                n=0
                        CCT=449*(n**3)+3525*(n**2)+6823.3*n+5520.33
                        
                       
       
                        print >>f,img+","+str(r)+","+str(g)+","+str(b)+","+str(CCT)+","+str(flag)
 
                   
print sum        

path3='/home/smriti/Desktop/project_python/indoor_resized/*.jpg' 
files=glob.glob(path3)
for img in files: 
        cal_rgb(img,0)
        
path3='/home/smriti/Desktop/project_python/outdoor_resized/*.jpg' 
files=glob.glob(path3)
for img in files: 
        cal_rgb(img,1)

                               

           
                
                
                
                
                
                
                
                
