dict = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
l1 = []
# dict2 = [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
# print(len(dict['Science']))

for x in range (len(dict['Science'])):
    dict2 = {}
    for key in dict:
        
        dict2.update({key : dict[key][x]})
    l1.append(dict2)
print(l1)

        
    
