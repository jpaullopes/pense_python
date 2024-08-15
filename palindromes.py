from utils import my_string_zfill

#função que retorna qual o valor máximo um númeor tem com certa quantidade de digitos
def max_number(digits):
    number_max = ''
    
    for d in range(digits):
        number_max += '9'
    number_max = int(number_max)

    return number_max


#função que reverte um palavra
def reverse_characters(word):
   new_word = ''
   for l in word:
      new_word = l + new_word
   return new_word


#função que retorna True ou False se a palavra for palindrome
def palindrome(word):

    reverse_word = reverse_characters(word)

    if reverse_word == word:
        return True
    return False


def main():
    digits = int(input('Informe a quantidade de digitos os núemeros terão: '))

    number = ''
    count = count_palindromes = 0

    while count < max_number(digits):
        count += 1
        #a explicação da função está na utils
        number = my_string_zfill(str(count),digits)

        if palindrome(number):
            count_palindromes += 1
            print(number)

    print(f'Um total de {[count_palindromes]} números são palindromes.')


main()