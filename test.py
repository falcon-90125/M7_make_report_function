grocery = {'Кабель ZMI USB - microUSB (AL600) 1 м черный': {1: 17, 2: 17, 3: 19, 4: 14, 5: 23, 6: 19, 7: 9}, 'ArtSpace Набор обложек для дневников и тетрадей 210х350 мм': {1: 13, 2: 22, 3: 17, 4: 13, 5: 23, 6: 20, 7: 8}}
print(grocery)
# lm = []
# for i in range(len(grocery[0])):
#     lm.append(0)
# print(lm)
# print(grocery.items()[0])
grocery_keys = []
for i in grocery.keys():
    grocery_keys.append(i)
print(grocery_keys)

for i in grocery_keys:
    print(grocery[i])

print(grocery['Кабель ZMI USB - microUSB (AL600) 1 м черный'].keys())
