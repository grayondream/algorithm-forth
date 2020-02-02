from tools import list_tools
from src import sort
import time
from tools import file_tools, visualization, performance
import platform
from tools.iostream import printw
import os
import matplotlib.pyplot as plt


bubble_sort = [sort.bubble_sort.bubble_sort, 
            sort.bubble_sort.bubble_sort_II, 
            sort.bubble_sort.bubble_sort_III]
            
insert_sort = [sort.insert_sort.insert_sort,
            sort.insert_sort.insert_sort_II]
            
selection_sort = [sort.selection_sort.selection_sort]
shell_sort = [sort.shell_sort.shell_sort_normal,
            sort.shell_sort.shell_sort_poly1, 
            sort.shell_sort.shell_sort_poly12,
            sort.shell_sort.shell_sort_geo]
            
merge_sort = [sort.merge_sort.merge_sort_top2down,
            sort.merge_sort.merge_sort_down2top,
            sort.merge_sort.merge_sort_nature,
            sort.merge_sort.merge_sort_mult,
            sort.merge_sort.merge_sort_top2down_im,
            sort.merge_sort.merge_sort_alter]
            
quick_sort = [sort.quick_sort.quick_sort,
            sort.quick_sort.quick_sort_II,
            sort.quick_sort.quick_sort3way,
            sort.quick_sort.quick_sort3way_faster,
            sort.quick_sort.quick_sort5sample,
            sort.quick_sort.quick_sort_cyc]
            
heap_sort = [sort.heap_sort.heap_sort]

all_sorts = [bubble_sort, selection_sort, insert_sort, shell_sort, merge_sort, quick_sort, heap_sort]


def get_all():
    return [func for ele in all_sorts for func in ele]
            
def get_standard():
    '''
    只获取标准的需要进行可视化的排序函数
    '''
    ret = [ele[0] for ele in all_sorts]
    return ret
    
    
def sort_vertify(funcs, count=100, n=100):
    '''
    @brief  验证算法的可行性
    @param  func    进行测试的排序函数
    @param  count   单个排序算法测试的次数 
    @param  n   测试使用的数据量
    '''
    for func in funcs:
        error = 0
        start = time.clock()
        func_name = file_tools.get_func_name(func)
        for i in range(count):
            data = list_tools.generate_list(n, 0, n)
            data_copy = data.copy()
            func(data, 0, len(data) - 1, None)
            data_copy.sort()
            if data != data_copy:
                error += 1
                
        end = time.clock()
        ratio = (count - error)/count * 100
        line = '%25s: failed %03d, successed %03d, ratio:%03d%s%%, cost time: %fs' % (func_name, error, count - error, int(ratio), ('%.2f' % (ratio - int(ratio)))[1:], end - start)
        color = None
        if ratio != 100:
            color = 'red'
        else:
            color = 'green'
            
        printw(line, color, None)

    
def sort_visualization(n, sort_func, visual_func, path, fps=20):
    '''
    @brief  排序算法流程可视化
    @param  n   数据量
    @param  sort_func   排序算法
    @param  visual_func hook函数
    @param  fps
    '''
    l = list_tools.generate_list(n, 1, n)
    sort_func(l, 0, len(l) - 1, visual_func)
    desc = file_tools.get_func_name(sort_func)
    visualization.generate_gif_dir(os.path.join(path, desc), os.path.join(path, '%s.gif' % desc), fps=fps)
    

def test_sort_preformance(path, sort_funcs, random_index, count=1000):
    '''
    @brief  不同排序算法性能对比
    '''
    total_times = []
    ranges = range(10, count, 10)
    for n in ranges:
        times = performance.sort_performance(n, sort_funcs, random_index, repeat=5)    
        total_times.append(times)
        print(n)
            
    plt.figure(dpi=200, figsize=(16, 9))
    plt.title(random_index)
    plt.xlabel('number')
    plt.ylabel("time(s)")
    
    for i in range(len(total_times[0])):
        plt.plot(list(ranges), [ele[i] for ele in total_times], label=str(file_tools.get_func_name(sort_funcs[i])))
    
    plt.legend()
    plt.savefig(os.path.join(path, random_index + '.png'))
    #plt.show()
    
    
def main():
    pass
    
if __name__ == '__main__':
    main()