# day 1 advent of code

maxCalories = 0
currCalories = 0
with open('day-1-input.txt') as f:
    for index, line in enumerate(f):
        strValue = line.strip()
        if len(strValue) == 0:
            maxCalories = currCalories if currCalories > maxCalories else maxCalories
            currCalories = 0
        else:
            currCalories += int(strValue)

print("max calories", maxCalories)
