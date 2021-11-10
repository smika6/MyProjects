#Jacob Hopkins
#7/3/2017
#takes in user imput and averages the scores
#InputNAvgScore.py
#Assignment 4

#Given a graphics library, My clusters would be gemini, some very close,
#some very spread out. I think that Pass 0 has the closest clusters off all of them,
#I used only 3 passes, and only 4 clusters.
#I think that doing this has eliminated some of the empty clusters, and
#might just contain the clusters more accurately
import random
import math

def euclidD(point1, point2):
    sum = 0
    for index in range(len(point1)):
        diff = (point1[index]-point2[index]) ** 2
        sum = sum + diff
        
    euclidDistance = math.sqrt(sum)
    return euclidDistance

def readFile(filename):
    datafile = open(filename, "r")
    datadict = {}

    key = 0
    for aline in datafile:
       key = key + 1
       score = int(aline)

       datadict[key] = [score]   
       
    return datadict


def createCentroids(k, datadict):
    centroids=[]           
    centroidCount = 0
    centroidKeys = []

    while centroidCount < k: 
       rkey = random.randint(1,len(datadict))
       if rkey not in centroidKeys:
           centroids.append(datadict[rkey])   
           centroidKeys.append(rkey)       
           centroidCount = centroidCount + 1   
           
    return centroids
    
def createClusters(k, centroids, datadict, repeats):
    for apass in range(repeats):
        print("****PASS",apass,"****")
        clusters = []                      
        for i in range(k):
           clusters.append([])             

        for akey in datadict:
           distances = []                     
           for clusterIndex in range(k):    
               dist = euclidD(datadict[akey],centroids[clusterIndex])
               distances.append(dist)       

           mindist = min(distances)         
           index = distances.index(mindist)   

           clusters[index].append(akey)     

        dimensions = len(datadict[1])      
        for clusterIndex in range(k):      
           sums = [0]*dimensions
           for akey in clusters[clusterIndex]:
               datapoints = datadict[akey]
               for ind in range(len(datapoints)):           
                   sums[ind] = sums[ind] + datapoints[ind]  
           for ind in range(len(sums)):                    
               clusterLen = len(clusters[clusterIndex])
               if clusterLen != 0:
                  sums[ind] = sums[ind]/clusterLen   
       
           centroids[clusterIndex] = sums   
           
        end = ""
        for c in clusters:
           print ("CLUSTER")
           for key in c:
               print(datadict[key], end==" ")
           print()
           
    return clusters
#implemented from the book and used
def clusterAnalysis(dataFile):
    examDict = readFile(dataFile)
    examCentroids = createCentroids(4,examDict)
    examClusters = createClusters(4,examCentroids,examDict,3)
    print(examClusters)

clusterAnalysis("cs150exams.txt")

#dd=readFile("cs150exams.txt")
#c=createCentroids(5,dd)
#cl=createClusters(5,c,dd,4)
#print(cl)

#Python v3.5.1
#IDLE v3.5.1
#Windows 10
#No additional libraries
