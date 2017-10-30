def reverse(text):
    length = len(text)
    result = ""

    while length != 0:
        length = length - 1
        result = result + text[length]
    return result



reverse("the!")