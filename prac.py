dict = {1:'one',2:'two',7:'seven',4:'four',60:'sixty',50:'fifty',40:'forty'}

x = []
t = 1
while t<4:
    y = int(input())
    x.append(y)
    t+=1

for z in range (len(x)):
    if x[z] in dict:
        dict.pop(x[z])
print(dict)


