# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 2019

@author: Jacob Hopkins
"""
import neuralNetwork 
#import numpy as np
#import matplotlib.pyplot as plt
import mnist_loader

# =============================================================================
# with np.load('mnist.npz') as data:
#     training_data = zip(data['training_images'], data['training_labels'])
#     test_data = zip(data['test_images'],data['test_labels'])
# =============================================================================
    
#print(training_images.shape)
#print(training_labels[0])

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

layer_sizes = (784,100,50,10)

net = neuralNetwork.NeuralNetwork(layer_sizes)

net.showLayerSizes()
net.showWeightShapes()
net.showWeights()
net.showBiases()

net.SGD(training_data, 10, 10, 2.0, test_data=test_data)
#net.showLayerSizes()
#net.showWeightShapes()
net.showWeights()
net.showBiases()
#net.predict()


#guess = net.predict(training_images)
#plt.imshow(training_images[0].reshape(28,28), cmap = 'gray')
#plt.show()
#print(guess[0])
