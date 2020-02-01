'''
统计代码量
'''
import os
from tools import file_tools

    
def get_effective_no(filename):
    count = 0
    with open(filename, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        for line in lines:
            if line != '\n':
                count += 1
                
    return count
    
    
def main():
    path = '.'
    ext = 'py'
    ret = file_tools.get_all_files(path, ext)
    no = 0
    for file in ret:
        print(file)
        no += get_effective_no(file)
    
    print(no)
    
    
if __name__ == '__main__':
    main()