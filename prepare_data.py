import numpy
from keras.utils import np_utils
from preprocess	import get_seq_of_word,get_seq_of_char
from map_char_with_int import map_char_with_int
import model
def prepare_data(is_char,seq_length):
    prepared_data = model.Data()
    if is_char:
        raw_text = get_seq_of_char()
        raw_text = map_char_with_int(raw_text)
    else:
        raw_text = get_seq_of_word()
    prepared_data.raw_text = raw_text
    
    chars = sorted(list(set(raw_text)))
    prepared_data.char_to_int = dict((c,i) for i,c in enumerate(chars))
    prepared_data.int_to_char = dict((i, c) for i, c in enumerate(chars))
    
    n_chars = len(raw_text)
    n_vocab = len(chars)
    prepared_data.n_vocab = n_vocab
    print ("Total Thai Vocab: %s"%(n_chars))
    print ("Total Unique Vocab: %s"%(n_vocab))
    # print(chars)
    # seq_length = 10
    dataX = []
    dataY = []
    for i in range(0,n_chars - seq_length,1):
        seq_in = raw_text[i:i+seq_length]
        seq_out = raw_text[i+seq_length]
        dataX.append([prepared_data.char_to_int[char] for char in seq_in])
        dataY.append(prepared_data.char_to_int[seq_out])
    n_patterns = len(dataX)
    prepared_data.dataX = dataX
    prepared_data.dataY = dataY
    print ("Total Patterns: %s"%(n_patterns))
    # print(dataX[0])
    X = numpy.reshape(dataX, (n_patterns, seq_length, 1))
    # print (X)
    prepared_data.X = X/float(n_vocab)
    prepared_data.Y = np_utils.to_categorical(dataY)
    # print (X)
    # print(Y)
    return prepared_data





