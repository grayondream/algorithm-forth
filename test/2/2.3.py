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
        