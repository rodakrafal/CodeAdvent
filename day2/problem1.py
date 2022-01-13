# --- Day 2: Dive! ---

# It seems like the submarine can take a series of commands like forward 1, 
# down 2, or up 3:
# - forward X increases the horizontal position by X units.
# - down X increases the depth by X units.
# - up X decreases the depth by X units.

# Note that since you're on a submarine, down and up affect your depth, 
# and so they have the opposite result of what you might expect.

# Wczytywanie danych z pliku działa identycznie jak w poprzednim dniu, z różnicą
# że tworzona jest tym razem tablica 2d. Dalej w pętli sprawdzany jest 1 element 
# z tablicy, w zależności od jego wartości a raczej napisu zmieniona zostanie wartość
# położenia wzdłuż bądź wszerz. Na koniec wypisany jest iloczyn tych wartości. 

# Your puzzle answer was 1990000.

f = open("data.txt","r")
points=[]
for line in f:
    points.append((line.rstrip("\n").split(" ")))
horizontal = depth = 0
for x in points:
    if x[0] == "forward": horizontal += int(x[1])
    if x[0] == "up": depth -= int(x[1])
    if x[0] == "down": depth += int(x[1])
print(horizontal * depth)

