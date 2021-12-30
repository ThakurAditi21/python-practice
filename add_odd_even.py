n = int(input())
c1 =0
c2 =0
for x in range (n):
    if x%2 == 0:
        c1 = c1+x
    else:
        c2 = c2+x
if c1>c2:
    diff= c1-c2
    
else:
    diff=c2-c1

print(diff)