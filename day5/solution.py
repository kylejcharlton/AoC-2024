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
    r = rule.split("|")
    if not r[0] in rule_order and not r[1] in rule_order:
        rule_order.append(r[0])
        rule_order.append(r[1])
    elif r[0] in rule_order and not r[1] in rule_order:
        rule_order.insert(rule_order.index(r[0]) + 1, r[1])
    elif not r[0] in rule_order and r[1] in rule_order:
        rule_order.insert(rule_order.index(r[1]), r[0])

total = 0
for update in updates:
    u = update.split(",")
    last_index = -1
    success = True
    for item in u:
        if item in rule_order:
            index = rule_order.index(item)
            print(index)
            if index < last_index:
                last_index = index
            else:
                success = False
                break
    if success:
        total += int(u[(len(u) // 2) + 1])

print(total)