import random
from collections import Counter
from turtle import write_docstringdict

Auta = '''bmw mercedes ford mazda kia rollsroyce ferrari lamborghini fiat 
corvette alfaromeo honda audi bugatti wolkswagen smart'''

Auta = Auta.split(' ')
word = random.choice(Auta)



if __name__ == '__main__':
        print('Zgadnij slowo! Kategoria: Auta' )
        for i in word:
            print('_', end=' ')
        print()

        playing = True
        letterGuessed = ''
        szanse = len(word) + 2
        correct = 0
        flag = 0
        try:
            while (szanse != 0) and flag == 0:
                print()
                szanse -= 1
                try:
                    guess = str(input('Wpisz jedna litere: '))
                except:
                    print('Wpisz tylko jedna litere!')
                    continue
                if not guess.isalpha():
                    print('Prosze o wpisanie jedynie liter!')
                    continue
                elif len(guess) > 1:
                    print('Prosze wpisac jedna litere nie kilka!')
                    continue
                elif guess in letterGuessed:
                    print('Juz wpisales ta litere')
                    continue
                if guess in word:
                    k = word.count(guess)
                    for _ in range(k):
                        letterGuessed += guess
                for char in word:
                    if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                        print(char, end=' ')
                        correct += 1
                    elif (Counter(letterGuessed) == Counter(word)):
                        print("\nOdpowiedz to: ", end=' ')
                        print(word)
                        flag = 1
                        print('Gratulacje, wygrales!\n')
                        break
                    else:
                        print('_', end=' ')
            if szanse <= 0 and (Counter(letterGuessed) != Counter(word)):
                print()
                print('\nPrzegrales!, sproboj ponownie..')
                print('Slowem bylo: {}!'.format(word))
        except KeyboardInterrupt:   
            print()
            print('Narazie!,sproboj ponownie!')
            exit()