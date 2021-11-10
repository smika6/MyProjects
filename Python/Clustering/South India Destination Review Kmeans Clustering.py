4.	import numpy as np
5.	import pandas as pd
6.	import matplotlib.pyplot as plt
7.	from mpl_toolkits import mplot3d
8.	from sklearn.cluster import KMeans
9.	
10.	##@Author: Jacob Hopkins
11.	## 3d plot refernce https://likegeeks.com/3d-plotting-in-python/#Putting_legends
12.	
13.	## read from csv file
14.	dataset_filename = 'buddymove.csv'
15.	data = pd.read_csv(dataset_filename)
16.	
17.	##The following code displays the shape of data set
18.	print(data.shape)
19.	print(data.head())
20.	
21.	#names of columns
22.	f1label = 'Sports'
23.	f2label = 'Religious'
24.	f3label = 'Nature'
25.	f4label = 'Theatre'
26.	f5label = 'Shopping'
27.	f6label = 'Picnic'
28.	
29.	##Extracting each column
30.	f1 = data[f1label]
31.	f2 = data[f2label]
32.	f3 = data[f3label]
33.	f4 = data[f4label]
34.	f5 = data[f5label]
35.	f6 = data[f6label]
36.	
37.	## Creating an array of data points
38.	X = np.array(list(zip(f1,f2,f3,f4,f5,f6)))
39.	
40.	## K-Means clustering algorithm with different parameters, 3-5 clusters
41.	
42.	for k in range(3,6):
43.	    print(f'\n\nClustering {dataset_filename} with K-Means(k={k})')
44.	    
45.	    kmeans = KMeans(n_clusters=k, random_state=0).fit(X)
46.	    
47.	    lables = kmeans.labels_
48.	    unique_labels = np.unique(lables)
49.	
50.	    ## print cluster labels
51.	    print("Unique labels: ")
52.	    print(unique_labels)
53.	    
54.	    print("Labels: ")
55.	    print(lables)
56.	
57.	    print("Centers: ")
58.	    print(kmeans.cluster_centers_)
59.	
60.	    ## visualize the clusters
61.	    fig = plt.figure(figsize=(8,4))
62.	
63.	    ## plot of features 0 1 2
64.	    ax = fig.add_subplot(121, projection='3d')
65.	
66.	    for l in unique_labels:
67.	        ax.scatter(X[lables == l , 0] , X[lables == l , 1] , X[lables == l , 2], label = l)
68.	    
69.	    ax.set_title(f'Kmeans(k={k}) Clustering of {dataset_filename}')
70.	    ax.grid(False)
71.	    ax.legend(loc="best")
72.	
73.	    ## plot of features 3, 4, 5
74.	    ax2 = fig.add_subplot(122, projection='3d')
75.	
76.	    for l in unique_labels:
77.	        ax2.scatter(X[lables == l , 3] , X[lables == l , 4] , X[lables == l , 5], label = l)
78.	    
79.	    ax2.grid(False)
80.	    plt.show()
