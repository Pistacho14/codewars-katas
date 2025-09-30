def to_camel_case(text):
    camel_string = ""
    count = 0
    for letter in text:
        if letter.isalpha() and text[count].isalpha():
            if text[count - 1].isalpha():
                camel_string += letter
            else:
                camel_string += letter.upper()
            count += 1
        else:
            count += 1
            continue
    return camel_string