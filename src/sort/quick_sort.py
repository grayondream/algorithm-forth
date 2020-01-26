from src.sort import insert_sort


count = 0
def partition(l, left, right, hook_func):
    '''
    @brief  选择一个锚点将所有元素分割为两部分[left, right)，以第一个元素为锚点
    @param  l   list
    @param  left
    @param  right
    @param  hook_func   hook函数
    @return 锚点
    '''
    value = l[left]
    i = left + 1
    j = right - 1
    while True:
        if hook_func is not None:
            global count    
            count += 1
            hook_func(l, i, j, count)
            
        while l[i] < value and i < j:
            i += 1
        
        while l[j] > value and i < j:
            j -= 1
            
        if j >= i:
            break
            
        l[i], l[j] = l[j], l[i]
        
    l[left],l[j] = l[j], l[left]
    return j
    
    
def quick_sort(l, left, right, hook_func=None):
    '''
    @brief  快速排序[left, right)
    @param  l   list
    @param  left    左边边界
    @param  right   右边边界
    @param  hook_func   hook用function
    '''
    if left >= right:
        return
        
    anchor = partition(l, left, right, hook_func)
    quick_sort(l, left, anchor)        
    quick_sort(l, anchor + 1, right)  
    
    
def quick_sort_II(l, left, right, hook_func=None):
    '''
    @brief  快速排序[left, right)，当问题规模足够小时，使用插入排序代替
    @param  l   list
    @param  left    左边边界
    @param  right   右边边界
    @param  hook_func   hook用function
    '''
    if left >= right:
        return
        
    if right - left < 16:
        insert_sort.insert_sort(l, left, right, None)
        return
        
    anchor = partition(l, left, right, hook_func)
    quick_sort(l, left, anchor)        
    quick_sort(l, anchor + 1, right)  
    
    
def partition3way(l, left, right, hook_func):
    '''
    @param  三取样切分，将整个数组分成，小于当前元素，等于当前元素和大于当前元素三个部分[left, right)
    @param  l
    @param  left
    @param  right
    @param  hook_func
    '''
    if left < right:
        value = l[left]    
        i = left + 1
        lt = left
        gt = right - 1
        while i < right:
            if hook_func is not None:
                hook_func(l, lt, gt, count)
                global count
                count += 1
                
            if l[i] < value:
                l[i], l[lt] = l[lt], l[i]
                lt += 1
            elif l[i] > value:
                l[i], l[gt] = l[gt], l[i]
                gt -= 1
            else:
                i+= 1
        
        return lt, gt + 1
        
        
def quick_sort3way(l, left, right, hook_func=None):
    '''
    @brief  快速排序[left, right)，当问题规模足够小时，使用插入排序代替
    @param  l   list
    @param  left    左边边界
    @param  right   右边边界
    @param  hook_func   hook用function
    '''
    if left < right:
        lt, gt = partition3way(l, left, right)
        quick_sort3way(l, left, lt, hook_func)
        quick_sort3way(l, gt, right, hook_func)