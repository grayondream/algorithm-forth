


def selection_sort(l, start, end, hook_func=None):
    '''
    @brief  选择排序算法[start, end]
    @param  l   需要进行排序的list
    @param  start   开始位置
    @param  end 结束位置
    @param  hook_func   进行可视化的函数
    '''
    count = 0
    for i in range(start, end + 1):
        minindex = i
        for j in range(i + 1, end + 1):
            if hook_func is not None:
                hook_func(l, i, j, count)
                count += 1
                
            if l[minindex] > l[j]:
                minindex = j
            
        l[minindex], l[i] = l[i], l[minindex]
    

def selection_sort_II(l, start, end, hook_func=None):
    '''
    @brief  选择排序算法[start, end]
    @param  l   需要进行排序的list
    @param  start   开始位置
    @param  end 结束位置
    @param  hook_func   进行可视化的函数
    @note   通过每次遍历寻找最大值和最小值减少遍历次数，即便时间复杂度并未改变
    '''
    left = start
    right = end
    while left < right:
        min_index = left
        max_index = right
        for j in range(left, right + 1):
            if l[min_index] > l[j]:
                min_index = j

            if l[max_index] < l[j]:
                max_index = j
                
        if max_index != right:
            l[max_index], l[right] = l[right], l[max_index]
            
        if min_index == right:      
            min_index = max_index
		
        if min_index != left:
            l[min_index], l[left] = l[left], l[min_index]
            
        left += 1
        right -= 1
        
all = [selection_sort,
                selection_sort_II]