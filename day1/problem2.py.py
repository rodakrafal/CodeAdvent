# # --- Day 1: Sonar Sweep ---

# --- Part Two ---

# Consider sums of a three-measurement sliding window. 
# Again considering the above example

# Podobnie jak w zadaniu 1 podane dane odczytuje w pętli oraz zapisuje do tablicy, następnie w
# kolejnej pętli iteruje po wszystkich jej elementach. Podczas każdej iteracji sprawdzam warunki
# "filtrujące" odpowiednie elementy. Mianowicie aby nie wyjść poza zakres tablicy wywołuje się 
# bloki w warunkach if, odpowiednio sprawdzające jej ilość. Dla przykładu jeżeli będziemy na 
# ostatnim elemencie to nie będziemy sprawdzać następnych 2 elementów tylko ostatni. Reszta kodu
# to tylko dodawanie jeżeli średnia zmiennej point jest wieksza od zmiennej tmp.

# Your puzzle answer was 1457.

f = open("data.txt","r")
points=[]
for line in f:
    points.append(int(line))
tmp = i = 0
count = -1

for x in points:
    if(i >= len(points)):
        point = points[i]
    if(i == len(points)-2): 
        point = points[i] + points[i+1]
    if(i < len(points)-2):
        point = points[i] + points[i+1] + points[i+2]
    if(point > tmp):
        count +=1
    tmp = point
    i += 1

print(count)