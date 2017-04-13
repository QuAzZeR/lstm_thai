# Load LSTM network and generate text
import sys
import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils
from preprocess import get_seq_of_word
FILE_NAME = "../Data/Dek-d/RealFace/"
# load ascii text and covert to lowercase
#raw_text =""
#for i in range(1,16):
#    raw_text += open(FILE_NAME+str(i)).read()
def testing_model(seq_length,filename):
    print (seq_length,filename)
    # return/ 1
    raw_text = get_seq_of_word()
    # create mapping of unique chars to integers, and a reverse mapping
    chars = sorted(list(set(raw_text)))
    char_to_int = dict((c, i) for i, c in enumerate(chars))
    int_to_char = dict((i, c) for i, c in enumerate(chars))
    # summarize the loaded data
    #print(char_to_int)
    n_chars = len(raw_text)
    n_vocab = len(chars)
    print ("Total Thai Vocab: %s"%( n_chars))
    print ("Total Unique Vocab: %s"%( n_vocab))
    # prepare the dataset of input to output pairs encoded as integers
    # seq_length = 10
    dataX = []
    dataY = []
    for i in range(0, n_chars - seq_length, 1):
        seq_in = raw_text[i:i + seq_length]
        seq_out = raw_text[i + seq_length]
        dataX.append([char_to_int[char] for char in seq_in])
        dataY.append(char_to_int[seq_out])
    n_patterns = len(dataX)
    print ("Total Patterns: %s"%(n_patterns))
    # reshape X to be [samples, time steps, features]
    X = numpy.reshape(dataX, (n_patterns, seq_length, 1))
    # normalize
    X = X / float(n_vocab)
    # one hot encode the output variable
    y = np_utils.to_categorical(dataY)
    # define the LSTM model
    model = Sequential()
    model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2])))
    model.add(Dropout(0.2))
    model.add(Dense(y.shape[1], activation='softmax'))
    # load the network weights
    # filename = "Result/RealFaceWordWindowSize10/weights-improvement-63-4.0191.hdf5"
    # filename = filep
    model.load_weights(filepath)
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    # pick a random seed
    start = numpy.random.randint(0, len(dataX)-1)
    pattern = dataX[start]
    print ("Seed:")
    print ("\""+ ''.join([int_to_char[value] for value in pattern])+ "\"")
    print("----------------------------------\n")
    # generate characters
    for i in range(1000):
        x = numpy.reshape(pattern, (1, len(pattern), 1))
        x = x / float(n_vocab)
        prediction = model.predict(x, verbose=0)
        index = numpy.argmax(prediction)
        result = int_to_char[index]
        seq_in = [int_to_char[value] for value in pattern]
        sys.stdout.write(result)
        pattern.append(index)
        pattern = pattern[1:len(pattern)]
    print ("\nDone.")
if __name__ =='__main__':
    testing_model(int(sys.argv[1]),sys.argv[2])
	