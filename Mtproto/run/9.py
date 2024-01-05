import os

files_to_remove = ['Mtproto/temp/1.txt', 'Mtproto/temp/2.txt', 'Mtproto/temp/3.txt' , 'Mtproto/temp/4.txt', 'Mtproto/temp/5.txt', 'Mtproto/temp/6.txt', 'Mtproto/temp/7.txt']

for file in files_to_remove:
    os.remove(file)