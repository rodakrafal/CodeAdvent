# --- Day 4: Giant Squid ---
# --- Part Two ---

# On the other hand, it might be wise to try a different strategy: let the giant squid win.

# You aren't sure how many bingo boards a giant squid could play at once, so 
# rather than waste time counting its arms, the safe thing to do is to figure 
# out which board will win last and choose that one. That way, no matter which 
# boards it picks, it will win for sure.

# In the above example, the second board is the last to win, which happens 
# after 13 is eventually called and its middle column is completely marked. 
# If you were to keep playing until this point, the second board would have 
# a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

# Figure out which board will win last. Once it wins, what would its final score be?

# Wczytywanie danych oraz ogólna struktura je przetrzymująca jest identyczna jak w
# zadaniu 1 - tablica 3d będąca listą tablic bingo oraz do tego tablica zawierająca
# wszystkie wylosowane numery w bingo. W zadaniu 2 należało znaleźć ostatnią listę 
# bingo która wygra, dokonano w tym celu modyfikacji kodu poprzedniego zadania. 
# Mianowicie dodano warunek sprawdzający długość tymczasowej tablicy do której 
# zapisywałem numery (tylko raz) listy bingo która właśnie wygrała. W momencie 
# osiągnięcia przez tą tablice rozmiaru maksymalnego (100) zwrócony zostanie 
# ten wylosowany numer oraz ostatni element tablicy będący numerem ostatniej 
# tablicy bingo która wygrała. Dalej liczenie wyniku jest identyczne jak w zadaniu 1.

# Your puzzle answer was 2980.

import numpy as np
bingo_cards = np.zeros((100, 5, 5), dtype='int')

def main ():
    with open("data.txt","r") as f:
        points = f.read().splitlines()
    numbers = list(points)[0].split(",")
    insides= [x.split() for x in points if x != "" and x != points[0]]

    i = 0
    for x,_ in enumerate(bingo_cards):
        for y in range(5):
            bingo_cards[x][y] = insides[i]
            i+=1
    tmp = []
    for num in numbers:    
        for x,y in enumerate(bingo_cards):
            for inx, val in enumerate(y):
                if int(num) in val : bingo_cards[x][inx][np.where(val == int(num))[0][0]] = -1
                if np.sum(val) == -5 : 
                    if x not in tmp: tmp.append(x)
                    if len(tmp) == 100 : return [tmp[99], num]
            for i in range(5):
                if np.sum(y[:,i]) == -5 : 
                    if x not in tmp: tmp.append(x)   
                    if len(tmp) == 100 : return [tmp[99], num]

if __name__ == '__main__':
    tmp = main()
    sum = 0
    print(tmp)
    for x in bingo_cards[tmp[0]]:
        for y in range(5):
            if x[y] != -1: sum +=x[y]
    print(sum*int(tmp[1]))
