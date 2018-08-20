
#!/usr/bin/python
from PIL import Image
import os, sys
import glob
import numpy as np
from sklearn import preprocessing,cross_validation,neighbors
import pandas as pd


#knn classifier....
df=pd.read_csv('/home/smriti/Desktop/project_python/refined_programs/RGB_CCT.data.txt')
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

 
f = open('/home/smriti/Desktop/project_python/refined_programs/RGB_CCT_pred.csv','w')
print >>f,"Path,Prediction,Class"

def cal_rgb(img,flag):
        sum=0
        r_sum=0
        g_sum=0
        b_sum=0
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
                    #    print(str(sum)+"R"+str(r_sum)+"="+str(r_sum)+"+"+str(pix[i,j][0])+"="+str(r_sum+pix[i,j][0]))


                     #   print(str(sum)+"G"+str(g_sum)+"="+str(g_sum)+"+"+str(pix[i,j][1])+"="+str(g_sum+pix[i,j][1]))
                     #   print(str(sum)+"B"+str(b_sum)+"="+str(b_sum)+"+"+str(pix[i,j][2])+"="+str(b_sum+pix[i,j][2]))
                        r_sum=r_sum+pix[i,j][0]
                                               
                        g_sum=g_sum+pix[i,j][1]
                       
                        
                        b_sum=b_sum+pix[i,j][2]
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
                       
        r_avg=float(r_sum/(float(i+1)*float(j+1)))
        g_avg=float(g_sum/(float(i+1)*float(j+1)))
        b_avg=float(b_sum/(float(i+1)*float(j+1)))
        cct_avg=float(CCT_sum/(float(i+1)*float(j+1)))

        
      
     #  print img+","+str(r_avg)+","+str(g_avg)+","+str(b_avg)+","+str(flag)
      # print str(r_avg)+","+str(g_avg)+","+str(b_avg)+","+str(h_avg)+","+str(s_avg)+","+str(v_avg)
        example_measures=np.array([r_avg,g_avg,b_avg,cct_avg])
        example_measures=example_measures.reshape(1,-2)
        prediction=clf.predict(example_measures)
        print >>f,img+","+str(prediction)+","+str(flag)
           
        return prediction
       # print(prediction) 
    #   print sum'''
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


         
                
                
                
                
                
                
                
                
