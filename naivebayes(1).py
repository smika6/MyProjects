
# A skeleton for implementing Naive Bayes Classifier in Python.
# Author: Jacob Hopkins

import numpy
import random
import time
import math
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

def seperate_into_dictionary_by_class(dataset):
    seperated = {}

    for data in dataset:
        class_value = data[-1]

        if class_value not in seperated:
            seperated[class_value] = []

        seperated[class_value].append(data)

    return seperated

def mean(numbers):
    return sum(numbers)/float(len(numbers))


def stdev(numbers):
    avg = mean(numbers)
    variance = sum([(x-avg)**2 for x in numbers]) / float(len(numbers)-1)
    return math.sqrt(variance)


def gaussian_pdf(x, mean, stdev):
    exponent = math.exp(-((x-mean)**2 / (2 * stdev**2)))
    return (1 / (math.sqrt(2 * math.pi) * stdev)) * exponent

def summarize_dataset(dataset):
  #find the mean stdev and number of elements in each row of the dataset
	summaries = [(mean(column), stdev(column), len(column)) for column in zip(*dataset)]
  #truncate the summary of the classifing data
	del(summaries[-1])
  #return said summary
	return summaries

def summarize_by_class(dataset):
	separated = seperate_into_dictionary_by_class(dataset)
	summaries = {}
	for class_value, rows in separated.items():
		summaries[class_value] = summarize_dataset(rows)
	return summaries

def calculate_class_probabilities(summaries, row):
	total_rows = sum([summaries[label][0][2] for label in summaries])
	probabilities = dict()
	for class_value, class_summaries in summaries.items():
		probabilities[class_value] = summaries[class_value][0][2]/float(total_rows)
		for i in range(len(class_summaries)):
			mean, stdev, count = class_summaries[i]
			probabilities[class_value] *= gaussian_pdf(row[i], mean, stdev)
	return probabilities

def predict(summaries, row):
	probabilities = calculate_class_probabilities(summaries, row)
	best_label, best_prob = None, -1
	for class_value, probability in probabilities.items():
		if best_label is None or probability > best_prob:
			best_prob = probability
			best_label = class_value
	return best_label

def naive_bayes(train, test):
	summarize = summarize_by_class(train)
	predictions = list()
	for row in test:
		output = predict(summarize, row)
		predictions.append(output)
	return(predictions)

def evaluate_naive_bayes(trainingFile,testingFile):
  train = numpy.loadtxt(trainingFile)
  test = numpy.loadtxt(testingFile)

  trainlabels = [y[0] for y in train[:,-1:]]
  testlabels = [y[0] for y in test[:,-1:]]

  trainpredictions = naive_bayes(train, train)
  testpredictions = naive_bayes(train, test)

  print("\n\n Training Results")
  print("Predictions: \n",trainpredictions)
  print("Labels: \n",trainlabels)
  print("Accuracy: \n", accuracy_score(trainlabels,trainpredictions))
  print("Classification Report \n", classification_report(trainlabels,trainpredictions))
  print('Note: In a binary classification, the count of true negatives is C(0,0), false negatives is C(1,0), true positives is C(1,1) and false positives is C(0,1).')
  print("Confusion Matrix: \n", confusion_matrix(trainlabels,trainpredictions))


  print("\n\n Testing Results")
  print("Predictions: \n", testpredictions)
  print("Labels: \n",testlabels)
  print("Accuracy: \n", accuracy_score(testlabels,testpredictions))
  print("Classification Report \n", classification_report(testlabels,testpredictions))
  print('Note: In a binary classification, the count of true negatives is C(0,0), false negatives is C(1,0), true positives is C(1,1) and false positives is C(0,1).')
  print("Confusion Matrix: \n", confusion_matrix(testlabels,testpredictions))


trainingFile = "irisTraining.txt"
testingFile = "irisTesting.txt"

print('*** iris ***')
evaluate_naive_bayes(trainingFile,testingFile)

secondaryTestFile = "irisPCTesting.txt"
secondaryTrainFile = "irisPCTraining.txt"

print('\n\n*** irisPC *** ')
evaluate_naive_bayes(secondaryTrainFile,secondaryTestFile)