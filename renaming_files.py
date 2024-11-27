import os

#getting information
path_of_folder = input("The path of folder including your files(complete path): ")
mode = int(input("type in number to choose the mode. 1: adding prefix 2: adding suffix"))
str_added = input("what would you add?")
path_of_folder = path_of_folder.replace("\\", "/")
list_of_file = os.listdir(path_of_folder)

#prefix
def add_suffix(file_list, suffix, folder_path):
    for i in file_list:
         name = i.split(".")
         renamed = name[0] + "_" + suffix + '.' + name[1]
         os.rename(folder_path+"/"+i, folder_path+"/"+renamed)

def add_prefix(file_list, prefix, folder_path):
    for i in file_list  :
        name = prefix + "_" + i 
        os.rename(folder_path+"/"+i, folder_path+"/"+name)

def main(mode):
    if mode == 1:
        add_prefix(list_of_file, str_added, path_of_folder)
        return True
    elif mode == 2:
        add_suffix(list_of_file, str_added, path_of_folder)
        return True
    else:
        print("invalid input")
   
main(mode)