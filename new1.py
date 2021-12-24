# dict1 = {3:'c',2:'b',5:'e',1:'a',4:'d'}
# dict2 = {3:'z',1:'ay', 8: 'h', 10:'j'}
# print(dict2[3])

# for keys in dict2:
#     dict1.update({keys : dict2[keys]})
      
# print (dict1)

c = input()
b = input()

def count(a):
    d1={}
    for x in range (len(a)):
        if a[x] in d1:
            d1.update({a[x] : d1[a[x]]+1})
        else:
            d1.update({a[x] : 1})
    return(d1)

d3 ={}
d2 ={}
d3 = count(c.lower())
d2 = count(b.lower())

if d2 == d3:
    print(c,'equals',b)
else:
    print(c,'not equals to',b)


























