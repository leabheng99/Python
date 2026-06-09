dic = {1,2,3,4,5}
print(type(dic))

dic = dict()
print(type(dic))

dic = {0:10, 1:20, 2:30, 3:40}
print(dic)

dic = {0:10, 1:20, 2:30, 3:40}
print(dic[2])

dic = {0:10, 1:20, 2:30, 3:40}
dic[0] = 100
print(dic)

dic = {0:10, 1:20, 2:30, 3:40}
dic[0] = 100
dic[4] = 50
print(dic)

dic = {0:10, 1:20, 2:30, 3:40}
dic[0] = 100
dic[4] = 50
del dic[3]
print(dic)

dic = {'id': 1, 'name': 'lean', 'age': '18', 'address': 'phnom penh'}
print(dic)

dic = {'id': 1, 'name': 'lean', 'age': '18', 'address': 'phnom penh'}
print(dic['name'])

dic = {'id': 1, 'name': 'lean', 'age': '18', 'address': 'phnom penh'}
for e in dic:
    print(e)


dic = {'id': 1, 'name': 'lean', 'age': '18', 'address': 'phnom penh'}
for e in dic.values():
    print(e)


dic = {'id': 1, 'name': 'lean', 'age': '18', 'address': 'phnom penh'}
for e in dic.keys():
    print(e)
    

dic = {'id': 1, 'name': 'lean', 'age': '18', 'address': 'phnom penh'}
for k,v in dic.items():
    print(f'{k} : {v}')