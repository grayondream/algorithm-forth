from src.sort import insert_sort
from src.basic import linklist


#归并排序
count = 0
def merge(l, start, mid, end, hook_func=None):
    '''
    @brief  合并有已经有序的部分，合并区间[left, mid],[mid + 1, end]
    @param  l   数据
    @param  start    左边边界
    @param  end   右边边界
    @param  mid     中间分割点
    @param  hook_func   hook函数
    '''
    tmp = l.copy()
    i = start
    j = mid + 1
    k = start
        
    while i <= mid and j <= end:
        if hook_func is not None:
            hook_func(l, start, end, count)
            global count 
            count += 1
        if tmp[i] < tmp[j]:
            l[k] = tmp[i]
            i += 1
        else:
            l[k] = tmp[j]
            j += 1

        k += 1
                
    while i <= mid:
        l[k] = tmp[i]
        k += 1
        i+= 1

    while j <= end:
        l[k] = tmp[j]
        k += 1
        j+= 1
        
        
def merge_im(l, start, mid, end, hook_func=None):
    '''
    @brief  合并有已经有序的部分，合并区间[left, mid],[mid + 1, end]
    @param  l   数据
    @param  left    左边边界
    @param  end   右边边界
    @param  mid     中间分割点
    @param  hook_func   hook函数
    @note   merge改进当l[mid - 1] < l[mid]表示已经有序
    '''
    if l[mid] < l[mid + 1]:
        return
        
    tmp = l.copy()
    i = start
    j = mid + 1
    for k in range(start, end + 1):
        if hook_func is not None:
            hook_func(l, start, end, count)
            global count 
            count += 1
            
        if i <= mid and j <= end:
            if tmp[i] < tmp[j]:
                l[k] = tmp[i]
                i += 1
            else:
                l[k] = tmp[j]
                j += 1
        else:
            while i <= mid:
                l[k] = tmp[i]
                i += 1
                
            while j <= end:
                l[k] = tmp[j]
                j += 1
                

def merge_im_II(l, start, mid, end, hook_func=None):
    '''
    @brief  合并有已经有序的部分，合并区间[left, mid],[mid + 1, end]
    @param  l   数据
    @param  start    左边边界
    @param  end   右边边界
    @param  mid     中间分割点
    @param  hook_func   hook函数
    @note   merge改进当l[mid] < l[mid + 1]表示已经有序，将后半段按照降序复制到aux中再归并到l中取消对部分边界检测
    '''
    if l[mid] < l[mid + 1]:
        return
        
    aux = [0] * len(l)
    for i in range(start, mid + 1):
        aux[i] = l[i]
        
    for i in range(mid, end + 1):
        aux[end - i] = l[i]
        
    i = start
    j = end + 1
    for k in range(start, end):
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
        
    mid = int(start + (end - start)/2)
    merge_sort_top2down(l, start, mid, hook_func)
    merge_sort_top2down(l, mid + 1, end, hook_func)
    
    if hook_func is not None:
        hook_func(l, start, end, count)
        global count 
        count += 1
    merge(l, start, mid, end, hook_func)
    if hook_func is not None:
        hook_func(l, start, end, count)
        global count 
        count += 1
    

def merge_sort_down2top(l, start, end, hook_func):
    '''
    @brief  自底向上二路归并
    @param  l   list
    @param  start
    @param  end
    @param  hook_func   hook操作函数
    '''
    size = end - start + 1
    gap = 1    #每一次归并时采用的长度
    right = None
    left = None
    while gap < size:
        times = int(size/(2 * gap))
        if hook_func is not None:
            hook_func(l, start, end, count)
            global count 
            count += 1
        
        for i in range(times):
            left = start + i * gap * 2
            mid = left + gap - 1
            right = min(mid + gap, end)
            merge(l, left, mid, right, hook_func)
            
        if right != end:
            merge(l, left, right, end)
        
        if hook_func is not None:
            hook_func(l, start, end, count)
            global count 
            count += 1
        gap = 2 * gap
        
        
def merge_sort_top2down_im(l, start, end, hook_func):
    '''
    @brief  自顶向下二路归并排序改进版本
    @param  l   list
    @param  start
    @param  end
    @param  hook_func   hook操作函数
    @note   当数据规模足够小时使用插入排序进行排序
    '''
    if end < start:
        return
        
    if end - start < 16:            #magic number
        insert_sort.insert_sort_II(l, start, end, None)
        return
        
    mid = int(start + (end - start)/2)
    merge_sort_top2down(l, start, mid, hook_func)
    merge_sort_top2down(l, mid + 1, end, hook_func)
    
    merge(l, start, mid, end, hook_func)
    
    
