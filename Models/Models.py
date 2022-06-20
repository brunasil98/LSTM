#Import Libraries

from keras.models import Sequential 
from keras.layers.core import Dense, Activation, Dropout 
from keras.layers.recurrent import LSTM
from keras.callbacks import EarlyStopping

def model_2LSTM():
    
    # Define the hidden neuron
    
    out_neurons = 7200
    hidden_neurons = 6200 
    hidden_neurons_2 = 5800
    hidden_neurons_3 = 5350
    hidden_neurons_4 = 4900


    #Create a Model
    
    model = Sequential()  
    model.add(LSTM(out_neurons, input_dim=5, return_sequences=True)) 
    model.add(LSTM(hidden_neurons, return_sequences=True))
    model.add(Dense(hidden_neurons_2))
    model.add(Dense(hidden_neurons_3))
    model.add(Dense(hidden_neurons_4))
    
    return model

def model_3LSTM():
    
    # Define the hidden neuron
    
    out_neurons = 8400
    out_neurons_2 = 7400
    out_neurons_3 = 6400
    hidden_neurons_2 = 5800
    hidden_neurons_3 = 5350
    hidden_neurons_4 = 4900


    #Create a Model
    
    model = Sequential()  
    model.add(LSTM(out_neurons, input_dim=5, return_sequences=True)) 
    model.add(LSTM(out_neurons_2, return_sequences=True))
    model.add(LSTM(out_neurons_3, return_sequences=True))
    model.add(Dense(hidden_neurons_2))
    model.add(Dense(hidden_neurons_3))
    model.add(Dense(hidden_neurons_4))

    return model

def model_compile(model):
    model.compile(loss='mean_squared_error', optimizer="adam")
    es_monitor = EarlyStopping(patience=50, mode = 'min',restore_best_weights=True)
    
    return model, es_monitor
