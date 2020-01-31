from src.sort import insert_sort
import random
from src.basic import stack


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
    if (right - left) < 2:
        return left
    
    value = l[left]
    i = left
    j = right - 1
    while i < j:
        if hook_func is not None:
            global count    
            count += 1
            hook_func(l, i, j, count)
            
        while l[i] <= l[left] and i < j:
            i += 1
        
        l[j] = l[i]
        while l[j] > l[left] and i < j:
            j -= 1
            
        l[i] = l[j]
        
    l[i] = value
    return i + 1
    
    
def quick_sort(l, left, right, hook_func=None):
    '''
    @brief  快速排序[left, right)
    @param  l   list
    @param  left    左边边界
    @param  right   右边边界
    @param  hook_func   hook用function
    '''
    if right - left < 2:
        return
        
    anchor = partition(l, left, right, hook_func)
    if anchor == right or anchor == left:
        return
        
    quick_sort(l, left, anchor)        
    quick_sort(l, anchor, right)  
    
    
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
    
    return lt, gt
        
        
def quick_sort3way(l, left, right, hook_func=None):
    '''
    @brief  快速排序[left, right)，当问题规模足够小时，使用插入排序代替
    @param  l   list
    @param  left    左边边界
    @param  right   右边边界
    @param  hook_func   hook用function
    '''
    if left < right:
        lt, gt = partition3way(l, left, right, hook_func)
        quick_sort3way(l, left, lt, hook_func)
        quick_sort3way(l, gt, right, hook_func)
        

def partition3way_faster(l, left, right, hook_func):
    '''
    @param  三取样切分，将整个数组分成，小于当前元素，等于当前元素和大于当前元素三个部分[left, right)
    @param  l
    @param  left
    @param  right
    @param  hook_func
    @note   将left和right分为四段=anchor,<anchor,>anchor,=anchor    [left,p,i,j,q,right]
            [left, p)   =v
            [p, i)      <v
            [i,j)       ?
            [j,q)       >v
            [q,right)   =v
    '''
    anchor = l[left]
    i = left + 1
    j = right
    p = i
    q = j
    
    while i < j:
        if l[i] == anchor:
            l[i], l[p] = l[p], l[i]
            i += 1
            p += 1
        elif l[i] < anchor:
            i += 1
        else:
            l[i], l[j] = l[j], l[i]
            j -= 1
            
        if i >= j:
            break
            
        if [j] == anchor:
            l[j], l[q] = l[q], l[j]
            j -= 1
            q -= 1
        elif l[j] < anchor:
            j -= 1
        else:
            l[i], l[j] = l[j], l[i]
            i += 1
        
        #结束之后
        #[left, p, ij, q, right]
        while p != left:
            l[p - 1], l[i - 1] = l[i - 1], l[p - 1]
            p = p - 1
            i = i - 1
        
        while q != right:
            l[q + 1], l[j + 1] = l[q + 1], l[j + 1]
            q = q + 1
            j = j + 1
            
    return i, j
    
    
def quick_sort3way_faster(l, left, right, hook_func=None):
    '''
    @brief  快速排序[left, right)，当问题规模足够小时，使用插入排序代替
    @param  l   list
    @param  left    左边边界
    @param  right   右边边界
    @param  hook_func   hook用function
    '''
    if left < right:
        lt, gt = partition3way(l, left, right, hook_func)
        quick_sort3way_faster(l, left, lt, hook_func)
        quick_sort3way_faster(l, gt, right, hook_func)
        

def partition5sample(l, left, right, hook_func):
    '''
    @brief  五取样切分使用从数组中采样的五个数的中位数进行parition
    @param  l   
    @param  left
    @param  right
    @param  hook_func
    '''
    def get_mid(l, part_list):
        '''
        @brief  返回中位数对应的value在l中的索引，如果l的数组为偶数则选择len(l)/2
        '''
        part_values = [l[i] for i in part_list]
        mid_value = part_values[int(len(part_values)/2)]
        for i in part_list:
            if l[i] == mid_value:
                return i, mid_value
    
    sample_no = 5       #采样数
    part_index_list = [random.randint(left, right) for i in range(sample_no)]
    anchor, anchor_value = get_mid(l, part_index_list)
    
    i = left
    j = right - 1
    while i < j:
        while i < j and l[i] < anchor_value:
            i += 1
            
        while i < j and l[j] > anchor_value:
            j -= 1
            
        if i < j:
            l[i], l[j] = l[j], l[i]
            
    l[j] = anchor_value
    return j
    
    
def quick_sort5sample(l, left, right, hook_func=None):
    '''
    @brief  快速排序[left, right)，parition时使用从数组中随机采样的五个数的中位数进行切分
    @param  l   list
    @param  left    左边边界
    @param  right   右边边界
    @param  hook_func   hook用function
    '''
    if left < right:
        anchor = partition5sample(l, left, right, hook_func)
        quick_sort5sample(l, left, anchor - 1, hook_func)
        quick_sort5sample(l, anchor + 1, right, hook_func)
        

def quick_sort_cyc(l, left, right, hook_func=None):
    '''
    @brief  快速排序非递归版本
    @param  l   list
    @param  left
    @param  right
    @parma  hook_func
    @note   建立一个容器，容器的每个元素是一个tuple表示需要进行partition的left和right
    '''
    rst = stack.stack()
    snd = stack.stack()
    rst.push((left, right))
    while rst.empty():
        while rst.empty():
            left, right = rst.pop()
            anchor = partition(l, left, right, hook_func)
            if anchor - 1 > left and anchor + 1 < right:
                snd.push((left, anchor - 1))
                snd.push((anchor + 1, right))
            
        rst, snd = snd, rst
        
    