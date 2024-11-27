import os 

output_folder = "output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
#selecting mode
mode = int(input("how would you creat the files? 1: name+number 2: name + alphabet sequence(max of 676) 3: exit"))

#functions
def get_file_location_creating():
    file_location = str(input("enter the location which the files would be created."))
    return file_location
def number_of_file_created():
    file_number = int(input("How many files would you create?"))
    file_number_list = []
    for i in range(file_number):
        file_number_list.append(i+1)
    return file_number_list
def name_of_file_created():
    file_name = input("What is the name without suffix?")
    return file_name
def suffix_of_created():
    return input("what is the suffix of the file?")

#creating the file
def output_file(file_number_list, file_name_list):
    output_folder = "output"
    for i in range(len(file_number_list)):
        file_path = os.path.join(output_folder, file_name_list[i])
        with open(file_path, "w") as file:
            file.write("")

#main programme
def main(mode):
    if mode == 3:
        return False
    elif mode == 1:
        file_number_list = number_of_file_created()
        file_name = name_of_file_created()
        file_name_list = []
        suffix = suffix_of_created()
        for i in range(len(file_number_list)):
            file_name_list.append(file_name + "_" + str(file_number_list[i]) + suffix)
        output_file(file_number_list, file_name_list)
        exit_status = int(input("type 1 to exit otherwise the programme continues"))
        if exit_status == 1:
            return False
        return True
    elif mode == 2:
        alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                         'n','o','p','q','r','s','t','u','v','w','x','y','z']
        file_number_list = number_of_file_created()
        file_name = name_of_file_created()
        file_name_list = []
        suffix = suffix_of_created()
        if len(file_number_list) > 702:
            print("it should be less or equal to 702!!!")
            file_number_list = number_of_file_created()
        if len(file_number_list) < 26:
            for i in range(len(file_number_list)):
                file_name_list.append(file_name + "_" + alphabet_list[i] + suffix)
        else:
            j = 0
            k = 0
            for i in range(26):
                file_name_list.append(file_name + "_" + alphabet_list[i] + suffix)
            while i+1 < file_number_list[-1]:
                temp = alphabet_list[j] + alphabet_list[k]
                file_name_list.append(file_name + "_" + temp + suffix)
                k += 1
                i += 1
                if k == 26:
                    k = 0
                    j += 1
        output_file(file_number_list, file_name_list)
        exit_status = int(input("type 1 to exit otherwise the programme continues"))
        if exit_status == 1:
            return False
        return True
    else:
        print("invalid input")
        return False

while main(mode):
    pass
