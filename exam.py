t = int(input())
asci=[]
asci2=[]
for x in range (t):
    val = input()
    asci.append(val)

for y in range (len(asci)):
    val2=ord(asci[y])
    asci2.append(val2)
for z in range (len(asci2)):
    print('ascii value of',asci[z],'is',asci2[z])
    if asci2[z]%2 == 0:
        print(asci2[z],'is even number')
    else:
        print(asci2[z],'is odd number')
    count=0
    for n in range (2,asci2[z]):
        if asci2[z]%n == 0:
            count+=1
    if count==0:
        print(asci2[z],'is prime number')
    else:
        print(asci2[z],'is composite number')
    fact = 1
    i=1
    while i<=asci2[z]:
        fact = fact*asci2[z]
        i+=1
    print('factorial of',asci[z],'is :',fact)


    


    

    



    
