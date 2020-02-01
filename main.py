from tools import list_tools, visualization, performance
from src.search import binary_search
from src.sort import bubble_sort, insert_sort, shell_sort, selection_sort, merge_sort, quick_sort, heap_sort
import random
import os
from matplotlib import pyplot as plt
from test import test


def vertify_sort_test():
    '''
    验证算法的可行性
    '''
    func = test.sort.get_all()
    count = 10
    n = 2000
    test.sort.sort_vertify(func, count, n)    
    
    
def test_sort_visualize():
    '''
    @brief  排序算法可视化
    '''
    n = 100
    sort_func = bubble_sort.bubble_sort
    visual_func = visualization.bubble_sort_visualization
    path = './img'
    fps = 20
    test.sort.sort_visualization(n, sort_func, visual_func, path, fps)


def test_sort_performance():
    random_dict = list_tools.random_dict.keys()
    path = 'G:/altas/algorithm-forth/img/sort/performance/bubble'
    sort_funcs = test.sort.bubble_sort
    for key in random_dict:        
        test.sort.test_sort_preformance(path, sort_funcs, key, count=1000)
    
    
def main():
    #vertify_sort_test()
    #test_sort_visualize()
    test_sort_performance()
    
if __name__ == '__main__':
    main()