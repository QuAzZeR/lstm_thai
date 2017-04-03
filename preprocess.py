from word_tokenize import word_tokenize
FILE_PATH = '../data/Dek-d/RealFace/%d'
RANGE = range(1,16)
list_thai_char='ๅ๑๒ภ๓ถ๔ุูึ฿ค๕ต๖จ๗ข๘ช๙ๆ๐ไำฎพฑะธัํี๊รณนฯยญบฐลฟฤหฆกฏดโเฌ้็่๋าษสศวซงผปแฉอฮิฺื์ทมฒใฬฝฦ'
def get_seq_of_word():
    sequence_word = []
    for i in RANGE:
        with open(FILE_PATH%(i),'r') as text_file:
            lines = text_file.readlines()
            # print(lines)
            for line in lines:
                if line == '\n':
                    continue
                # print([line])
                line_remove = ''.join([i for i in line.strip() if i.isalnum() or i ==' ' or i in list_thai_char])
                # print([line_remove])
                if line_remove != '':
                    sequence_word+=word_tokenize(line_remove)
                    sequence_word += '\n'
                # print (sequence_word)
                # break


	return sequence_word


if __name__ == '__main__':
    get_seq_of_word()
    # for i in (list_thai_char):
    #     print ([i])
