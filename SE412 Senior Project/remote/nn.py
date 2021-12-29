import matplotlib.pyplot as plt
import os
import re
import shutil
import string
import tensorflow as tf

from tensorflow.keras import layers
from tensorflow.keras import losses
from tensorflow.keras import preprocessing

import losses_utils

# def custom_standardization(input_data):
#   # Could be Juan's Cleaning Code
#   lowercase = tf.strings.lower(input_data)
#   stripped_html = tf.strings.regex_replace(lowercase, '<br />', ' ')
#   return tf.strings.regex_replace(stripped_html,
#                                   '[%s]' % re.escape(string.punctuation),
#                                   '')

def vectorize_text(text, label):
  text = tf.expand_dims(text, -1)
  return vectorize_layer(text), label


print(tf.__version__)

batch_size = 32
seed = 42

raw_train_ds = tf.keras.preprocessing.text_dataset_from_directory(
    'dataset/train', 
    label_mode='int',
    batch_size=batch_size, 
    validation_split=0.2, 
    subset='training', 
    seed=seed)
  

raw_val_ds = tf.keras.preprocessing.text_dataset_from_directory(
    'dataset/train', 
    label_mode='int',
    batch_size=batch_size, 
    validation_split=0.2, 
    subset='validation', 
    seed=seed)

for text_batch, label_batch in raw_train_ds.take(1):
  for i in range(3):
    print("article", text_batch.numpy()[i])
    print("Label", label_batch.numpy()[i])

print("Label 0 corresponds to", raw_train_ds.class_names[0])
print("Label 1 corresponds to", raw_train_ds.class_names[1])
print("Label 2 corresponds to", raw_train_ds.class_names[2])
print("Label 3 corresponds to", raw_train_ds.class_names[3])
print("Label 4 corresponds to", raw_train_ds.class_names[4])
print("Label 5 corresponds to", raw_train_ds.class_names[5])
print("Label 6 corresponds to", raw_train_ds.class_names[6])
print("Label 7 corresponds to", raw_train_ds.class_names[7])
print("Label 8 corresponds to", raw_train_ds.class_names[8])
print("Label 9 corresponds to", raw_train_ds.class_names[9])
print("Label 10 corresponds to", raw_train_ds.class_names[10])


raw_test_ds = tf.keras.preprocessing.text_dataset_from_directory(
    'dataset/test', 
    batch_size=batch_size)

max_features = 10000
sequence_length = 250

vectorize_layer = layers.TextVectorization(
    standardize='lower_and_strip_punctuation', #custom_standardization,
    max_tokens=max_features,
    output_mode='int',
    output_sequence_length=sequence_length)

train_text = raw_train_ds.map(lambda x, y: x)
vectorize_layer.adapt(train_text)

text_batch, label_batch = next(iter(raw_train_ds))
first_review, first_label = text_batch[0], label_batch[0]
print("Article", first_review)
print("Label", raw_train_ds.class_names[first_label])
print("Vectorized Article", vectorize_text(first_review, first_label))

train_ds = raw_train_ds.map(vectorize_text)
val_ds = raw_val_ds.map(vectorize_text)
test_ds = raw_test_ds.map(vectorize_text)

AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
test_ds = test_ds.cache().prefetch(buffer_size=AUTOTUNE)

embedding_dim = 16

model = tf.keras.Sequential([
  layers.Embedding(max_features + 1, embedding_dim),
  layers.Dropout(0.2),
  layers.GlobalAveragePooling1D(),
  layers.Dropout(0.2),
  layers.Dense(11)])

model.summary()



model.compile(loss=losses.SparseCategoricalCrossentropy(from_logits=False, reduction=losses_utils.ReductionV2.AUTO,
    name='sparse_categorical_crossentropy'),
              optimizer='adam',
              metrics=['accuracy',tf.metrics.SparseCategoricalAccuracy()]) #tf.metrics.SparseCategoricalAccuracy()

epochs = 15

history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=epochs)

loss, accuracy = model.evaluate(test_ds)

print("Loss: ", loss)
print("Accuracy: ", accuracy)


history_dict = history.history
history_dict.keys()



acc = history_dict['accuracy']
val_acc = history_dict['val_accuracy']
loss = history_dict['loss']
val_loss = history_dict['val_loss']

epochs = range(1, len(acc) + 1)

# "bo" is for "blue dot"
plt.plot(epochs, loss, 'bo', label='Training loss')
# b is for "solid blue line"
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()


plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')

plt.show()

export_model = tf.keras.Sequential([
  vectorize_layer,
  model,
  layers.Activation('sigmoid')
])

export_model.compile(
    loss=losses.SparseCategoricalCrossentropy(from_logits=False, reduction=losses_utils.ReductionV2.AUTO,
    name='sparse_categorical_crossentropy'), optimizer="adam", metrics=['accuracy']
)

# Test it with `raw_test_ds`, which yields raw strings
loss, accuracy = export_model.evaluate(raw_test_ds)
print(accuracy)

examples = ["""Twitter said on Tuesday that it would give users access to ad-free articles from The Washington Post, Reuters, BuzzFeed and other publications through its subscription service, called Twitter Blue.

The offering is part of Twitter’s push to find new sources of revenue. In January, the company acquired Revue, a service that enables people to create newsletters, and said it would take a small percentage of subscription fees from newsletter writers. And in May, Twitter bought Scroll, a subscription company that created ad-free reading services for publishers.

In June, the company announced Twitter Blue and a plan to charge users a small fee in exchange for extra features like the ability to organize bookmarks and undo tweets. On Tuesday, Twitter said it would ask users to pay $3 a month for those features, as well as access to the ad-free articles.

“In continuing our commitment to strengthen and support publishers and a free press, a portion of the revenue from Twitter Blue subscription fees goes directly to publishers within our network,” two Twitter project managers, Sara Beykpour and Smita Gupta, wrote in a blog post. “Our goal is to help each publishing partner make 50 percent more per person than they would’ve made from serving ads to that person.”

Twitter also said it would revive features associated with Nuzzel, a service offered by Scroll that alerted users about articles that were widely shared by people they follow on Twitter. Twitter shuttered Nuzzel when it acquired Scroll, prompting an outcry from users who said the service helped cut through the noise of their crowded social media feeds.""",
"""In the 18 years since he founded Barstool Sports, Dave Portnoy has developed a reputation as a tough-talking digital provocateur and opponent of what he considers political correctness, whether it’s defending the New England Patriots, his pizza preferences or his controversial interview last year at the White House with Donald Trump.

So when Insider.com published an investigative article accusing Portnoy of choking two women during sexual encounters and filming them without their consent, he immediately went on the offensive with an emotional two-part video response attacking the article as a “hit piece” that he said bore no resemblance to reality.

He was just getting started.

Since then, Portnoy is waging an all-out war on Insider, writer Julia Black, global editor in chief Nicholas Carlson, company CEO and co-founder Henry Blodget and even Axel Springer, the German media conglomerate that purchased the online publication in 2015 — simultaneously outraging critics and thrilling many of his 2.7 million followers on Twitter that have taken up his cause to launch their own social media attacks on the company and its employees.

“Here is what people have to know about me,” Portnoy wrote on Twitter on Saturday. “If you wrong me I will burn you to the ground. If I burn with it that’s the cost of doing business. I’ve always been that way.” Accusing Insider of “exploiting” the unnamed women quoted in the story “for political agendas and financial gain,” he tried to get the hashtag “CancelBusinessInsid"""]

export_model.predict(examples)

export_model.save('models/production_model')