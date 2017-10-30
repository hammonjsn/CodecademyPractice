def censor(text,word):
    word_list = text.split()
    print(word_list)
    print(word_list.count(word))
    new_word = ''

    for iword in word_list:
        if iword == word:
            print(True)
            for char in range(0,len(iword)):
                new_word = new_word + "*"
            #word_list.replace()
            word_list.insert(new_word)
        print(iword)
    print(word_list)




censor("i have a dog", "dog")

# Not working, can't figure out how to replace the old word with the new word "***"