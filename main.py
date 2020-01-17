from tools import list_tools, visualization
from src.search import binary_search
import random
import os

def test_binary():
    for i in range(1):
        l = list_tools.generate_list(10 , 0, 20, True)
        print(l)
        value = random.randint(0, 20)
        print(value, binary_search.binary_search(l, 0, len(l) - 1, value, visualization.search_visualization_hook))

    path = '/home/altas/altas/algorithm/algorithm-forth/img/binary_search'
    visualization.generate_gif_dir(path, os.path.join(path, 'bin.gif'))

def main():
    test_binary()

if __name__ == '__main__':
    main()