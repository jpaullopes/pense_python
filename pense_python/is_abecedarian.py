import utils as ut


def is_abecedarian(word):
    letters_list = []
    new_word = ''

    for l in word:
        letters_list.append(ord(l))

    letters_list = ut.my_sorted(letters_list)
    for n in letters_list:
        new_word += chr(n)
    
    if new_word == word:
        return True
    return False



def main():
    
    fin = open('words.txt')
    count_abecedarian = 0

    for line in fin:
        word = line.strip()
        word = ut.remove_space(word)

        if is_abecedarian(word):
            count_abecedarian += 1
            print(word)
    
    print(f'Um total de [{count_abecedarian}] palavras estão em ordem alfabetica')


main()