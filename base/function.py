#slice
L=['hanyue','mengyun','zhichi','tianya']
#copy a list from L,index form 0 to 3 but not include 3
L1 = L[0:3]
print(L1)
#copy a same list
L2= L[:]
print(L2)
#cpoy a list from L every 2 element
L3 = L[::5]
print(L3)
#upon is also used in tuple and string

#iteration
from collections import Tterable,Iterator

print('Iterable?[1,2,3]:',isinstance([1,2,3],Iterable))
print('Iterable?123:',isinstance(123,Iterable))
print('Iterable?\'abc\':',isinstance('abc',Iterable))

#iter list
for i in [1,2,3,4,5,6]:
    print(i)

for each in range(20):
    print(each)


#List Comprehensions
list(range(10))

[x*x for x in range(1,11)]
[1,4,9,16,25,36,49,64,81,100]

[m+n for m in 'ABC' for n in 'XYZ']
['AX','AY','AZ','BX','BY','BZ','CX','CY','CZ']

L1 = ['Hello','World',18,'Apple',None]
L2 = [x for x in L1 if isinstance(x,str)]
print(L2)

#generator

