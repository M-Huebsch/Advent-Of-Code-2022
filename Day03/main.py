# Advent of Code Day3
# Liste einlesen, Zeichen in Zeile 50/50 splitten, welches Zeichen doppelt, Zahlenwert der Zeichen berechnen

import string

length = 0
buchstaben = []
werte = 0

with open("Day03/input.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]

# Part 1
werte = 0

for line in data:
    length = len(line)//2
    for i in line[0:length]:
        if i in line[length:]:
            werte += string.ascii_letters.index(i) + 1
            break
           
print (werte)

# Part 2

werte2 = 0

for i in range (0,len(data),3):
    s1, s2, s3 = [set(elf) for elf in data[i : i+3]]
    werte2 += string.ascii_letters.index((s1 & s2 & s3).pop()) + 1

print (werte2)

