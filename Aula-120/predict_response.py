import nltk
nltk.download('punkt')

import json
import pickle
import numpy as np
import random
import tensorflow
from data_preprocessing import get_stem_words

ignore_words = ['?', '!',',','.', "'s", "'m"]
model = tensorflow.keras.models.load_model('./chatbot_model.h5')
intents = json.loads(open('./intents.json').read())
words = pickle.load(open('./words.pkl', 'rb'))
classes = pickle.load(open('./classes.pkl', 'rb'))

def preprocess_user_input(user_input):
    input_word_token1 = nltk.word_tokenize(user_input)
    input_word_token2 = get_stem_words(input_word_token1, ignore_words)
    input_word_token2 = sorted(list(set(input_word_token2)))
    bag = []
    bag_of_words = []
    
    for word in words:
        if word in input_word_token2:
            bag_of_words.append(1)
        else:
            bag_of_words.append(0)
            
    bag.append(bag_of_words)
    
    return np.array(bag)

def bot_class_prediction(user_input):
    inp = preprocess_user_input(user_input)

    prediction = model.predict(inp)
    predicted_label = np.argmax(prediction[0])
    
    return predicted_label

def bot_response(user_input):
    predicted_class_label = bot_class_prediction(user_input)
    predicted_class = classes[predicted_class_label]
    
    for intent in intents['intents']:
        if intent['tag'] == predicted_class:
            bot_response = random.choice(intent['responses'])
            
            return bot_response
        
print('Oi eu sou Estela, como posso te ajudar?')

while True:
    user_input = input('Digite aqui...')
    print('ENTRADA DO USUÁRIO: ', user_input)
    response = bot_response(user_input)
    print('RESPOSTA DO ROBÔ: ', response)