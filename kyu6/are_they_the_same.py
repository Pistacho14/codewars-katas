import math

def comp(array1, array2):
    if check_integrity(array1, array2):
        array1_copy = array1.copy()
        array2_copy = array2.copy()
        for element in array1:
            if element ** 2 in array2_copy:
                array1_copy.remove(element)
                array2_copy.remove(element**2)
                continue
            else:
                return False
        return True
    else:
        return False

def check_integrity(array1, array2):
    if array1 is not None and array2 is not None:
        if len(array1) == len(array2):
            return True
    else:
        return False
