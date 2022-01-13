# --- Day 5: Hydrothermal Venture ---

# You come across a field of hydrothermal vents on the ocean floor! 
# These vents constantly produce large, opaque clouds, so it would be 
# best to avoid them if possible.

# They tend to form in lines; the submarine helpfully produces a list of
# nearby lines of vents (your puzzle input) for you to review. Each line 
# of vents is given as a line segment in the format x1,y1 -> x2,y2 where 
# x1,y1 are the coordinates of one end the line segment and x2,y2 are the 
# coordinates of the other end. These line segments include the points at 
# both ends. 

# Wczytywanie danych działa tak samo jak w dniu 4, podobnie też użyto tablicy
# 1000 na 1000 z numpy wypełniając ją zerami (tyle danych zostało podanych). W głównej 
# pętli iteracja odbywa się po wszystkich rzędach, wewnątrz jej znajdują się warunku 
# sprawdzające czy podane punkty się zgadzają to znaczy czy wystąpiła sytuacja 
# jak 1,1 -> 1,3 lub 9,7 -> 7,7 gdzie x1 = x2 bądź y1 = y2. Dalej w zależności od 
# tego czy pierwsza czy druga współrzędna jest większa wykonana będzie zagnieżdżona 
# pętla iterują się po tych współrzędnych do wartości większej, zwiększając wartość
# tej komórki w tablicy temp o 1. Po zakończeniu pętli liczę ile jest elementów wewnątrz
# tej tablicy o wartości większej niż 2.

# Your puzzle answer was 7473.

import numpy as np
temp = np.zeros((1000,1000), dtype='int')

def main ():
    with open("datav2.txt","r") as f:
        points = f.read().splitlines()
    lines = [list( map(int,i) ) for i in [x.split() for x in points]]
    for x1, y1, x2, y2 in lines:
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                temp[y1][x] += 1

        elif x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                temp[y][x1] += 1
    count = np.count_nonzero(temp >= 2)
    return count

if __name__ == '__main__':
    answer = main()
    print(answer)
 
