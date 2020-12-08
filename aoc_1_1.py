
def fuel_needed(mass):
    fuel = (mass//3)-2
    return fuel

totalFuel =0

with open('adventofcoding1_1_data.txt') as f:
    for line in f:
        totalFuel += fuel_needed(int(line))

print(totalFuel)
