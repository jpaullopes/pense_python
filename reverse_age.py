from utils import my_string_zfill

#sinceramente professor, nã consegui, não encontrei a lógica pra essa questão 
#minha cabeça tá pifando já
#Desisto dela T_T T_T



#função que reverte um palavra
def reverse_characters(word):
   new_word = ''
   for l in str(word):
      new_word = l + new_word
   return new_word


def reverse_age():
    count = 0
    years_mother = years_child = 100

    while years_mother > 1:
       years_child -= 1 
       years_mother -= 1

       if reverse_characters(my_string_zfill(str(years_mother),2)) == my_string_zfill(str(years_child),2):
            count += 1


def main():

    casos = reverse_age()
 
    print(casos)


main()