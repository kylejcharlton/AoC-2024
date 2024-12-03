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
            start = i + 4
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
            i += 4
        else:
            i += 1

print(total)

total2 = 0

do = True
for line in lines:
    i = 0
    while i < len(line):
        if do and line[i:].startswith("mul("):
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
                    total2 += int(tokens[0]) * int(tokens[1])
            i += 4
        elif not do and line[i:].startswith("do()"):
            do = True
            i += 4
        elif do and line[i:].startswith("don't()"):
            do = False
            i += 7
        else:
            i += 1

print(total2)