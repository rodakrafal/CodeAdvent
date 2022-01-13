# --- Day 3: Binary Diagnostic ---
# --- Part Two ---

# Next, you should verify the life support rating, which can be determined by multiplying 
# the oxygen generator rating by the CO2 scrubber rating.

# Both the oxygen generator rating and the CO2 scrubber rating are values that can be found 
# in your diagnostic report - finding them is the tricky part. Both values are located 
# using a similar process that involves filtering out values until only one remains. 
# Before searching for either rating value, start with the full list of binary numbers 
# from your diagnostic report and consider just the first bit of those numbers. Then:

# - Keep only numbers selected by the bit criteria for the type of rating value 
#   for which you are searching. Discard numbers which do not match the bit criteria.
# - If you only have one number left, stop; this is the rating value 
#   for which you are searching.
# - Otherwise, repeat the process, considering the next bit to the right.

# Polecenie jest długie do znalezienia pod tym adresem: https://adventofcode.com/2021/day/3

# Wczytywanie danych działa tak samo jak w 1 zadaniu, dodatkowo do 2 tablic o odpowiednio nazwach
# oxygen oraz co2 skopiowana została zawartość tablicy points zawierająca wczytane dane aby
# wykonywać na nich odpowiednie operacje. Dalej w dwóch pętlach wykonujących się
# 12 razy czyli tyle ile kolumn otrzymałem w swoich danych sprawdzam każdy jej 
# element ustalając ilość 0 oraz 1. W zależności od wartości którą chce otrzymać będą tam występować
# inne warunki sprawdzania. Podczas sprawdzania C02 sprawdzamy ilość najrzadziej występującego
# elementu, podobnie jak w wariancie 1 iterować będziemy po kolumnach. Sprawdzając zawartość co2
# jak wspomniałem wybieramy najrzadziej występujący element, usuwając częściej występujące elementy
# to znaczy jeżeli rzadziej występuje 0 to wtedy usuwany z listy co2 elementy posiadające w tym 
# miejscu wartość 1. Dzięki temu filtrujemy listę na końcu dostając wartość binarną C02. Druga pętla
# sprawdzająca ilość tlenu działa analogicznie, tylko w tym miejscu używam metody remove, a nie jak
# w poprzedniej pętli "podmieniania" tablicy. Wynik nie jest wyświetlany jako gotowy, trzeba go trochę
# przerobić, mianowicie wypisuje obydwie wartości jako liczby binarne. Wystarczy je ręcznie zamienić
# na decymalne i pomnożyć.

# Your puzzle answer was 1662846.

with open("data.txt","r") as f:
    points = f.read().splitlines()

oxygen = list(points)
co2 = list(points)

for y,_ in enumerate(points[0]):
    if(len(oxygen)==1): break
    one = 0
    zero = 0
    for x in oxygen:
        if x[y] == '1': one += 1
        else : zero += 1
    if one >= zero: choice = '1'
    else: choice = '0'
    oxygen = [x for x in oxygen if x[y] == choice]

for y,_ in enumerate(points[0]):
    if(len(co2)==1): break
    one = zero = 0
    for x in co2:
        if x[y] == '1': one += 1
        else : zero += 1
    if one >= zero : choice = '0'
    else: choice = '1'
    for x in list(co2):  
        if x[y] != choice:
            co2.remove(x) 

print(oxygen)
print(co2)

