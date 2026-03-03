def piglatin_book():
    pig_latin = []  # a list contains letters of pig latin
    for word in message.split():
        #get non alpha from start
        prefix_non_letters = ''
        while len(word) > 0 and not word[0].isalpha():
            prefix_non_letters += word[0]
            word = word[1:]

        if len(word) == 0:
            pig_latin.append(prefix_non_letters)
            continue

        # get non alpha from end
        # can't parse each letter in a pattern like this:
        # 2026Python-03Month-02Day-10:00
        suffix_non_letters = ''
        while not word[-1].isalpha():
            suffix_non_letters = word[-1] + suffix_non_letters
            word = word[:-1]

        was_upper = word.isupper()
        was_title = word.istitle()

        word = word.lower()

        prefix_consonants = ''
        while len(word) > 0 and not word[0] in VOWELS:
            prefix_consonants += word[0]
            word = word[1:]

        if prefix_consonants != '':
            word += prefix_consonants + 'ay'
        else:
            word += 'yay'

        if was_upper:
            word = word.upper()
        if was_title:
            word = word.title()

        pig_latin.append(prefix_non_letters + word + suffix_non_letters)
    print('Pig Latin Follows Book: ', end="")
    print(' '.join(pig_latin))

# to handle a word "2026Python-03Month-02Day-10:00" in a message
def piglatin_customized():
    pig_latin = []  # a list contains letters of pig latin
    for text in message.split():
        pig_latin.append(transform_string(text))
    print('Pig Latin Customized: ', end="")
    print(' '.join(pig_latin))

def transform_string(text):
    result = []
    i = 0
    w_len = len(text)
    while i < w_len:
        if text[i].isalpha():
            start = i
            while i < w_len and text[i].isalpha():
                i += 1
            word = text[start:i]
            result.append(piglatin_word(word))
        else:
            result.append(text[i])
            i += 1
    return ''.join(result)

def piglatin_word(word):
    was_upper = word.isupper()
    was_title = word.istitle()

    word = word.lower()

    prefix_consonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefix_consonants += word[0]
        word = word[1:]

    if prefix_consonants != '':
        word += prefix_consonants + 'ay'
    else:
        word += 'yay'
    if was_upper:
        word = word.upper()
    if was_title:
        word = word.title()
    return word


print('''
Pig Latin Rules
    * If letter starts with vowel(a,e,i,u,o,y), appends "yay" at the end of 
        this 
        letter.
    * if letter starts with consonant, moves the consonant to the end, 
        and appends "ay"at the end.
''')
print('Enter the English message to translate into pig latin:')
message = input()
VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
piglatin_book()
piglatin_customized()





