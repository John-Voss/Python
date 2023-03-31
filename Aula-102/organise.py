import os
import shutil

from_dir = 'C:/Users/brand/Downloads'
to_dir = 'C:/Users/brand/Documents/Programação/VSCode/Python/Aula-102/Programs'
list_of_files = os.listdir(to_dir)

#print(list_of_files)

for file_name in list_of_files:
    name,extencion = os.path.splitext(file_name)
    #print(name)
    #print(extencion)
    if extencion == '':
        continue
    if extencion in ['.png', '.jpg', '.jpeg', '.gif', '.jfif']:
        path1 = from_dir+'/'+file_name
        path2 = to_dir+'/'+'Images'
        path3 = to_dir+'/'+'Images'+'/'+file_name
        if os.path.exists(path2):
            print('Movendo arquivo ', file_name)
            shutil.move(path1, path3)
        else:
            os.mkdir(path2)
            print('Movendo arquivo ', file_name)
            shutil.move(path1, path3)
    if extencion in ['.doc', '.pdf', '.txt']:
        path1 = from_dir+'/'+file_name
        path2 = to_dir+'/'+'Documents'
        path3 = to_dir+'/'+'Documents'+'/'+file_name
        if os.path.exists(path2):
            print('Movendo arquivo ', file_name)
            shutil.move(path3, path1)
        else:
            os.mkdir(path2)
            print('Movendo arquivo ', file_name)
            shutil.move(path3, path1)
    if extencion in ['.exe','.msi']:
        path1 = from_dir+'/'+file_name
        path2 = to_dir
        path3 = to_dir+'/'+file_name
        if os.path.exists(path2):
            print('Movendo arquivo ', file_name)
            shutil.move(path3, path1)
        else:
            os.mkdir(path2)
            print('Movendo arquivo ', file_name)
            shutil.move(path3, path1)