import re

lines = []
with open('input.txt') as f:
    for line in f:
        lines.append(line.strip())

total = 0

for line in lines:
    i = 0
    while i < len(line):
        if line[i:].startswith("mul("):
            start = i+4
            j = start
            end = -1
            while j < len(line):
                if line[j] == ")":
                    end = j
                    break
                j += 1

            if end != -1:
                capture = line[start:end]
                tokens = capture.split(",")
                if (len(tokens) == 2 and re.match(r"^\d{1,3}$", tokens[0]) and re.match(r"^\d{1,3}$", tokens[1])):
                    total += int(tokens[0]) * int(tokens[1])
                i = i+4
        i += 1

print(total)