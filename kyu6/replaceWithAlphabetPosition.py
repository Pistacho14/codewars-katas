def alphabet_position(text):
    code = ''
    for character in text:
        if character.isalpha():
            code = code + ' ' + str(ord(character.lower()) - 96)
            
    return code.rstrip().lstrip()