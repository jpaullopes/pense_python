def remove_space(word):#função que retira os espaços em branco das palavras
    new_word = ''

    for character in word:

        if character != ' ':
            new_word += character
        else:
            continue

    return new_word


#função que verifica se tem a letra "e" na palavra
def has_no_e(word):
    formated_word = remove_space(word)

    for letter in formated_word:
        if letter == 'e':
            return False
        
    return True


def main():
    #abertura do arquivo
    fin = open("words.txt")

    words_without_letter_e = 0
    count_words = 0

    for line in fin:
        word = line.strip()
        word = remove_space(word)

        count_words += 1
        
        if has_no_e(word):
            print(word)
            words_without_letter_e += 1

    percentage = words_without_letter_e / count_words * 100

    print(f'Um total de {percentage:.2f} % das palavras não contém a letra "e".')


main()