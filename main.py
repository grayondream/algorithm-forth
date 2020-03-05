#coding=utf-8
from tools import list_tools, visualization, performance, file_tools
from src.search import binary_search
from src.sort import bubble_sort, insert_sort, shell_sort, selection_sort, merge_sort, quick_sort, heap_sort
from src.string.kmp import kmp_test
from src.string.boyemoore import boyemoore_test
from src.string.rabinkarp import rabinkarp_test
import random
import os
from matplotlib import pyplot as plt
from test import test
from src.string import compare


def vertify_sort_test():
    '''
    验证算法的可行性
    '''
    func = merge_sort.all
    count = 10
    n = 8
    test.sort.sort_vertify(func, count, n)    
    
    
def test_sort_visualize():
    '''
    @brief  排序算法可视化
    '''
    n = 100
    sort_func = merge_sort.merge_sort_down2top
    visual_func = visualization.merge_sort_down2top_visualization
    path = './img'
    fps = 20
    test.sort.sort_visualization(n, sort_func, visual_func, path, fps)


def test_sort_performance():
    random_dict = list_tools.random_dict.keys()
    path = 'G:/altas/algorithm-forth/img/sort/performance/merge/std'
    file_tools.makesure_path(path)
    func = [f for ele in [merge_sort.merge_sort_std, merge_sort.merge_others] for f in ele]
    for key in random_dict:        
        test.sort.test_sort_preformance(path, func, key, count=1000)
    
    
def main():
    #vertify_sort_test()
    #test_sort_visualize()
    #test_sort_performance()
    #kmp_test()
    #boyemoore_test()    
    #rabinkarp_test()
    compare.compare_test()
    
    
if __name__ == '__main__':
    main()