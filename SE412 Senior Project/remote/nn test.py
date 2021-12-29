
import matplotlib.pyplot as plt
import os
import re
import shutil
import string
import tensorflow as tf
import numpy as np

from tensorflow.keras import layers
from tensorflow.keras import losses
from tensorflow.keras import preprocessing

import losses_utils

import csv

def confustion_lists_to_file():

  model = tf.keras.models.load_model(os.getcwd() + 'models/production_model2')

  model.summary()

  true_labels = []
  predicted_labels = []

  directory = os.getcwd() + '/dataset2/test/'

  #print(directory)

  proper_label_index = -1

  for folder in os.listdir(directory):
    print(folder)
    proper_label_index += 1

    for file in os.listdir(directory + folder):

      print(file)
      
      with open(os.path.join(directory,folder,file), 'r', encoding='utf-8') as f:

        lines = f.readlines()
        example = [str(lines[0])]

        predictions = model.predict(example)

        index_max_p = np.argmax(predictions[0]) 

        true_label = proper_label_index
        prediction = index_max_p

        true_labels.append(true_label)
        predicted_labels.append(prediction)
  
  output_labels_path = os.path.join(os.getcwd() + '/labels2.txt')

  with open(output_labels_path,'w') as output_true_f:
    output_true_f.write('true,predicted\n')
    for true,predict in zip(true_labels,predicted_labels):
      output_true_f.write(str(true) + ',' + str(predict) + '\n')

if __name__ == '__main__':
  confustion_lists_to_file()

# Label 0 corresponds to bias
# Label 1 corresponds to clickbait
# Label 2 corresponds to conspiracy
# Label 3 corresponds to fake
# Label 4 corresponds to hate
# Label 5 corresponds to junksci
# Label 6 corresponds to political
# Label 7 corresponds to reliable
# Label 8 corresponds to satire
# Label 9 corresponds to state
# Label 10 corresponds to unreliable