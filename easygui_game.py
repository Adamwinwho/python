import easygui as f
import random as r

num = r.randint(1,10)
string = '不妨猜一下胡大爷现在心里想的是哪个数字(1,10)'
str1 = '你真牛逼，你是大爷肚子里的蛔虫吗？'
str2 = '大啦，打啦，哈哈哈！！！'
str3 = '小啦，小啦，哈哈哈！！！'

count = 0

while count < 3:
    temp = f.enterbox(string)
    number = int(temp)

    if num == number:
        f.msgbox(str1)
        break
    else:
        if num > number:
            f.msgbox(str3)
        else:
            f.msgbox(str2)
    count += 1

    
    
