


vowel= 'แิฺื์ใฦฤโเ็าฯีัํะำไๆึุูๅ'
tone_mark = '่้๊๋'
consonant = 'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟมยรลภวศษสหฬอฮ'
thai_number = '๑๒๓๔๕๖๗๘๙๐'
list_thai_char='ๅ๑๒ภ๓ถ๔ุูึ฿ค๕ต๖จ๗ข๘ช๙ๆ๐ไำฎพฑะธัํี๊รณนฯยญบฐลฟฤหฆกฏดโเฌ้็่๋าษสศวซงผปแฉอฮิฺื์ทมฒใฬฝฦ'






def map_char_with_int (seq_of_char):
    # for i in range(len(seq_of_char)):
    #     print(seq_of_char[i],end='')
    e = sorted(set(consonant))
    
    d = sorted(set(tone_mark))
    c = sorted(set(vowel))
    b = sorted(set(thai_number))
    a = sorted(set(list_thai_char))
    print(len(e),len(d),len(c),len(b),len(a))
    print(type(a))
    
