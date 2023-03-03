import os

files_list =[]
path = os.getcwd()
with os.scandir(path) as files:
    for f in files:
        if f.name[-4:] == '.txt' and f.name != '4.txt':
            files_list.append(f.name)

print(files_list)
some_dict = {}
for file in files_list:
    with open(file, 'r', encoding='utf-8') as f:
        len1 = len(f.readlines())
        some_dict[file] = len1

sorted_dict = dict(sorted(some_dict.items(), key=lambda item: item[1]))

with open('4.txt', 'w', encoding='utf-8') as file_write:
    for key in sorted_dict.keys():
        with open(key, 'r', encoding='utf-8') as f_read:
            file_write.write(key + '\n')
            file_write.write(str(sorted_dict[key]) + '\n')
            file_write.write(''.join(f_read.readlines()) + '\n')



