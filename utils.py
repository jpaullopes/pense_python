def my_split(word):
    list = []

    for l in word:
        list.append(l)

    return list


def remove_space(word):#função que retira os espaços em branco das palavras
    new_word = ''

    for character in word:

        if character != ' ':
            new_word += character

    return new_word


#deus me abençoe nisso
#algoritmo de organização de array bobble sort
def bobble_sort(array):
    number_elements = len(array)

    for f in range(number_elements):
        for e in range(0,number_elements-f-1):
            if array[e] > array[e + 1]:
                array[e], array[e + 1] = array[e + 1], array[e]

    return array


#uma função que tenta replicar as funções básicas do metódo sort
def my_sorted(array):
    
    new_array = array.copy()

    for i in range(len(new_array)):
        new_array = bobble_sort(new_array)
    
    return new_array


#zfill replicado por min. ps: também pode ser usado como um ljust
def my_string_zfill(word,width, character = '0'):
    new_word = word
    while len(new_word) < width:
        new_word = character + new_word 
    
    return new_word

