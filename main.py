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
    count = 2
    n = 10
    try:
        test.sort.sort_vertify(func, count, n)    
    except Exception as e:
        print(e)
    
    
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


def test_sort_visualize():
    '''
    @brief  排序算法可视化
    '''
    l = list_tools.generate_list(100, 1, 100)
    #bubble_sort.bubble_sort(l, 0, len(l), visualization.bubble_sort_visualization)
    #selection_sort.selection_sort(l, 0, len(l), visualization.selection_sort_visualization)
    #insert_sort.insert_sort(l, 0, len(l), visualization.insert_sort_visualization)
    #shell_sort.shell_sort(l, 0, len(l), visualization.shell_sort_visualization)
    merge_sort.merge_sort_down2top(l, 0, len(l), visualization.merge_sort_down2top_visualization)
    path = './img/'
    desc = 'merge_sort_down2top'
    visualization.generate_gif_dir(os.path.join(path, desc), os.path.join(path, '%s.gif' % desc), fps=20)
    

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
    #test_binary_search()
    #test_sort()
    #test_sort_preformance()
    vertify_sort_test()
    
    
if __name__ == '__main__':
    main()