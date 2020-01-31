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
    sort_func = merge_sort.merge_sort_down2top
    visual_func = visualization.bubble_sort_visualization
    path = './img'
    fps = 20
    test.sort.sort_visualization(n, sort_func, visual_func, path, fps)
    
    
def test_search():
    '''
    @brief  查找算法测试
    '''
    for i in range(1):
        l = list_tools.generate_list(100 , 1, 100, True)
        value = random.randint(0, 100)
        print(value, binary_search.binary_search(l, 0, len(l) - 1, value, visualization.search_visualization_hook))

    path = './img/'
    visualization.generate_gif_dir(os.path.join(path, 'binary_search'), os.path.join(path, 'bin_search.gif'), fps=2)



def test_sort_preformance():
    '''
    @brief  不同排序算法性能对比
    '''
    sort_funcs = [bubble_sort.bubble_sort, insert_sort.insert_sort, shell_sort.shell_sort, selection_sort.selection_sort, insert_sort.insert_sort_II]
    sorted = True
    reverse = True
    
    total_times = []
    ranges = range(100, 1000, 10)
    for n in ranges:
        times = performance.sort_performance(n, sort_funcs, sorted=sorted, reverse=reverse, repeat=5)    
        total_times.append(times)
        print(n, times)
            
    plt.figure()
    plt.title('random sorted reversed data')
    plt.xlabel('number')
    plt.ylabel("time(s)")
    
    for i in range(len(total_times[0])):
        print(sort_funcs[i])
        plt.plot(list(ranges), [ele[i] for ele in total_times], label=str(sort_funcs[i])[10:-23])
    
    plt.legend()
    plt.show()
    
    
def main():
    #vertify_sort_test()
    test_sort_visualize()
    
if __name__ == '__main__':
    main()