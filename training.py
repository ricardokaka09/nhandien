
# coding: utf-8

# In[1]:
import pyttsx3
import speech_recognition


import nltk
from nltk.stem.lancaster import LancasterStemmer
# from pyvi.pyvi import ViTokenizer

stemmer = LancasterStemmer()

import numpy as np
import tflearn
import tensorflow as tf
import random


# In[2]:


import json

with open('data/intents.json' , encoding="utf8") as json_data:
    intents = json.load(json_data)


# In[42]:


def ngrams(str, n):
    tokens = str.split(' ')
    arr = []
    for i in range(len(tokens)):
        new_str = ''
        if i == 0 and n>1:
            new_str = '_'
            for j in range(n):
                if j < n - 1:
                    if (i + j) <= len(tokens):
                        new_str += ' '+tokens[i+j]
                    else:
                        new_str += ' _'
        else:
            for j in range(n):
                if j < n:
                    if (i + j) < len(tokens):
                        if j == 0:
                            new_str += tokens[i+j]
                        else:
                            new_str += ' '+tokens[i+j]
                    else:
                        new_str += ' _'
        arr.append(new_str)
    return arr


# In[43]:


ngrams('a b c d e f g h', 4)


# In[3]:


words = []
classes = []
documents = []
ignore_words = ['?', 'và', 'à', 'ừ', 'ạ', 'vì', 'từng', 'một_cách']

for intent in intents['intents']:
    for pattern in intent['patterns']:

        w = nltk.word_tokenize(pattern)
        words.extend(w)
        documents.append((w, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))

classes = sorted(list(set(classes)))

print (len(documents), "documents")
print (len(classes), "classes", classes)
print (len(words), "unique stemmed words", words)


# In[4]:


#Create training data
training = []
output = []

output_empty = [0] * len(classes)

for doc in documents:
    bag = []
    pattern_words = doc[0]
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]

    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

random.shuffle(training)
training = np.array(training)

train_x = list(training[:,0])
train_y = list(training[:,1])


# In[5]:


print(train_x[1])
print(train_y[1])


# In[6]:


tf.reset_default_graph()

net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net, optimizer='adam', loss='categorical_crossentropy')

model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')

model.fit(train_x, train_y, n_epoch=1000, batch_size=8, show_metric=True)
model.save('models/model.tflearn')

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)

    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words, show_details=False):
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)

    return(np.array(bag))

bow('I want to special food', words)


# In[8]:


import pickle
pickle.dump( {'words':words, 'classes':classes, 'train_x':train_x, 'train_y':train_y}, open( "models/training_data", "wb" ) )

context = {}

# ERROR_THRESHOLD = 0.25
# def classify(sentence):
#     results = model.predict([bow(sentence, words)])[0]
#     results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD]
#     results.sort(key=lambda x: x[1], reverse=True)
#     return_list = []
#     for r in results:
#         return_list.append((classes[r[0]], r[1]))
#     return return_list

# def response(sentence, userID='1', show_details=False):
#     results = classify(sentence)
#     if results:
#         while results:
#             for i in intents['intents']:
#                 if i['tag'] == results[0][0]:
#                     if 'context_set' in i:
#                         if show_details: print ('context:', i['context_set'])
#                         context[userID] = i['context_set']
#                     if not 'context_filter' in i or                         (userID in context and 'context_filter' in i and i['context_filter'] == context[userID]):
#                         if show_details: print ('tag:', i['tag'])
#                         res = random.choice(i['responses'])
#                         aispeak = pyttsx3.init()
#                         aispeak.setProperty('rate' , 150)
#                         aispeak.say(
#                         res)
#                         aispeak.runAndWait()
#                         return print(res)

#             results.pop(0)
# def chat():
#     print("Ban muon hoi gi nao:(go quit de thoat)")
#     while True:
#         hear = speech_recognition.Recognizer()
#         with speech_recognition.Microphone() as mic:
#             print('i can listening......')
#             audio = hear.listen(mic)
#         try:
#             inp = hear.recognize_google(audio)
#         except:
#             inp = ""
#         # inp = input("you:")
#         if  "quit" in inp:
#             break
#         response(inp, userID='1', show_details=False)

# chat()

