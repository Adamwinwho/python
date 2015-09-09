import pickle

def pickle_file(boy,girl,count):
    file_name_boy = 'boy_'+str(count)+'.txt'
    file_name_girl = 'girl_'+str(count)+'.txt'

    boy_file = open(file_name_boy,'wb')
    girl_file = open(file_name_girl,'wb')

    pickle.dump(boy,boy_file)
    pickle.dump(girl,girl_file)

    boy_file.close()
    girl_file.close()


def split_file(file_path):

    count = 1
    boy = []
    girl = []

    files = open(file_path)
    for each_line in files:
        if each_line[:6] != '======':
            (name,speek) = each_line.split(':',1)
            if name == '小甲鱼':
                boy.append(speek)
            else:
                girl.append(speek)
         
        else:
            pickle_file(boy,girl,count)

            boy = []
            girl = []
            count += 1

    pickle_file(boy,girl,count)
    files.close()

split_file('H:\\record.txt')
        
    
