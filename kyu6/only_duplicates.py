def only_duplicates(st):
    clean_st = ''
    for letra in st:
        if st.count(letra) >= 2:
            clean_st += letra
        else:
            continue    
    return clean_st

only_duplicates('abccdefee')