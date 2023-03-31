import os
import shutil
import time

from_dir = "C:/Users/brand/Downloads"
to_dir = "C:/Users/brand/Pictures"
list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    
    if extension == '':
        continue
    if extension in ['.pdf', '.jpg', '.jpeg', '.gif', '.jfif']:
        path1 = from_dir+'/'+file_name
        path2 = to_dir+'/'+'Images'
        path3 = to_dir+'/'+'Images'+'/'+file_name
        
        if os.path.exists(path2):
            print('MOVENDO ARQUIVO...')
            shutil.move(path1, path3)
            time.sleep(2)
            print('ARQUIVO MOVIDO!')
        else:
            os.mkdir(path2)
            print('MOVENDO ARQUIVO...')
            shutil.move(path1, path3)
            time.sleep(2)
            print('ARQUIVO MOVIDO!')