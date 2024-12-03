reports = []

with open('input.txt') as f:
    for line in f:
        reports.append(line.strip().split())

safe = 0

for r in reports:
    if len(r) == 1:
        safe += 1
        continue
  
    dir = int(r[1]) - int(r[0])

    good = True
    for i in range(1, len(r)):
        diff = int(r[i]) - int(r[i-1])
        if abs(diff) > 3 or abs(diff) < 1:
            good = False
            break

        if (dir < 0 and diff > 0) or (dir > 0 and diff < 0):
            good = False
            break

    if good:
        safe += 1

print(safe)