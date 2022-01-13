# --- Day 3: Binary Diagnostic ---

# The diagnostic report (your puzzle input) consists of a list of binary numbers 
# which, when decoded properly, can tell you many useful things about the 
# conditions of the submarine. The first parameter to check is the power 
# consumption.

# You need to use the binary numbers in the diagnostic report to generate 
# two new binary numbers (called the gamma rate and the epsilon rate). The 
# power consumption can then be found by multiplying the gamma rate by the 
# epsilon rate.

# Each bit in the gamma rate can be determined by finding the most common 
# bit in the corresponding position of all numbers in the diagnostic report. 

# Wczytywanie danych działa tak samo jak w 1 i 2 dniu. Dalej w pętli wykonującej się
# 12 razy czyli tyle ile kolumn otrzymałem w swoich danych sprawdzam każdy jej 
# element ustalając ilość 0 oraz 1. W zależności od niej, jeżeli jest więcej zer to do 
# tablicy gamma dodane zostanie 0 a do tablicy epsilon 1, jeżeli jest więcej lub tyle samo
# jedynek to do tablicy gamma dodane zostanie 1 a do tablicy epsilon 0. Dalej używam 
# metody reduce z functools żeby zmienić jej wartość na decymalną i wyświetlam wynik.

# Your puzzle answer was 2954600.

from functools import reduce

f = open("data.txt","r")
points=[]
for line in f:
    points.append((line.rstrip("\n")))
one = zero = i = 0
gamma = []
epsilon = []
for y in range(12):
    for x in points:
        if int(x[y]) == 1: one += 1
        else : zero += 1
    if zero > one: 
        gamma.append(0) 
        epsilon.append(1)
    else : 
        gamma.append(1)
        epsilon.append(0)
    one = zero = 0
one = reduce(lambda a,b: 2*a+b, gamma)
zero = reduce(lambda a,b: 2*a+b, epsilon)
print(one*zero)