# Advent of Code Day2
# Liste einlesen, Schere Stein Papier Gewinn berechnen

#Sheet
sheet1 = {
    "A X" : 4,
    "A Y" : 8,
    "A Z" : 3,
    "B X" : 1,
    "B Y" : 5,
    "B Z" : 9,
    "C X" : 7,
    "C Y" : 2,
    "C Z" : 6,
}

score1 = 0
with open("Day2/input.txt", "r") as file:
    for line in file:
        line = line.strip()
        score1 = score1 + sheet1[line]
print (score1)

################################

sheet2 = {
    "A X" : 3,
    "A Y" : 4,
    "A Z" : 8,
    "B X" : 1,
    "B Y" : 5,
    "B Z" : 9,
    "C X" : 2,
    "C Y" : 6,
    "C Z" : 7,
}

score2 = 0
with open("Day2/input.txt", "r") as file:
    for line in file:
        line = line.strip()
        score2 = score2 + sheet2[line]
print (score2)
