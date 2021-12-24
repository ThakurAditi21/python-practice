n = int(input())
team1=[]
team2=[]
diff =[]
lead =[]
for x in range (n):
 
    team1.append(int(input()))
    team2.append(int(input()))

for y in range (n):

    if team1[y]>team2[y]:
        diff.append(team1[y] - team2[y])
        lead.append(1)
    else:
        diff.append(team2[y] - team1[y])
        lead.append(2)
for n in range (len(diff)-1):
    if diff[n]<diff[n+1]:
        x =diff[n+1]
        y = n+1
    else:
        x=diff[n]
        y=n
print(lead[y],x)
    



 











