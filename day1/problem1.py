# --- Day 1: Sonar Sweep ---

# Count the number of times a depth measurement increases from the 
# previous measurement. How many measurements are larger than the previous
# measurement?

# Proste zadanie polegające na odczytaniu podanych danych i sprawdzeniu w pętli
# ilości wartości które są większe od poprzedniej wartości. Nic specjalnie do 
# tłumaczenia

# Your puzzle answer was 1390.

f = open("data.txt","r")
points=[]
for line in f:
    points.append(int(line))
tmp = 0
count = -1
for x in points:
    if x > tmp:
        count += 1
    tmp = x
print(count)
