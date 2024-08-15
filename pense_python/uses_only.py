import utils as ut

#verifica se a palavra é composta apenas pelas letras informadas e retorna verdadeiro ou falso
def uses_only(word,letters):
    for l in letters:
        for c in word:
            if (l not in word) or (c not in letters): 
                    return False
        
    return True


def main():
    fin = open('words.txt')
    count = 0

    letters = str(input('Informe as letras que vão compor a palavra: '))

    for line in fin:
        word = line.strip()
        word = ut.remove_space(word)

        if uses_only(word,letters):
            count += 1
            print(word)

    print(f'O número de palavras formadas pelas letras [{letters}] é de [{count}]')


main()