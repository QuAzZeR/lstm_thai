import numpy
from keras.utils import np_utils
from preprocess	import get_seq_of_word,get_seq_of_char

def prepare_data(is_char,seq_length):
    if is_char:
        raw_text = get_seq_of_char()
    else:
        raw_text = get_seq_of_word()
    chars = sorted(list(set(raw_text)))
    char_to_int = dict((c,i) for i,c in enumerate(chars))
    n_chars = len(raw_text)
    n_vocab = len(chars)
    print ("Total Thai Vocab: %s"%(n_chars))
    print ("Total Unique Vocab: %s"%(n_vocab))
    # print(chars)
    # seq_length = 10
    dataX = []
    dataY = []
    for i in range(0,n_chars - seq_length,1):
        seq_in = raw_text[i:i+seq_length]
        seq_out = raw_text[i+seq_length]
        dataX.append([char_to_int[char] for char in seq_in])
        dataY.append(char_to_int[seq_out])
    n_patterns = len(dataX)
    print ("Total Patterns: %s"%(n_patterns))
    # print(dataX[0])
    X = numpy.reshape(dataX, (n_patterns, seq_length, 1))
    # print (X)
    X = X/float(n_vocab)
    Y = np_utils.to_categorical(dataY)
    # print (X)
    print(Y)
    return X,Y,dataX,dataY





