# --- Day 4: Giant Squid ---

# You're already almost 1.5km (almost a mile) below the surface of the ocean, 
# already so deep that you can't see any sunlight. What you can see, however, 
# is a giant squid that has attached itself to the outside of your submarine.

# Maybe it wants to play bingo?

# Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. 
# Numbers are chosen at random, and the chosen number is marked on all boards 
# on which it appears. (Numbers may not appear on all boards.) If all numbers 
# in any row or any column of a board are marked, that board wins. (Diagonals 
# don't count.)

# Z tego rozwiązania jestem chyba najbardziej dumny. Wczytanie danych do tablicy
# jest nareszcie wykonane "po wężowemu", na początku deklarowana jest również 
# zmienna bingo_cards będąca tablicą 3d z numpy w której przetrzymywane będą wszystkie
# tablice bingo - lista 2d tablic bingo. Do zmiennej numbers zapisywane są kolejno 
# losowane numery bingo, a w pierwszej pętli metody main do wcześniej wspomnianej tablicy 
# bingo cards wrzucane są przekazane w danych tablice bingo. W następnej pętli
# a raczej pętli pętli pętli (troche to zagmatwane) sprawdzana jest obecność bingo.
# W uproszczeniu przechodzimy po kolejnych elementach z tablicy numbers zawierającej
# kolejno wylosowane numery i sprawdzamy ich obecność w tablicach bingo. Jeżeli wykryta
# zostanie obecność bingo w rzędzie bądź kolumnie to zwrócona zostanie tablica zawierająca
# numer wygranej tablicy bingo oraz wygrany numer. Dalej w pętli policzymy wartość wszystkich
# nie wylosowanych numerów którą następnie pomnożymy przez wygraną liczbę. Wynik jest
# wypisywany w konsoli 

# Your puzzle answer was 55770.

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

    for num in numbers:    
        for x,y in enumerate(bingo_cards):
            for inx, val in enumerate(y):
                if int(num) in val : bingo_cards[x][inx][np.where(val == int(num))[0][0]] = -1
                if np.sum(val) == -5 : return [x,num]
            for i in range(5):
                if np.sum(y[:,i]) == -5 : return [x,num]      

if __name__ == '__main__':
    tmp = main()
    sum = 0
    print(tmp)
    for x in bingo_cards[tmp[0]]:
        for y in range(5):
            if x[y] != -1: sum +=x[y]
    print(sum*int(tmp[1]))
