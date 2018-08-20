
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
              #  print H
        elif C_max==Gg:
                H=60*(((Bb-Rr)/delta)+2)
               # print H
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

   
f = open('/home/smriti/Desktop/project_python/refined_programs/HSV_ARRAY.csv','w')
print >>f,"Path,Hue,Saturation,Value,Class"
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
        
      #  print img                        
        for i in range(20):
                for j in range(20):
                        im = Image.open(img)
                        pix = im.load()
                    #    print(str(sum)+"R"+str(r_sum)+"="+str(r_sum)+"+"+str(pix[i,j][0])+"="+str(r_sum+pix[i,j][0]))
                     #   print(str(sum)+"G"+str(g_sum)+"="+str(g_sum)+"+"+str(pix[i,j][1])+"="+str(g_sum+pix[i,j][1]))
                     #   print(str(sum)+"B"+str(b_sum)+"="+str(b_sum)+"+"+str(pix[i,j][2])+"="+str(b_sum+pix[i,j][2]))
                        
                        Rr=float(pix[i,j][0])/255.0
                        
                     
                        Gg=float(pix[i,j][1])/255.0
                   
                        Bb=float(pix[i,j][2])/255.0
                       
                        H=hue_cal(Rr,Gg,Bb)
                        hue_sum=hue_sum+H
                        
                        S=saturation_cal(Rr,Gg,Bb)
                        sat_sum=sat_sum+S
                        
                        V=max(Rr,Gg,Bb)
                        val_sum=val_sum+V
                        print >>f,img+","+str(H)+","+str(S)+","+str(V)+","+str(flag)
        
      
     #   print img+","+str(r_avg)+","+str(g_avg)+","+str(b_avg)+","+str(flag)
        
       # print sum
    #print('Filename:', filename, file=f) 
    
     #   with open('/home/smriti/Desktop/out.txt', 'w'):
                   
        

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

                               

           
                
                
                
                
                
                
                
                