def merge_alter(l, aux, start, mid, end, hook_func=None):
    '''
    @brief  合并有已经有序的部分，合并区间[start, mid],[mid + 1, end]
    @param  l   数据
    @param  aux     辅助分区
    @param  start    左边边界
    @param  end   右边边界
    @param  mid     中间分割点
    @param  hook_func   hook函数
    @note   merge改进当l[mid - 1] < l[mid]表示已经有序，将后半段按照降序复制到aux中再归并到l中取消对部分边界检测，交换使用aux和l
    '''
    if aux[mid] < aux[mid + 1]: #已经有序
        return
        #print('l', str(l[start:mid + 1]), str(l[mid + 1: end + 1]))
        #print('aux', str(aux[start:mid + 1]), str(aux[mid + 1: end + 1]))
        
    i = start
    j = mid + 1
    k = start
    while i <= mid and j <= end:
        if hook_func is not None:
            hook_func(l, start, end, count)
            global count 
            count += 1
        if aux[i] < aux[j]:
            l[k] = aux[i]
            i += 1
        else:
            l[k] = aux[j]
            j += 1

        k += 1
                
    while i <= mid:
        l[k] = aux[i]
        k += 1
        i+= 1

    while j <= end:
        l[k] = aux[j]
        k += 1
        j+= 1

    pass
    
def merge_sort_top2down_alter(l, aux, start, end, hook_func):
    '''
    @brief  自顶向下二路归并排序
    @param  l   list
    @param  aux 辅助分支
    @param  start
    @param  end
    @param  hook_func   hook操作函数
    @note   TODO:   unsolved
    '''
    if end <= start:
        return
        
    if end - start < 8:            #magic number
        insert_sort.insert_sort_II(l, start, end, None)
        return
    
    mid = int(start + (end - start)/2)
    merge_sort_top2down_alter(aux, l, start, mid, hook_func)
    merge_sort_top2down_alter(aux, l, mid + 1, end, hook_func)
    
    merge_alter(l, aux, start, mid, end, hook_func)
    

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
    

def merge_mult(l, start, mid, end, hook_func):
    '''
    @brief  自顶向下二路归并排序
    @param  l   list
    @param  start
    @param  mid 
    @param  end
    @param  hook_func
    '''
    return merge(l, start, mid, end, hook_func)
    
    
def merge_sort_mult(l, start, end, hook_func=None, n=4):
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
        size = end - start + 1
        gap = int(size / n)  #需要进行修正如果元素为8个，数组长度为9，需要进行数据调整将八个数据分给千把个空位否则会出选stack overflow
        over_no = size - gap * n     #多出来的元素
        for i in range(1, n):
            #生成分界点数组
            if 1 == i:
                mid_list.append(mid_list[i - 1] + gap - 1)
            else:
                mid_list.append(mid_list[i - 1] + gap)
            
        #对初次生成的边界点进行调整
        j = 1
        for i in range(len(mid_list) - 1):
            if i < over_no:
                mid_list[i + 1] += j
                j += 1
            else:
                mid_list[i + 1] += j - 1
        
        mid_list.append(end)
        for i in range(n):
            if i == 0:
                merge_sort_mult(l, mid_list[i], mid_list[i + 1], hook_func, n)
            else:
                merge_sort_mult(l, mid_list[i] + 1, mid_list[i + 1], hook_func, n)
            
        for i in range(1, n):
            merge_mult(l, mid_list[0], mid_list[i], mid_list[i + 1], hook_func)
        
def next_unsorted(l, start, end):
    '''
    @brief  寻找出下一个未排序的点
    @param  l   数据
    @param  start   开始位置
    @param  end 结束位置
    '''
    for i in range(start + 1, end + 1):
        if l[i - 1] > l[i]:
            return i - 1
            
    return -1          #已经全部排序
    
    
def merge_sort_nature(l, start, end, hook_func=None):
    '''
    @brief  自然归并排序，归并的分界点不再是使用预先定义的位置，而是进行搜索得到
    @param  l   list
    @param  start
    @param  end
    @param  hook_func   hook操作函数
    '''
    left = start
    mid = next_unsorted(l, start, end)
    right = mid
    while end + 1 != mid and end != right:        
        right = next_unsorted(l, mid + 1, end)
        if -1 == right:
            right = end
            
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