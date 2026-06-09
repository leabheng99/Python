lst = []
n = int(input('n = '))
for i in range(0,n):
    people={}
    people['id']=input(' id = ')
    people['name']=input(' name = ')
    people['age']=input(' age = ')
    people['address']=input(' address = ')
    
    lst.append(people)
    print('----------------------------')
# print(ls)
print('id\tname\tage\taddress')

for p in lst:
    for v in p.values():
        print(f'{v}\t', end='')
    print()