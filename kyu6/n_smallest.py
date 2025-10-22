def first_n_smallest(lista, elementos_max):
    lista_elem_peque = sorted(lista)[:elementos_max]
    lista_definitiva = []
    [ lista_definitiva.append(elemento) or lista_elem_peque.remove(elemento) for elemento in lista if elemento in lista_elem_peque ]
    return lista_definitiva
