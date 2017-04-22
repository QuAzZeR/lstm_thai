start_vowel = 'เแใไโ'
karan = '์'
vowel= 'ๅุูึำะัํีฤ็าิฺืฦ'
tone_mark = '่้๊๋'
consonant = 'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟมยรลภวศษสหฬอฮ'
thai_number = '๑๒๓๔๕๖๗๘๙๐'
list_thai_char='ๅ๑๒ภ๓ถ๔ุูึ฿ค๕ต๖จ๗ข๘ช๙ๆ๐ไำฎพฑะธัํี๊รณนฯยญบฐลฟฤหฆกฏดโเฌ้็่๋าษสศวซงผปแฉอฮิฺื์ทมฒใฬฝฦฅฃ'
map_thai_char = {
    0: 'none',
    1: 'ton',
    2: 'sakod',
    3: 'kuab',
    4: 'vowel',
    5: 'karan',
    6: 'tone'
}
KEY_NONE = 0
KEY_TON = 1
KEY_SAKOD = 2
KEY_KUAB = 3
KEY_VOWEL = 4
KEY_KARAN = 5
KEY_TONE_MARK = 6

seq_of_char = ""
type_of_char = []
# print (len(start_vowel),len(karan),len(vowel),len(tone_mark),len(consonant),len(thai_number),len(list_thai_char))
# print (len(set(start_vowel)),len(set(karan)),len(set(vowel)),len(set(tone_mark)),len(set(consonant)),len(set(thai_number)),len(set(list_thai_char)))

# print([' ' + temp for temp in vowel])
# for i in list_thai_char:
#     if i not in start_vowel+karan+vowel+tone_mark+consonant+thai_number:
#         print(i)
# print("dasdasdj;aklsdasasdasdsadasdl;askdjasld;aklasjdas;jksdakls;djadkl;asjkl")
# temp = {}
# for i in start_vowel+karan+vowel+tone_mark+consonant+thai_number:
#     if i in temp:
#         temp[i] += 1
#     else:
#         temp[i] = 1
# print(temp)
# print ("_______")
# print (map_thai_char)
def check_karan(index):
    global type_of_char
    index_previous = index - 1
    index_previous_of_previous = index - 2
    index_previous_of_previous_of_previous = index - 3
    previous_char = seq_of_char[index_previous]
    previous_of_previous_char = seq_of_char[index_previous_of_previous]
    previous_of_previous_of_previous_char = seq_of_char[index_previous_of_previous_of_previous]
    
    if previous_char in vowel:
         type_of_char[index_previous_of_previous] = KEY_KARAN
    
    elif previous_char == 'ร' and previous_of_previous_char == 'ต':
        type_of_char[index_previous_of_previous] = KEY_KARAN

    elif previous_of_previous_char == 'ท' and (previous_char =='ร' or previous_char =='น'):
        type_of_char[index_previous_of_previous] = KEY_KARAN
    
    elif previous_char =='ย' and previous_of_previous_char in 'ิ' and previous_of_previous_of_previous_char == 'ร':
        
        type_of_char[index_previous_of_previous] = KEY_KARAN
        type_of_char[index_previous_of_previous_of_previous] = KEY_KARAN
    
    type_of_char[index_previous] = KEY_KARAN

    type_of_char.append(KEY_KARAN)

def check_vowel(index):
    global type_of_char
    index_previous = index - 1
    index_previous_of_previous = index - 2
    index_previous_of_previous_of_previous = index - 3
    
    current_char = seq_of_char[index]
    previous_char = seq_of_char[index_previous]
    previous_of_previous_char = seq_of_char[index_previous_of_previous]
    previous_of_previous_of_previous_char = seq_of_char[index_previous_of_previous_of_previous]
    
    if current_char in start_vowel:
        pass
    if current_char in 'ำะัีาิืุูึ็':
        if previous_char in 'รลว' and previous_of_previous_char in consonant:
            type_of_char[index_previous] = KEY_KUAB
            type_of_char[index_previous_of_previous] = KEY_TON
        elif previous_char in consonant:
            type_of_char[index_previous] = KEY_TON
        
        
    
    
    
    
    type_of_char.append(KEY_VOWEL)

def check_consonant(index):
    global type_of_char
    index_previous = index - 1
    index_previous_of_previous = index - 2
    index_previous_of_previous_of_previous = index - 3
    current_char = seq_of_char[index]
    previous_char = seq_of_char[index_previous]
    previous_of_previous_char = seq_of_char[index_previous_of_previous]
    previous_of_previous_of_previous_char = seq_of_char[index_previous_of_previous_of_previous]
    
    if previous_char in start_vowel :
        type_of_char.append(KEY_TON)
    elif previous_char in vowel or (previous_char in tone_mark and previous_of_previous_char in vowel):
        if current_char in 'อยว':
            type_of_char.append(KEY_VOWEL)
        else:
            type_of_char.append(KEY_SAKOD)   
    elif previous_char in tone_mark and previous_of_previous_char in consonant:
        type_of_char.append(KEY_SAKOD)
    elif previous_char in 'อยว':
        if previous_of_previous_char in consonant or ((previous_of_previous_char in tone_mark ) and (previous_of_previous_of_previous_char in consonant)):
            type_of_char[index_previous] = KEY_VOWEL
            type_of_char.append(KEY_SAKOD)
        else:
            type_of_char.append(KEY_NONE)
    else:
        type_of_char.append(KEY_NONE)
    
    
def map_char_with_int (data):
    global seq_of_char
    global type_of_char
    seq_of_char = data
    type_of_char = []
    for i in  range(len(seq_of_char)):
        current_char = seq_of_char[i]
        # print (current_char,seq_of_char[:i],i)
        if current_char in karan:
            check_karan(i)
        elif current_char in vowel or current_char in start_vowel:
            check_vowel(i)
        elif current_char in tone_mark:
            
            type_of_char.append(KEY_TONE_MARK)
        elif current_char in consonant:
            # print(current_char)
            check_consonant(i)
            # check_consonant()
        else:
            type_of_char.append(KEY_NONE)
    
    temp = []
    if len(seq_of_char) != len(seq_of_char):
        print("eiei")
    for i in range(len(seq_of_char)):
        temp.append(map_thai_char[type_of_char[i]] +"_"+ seq_of_char[i] )
    # print (temp)
    return temp    
        
    
    
        
if __name__ == '__main__':
    print(map_char_with_int('เอางี้ละกัน ช่างโง่เขลาซะเหลือเกิน'))
            

      
