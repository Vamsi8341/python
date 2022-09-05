a = [10,20,30,20,10,50,60,40,80,50,40]

rep_items = set()
uniq_items = []
for x in a:
    if x not in rep_items:
        uniq_items.append(x)
        rep_items.add(x)

print(rep_items)
