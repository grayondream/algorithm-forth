from tools import list_tools
from src import sort
import time
from tools import file_tools
import platform
from tools.iostream import printw


bubble_sort = [sort.bubble_sort.bubble_sort]
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
            sort.quick_sort.quick_sort3way,
            sort.quick_sort.quick_sort3way_faster,
            sort.quick_sort.quick_sort5sample,
            sort.quick_sort.quick_sort_cyc,
            sort.quick_sort.quick_sort_II]
            
heap_sort = [sort.heap_sort.heap_sort]
all_sorts = [bubble_sort, selection_sort, selection_sort, shell_sort, merge_sort, quick_sort]


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
            func(data, 0, len(data), None)
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

    
def main():
    pass
    
if __name__ == '__main__':
    main()