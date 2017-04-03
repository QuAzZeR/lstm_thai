from word_tokenize import word_tokenize
FILE_PATH = '../data/Dek-d/RealFace/%d'
RANGE = range(1,16)
list_thai_char='ๅ๑๒ภ๓ถ๔ุูึ฿ค๕ต๖จ๗ข๘ช๙ๆ๐ไำฎพฑะธัํี๊รณนฯยญบฐลฟฤหฆกฏดโเฌ้็่๋าษสศวซงผปแฉอฮิฺื์ทมฒใฬฝฦ'
def get_seq_of_word():
    sequence_word = []
    for i in RANGE:
        with open(FILE_PATH%(i),'r') as text_file:
            lines = text_file.read()
            sequence_word += word_tokenize(lines)
    return sequence_word


if __name__ == '__main__':

    for i in (list_thai_char):
        print ([i])
