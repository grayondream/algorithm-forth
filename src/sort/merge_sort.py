from src.sort import insert_sort
from src.basic import linklist


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
                

def merge_im_II(l, left, mid, right, hook_func=None):
    '''
    @brief  合并有已经有序的部分，合并区间[left, mid),[mid, right)
    @param  l   数据
    @param  left    左边边界
    @param  right   右边边界
    @param  mid     中间分割点
    @param  hook_func   hook函数
    @note   merge改进当l[mid - 1] < l[mid]表示已经有序，将后半段按照降序复制到aux中再归并到l中取消对部分边界检测
    '''
    if l[mid - 1] < l[mid]:
        return
        
    aux = [0] * len(l)
    for i in range(left, mid):
        aux[i] = l[i]
        
    for i in range(mid, right):
        aux[right - i - 1] = l[i]
        
    i = left
    j = right
    for k in range(left, right):
        if hook_func is not None:
            hook_func(l, left, right, count)
            global count 
            count += 1
                
        if i < j:
            if aux[i] < aux[j]:
                l[k] = aux[i]
                i += 1
            else:
                l[k] = aux[j]
                j -= 1
                
                
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
    
    
def merge_alter(l, aux, left, mid, right, hook_func=None):
    '''
    @brief  合并有已经有序的部分，合并区间[left, mid),[mid, right)
    @param  l   数据
    @param  aux     辅助分区
    @param  left    左边边界
    @param  right   右边边界
    @param  mid     中间分割点
    @param  hook_func   hook函数
    @note   merge改进当l[mid - 1] < l[mid]表示已经有序，将后半段按照降序复制到aux中再归并到l中取消对部分边界检测，交换使用aux和l
    '''
    if l[mid - 1] < l[mid]:
        return
        
    i = left
    j = mid
    for k in range(left, right):
        if hook_func is not None:
            hook_func(l, left, right, count)
            global count 
            count += 1
            
        if i < mid and j < right:
            if aux[i] < aux[j]:
                l[k] = aux[i]
                i += 1
            else:
                l[k] = aux[j]
                j += 1
        else:
            while i < mid:
                l[k] = aux[i]
                i += 1
                
            while j < right:
                l[k] = aux[j]
                j += 1
                
                
def merge_sort_top2down_alter(l, aux, start, end, hook_func):
    '''
    @brief  自顶向下二路归并排序
    @param  l   list
    @param  aux 辅助分支
    @param  start
    @param  end
    @param  hook_func   hook操作函数
    '''
    if end <= start:
        return
        
    if end - start < 16:            #magic number
        insert_sort.insert_sort_II(l, start, end, None)
        return
        
    mid = start + (end - start)/2
    merge_sort_top2down_alter(l, aux, start, mid, hook_func)
    merge_sort_top2down_alter(l, aux, mid, end, hook_func)
    
    merge_alter(l,aux, start, mid, end, hook_func)
    l, aux = aux, l
    

def merge_sort_alter(l, start, end, hook_func):
    '''
    @brief  自顶向下二路归并排序
    @param  l   list
    @param  start
    @param  end
    @param  hook_func   hook操作函数
    '''
    aux = l.copy()
    return merge_sort_top2down_alter(l, aux, start, end, hook_func)
    

def merge_mult(l, start, end, hook_func):
    '''
    @brief  自顶向下二路归并排序
    @param  l   list
    @param  start
    @param  end
    @param  hook_func
    '''
    return merge(l, start, end, hook_func)
    
    
def merge_sort_mult(l, start, end, hook_func=None, n=10):
    '''
    @brief  多路归并排序
    @param  l   list
    @param  start
    @param  end
    @param  n   路数
    @param  hook_func   hook操作函数
    '''
    if start < end:
        mid_list = []       #分界点数组
        mid_list.append(start)
        gap = int((end - start)/n)
        for i in range(1, n):
            #生成分界点数组
            mid_list.append(start + i * gap)
            
        mid_list.append(end)
        for i in range(n):
            merge_sort_mult(l, mid_list[i], mid_list[i + 1], hook_func, n)
            
        for i in range(1, n):
            merge_mult(l, mid_list[0], mid_list[i], hook_func)
            
        
def next_unsorted(l, start, end):
    '''
    @brief  寻找出下一个未排序的点
    @param  l   数据
    @param  start   开始位置
    @param  end 结束位置
    '''
    for i in range(start + 1, end):
        if l[i - 1] > l[i]:
            return i
            
    return end           #已经全部排序
    
    
def merge_sort_nature(l, start, end, hook_func=None):
    '''
    @brief  自然归并排序，归并的分界点不再是使用预先定义的位置，而是进行搜索得到
    @param  l   list
    @param  start
    @param  end
    @param  hook_func   hook操作函数
    '''
    left = start
    mid = next(l, start, end)
    right = mid
    while end != mid and end != right:        
        right = next(l, mid, end)
        merge(l, left, mid, right, hook_func)
        
        mid = right
        
        
def merge_link(left, mid, right):
    '''
    @brief  合并linklist
    @param  left    第一个链表的头
    @param  mid     第一个链表的结尾，第二个链表的头
    @param  right     第二个链表的结尾
    '''
    ret = linklist.linklist()
    rst_index = left
    snd_index = mid
    ret_index = ret
    while rst_index != mid and snd_index != right:
        if rst_index.data < snd_index.data:
            tmp = rst_index
            rst_index = rst_index.next
            ret_index.next = tmp
        else:
            tmp = snd_index
            snd_index = snd_index.next
            ret_index.next = tmp
            
        ret_index = ret_index.next
        
    if rst_index != mid:
        ret_index.next = rst_index
        
    if snd_index != right:
        ret_index.next = snd_index
        
    return ret