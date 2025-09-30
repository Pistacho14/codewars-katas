def duplicate_count(text):
    counter = 0
    for letter in set(text.lower()):
        if text.lower().count(letter) > 1:
            counter += 1
    return counter
