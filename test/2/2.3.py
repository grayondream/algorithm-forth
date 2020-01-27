def sort_binary(l, left, right):
    '''
    @brief  2.3.5 排序只有两种键值的数组[left, right)
    @param  l
    @param  left
    @param  right
    '''
    #先寻找较小的值
    min_index = 0
    for i in range(left + 1, right):
        if l[i] != l[left]:
            min_index = left if l[left] < l[i] else i
            break
            
    value = l[min_index]
    i = left
    j = right - 1
    while True:
        while i < j and value == l[i]:
            i += 1
        
        while i < j and value < l[j]:
            j -= 1
            
        if i >= j:
            break
            
        l[i], l[j] = l[j], l[i]
        
    
def partition_screws(screws, nuts, left, right):
    '''
    @brief  分治将数组分为小于当前的子数组和匹配的螺母和大于当前的数组
    @param  screws  螺母
    @param  nuts    螺丝
    @param  left
    @param  right
    @note   先使用nuts[left]作为哨兵进行分治排序，找到nuts[left]对应的screw的具体位置后用screw[j]作为哨兵排序nuts
    '''
    def partition(l, left, right, guard):
        lt = left
        gt = right - 1
        i = left + 1
        while i < right:
           if l[i] < guard:
               l[i], l[lt] = l[lt], l[i]
               lt += 1
           elif l[i] > guard:
               l[gt], l[i] = l[i], l[gt]
               gt -= 1
           else:
               i += 1
        
        l[gt] = guard
        return lt, gt
        
    lt, gt = partition(nuts, left, right, screws[left])
    lt, gt = partition(screws, left, right, nuts[gt])
    return lt, gt
    
    
def match_screws(screws, nuts, left, right):
    '''
    @brief  2.3.15  匹配螺母和螺丝，n个螺母和n个螺丝可以尝试匹配螺丝和螺母比较大小但不能直接将螺母和螺母或者螺丝和螺丝相比
    @param  screws  螺母数组
    @param  nuts    螺丝数组
    @param  left
    @param  right
    '''
    if left < right:
        lt, gt = partition_screws(screws, nuts, left, right)
        match_screws(screws, nuts, left, lt - 1)
        match_screws(screws, nuts, gt + 1, right)
        
        
'''
2.3.19  5取样切分见src.sort.quick_sort.quick_sort_5sample
'''


'''
2.3.20  非递归的快速排序见sort.quick_sort_cyc
'''



'''
@brief  2.3.22  快速三向切分
'''


'''
2.3.25~2.3.31   TODO:性能测试，和其他排序算法一起进行
'''