def file_compare(file1,file2):
    count = 0
    differ = []
    f1 = open(file1)
    f2 = open(file2)

    for line1 in f1:
        line2 = f2.readline()

        count += 1
        if line1 != line2:
            differ.append(count)

    f1.close()
    f2.close()

    num = len(differ)
    print('两个文件共有[%d]处不同:' % num)
    for i in differ:
        print('第%d行不一样' % i)

file1 = input('请输入需要比较的第一个文件名:')
file2 = input('请输入需要比较的第二个文件名:')
file_compare(file1,file2)
