from wordcutpy.wordcut import Wordcut

wordcut = 0
with open('wordcutpy/bigthai.txt') as dict_file:
    word_list = list(set([w.rstrip() for w in dict_file.readlines()]))
    word_list.sort()
    wordcut = Wordcut(word_list)


def word_tokenize(lines):
    lines = lines.replace('\n',' ')
    return [word.strip() for word in wordcut.tokenize(lines)]

def main():
    wordcut = 0
    list_line = []
    with open('../Data/Dek-d/RealFace/2','r') as book_file:
        book_lines = book_file.read()
        # for line in book_lines:
        list_line = word_tokenize(book_lines)
    print(list_line)



if __name__ == '__main__':
    main()
