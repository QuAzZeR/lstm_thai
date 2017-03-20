from word_tokenize import word_tokenize
FILE_PATH = '../data/Dek-d/RealFace/%d'
RANGE = range(1,16)
def get_seq_of_word():
    sequence_word = []
    for i in RANGE:
        with open(FILE_PATH%(i),'r') as text_file:
            lines = text_file.read()
            sequence_word += word_tokenize(lines)
    return sequence_word


if __name__ == '__main__':
    print(len(get_seq_of_word()))
