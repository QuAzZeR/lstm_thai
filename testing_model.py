# Load LSTM network and generate text
import sys
import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from prepare_data import prepare_data
def testing_model(seq_length,filename,is_char):
    print (seq_length,filename)
    # return/ 1
    prepared_data= prepare_data(is_char,seq_length)
    # define the LSTM model
    model = Sequential()
    model.add(LSTM(256,input_shape=(prepared_data.X.shape[1], prepared_data.X.shape[2]), return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(128))
    model.add(Dropout(0.2))
    model.add(Dense(prepared_data.Y.shape[1], activation='softmax'))
    # load the network weights
    # filename = "Result/RealFaceWordWindowSize10/weights-improvement-63-4.0191.hdf5"
    # filename = filep
    model.load_weights(filename)
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    # pick a random seed
    start = numpy.random.randint(0, len(prepared_data.dataX)-1)
    pattern = prepared_data.dataX[start]
    print ("Seed:")
    print ("\""+ ''.join([prepared_data.int_to_char[value] for value in pattern])+ "\"")
    print("----------------------------------\n")
    # generate characters
    for i in range(1000):
        x = numpy.reshape(pattern, (1, len(pattern), 1))
        x = x / float(prepared_data.n_vocab)
        prediction = model.predict(x, verbose=0)
        index = numpy.argmax(prediction)
        result = prepared_data.int_to_char[index]
        seq_in = [prepared_data.int_to_char[value] for value in pattern]
        sys.stdout.write(result)
        pattern.append(index)
        pattern = pattern[1:len(pattern)]
    print ("\nDone.")

if __name__ =='__main__':

	testing_model(int(sys.argv[1]),sys.argv[2],bool(int(sys.argv[3])))
