# Об'єднати кодувальну і декодувальну частину із decoder_project  в один проєкт

import pickle
import os

file_info = []

def get_data_info(filename):
    with open(filename,"rb") as file:
        return {"filename":filename,
                "size":len(file.read())}


while True:
    choice = input("[1]-add file [2]-view data [3]-code data [4]-decode data [q]-exit: ")
    if choice == "1":
        filename = input("Введіть назву файлу: ")
        if os.path.exists(filename):
            file_info.append(get_data_info(filename))
        else: print(f"Файл {filename} не можу знайти.") 
                   
    if choice == "2":
        for element in file_info:
            print(element)

    if choice == "3":
        result_file_name = input("Введіть назву результуючого файлу: ")
        if not os.path.exists(result_file_name) \
           or (os.path.exists(result_file_name) \
               and input(f"Файл {result_file_name} вже існує. Перезаписати його? (Y/n)")=='Y'):
            with open(result_file_name,"wb") as result_file:
                for data in file_info:
                    with open(data["filename"],"rb") as file:
                        result_file.write(file.read())
            with open("info.txt","wb") as file:
                file.write(pickle.dumps(file_info))
            print(f"Результуючий файл {result_file_name} створено.\nФайл з інформацією: info.txt")

    if choice == "4":
        with open(input("Введіть назву файлу з інформацією: "),"rb") as file:
            data_info = pickle.loads(file.read())   
        with open(input("Введіть назву файлу з даними: "),"rb") as result_file:
            for data in data_info:
                with open(data["filename"],"wb") as file:
                    file.write(result_file.read(data["size"]))
            
    if choice == "q":
        break
    
