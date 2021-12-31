file = open('sample.txt','r+')
# print(file.read())
lines = file.readlines()
# print(lines)
dict = {}

for l in lines:
    # print(l.split(':'))
    dict.update({l.split(':')[0] : l.split(':')[1]})
print(dict)
