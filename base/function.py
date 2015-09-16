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

#Higher-order function高阶函数，即一个函数可以接受另一个函数作为参数，这种函数就成为高阶函数
x = -5
y = 6
f = abs
def add(x,y,f)
    return f(x) + f(y)

#map / reduce

def f(x):
    return x*x

r = map(f,[1,2,3,4,5,6,7,8,9])

list(map(str,[1,2,3,4,5,6,7,8,9]))

#魔法方法学习
#1、文件删除时自动关闭的方法
class File:
    def __init__(self,filename):
        self.ofile = open(filename,'r+')
    def __del__(self,filename):
        self.ofile.close()
        del self.ofile
#温度转换
class C2F(float):
    "摄氏度转华氏度"
    def __new__(cls,arg=0.0):
        return float.__new__(cls,arg*1.8+32)

#返回输入字符串的ASCII码的和
class Nint(int):
    def __new__(cls,arg=0):
        if isinstance(arg,str):
            total = 0
            for each in arg:
                total += ord(each)
            arg = total
        return int.__new__(cls,arg)
#比较
class Word(str):
'''存储单词的类，定义比较单词的几种方法'''

    def __new__(cls, word):
        # 注意我们必须要用到 __new__ 方法，因为 str 是不可变类型
        # 所以我们必须在创建的时候将它初始化
        if ' ' in word:
            print "Value contains spaces. Truncating to first space."
            word = word[:word.index(' ')] #单词是第一个空格之前的所有字符
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)

        
