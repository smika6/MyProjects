import os
import tensorflow as tf
import pandas as pd


new_model = tf.keras.models.load_model('model/bertmodel.pt')

# Show the model architecture
new_model.summary()