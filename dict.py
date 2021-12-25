color= [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
dict={}
for x in range (len(color)):
    if color[x][0] in dict:
        dict[color[x][0]].append(color[x][1])
        
    else:
        dict.update({color[x][0] : [color[x][1]]})
        # dict.update({color[x][0] : color[x][1]})

print(dict)