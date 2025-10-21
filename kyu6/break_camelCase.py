def solution(string):
    clean_string =""
    for letter in string:
        if letter.isupper():
            clean_string += " " + letter
        else:
            clean_string += letter
    return clean_string
