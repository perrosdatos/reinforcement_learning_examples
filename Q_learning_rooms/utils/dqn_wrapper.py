from tensorflow.keras.models import load_model
from itertools import product
from sklearn.model_selection import KFold
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from tensorflow.keras import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout, Activation
import time
from tensorflow import keras
import pandas as pd
import numpy as np

class DQNWrapper:

    def __init__(self, q_model, gamma, terminal_state = None):
        self.q_model = q_model
        self.q_model_target = keras.models.clone_model(q_model)
        self.__update_q_target()
        self.gamma = gamma
        self.terminal_state = terminal_state

    def train(self, X, Y, YS, TS, num_qt_update = 100, num_batch = 1,epochs = 1000):
        sub_epochs = int(np.floor(epochs/num_qt_update))
        residual_epochs = epochs%num_qt_update

        #new_y = self.__get_y_target_reward(X,Y, YS, TS)
        #return Y, new_y
        for _ in range(sub_epochs):
            new_y = self.__get_y_target_reward(X,Y, YS, TS)
            self.q_model.fit(x=X, y = new_y,  batch_size = num_batch, epochs=num_qt_update, verbose=0)
            self.__update_q_target()
        if(residual_epochs != 0):
            new_y = self.__get_y_target_reward(X,Y, YS, TS)
            self.q_model.fit(x=X, y = new_y,  batch_size = num_batch, epochs=residual_epochs, verbose=0)
        return Y, new_y
    def __get_y_target_reward(self, x, y, ys, ts):
        new_y = y+self.gamma*np.array([np.max(self.q_model_target.predict(ys_iterator),axis=1) for ys_iterator in ys])
        new_y[ts == True] = y[ts == True]
        return new_y


    def __update_q_target(self):
        self.q_model_target.set_weights(self.q_model.get_weights())