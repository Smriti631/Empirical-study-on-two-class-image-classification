# -*- coding: utf-8 -*-

#!/usr/bin/python
from PIL import Image
import os, sys
import glob
import numpy as np
   
   
#hue calculation... in degree
def hue_cal(Rr,Gg,Bb):
        C_max=max(Rr,Gg,Bb)
        C_min=min(Rr,Gg,Bb)

        delta=C_max-C_min
        if delta==0:
                H=0
        elif C_max==Rr:
                H=60*(((Gg-Bb)/delta)%6)
                #print H
        elif C_max==Gg:
                H=60*(((Bb-Rr)/delta)+2)
                #print H
        elif C_max==Bb:
                H=60*(((Rr-Gg)/delta)+4)
                #print H
        return H
        
#saturation calculation..
def saturation_cal(Rr,Gg,Bb):
        C_max=max(Rr,Gg,Bb)
        C_min=min(Rr,Gg,Bb)

        delta=C_max-C_min
        if C_max==0:
                S=0
        elif C_max!=0:
                S=delta/C_max
        return S

avg=0
   
f = open('/home/smriti/Desktop/project_python/refined_programs/HSV_CCT.csv','w')
print >>f,"Path,Hue,Saturation,Value,CCT,Class"
def cal_rgb(img,flag):
        sum=0
        hue_sum=0
        sat_sum=0
        val_sum=0
        H=[]
        S=[]
        V=[]
        Rr=[]
        Gg=[]
        Bb=[]

        CCT_sum=0.0
        X=0.0
        Y=0.0
        Z=0.0
        x=0.0
        y=0.0
        z=0.0
        n=0.0
        CCT=0.0
      #  print img                        
        for i in range(20):
                for j in range(20):
                        im = Image.open(img)
                        pix = im.load()
                        Rr=float(pix[i,j][0])/255.0
                        
                        
                        Gg=float(pix[i,j][1])/255.0
                        
                     
                        Bb=float(pix[i,j][2])/255.0
                       
                        H=hue_cal(Rr,Gg,Bb)
                        hue_sum=hue_sum+H
                        
                        S=saturation_cal(Rr,Gg,Bb)
                        sat_sum=sat_sum+S
                        
                        V=max(Rr,Gg,Bb)
                        val_sum=val_sum+V
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
                        CCT_sum=CCT_sum+CCT
  
        h_avg=float(hue_sum/(float(i+1)*float(j+1)))
        s_avg=float(sat_sum/(float(i+1)*float(j+1)))
        v_avg=float(val_sum/(float(i+1)*float(j+1)))
        
        cct_avg=float(CCT_sum/(float(i+1)*float(j+1)))
       # print cct_avg
        #sum=sum+1
      
     #   print img+","+str(r_avg)+","+str(g_avg)+","+str(b_avg)+","+str(flag)
        print >>f,img+","+str(h_avg)+","+str(s_avg)+","+str(v_avg)+","+str(cct_avg)+","+str(flag)
       # print sum
    #print('Filename:', filename, file=f) 
    
     #   with open('/home/smriti/Desktop/out.txt', 'w'):
                   
print sum        

path3='/home/smriti/Desktop/project_python/indoor_resized/*.jpg' 
files=glob.glob(path3)
for img in files: 
        cal_rgb(img,0)
        
path3='/home/smriti/Desktop/project_python/outdoor_resized/*.jpg' 
files=glob.glob(path3)
for img in files: 
        cal_rgb(img,1)

                               

           
                
                
                
                
                
                
                
                
                
