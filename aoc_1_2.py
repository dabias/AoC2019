
def fuel_needed(mass):
    baseFuel = (mass//3)-2
    if (baseFuel > 0):
        fuel = baseFuel+fuel_needed(baseFuel)
    else:
        fuel =0
    return fuel

totalFuel =0

with open('aoc_1_data.txt') as f:
    for line in f:
        totalFuel += fuel_needed(int(line))

print(totalFuel)
