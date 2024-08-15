import utils as ut
#tentei muito essa e não tava dando certo, no final tive que pedir ajuda do gpt...:(

#retorna True ou False se veirem tres duplas letas seguidas an palavra
def tri_double_letters(word):
    count_double_letters = 0
    count = 0

    while count < len(word) - 1:

        if word[count] == word[count + 1]:
            count_double_letters += 1
            count += 2  
            if count_double_letters >= 3:
                return True
        else:
            count_double_letters = 0
            count += 1
    
    return False

def main():
    fin = open(str(input("Informe o nome do arqivo: ")))
    count_words = 0

    for line in fin:
        word = line.strip()
        word = ut.remove_space(word)

        if tri_double_letters(word):
            count_words += 1
            print(word)
    
    print(f'Um total de [{count_words}] palavras possuem três letras duplas seguidas.')


main()
