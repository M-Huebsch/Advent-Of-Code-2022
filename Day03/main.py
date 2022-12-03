# Advent of Code Day3
# Liste einlesen, Zeichen in Zeile 50/50 splitten, welches Zeichen doppelt, Zahlenwert der Zeichen berechnen

length = 0
buchstaben = []
werte = 0

with open("Day03/input.txt", "r") as file:
    for line in file:
        line = line.strip()
        length = len(line)//2
        for i in line[0:length]:
            if i in line[length:]:
                buchstaben.append(i)
                break
            
for letter in buchstaben:
    if letter.islower():
        werte = werte + ord(letter) - 96
    else:
        werte = werte + ord(letter) - 38

print (werte)


