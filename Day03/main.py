# Advent of Code Day3
# Liste einlesen, Zeichen in Zeile 50/50 splitten, welches Zeichen doppelt, Zahlenwert der Zeichen berechnen

import string

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
    werte += string.ascii_letters.index(letter) + 1

print (werte)