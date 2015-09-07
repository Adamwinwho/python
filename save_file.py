def savefile(boy,girl,count):
    file_name_boy = 'boy_'+str(count)+'.txt'
    file_name_girl = 'girl_'+str(count)+'.txt'

    boy_file = open(file_name_boy,'w')
    girl_file = open(file_name_girl,'w')

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()

def splitfile(file_name):
    f = open(file_name)

    boy = []
    girl = []
    count = 1

    for eachline in f:
        if eachline[:6] != "======":
            (role,line_spoken) = eachline.split(':',1)
            if role == '小甲鱼':
                boy.append(line_spoken)
            else:
                girl.append(line_spoken)
        else:
            savefile(boy,girl,count)

            boy = []
            girl = []
            count += 1
    savefile(boy,girl,count)
    f.close()

splitfile("h:\\record.txt")
