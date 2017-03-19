


def get_thai_list():
    filesname = []
    lines = []
    with open('../Data/article/list_name.txt','r')as list_filename:
        filesname = [line.strip() for line in list_filename.readlines()]
    #print (filesname)
    for filename in filesname[:20]:
        with open('../Data/article/'+filename,'r') as article_file:
            lines += [line.strip() for line in article_file.readlines()]
        print("finish read file" + filename)
        
    sequence_word = []
    for line in lines:
        line_split = line.split('|')
        
        sequence_word += line_split[:len(line_split)-1]
        sequence_word.append(' ')
        # print (sequence_word)
    return sequence_word
        



if __name__ == '__main__':
    get_thai_list()
