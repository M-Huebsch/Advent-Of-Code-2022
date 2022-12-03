# Advent of Code Day1
# Liste lesen, Absätze zusammenrechnen, Max suchen

numbers = []
with open("Day1/input.txt", "r") as file:
    for line in file:
        line = line.rstrip("\n")
        numbers.append(line)

maxcalories = []
calories = 0

for j in numbers:
    if j == "":
        maxcalories.append(calories)
        calories = 0 #reset
    else:
        calories = calories + int(j)

print ("Max: ", max(maxcalories))
print ("Sum Max 3: ", sum(sorted(maxcalories, reverse = True)[0:3]))