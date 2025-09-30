def permute_a_palindrome (input):
    odd_character = ""
    for character in input:
        occurrence = input.count(character)
        if not odd_character and occurrence % 2 != 0:
            odd_character = character
        elif odd_character == character:
            continue
        elif occurrence % 2 != 0:
            return False
        else:
            continue
    return True