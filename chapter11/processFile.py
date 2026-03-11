from pathlib import Path
import os, shutil, send2trash, zipfile

h = Path.cwd()

(h / 'spam').mkdir(exist_ok=True)
with open(h / 'spam/file1.txt', 'w', encoding='UTF-8') as file:
    file.write('Hello World.')

#Copy to current word directory
shutil.copy(h/'spam/file1.txt', h)

#Copy to spam and new file name is file2
shutil.copy(h/'spam/file1.txt', h/'spam/file2.txt')

# copy everything under the directory
# dirs_exist_ok to avoid folder exists error
shutil.copytree(h/'spam', h/'spam_backup', dirs_exist_ok=True)

(h/'spam2').mkdir(exist_ok=True)
#.move(h/'spam/file1.txt', h/'spam2')
shutil.move(h/'spam/file1.txt', h/'spam2/new_name.txt')

# 不包含子文件夹夏的文件
for filename in h.glob('*'):
    print(filename)

shutil.rmtree(h/'spam_backup')
os.unlink(h/'file1.txt')
#文件夹必须为空，不然报错OSError: [WinError 145] The directory is not empty
# os.rmdir(h/'spam2')
Path.mkdir(h/'spam3')
os.rmdir(h/'spam3')

#move to trash
send2trash.send2trash(h/'spam2')

#loop all the files and directories
print(os.listdir(h))
print(list(h.iterdir()))


for folder_name, subfolders, filenames in os.walk(h):
    print('The current folder is ' + folder_name)
    for subfolder in subfolders:
        print('Subfolder of ' + folder_name + ':' + subfolder)
    for filename in filenames:
        print('file inside ' + folder_name + ':' + filename)



