start_vowel = 'เแใไโ'
karan = '์'
vowel= 'ฦิฺืๅา็ฤๆำะัํฯุู'
tone_mark = '่้๊๋'
consonant = 'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟมยรลภวศษสหฬอฮ'
thai_number = '๑๒๓๔๕๖๗๘๙๐'
list_thai_char='ๅ๑๒ภ๓ถ๔ุูึ฿ค๕ต๖จ๗ข๘ช๙ๆ๐ไำฎพฑะธัํี๊รณนฯยญบฐลฟฤหฆกฏดโเฌ้็่๋าษสศวซงผปแฉอฮิฺื์ทมฒใฬฝฦ'
map_thai_char = {
    0: 'none',
    1: 'ton',
    2: 'sakod',
    3: 'kuab',
    4: 'vowel',
    5: 'karan',
    6: 'vowel',
    7: 'tone'
}

seq_of_char = ""
type_of_char = []
print (len(start_vowel),len(karan),len(vowel),len(tone_mark),len(consonant),len(thai_number),len(list_thai_char))
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
         type_of_char[index_previous_of_previous] = 5
    
    elif previous_char == 'ร' and previous_of_previous_char == 'ต':
        type_of_char[index_previous_of_previous] = 5

    elif previous_of_previous_char == 'ท' and (previous_char =='ร' or previous_char =='น'):
        type_of_char[index_previous_of_previous] = 5
    
    elif previous_char =='ย' and previous_of_previous_char in 'ิ' and previous_of_previous_of_previous_char == 'ร':
        
        type_of_char[index_previous_of_previous] = 5        
        type_of_char[index_previous_of_previous_of_previous] = 5    
    
    type_of_char[index_previous] = 5



    return 5

def map_char_with_int (data):
    
    global seq_of_char
    global type_of_char
    seq_of_char = data
    type_of_char = []
    for i in  range(len(seq_of_char)):
        current_char = seq_of_char[i]
        if current_char in karan:
            type_of_char.append(check_karan(i))
        elif current_char in vowel or current_char in start_vowel:
            type_of_char.append(6)
        elif current_char in tone_mark:
            type_of_char.append(7)
        elif current_char in consonant:
            type_of_char.append(1)
        else:
            type_of_char.append(0)  
    
    
        
            
            

            
