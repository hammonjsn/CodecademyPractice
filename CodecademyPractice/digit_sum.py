###Codecademy Practice Makes Perfect "digit_sum"

def digit_sum(n):

    #print("It works")

    digit = []
    #print(digit)

    n_as_string = str(n)

    digit_maker = len(str(n))
    print(digit_maker)

    for i in range(0, digit_maker):
        print(i)
        digit.append(int(n_as_string[i]))
    print(digit)

    return sum(digit)


print(digit_sum(397))
