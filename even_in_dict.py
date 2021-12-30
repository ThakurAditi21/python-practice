num = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}

for key in num:
    l = []
    for x in num[key]:
        if x%2 !=0:
            l.append(x)
    for y in l:
        num[key].remove(y)

print(num)

