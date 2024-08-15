import utils as ut

#função resposavel por limpar o terminal
def clean_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

#verifica as palavras que não tem as letras informadas
def avoids(word, banid_letters):
    for letter in word:
        if letter in banid_letters:
            return False

    return True

#verifica se as letras da palavra está em ordem alfabetica
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


#verifica se a palavra não tem 'e'
def has_no_e(word):
    formated_word = ut.remove_space(word)

    for letter in formated_word:
        if letter == 'e':
            return False
        
    return True

#verifica se a palavra é composta apenas pelas letras informadas e retorna verdadeiro ou falso
def uses_only(word,letters):
    for l in letters:
        for c in word:
            if (l not in word) or (c not in letters): 
                return False
        
    return True

#retorna se a palvra tem certas letras
def uses_all(word,letters):
    for l in letters:
        if l not in word: 
            return False
        
    return True


#menuzinho 
def menu_design():
    return """
        ======== WORD-PLAY ========
[ 1 ] - LOAD FILE
[ 2 ] - PALAVRAS COM MAIS DE 20 LETRAS
[ 3 ] - PALAVRAS SEM "X" LETRA
[ 4 ] - PALAVRAS COM MAIS DE "X" LETRAS
[ 5 ] - LETRAS PROIBIDAS
[ 6 ] - PALAVRA FORMADA APENAS POR "X" LETRAS
[ 7 ] - LETRAS OBRIGATÓRIAS
[ 8 ] - ORDEM ALFABETICA
[ 9 ] - PALAVRAS SEM A LETRA "E"
[ 0 ] - SAIR
    """


def main():
    #Exibição do menu
    menu = menu_design()

    print(menu)

    choice = int(input("Escolha uma Opção: "))


    while choice != 1 and choice != 0:

        print("Não é possivel realizar a ação selecionada antes do carregamento do arquivo.")
        choice = int(input("Escolha uma Opção: "))

    if choice == 1:
            
        file_name = str(input('''Informe o Arquivo [Ex: arquivo.txt]
:'''))


    while choice != 0:
        
        clean_screen()
        fin = open(file_name)
        print(menu)

        choice = int(input("Escolha uma Opção: "))

        if choice == 1:
            file_name = str(input('''Informe o Arquivo [Ex: arquivo.txt]
:'''))
            
            
        elif choice == 2: 
                for line in fin:
                    word = line.strip()

                    formated_word = ut.remove_space(word)

                    if len(formated_word) > 20:
                        print(formated_word)
        

        elif choice == 3:
            letter = str(input('Informe a Letra: '))
            count_words = 0
            words_without_letter = 0
            
            for line in fin:
                count_words += 1

                word = line.strip()
                formated_word = ut.remove_space(word)

                if letter not in word:
                    words_without_letter += 1
                    print(word)

            percentage = words_without_letter / count_words * 100

            print(f'Um total de {percentage:.2f} % das palavras desse documento não possuem a letra [{letter}]')
        
        elif choice == 4:

            X = int(input("Digite a Quantidade de Letras das Palavras: "))
            for line in fin:
                word = line.strip()

                formated_word = ut.remove_space(word)

                if len(formated_word) > X:
                    print(formated_word)
        
        elif choice == 5:

            count = 0

            forbidden_letters = str(input('Informe as letras probidas: '))

            for line in fin:
                word = line.strip()
                word = ut.remove_space(word)

                if avoids(word, forbidden_letters):
                    count += 1
                    print(word)

            print(f'O número de plavras que não contém a(s) letra(s) [{forbidden_letters}] é de [{count}]')

        #isso funciona tá
        elif choice == 6:
            count = 0

            letters = str(input('Informe as letras que vão compor a palavra: '))

            for line in fin:
                word = line.strip()
                word = ut.remove_space(word)

                if uses_only(word,letters):
                    count += 1
                    print(word)

            print(f'O número de palavras formadas apenas pelas letras [{letters}] é de [{count}]')
            

        elif choice == 7:
            count = 0

            letters = str(input('Informe as letras obrigatorias: '))

            for line in fin:
                word = line.strip()
                word = ut.remove_space(word)

                if uses_all(word,letters):
                    count += 1
                    print(word)

            print(f'O número de palavras que possuem as letras [{letters}] é de [{count}]')

        
        elif choice == 8:
            count_abecedarian = 0

            for line in fin:
                word = line.strip()
                word = ut.remove_space(word)

                if is_abecedarian(word):
                    count_abecedarian += 1
                    print(word)
            
            print(f'Um total de [{count_abecedarian}] palavras estão em ordem alfabetica')

        
        elif choice == 9:
            pass


        elif choice < 0 or choice > 9:
            print("Escolha uma opção válida.")

        #limpa telinha
        clear = input('\033[32mPRESSIONE ENTER\033[m')

    print('[ PROGRAMA FINALIZADO ]')        


main()