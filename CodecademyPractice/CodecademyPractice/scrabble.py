score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}


def scrabble_score(word):

    #Ensure lower case and make the input a list
    lower_word = list(word.lower())
    print(lower_word)

    #Get the value of the lenth of the string to iterate through the loop
    length = len(word)
    print(length)

    #initialize the variable "result"
    result = 0

    # start the loop from 0 to the length of the input
    for i in range(0,length):

        #Ensure that the letters of the list are printing
        print(lower_word[i])

        #Assigning the given letter to a variable for readability
        letter = (lower_word[i])

        #Conditional asking if the letter is in the dictionary, if so, return the number and add it
        if letter in score:
            result = result + (score[letter])
            print(result)
    return(result)



scrabble_score("pie")


#Attempt to refactor the code to simpler solution. It's harder to read though!
def scrabble_score2(word):

    lowercase = list(word.lower())
    result = 0
    for i in range(0, len(word)):
       if lowercase[i] in score:
           result = result + (score[lowercase[i]])
    return result

scrabble_score2("Test")
