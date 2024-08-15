import utils as ut


def avoids(word, banid_letters):
    for letter in word:
        if letter in banid_letters:
            return False

    return True


def main():
    fin = open('words.txt')
    count = 0

    forbidden_letters = str(input('Informe as letras probidas: '))

    for line in fin:
        word = line.strip()
        word = ut.remove_space(word)

        if avoids(word, forbidden_letters):
            count += 1
            print(word)

    print(f'O número de plavras que não contém a(s) letra(s) [{forbidden_letters}] é de [{count}]')


main()