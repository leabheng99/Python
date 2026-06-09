ls = [{'id':1,'name':'Dara'},{'id':2,'name':'Da'}]
for people in ls:
    for value in people.values():
        print(f'{value}\t' ,end='')
    print()
              
    # print(str(people['id'])+'\t'+people['name'])
