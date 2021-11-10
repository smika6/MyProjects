# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 2019

@author: Jacob
"""
import neuralNetwork 
import numpy

layer_sizes = (3,5,7,3,10)
x = numpy.ones((layer_sizes[0],1))

net = neuralNetwork.NeuralNetwork(layer_sizes)
net.showLayerSizes()
net.showWeightShapes()
net.showWeights()
net.showBiases()

prediction = net.predict(x)
print(prediction)
net.showPrediction(x)