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
                  bubble_sort: failed 000, successed 010, ratio:100.00%, cost time: 7.008732s
           selection_sort: failed 000, successed 010, ratio:100.00%, cost time: 5.425182s
              insert_sort: failed 000, successed 010, ratio:100.00%, cost time: 8.387779s
           insert_sort_II: failed 000, successed 010, ratio:100.00%, cost time: 5.125809s
        shell_sort_normal: failed 000, successed 010, ratio:100.00%, cost time: 5.669968s
         shell_sort_poly1: failed 000, successed 010, ratio:100.00%, cost time: 0.606079s
        shell_sort_poly12: failed 000, successed 010, ratio:100.00%, cost time: 0.317301s
           shell_sort_geo: failed 000, successed 010, ratio:100.00%, cost time: 0.610042s
      merge_sort_top2down: failed 000, successed 010, ratio:100.00%, cost time: 0.526480s
      merge_sort_down2top: failed 000, successed 010, ratio:100.00%, cost time: 0.490026s
        merge_sort_nature: failed 000, successed 010, ratio:100.00%, cost time: 6.295205s
          merge_sort_mult: failed 000, successed 010, ratio:100.00%, cost time: 1.047450s
   merge_sort_top2down_im: failed 000, successed 010, ratio:100.00%, cost time: 0.603435s
         merge_sort_alter: failed 010, successed 000, ratio:000.00%, cost time: 0.278434s
               quick_sort: failed 000, successed 010, ratio:100.00%, cost time: 0.238617s
            quick_sort_II: failed 000, successed 010, ratio:100.00%, cost time: 0.202510s
           quick_sort3way: failed 000, successed 010, ratio:100.00%, cost time: 0.286806s
    quick_sort3way_faster: failed 000, successed 010, ratio:100.00%, cost time: 0.301761s
        quick_sort5sample: failed 000, successed 010, ratio:100.00%, cost time: 0.567455s
           quick_sort_cyc: failed 000, successed 010, ratio:100.00%, cost time: 0.337837s
                heap_sort: failed 000, successed 010, ratio:100.00%, cost time: 0.433408s
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
    sort_func = quick_sort.quick_sort
    visual_func = visualization.quick_sort_visualization
    path = './img'
    fps = 20
    test.sort.sort_visualization(n, sort_func, visual_func, path, fps)


def test_sort_performance():
    random_dict = ['same', 'int', 'bin', 'norm', 'poiss']
    path = 'G:/altas/algorithm-forth/img/'
    sort_funcs = test.sort.shell_sort
    for key in random_dict:        
        test.sort.test_sort_preformance(path, sort_funcs, key, count=1000)
    
    
def main():
    #vertify_sort_test()
    #test_sort_visualize()
    test_sort_performance()
    
if __name__ == '__main__':
    main()