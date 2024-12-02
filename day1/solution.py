list1 = []
list2 = []

with open('input.txt') as f:
    for line in f:
        a = line.strip().split()
        list1.append(int(a[0]))
        list2.append(int(a[1]))

list1.sort()
list2.sort()

sum = 0
for i in range(len(list1)):
    sum += abs(list1[i] - list2[i])

print(sum)