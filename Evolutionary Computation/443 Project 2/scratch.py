# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 22:18:01 2020

@author: smika
"""

from sklearn.metrics import silhouette_score
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import random

X = [[random.randint(-10, 10), random.randint(-10, 10) ] for _ in range(100)]
l = [random.randint(0,5) for _ in range(len(X))]

print(X)

for n_cluster in range(2,5):
    sil_coeff = silhouette_score(X, l, metric='euclidean')
    print("For n_clusters={}, The Silhouette Coefficient is {}".format(n_cluster, sil_coeff))