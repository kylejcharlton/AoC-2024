rules = []
updates = []
with open('input.txt') as f:
    end_of_rules = False
    for line in f:
        l = line.strip()
        if len(l) == 0:
            end_of_rules = True
            continue
        if (not end_of_rules):
            rules.append(l)
        else:
            updates.append(l)

rule_order = []
for rule in rules:
    rule_order.append(rule.split("|"))

total = 0
for update in updates:
    u = update.split(",")
    is_sorted = True
    for rule in rule_order:
        if rule[0] in u and rule[1] in u and u.index(rule[0]) > u.index(rule[1]):
            is_sorted = False
            break

    if is_sorted:
        total += int(u[len(u) // 2])

print(total)

total2 = 0
for update in updates:
    u = update.split(",")
    wasnt_sorted = False
    while True:
        is_sorted = True
        for rule in rule_order:
            if rule[0] in u and rule[1] in u and u.index(rule[0]) > u.index(rule[1]):
                del u[u.index(rule[0])]
                u.insert(u.index(rule[1]), rule[0])
                is_sorted = False
                wasnt_sorted = True
        if is_sorted:
            break

    if wasnt_sorted:
        total2 += int(u[len(u) // 2])

print(total2)