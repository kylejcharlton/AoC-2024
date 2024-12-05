lines = []
with open('input.txt') as f:
    for line in f:
        lines.append(line.strip())

total = 0
for i in range(len(lines[0])):
    for j in range(len(lines)):
        if i < len(lines[0]) - 3 and (lines[j][i:i+4] == "XMAS" or lines[j][i:i+4] == "SAMX"):
            total += 1
        if j < len(lines) - 3:
            possibleXmas = lines[j][i] + lines[j+1][i] + lines[j+2][i] + lines[j+3][i]
            if possibleXmas == "XMAS" or possibleXmas == "SAMX":
                total += 1
        if i < len(lines[0]) - 3 and j < len(lines) - 3:
            possibleXmas = lines[j][i] + lines[j+1][i+1] + lines[j+2][i+2] + lines[j+3][i+3]
            if possibleXmas == "XMAS" or possibleXmas == "SAMX":
                total += 1
        if i >= 3 and j < len(lines) - 3:
            possibleXmas = lines[j][i] + lines[j+1][i-1] + lines[j+2][i-2] + lines[j+3][i-3]
            if possibleXmas == "XMAS" or possibleXmas == "SAMX":
                total += 1

print(total)

total2 = 0
for i in range(1, len(lines[0]) - 1):
    for j in range(1, len(lines) - 1):
        if lines[j][i] == "A":
            possibleMas1 = lines[j-1][i-1] + lines[j][i] + lines[j+1][i+1]
            possibleMas2 = lines[j+1][i-1] + lines[j][i] + lines[j-1][i+1]
            if (possibleMas1 == "MAS" or possibleMas1 == "SAM") and (possibleMas2 == "MAS" or possibleMas2 == "SAM"):
                total2 += 1

print(total2)