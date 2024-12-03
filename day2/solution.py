def check(arr):
    if len(arr) == 1:
        return True
    dir = int(arr[1]) - int(arr[0])
    good = True
    for i in range(1, len(arr)):
        diff = int(arr[i]) - int(arr[i-1])
        if abs(diff) > 3 or abs(diff) < 1:
            good = False
            break

        if (dir < 0 and diff > 0) or (dir > 0 and diff < 0):
            good = False
            break
    return good


reports = []

with open('input.txt') as f:
    for line in f:
        reports.append(line.strip().split())

safe = 0
for r in reports:
    if check(r):
        safe += 1

print(safe)

safe2 = 0
for r in reports:
    if len(r) == 1:
        safe2 += 1
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
        safe2 += 1
    else:
        r1 = r.copy()
        del r1[i]
        r2 = r.copy()
        del r2[i-1]
        r3 = r.copy()
        del r3[i-2]

        if check(r1) or check(r2) or check(r3):
            safe2 += 1

print(safe2)