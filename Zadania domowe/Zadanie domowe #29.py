'''Napisz program, który wyświetli nazwę największego pliku w tym katalogu'''

import os

def bigger_file():
    all_files = os.listdir('.')
    files_size = []
    for i in all_files:
        size = os.path.getsize(i)
        files_size.append(size)
    print(max(files_size))

bigger_file()

