dict =  {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
dict3={}
for key in dict:
    dict3.update({dict[key].split()[0] : dict[key].split()[1]})
print(dict3)

 



# dict2 = {}
# for key in dict:
#     dict2.update({dict[key] : len(dict[key])})
# print (dict2)

