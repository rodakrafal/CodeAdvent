# --- Day 5: Hydrothermal Venture ---
# --- Part Two ---
# Unfortunately, considering only horizontal and vertical lines doesn't give 
# you the full picture; you need to also consider diagonal lines.

# Because of the limits of the hydrothermal vent mapping system, the 
# lines in your list will only ever be horizontal, vertical, or a diagonal 
# line at exactly 45 degrees. In other words:

# An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
# An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.

# Kod do 2 zadania bazuje na zadaniu 1, tak samo wykorzystuje tablice 2d z 
# numpy wypełnioną zerami oraz funkcję liczącą wartości większe od 2. Dołożony
# został warunek wewnątrz pętli sprawdzający czy wystepują linie pod kątem 45
# stopni gdzie mogą wystąpić aż 4 warunki.

# Your puzzle answer was 24164.

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

        else:
            if x1 > x2:
                x_range = x2 - 1
                cx = -1
            else:
                x_range = x2 + 1
                cx = 1
            y = y1
            if y1 > y2:
                cy = -1
            else:
                cy = 1
            for x in range(x1, x_range, cx):
                temp[y][x] += 1
                y += cy

    count = np.count_nonzero(temp >= 2)
    return count

if __name__ == '__main__':
    answer = main()
    print(answer)
 
