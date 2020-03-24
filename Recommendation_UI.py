# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 15:09:49 2017

@author: admin
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import euclidean_distances
#from sklearn.metrics.pairwise import cosine_similarity        
#--------------------------code part 2---------------------(using unique hotels)

#The data set is stored in datau after creating primary key by concatenating location with hotel name in unique hotel csv file

path= "C:/Users/admin/Documents/Python Scripts/unique_hotel.csv"
datau = pd.read_csv(path,encoding='latin')
data2= (datau.pivot_table(index='username', columns='uniquehotel', values='rating').fillna(0))  #creating utility matrix using unique username as rows and unique hotel name as column with values of the cell as rating
original=data2
data2.shape                                        #shape is 1098X12850
#dist = cosine_similarity(data2)
dist2 = 1-euclidean_distances(data2)               #using euclidean distance for similarity
distn = MinMaxScaler().fit(dist2).transform(dist2) #normalizing the similarity between o to 1
data3=np.zeros((1098,12850),dtype=float)           # creating an empty matrix to store 
data2['mean']=np.sum(data2, axis=1)
rows    = (data2 != 0).sum(1)
data2['mean']=data2['mean']/rows                 #Storing row mean in the last column of data2
data2=np.array(data2)                            #converting data2 to numpy array
np.savetxt("C:/Users/admin/Documents/Python Scripts/change/original.csv", original, delimiter=",") #write the file to later use it for SVD calculation in R

#scarpping the data using the code written in a separate file attached here

#contributor level is converted in range from 0.1 to 0.7 and added to the last column of data2
#the scrapped average rating of hotel is stored in the last row of data2
#the final file is renamed as data2n

#now scraped average and contributor included
path= "C:/Users/admin/Documents/Python Scripts/change/data2n.csv" #data2n is the final data with contributor numerric value and 
data4 = pd.read_csv(path,header=None)
data4=np.array(data4)
data6=np.zeros((1098,12850),dtype=float) #creating an empty matrix to store
i=0
j=0
k=0                                     
for i in range(1098):           #for loop triple nested to calculate final rating after adding final bias
    for j in range (12850):
        if (data4[i,j]!=0):     
            data6[i,j]=data4[i,j]   #if rating is present then paste it as it is else do the calculations
        else:
            bias=0
            n=0
            for k in range(1098):       
                if (data4[k,j]!=0):
                    bias=bias+(data4[k,j]-data4[k,12850])*distn[i,k]*data4[k,12851] #final bias calculation
                    n=n+1
            data6[i,j]=0.35*data4[1098,j]+0.65*data4[i,12850]+bias/n # weighted average rating plus the average bias
            
np.savetxt("C:/Users/admin/Documents/Python Scripts/change/data6n.csv", data6, delimiter=",")

#SVD coding using 'data6' and 'orginal' data are done  in R file 



#final_result interface, function called with username,cityname and no. of recommendations
path= "C:/Users/admin/Documents/Python Scripts/change/final_result.csv"
finaldata = pd.read_csv(path,header=None,encoding='latin')
df=np.array(finaldata)
b=np.empty((1000,2),dtype=object)

def Recommendation(name,city,n):
    b=np.empty((1000,2),dtype=object)
    for i in range(1100):
        if (df[0,i]==name):
            break
    k=0
    for j in range(12851):
        if (df[j,0]==city):
            b[k,0]=df[j,i]
            b[k,1]=df[j,1]
            k=k+1
    print(b[:n])                        #print the top n recommendations with hotel rating and hotel name
name = str(input("Enter the user name--"))
city = str(input("Enter the city name--"))
top_n = int(input("Enter the number of recommendations required--"))
Recommendation(name,city,top_n) #function called with username,cityname and no. of recommendations as input
    
#10179k79, 007solotraveler