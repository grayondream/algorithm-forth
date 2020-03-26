#coding=utf-8
from tools import list_tools, visualization, performance, file_tools
from src.search import binary_search
from src.sort import bubble_sort, insert_sort, shell_sort, selection_sort, merge_sort, quick_sort, heap_sort, bucket_sort
from src.string.kmp import kmp_test
from src.string.boyemoore import boyemoore_test
from src.string.rabinkarp import rabinkarp_test
import random
import os
from matplotlib import pyplot as plt
from test import test
from src.string import compare
from src.basic.tgraph import tgraph_test
from src.basic.mgraph import mgraph_test
from src.basic.undiagraph import undiagraph_test
from src.basic.diagraph import diagraph_test
from src.basic.wundiagraph import wundiagraph_test
from src.basic.wdiagraph import wdiagraph_test
from src.basic.nfa import nfa_test


def vertify_sort_test():
    '''
    验证算法的可行性
    '''
    #func = heap_sort.all
    func = test.sort.get_all()
    count = 100
    n = 10
    test.sort.sort_vertify(func, count, n)


def test_sort_visualize():
    '''
    @brief  排序算法可视化
    '''
    n = 100
    sort_func = heap_sort.heap_sort_sink7
    visual_func = visualization.heap_sort_visualization
    path = './img/'
    fps = 20
    test.sort.sort_visualization(n, sort_func, visual_func, path, fps)


def test_sort_performance():
    random_dict = list_tools.random_dict.keys()
    path = './img/sort/performance/bucket'
    file_tools.makesure_path(path)
    func = bucket_sort.buckets
    for key in random_dict:
        test.sort.test_sort_preformance(path, func, key, count=1000)


def graph_test_main():
    #mgraph_test()
    #diagraph_test()
    #wundiagraph_test()
    wdiagraph_test()


def nfa_test_main():
    nfa_test()
    
    
def main():
    #vertify_sort_test()
    #test_sort_visualize()
    #test_sort_performance()
    #kmp_test()
    #boyemoore_test()
    #rabinkarp_test()
    #compare.compare_test()
    #graph_test_main()
    nfa_test_main()

if __name__ == '__main__':
    main()