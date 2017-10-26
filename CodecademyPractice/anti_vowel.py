def anti_vowel(text):
    #Ensure proper input
    print(str(text))


    #gets the length of the input
    length = len(str(text))
    print(length)

    #Creates the test case list
    vowel = ["A","a","E", "e", "I", "i", "O", "o", "U", "u"]

    #Creates the input as a list
    result = list(text)
    print(result)

    #For loop to check each instance
    for i in range(0, length):
        if text[i] in vowel:
            print(True)
            result.remove(text[i])
            print(result)
        answer = ''.join(result)
    return(answer)



anti_vowel("Hey Look Words!")