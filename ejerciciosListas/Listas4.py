n=int(input('Dígame un número: '))
list=[]
for i in range (1,n+1):
   primo=True
   for j in range(2,i):
        if i == j:
           break
        elif i%j == 0:
           primo = False
        else:
           continue
   if primo == True:
      list.append(i)
print(f'Primos hasta {n}: {list}')