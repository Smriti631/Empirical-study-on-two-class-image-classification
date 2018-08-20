
#!/usr/bin/python
from PIL import Image
import os, sys
import glob
import numpy as np

avg=0

   
f = open('/home/smriti/Desktop/project_python/refined_programs/ONLY_RGB.csv','w')
print >>f,"Path,Red,Green,Blue,Class"
def cal_rgb(img,flag):
        sum=0
        r_sum=0
        g_sum=0
        b_sum=0
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
                        r_sum=r_sum+pix[i,j][0]
                                               
                        g_sum=g_sum+pix[i,j][1]
                       
                        
                        b_sum=b_sum+pix[i,j][2]
                     
 
        r_avg=float(r_sum/(float(i+1)*float(j+1)))
        g_avg=float(g_sum/(float(i+1)*float(j+1)))
        b_avg=float(b_sum/(float(i+1)*float(j+1)))

        
      
     #   print img+","+str(r_avg)+","+str(g_avg)+","+str(b_avg)+","+str(flag)
        print >>f,img+","+str(r_avg)+","+str(g_avg)+","+str(b_avg)+","+str(flag)
       # print sum
    #print('Filename:', filename, file=f) 
    
     #   with open('/home/smriti/Desktop/out.txt', 'w'):
                   
        

path3='/home/smriti/Desktop/project_python/indoor_resized/*.jpg' 
files=glob.glob(path3)
for img in files: 
        cal_rgb(img,0)
        
path3='/home/smriti/Desktop/project_python/outdoor_resized/*.jpg' 
files=glob.glob(path3)
for img in files: 
        cal_rgb(img,1)

                               

           
                
                
                
                
                
                
                
                
