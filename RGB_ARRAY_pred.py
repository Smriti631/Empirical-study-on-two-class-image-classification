
#!/usr/bin/python
from PIL import Image
import os, sys
import glob
import numpy as np
from sklearn import preprocessing,cross_validation,neighbors
import pandas as pd
import colorsys

#knn classifier....
df=pd.read_csv('/home/smriti/Desktop/project_python/refined_programs/RGB_ARRAY.data.txt')
df.replace('?', -9999, inplace=True)
df.drop(['Path'],1,inplace=True)

X = np.array(df.drop(['Class'],1))
y = np.array(df['Class'])

X_train, X_test, y_train, y_test=cross_validation.train_test_split(X,y,test_size=0.2)
clf=neighbors.KNeighborsClassifier()
clf.fit(X_train,y_train)
 
accuracy=clf.score(X_test,y_test)
print(accuracy)
avg=0

   
f = open('/home/smriti/Desktop/project_python/refined_programs/RGB_ARRAY_pred.csv','w')
print >>f,"Path,Prediction,flag"
def cal_rgb(img,flag):
        sum=0
        r=[]
        g=[]
        b=[]
      #  print img   
                
        for i in range(20):
                for j in range(20):
                        im = Image.open(img)
                        pix = im.load()
                    #    print(str(sum)+"R"+str(r_sum)+"="+str(r_sum)+"+"+str(pix[i,j][0])+"="+str(r_sum+pix[i,j][0]))
                     #   print(str(sum)+"G"+str(g_sum)+"="+str(g_sum)+"+"+str(pix[i,j][1])+"="+str(g_sum+pix[i,j][1]))
                     #   print(str(sum)+"B"+str(b_sum)+"="+str(b_sum)+"+"+str(pix[i,j][2])+"="+str(b_sum+pix[i,j][2]))
                       # V=np.array([[pix[i,j][0], pix[i,j][1],pix[i,j][2]],[0,1, 0],[0,0,1]])
                     #   print >>f,img+","+str(pix[i,j][0])+","+str(pix[i,j][1])+","+str(pix[i,j][2])+","+str(flag)
                        r=pix[i,j][0]
                        g=pix[i,j][1]
                        b=pix[i,j][2]
    
        example_measures=np.array([r,g,b])
        example_measures=example_measures.reshape(1,-2)
        prediction=clf.predict(example_measures)
        print >>f,img+","+str(prediction)+","+str(flag)
        return prediction
     #   print img+","+str(r_avg)+","+str(g_avg)+","+str(b_avg)+","+str(flag)
        
       # print sum
    #print('Filename:', filename, file=f) 
    
     #   with open('/home/smriti/Desktop/out.txt', 'w'):
     
pred_zero=0
pred_one=0
zero=0
one=0
path3='/home/smriti/Desktop/project_python/indoor_resized_test/*.jpg' 
#path4='/home/smriti/Desktop/indoor_resized/'    
files=glob.glob(path3)
for img in files: 
        pred_zero=cal_rgb(img,0)
        if(pred_zero==0):
                zero=zero+1
        
        
path3='/home/smriti/Desktop/project_python/outdoor_resized_test/*.jpg' 
#path4='/home/smriti/Desktop/outdoor_resized/'    
files=glob.glob(path3)
for img in files: 
        pred_one=cal_rgb(img,1)
        if(pred_one==1):
                one=one+1
print "indoor :"+str(zero)+"/90"+", outdoor :"+str(one)+"/90" 
