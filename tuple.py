tup = (1, 20, 30)

# for x in tup:
#     print(x)

list_1 = list(tup)

list_2 = [x for x in tup]

list_3 = []

for x in tup:
    list_3.append(x)

print(list_3)