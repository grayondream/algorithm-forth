from src.sort import insert_sort

#归并排序
count = 0
def merge(l, left, mid, right, hook_func=None):
    '''
    @brief  合并有已经有序的部分，合并区间[left, mid),[mid, right)
    @param  l   数据
    @param  left    左边边界
    @param  right   右边边界
    @param  mid     中间分割点
    @param  hook_func   hook函数
    '''
    tmp = l.copy()
    i = left
    j = mid
    for k in range(left, right):
        if hook_func is not None:
            hook_func(l, left, right, count)
            global count 
            count += 1
            
        if i < mid and j < right:
            if tmp[i] < tmp[j]:
                l[k] = tmp[i]
                i += 1
            else:
                l[k] = tmp[j]
                j += 1
        else:
            while i < mid:
                l[k] = tmp[i]
                i += 1
                
            while j < right:
                l[k] = tmp[j]
                j += 1
                
                
def merge_im(l, left, mid, right, hook_func=None):
    '''
    @brief  合并有已经有序的部分，合并区间[left, mid),[mid, right)
    @param  l   数据
    @param  left    左边边界
    @param  right   右边边界
    @param  mid     中间分割点
    @param  hook_func   hook函数
    @note   merge改进当l[mid - 1] < l[mid]表示已经有序
    '''
    if l[mid - 1] < l[mid]:
        return
        
    tmp = l.copy()
    i = left
    j = mid
    for k in range(left, right):
        if hook_func is not None:
            hook_func(l, left, right, count)
            global count 
            count += 1
            
        if i < mid and j < right:
            if tmp[i] < tmp[j]:
                l[k] = tmp[i]
                i += 1
            else:
                l[k] = tmp[j]
                j += 1
        else:
            while i < mid:
                l[k] = tmp[i]
                i += 1
                
            while j < right:
                l[k] = tmp[j]
                j += 1
                
def merge_sort_top2down(l, start, end, hook_func):
    '''
    @brief  自顶向下二路归并排序
    @param  l   list
    @param  start
    @param  end
    @param  hook_func   hook操作函数
    '''
    if end <= start:
        return
        
    mid = start + (end - start)/2
    merge_sort_top2down(l, start, mid, hook_func)
    merge_sort_top2down(l, mid, end, hook_func)
    
    merge(l, start, mid, end, hook_func)
    

def merge_sort_down2top(l, start, end, hook_func):
    '''
    @brief  自底向上二路归并
    @param  l   list
    @param  start
    @param  end
    @param  hook_func   hook操作函数
    '''
    i = 1
    j = 0
    while i < len(l):
        while j < len(l) - i:
            merge(l, j, j + i - 1, min(j + 2 * i - 1, len(l) - 1))
            j += i + i
        
        i = 2 * i
    

def merge_sort_top2down_im(l, start, end, hook_func):
    '''
    @brief  自顶向下二路归并排序改进版本
    @param  l   list
    @param  start
    @param  end
    @param  hook_func   hook操作函数
    @note   当数据规模足够小时使用插入排序进行排序
    '''
    if end <= start:
        return
        
    if end - start < 16:            #magic number
        insert_sort.insert_sort_II(l, start, end, None)
        return
        
    mid = start + (end - start)/2
    merge_sort_top2down(l, start, mid, hook_func)
    merge_sort_top2down(l, mid, end, hook_func)
    
    merge_im(l, start, mid, end, hook_func)
    