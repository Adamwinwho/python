#根据输入的初始文件目录和文件名查找，并返回显示文件路径
import os

def find_file(dirctory,file_name):
    os.chdir(dirctory)
    for each in os.listdir(os.curdir):
        if each == file_name:
            print(os.getcwd()+os.sep+each)
        elif os.path.isdir(each):
            find_file(each,file_name)
            os.chdir(os.pardir)

dirc = input('请输入待查找的初始目录:')
file = input('请输入需要查找的目标文件:')
find_file(dirc,file)
