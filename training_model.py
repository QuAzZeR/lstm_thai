import sys
import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint

from prepare_data import prepare_data
def train_model(seq_length,path,is_char):
    print (seq_length,path,is_char)
    # return
    X, Y, dataX, dataY= prepare_data(is_char,seq_length)
    
    #define the LSTM model
    model = Sequential()
    model.add(LSTM(256,input_shape=(X.shape[1], X.shape[2]), return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(128))
    model.add(Dropout(0.2))
    model.add(Dense(Y.shape[1], activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    # define the checkpoint
    filepath=path+"/weights-improvement-{epoch:02d}-{loss:.4f}.hdf5"
    checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
    callbacks_list = [checkpoint]
    model.fit(X, Y, nb_epoch=80, batch_size=128, callbacks=callbacks_list)
    
if __name__ == '__main__' :
    train_model(int(sys.argv[1]),sys.argv[2],bool(int(sys.argv[3])))
