def find_needle(haystack):
    for item in haystack:
        if item == 'needle':
            return 'found the needle at position ' + str(haystack.index(item))
