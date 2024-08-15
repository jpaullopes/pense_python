import utils as ut

#função que verifica se a palavra informada possui as letras informadas
def uses_all(word,letters):
    for l in letters:
        if l not in word: 
            return False
        
    return True


def main():
    fin = open('words.txt')
    count = 0

    letters = str(input('Informe as letras obrigatorias: '))

    for line in fin:
        word = line.strip()
        word = ut.remove_space(word)

        if uses_all(word,letters):
            count += 1
            print(word)

    print(f'O número de palavras que possuem as letras [{letters}] é de [{count}]')


main()