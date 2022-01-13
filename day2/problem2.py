# --- Day 2: Dive! ---
# --- Part Two ---

# In addition to horizontal position and depth, you'll also need to track a 
# third value, aim, which also starts at 0. The commands also mean something 
# entirely different than you first thought:
# - down X increases your aim by X units.
# - up X decreases your aim by X units.
# - forward X does two things:
#       - It increases your horizontal position by X units.
#       - It increases your depth by your aim multiplied by X.
# Again note that since you're on a submarine, down and up do the opposite 
# of what you might expect: "down" means aiming in the positive direction.

# Wczytywanie danych z pliku działa identycznie jak w wariancie 1. Dalej podobnie
# jak wcześniej w pętli podczas każdej iteracji sprawdzany jest 1 element tablicy
# 2d, w zależności od kierunku liczona zostanie odpowiednio głębokość oraz chyba to 
# długość (?). Zmianie w porównianiu do wariantu 1 uległ ruch do przodu gdzie mnożymy go przez
# aim który się zmienia w warunkach "up" i "down" o odpowienie wartości 2 elementu tablicy. 

# Your puzzle answer was 1975421260.

f = open("data.txt","r")
points=[]
for line in f:
    points.append((line.rstrip("\n").split(" ")))
horizontal = depth = aim = 0
for x in points:
    if x[0] == "forward": 
        depth += int(x[1]) * aim
        horizontal += int(x[1])
    if x[0] == "up": aim -= int(x[1])
    if x[0] == "down": aim += int(x[1])
print(horizontal * depth)

