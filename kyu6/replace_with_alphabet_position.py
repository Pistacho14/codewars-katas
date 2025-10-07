def alphabet_position(text):
    encoded_text = ''
    for character in text:
        if character.isalpha():
            encoded_text = encoded_text + ' ' + str(ord(character.lower()) - 96)
    return encoded_text.lstrip()
