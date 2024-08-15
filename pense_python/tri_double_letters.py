def tri_double_letters(word):
    new_word = word
    count_double = 0

    for l in range(len(new_word)-1):
        if new_word[l] == new_word[l + 1]:
            count_double += 1
            #new_word = new_word[l:]
            if count_double == 3:
                return True
            l += 1
        else:
            count_double = 0

    
    return  'fails'


def main():
    word_test = 'aacciicuo'

    blabla = tri_double_letters(word_test)

    print(blabla)

    #if tri_double_letters(word_test):
       # print(word_test)
    #else:
       # print('fail')


main()