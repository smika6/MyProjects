# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 2019

references!
https://www.youtube.com/watch?v=8bNIkfRJZpo
http://neuralnetworksanddeeplearning.com/chap1.html

@author: Jacob and heavily references
"""
import random
import numpy as np

class NeuralNetwork:
    def __init__(self, layer_sizes):
        print('Loading New Neural Network')
        self.num_layers = len(layer_sizes)
        self.layer_sizes = layer_sizes
        self.weight_shapes = [(a,b) for a,b in zip(layer_sizes[1:],layer_sizes[:-1])]
        self.weights = [np.random.standard_normal(s)/s[1]**.5 for s in self.weight_shapes]
        self.biases = [np.zeros((s,1)) for s in layer_sizes[1:]]
        print('Done')
    
    @staticmethod
    def sigmoid(x):
        return 1 / (1+np.exp(-x))
    
    @staticmethod
    def sigmoid_prime(self, z):
        """Derivative of the sigmoid function."""
        return self.sigmoid(z)*(1-self.sigmoid(z))

    def predict(self, a):
        for w,b in zip(self.weights, self.biases):
            a = self.sigmoid((np.matmul(w,a) + b))
        return a;
    
    def feedforward(self, a):
        """Return the output of the network if ``a`` is input."""
        for b, w in zip(self.biases, self.weights):
            a = self.sigmoid(np.dot(w, a)+b)
        return a
    
    def showPrediction(self, a):
        print ('')
        print('All Predictions to Confidences')
        for w in a:
            print w
        a = self.predict(a)
        guess = -1
        n = 0
        print ""
        for g in a:
            print n,g[0] 
            if(g==max(a)):
                guess = n
            n+=1
        print('----------------------')
        print('Conclusion')
        print 'Guess:',guess
        print 'Confidence:', max(a)
        print('----------------------')
        return guess, max(a)
    
    def showWeightShapes(self):
        print('\nShowing Weight Shapes\'s----------')
        print(self.layer_sizes[0], 1 )
        for s in self.weight_shapes:
            print(s)
        print(self.layer_sizes[len(self.layer_sizes)-1], 1)
        print('------------------------------------')
    
    def showWeights(self):
        print('\nShowing Weight Matrix\'s----------')
        for w in self.weights:
            print(w)
        print('------------------------------------')
    
    def showBiases(self):
        print('\nShowing Bias Matrix\'s----------')
        for b in self.biases:
            print(b)
        print('----------------------------------')
    
    def showLayerSizes(self):
        print('\nShowing Layer Shapes\'s----------\n')
        print(self.layer_sizes)
        print('-----------------------------------')
        
    #end of things that I had any hand in making/fully understanding haha
    def SGD(self, training_data, epochs, mini_batch_size, eta,
            test_data=None):
        """Train the neural network using mini-batch stochastic
        gradient descent.  The ``training_data`` is a list of tuples
        ``(x, y)`` representing the training inputs and the desired
        outputs.  The other non-optional parameters are
        self-explanatory.  If ``test_data`` is provided then the
        network will be evaluated against the test data after each
        epoch, and partial progress printed out.  This is useful for
        tracking progress, but slows things down substantially."""
        if test_data: n_test = len(test_data)
        n = len(training_data)
        for j in range(epochs):
            random.shuffle(training_data)
            mini_batches = [
                training_data[k:k+mini_batch_size]
                for k in range(0, n, mini_batch_size)]
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)
            if test_data:
                print 'Epoch ', j, ':', self.evaluate(test_data), ' / ', n_test
            else:
                print "Epoch ", j, " complete"

    def update_mini_batch(self, mini_batch, eta):
        """Update the network's weights and biases by applying
        gradient descent using backpropagation to a single mini batch.
        The ``mini_batch`` is a list of tuples ``(x, y)``, and ``eta``
        is the learning rate."""
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)
            nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        self.weights = [w-(eta/len(mini_batch))*nw
                        for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b-(eta/len(mini_batch))*nb
                       for b, nb in zip(self.biases, nabla_b)]

    def backprop(self, x, y):
        """Return a tuple ``(nabla_b, nabla_w)`` representing the
        gradient for the cost function C_x.  ``nabla_b`` and
        ``nabla_w`` are layer-by-layer lists of numpy arrays, similar
        to ``self.biases`` and ``self.weights``."""
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        # feedforward
        activation = x
        activations = [x] # list to store all the activations, layer by layer
        zs = [] # list to store all the z vectors, layer by layer
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation)+b
            zs.append(z)
            activation = self.sigmoid(z)
            activations.append(activation)
        # backward pass
        delta = self.cost_derivative(activations[-1], y) * \
            sigmoid_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())
        # Note that the variable l in the loop below is used a little
        # differently to the notation in Chapter 2 of the book.  Here,
        # l = 1 means the last layer of neurons, l = 2 is the
        # second-last layer, and so on.  It's a renumbering of the
        # scheme in the book, used here to take advantage of the fact
        # that Python can use negative indices in lists.
        for l in range(2, self.num_layers):
            z = zs[-l]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
        return (nabla_b, nabla_w)

    def evaluate(self, test_data):
        """Return the number of test inputs for which the neural
        network outputs the correct result. Note that the neural
        network's output is assumed to be the index of whichever
        neuron in the final layer has the highest activation."""
        test_results = [(np.argmax(self.feedforward(x)), y)
                        for (x, y) in test_data]
        return sum(int(x == y) for (x, y) in test_results)

    def cost_derivative(self, output_activations, y):
        """Return the vector of partial derivatives \partial C_x /
        \partial a for the output activations."""
        return (output_activations-y)
    
def sigmoid(z):
    """The sigmoid function."""
    return 1.0/(1.0+np.exp(-z))

def sigmoid_prime(z):
    """Derivative of the sigmoid function."""
    return sigmoid(z)*(1-sigmoid(z))