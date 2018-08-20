
#!/usr/bin/python
from PIL import Image
import os, sys
import glob
import numpy as np
from sklearn import preprocessing,cross_validation,neighbors
import pandas as pd


#knn classifier....
df=pd.read_csv('/home/smriti/Desktop/6th_Semester/project_python/refined_programs/Final/RGB_HSV.data.txt')
df.replace('?', -9999, inplace=True)
df.drop(['Path'],1,inplace=True)

X = np.array(df.drop(['Class'],1))
y = np.array(df['Class'])

X_train, X_test, y_train, y_test=cross_validation.train_test_split(X,y,test_size=0.2)
clf=neighbors.KNeighborsClassifier()
clf.fit(X_train,y_train)
 
accuracy=clf.score(X_test,y_test)
print(accuracy)

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

 
f = open('/home/smriti/Desktop/6th_Semester/project_python/refined_programs/Final/RGB_HSV_predict.csv','w')
print >>f,"Path,Red,Green,Blue,Hue,Saturation,Value,Prediction,Class"

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
                        #print(str(r_sum)+"="+str(r_sum)+"+"+str(pix[i,j][0])+"="+str(r_sum+pix[i,j][0]))
                        #print(str(g_sum)+"="+str(g_sum)+"+"+str(pix[i,j][1])+"="+str(g_sum+pix[i,j][1]))
                        #print(str(b_sum)+"="+str(b_sum)+"+"+str(pix[i,j][2])+"="+str(b_sum+pix[i,j][2]))
                        r_sum=r_sum+pix[i,j][0]
                        Rr=float(pix[i,j][0])/255.0
                        
                        g_sum=g_sum+pix[i,j][1]
                        Gg=float(pix[i,j][1])/255.0
                        
                        b_sum=b_sum+pix[i,j][2]
                        Bb=float(pix[i,j][2])/255.0
                       
                        H=hue_cal(Rr,Gg,Bb)
                        hue_sum=hue_sum+H
                        
                        S=saturation_cal(Rr,Gg,Bb)
                        sat_sum=sat_sum+S
                        
                        V=max(Rr,Gg,Bb)
                        val_sum=val_sum+V
                         
                    
                  #      print(str(sum)+"R ="+str(pix[i,j][0]))
                   #     print(str(sum)+"G ="+str(pix[i,j][1]))
                   #     print(str(sum)+"B ="+str(pix[i,j][2]))
 
                   #     print(str(sum)+"H ="+str(H))
                   #     print(str(sum)+"S ="+str(S))
                   #     print(str(sum)+"V ="+str(V))
                    #    sum=sum+1
       # print sum                
        r_avg=float(r_sum/(float(i+1)*float(j+1)))
        g_avg=float(g_sum/(float(i+1)*float(j+1)))
        b_avg=float(b_sum/(float(i+1)*float(j+1)))
        h_avg=float(hue_sum/(float(i+1)*float(j+1)))
        s_avg=float(sat_sum/(float(i+1)*float(j+1)))
        v_avg=float(val_sum/(float(i+1)*float(j+1)))
        
      
     #  print img+","+str(r_avg)+","+str(g_avg)+","+str(b_avg)+","+str(flag)
      # print str(r_avg)+","+str(g_avg)+","+str(b_avg)+","+str(h_avg)+","+str(s_avg)+","+str(v_avg)
        example_measures=np.array([r_avg,g_avg,b_avg,h_avg,s_avg,v_avg])
        example_measures=example_measures.reshape(1,-2)
        prediction=clf.predict(example_measures)
        print >>f,img+","+str(r_avg)+","+str(g_avg)+","+str(b_avg)+","+str(h_avg)+","+str(s_avg)+","+str(v_avg)+","+str(prediction).strip('[').strip(']')+","+str(flag)
           
        return prediction
       # print(prediction) 
    #   print sum'''
    #print('Filename:', filename, file=f) 
    
     #   with open('/home/smriti/Desktop/out.txt', 'w'):

        
pred_zero=0
pred_one=0
zero=0
one=0
path3='/home/smriti/Desktop/6th_Semester/project_python/indoor_resized_test/*.jpg' 
#path4='/home/smriti/Desktop/indoor_resized/'    
files=glob.glob(path3)
for img in files: 
        pred_zero=cal_rgb(img,0)
        if(pred_zero==0):
                zero=zero+1
        
        
path3='/home/smriti/Desktop/6th_Semester/project_python/outdoor_resized_test/*.jpg' 
#path4='/home/smriti/Desktop/outdoor_resized/'    
files=glob.glob(path3)
for img in files: 
        pred_one=cal_rgb(img,1)
        if(pred_one==1):
                one=one+1

print "indoor :"+str(zero)+"/90"+", outdoor :"+str(one)+"/90"                               


         
                
                
                
                
                
                
                
                
