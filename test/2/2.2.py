from src.basic import queue
from src.sort import merge_sort


'''
2.2.10  见sort.merge_sort.merge_im_II实现
'''


'''
2.2.11  归并排序改进：小规模使用插入排序，有序归并检查，数组和辅助数组交换较少访存
见sort.merge_sort.merge_sort_alter实现
'''


'''
2.2.12  多路归并排序，见merge_sort_mult实现
'''


def merge_queue(rst, snd):
    '''
    @brief  2.2.14  归并两个有序队列得到一个有序的队列
    '''
    ret = queue.queue()
    while rst.empty() and snd.empty():
        if rst.front() < snd.front():
            ret.enqueue(rst.dequeue())
        else:
            ret.enqueue(snd.dequeue())
            
    while rst.empty():
        ret.enqueue(rst.dequeue())
        
    while ret.empty():
        ret.enqueue(snd.dequeue())
        
    return ret
    
    
def merge_sort_queue(l):
    '''
    @brief  2.2.15  队列归并排序
    @param  l   数据
    @note   对于l的每个元素创建多个队列，然后组成一个包含队列的队列，不断将对头的两个元素合并直到只剩下一个队列位置
    '''
    q_queue = queue.queue()
    for ele in l:
        tmp = queue.queue()
        tmp.enqueue(ele)
        q_queue.enqueue(tmp)
        
    while q_queue.size() != 1:
        rst = q_queue.dequeue()
        snd = q_queue.dequeue()
        ret = merge_queue(rst, snd)
        q_queue.enqueue(ret)
        
    return q_queue.dequeue()
    
    
'''
2.2.16  自然归并排序，归并的分组不再是预先定义的而是使用目前数组的有序状态进行区分
见sort.merge_sort.merge_sort_nature
'''
    

def find_next_unsorted(head, tail):
    '''
    @brief  寻找出链表中下一个未经过排序的节点
    '''
    index = head
    while index.next != tail:
        if index.next.data < index.data:
            return index.next
            
        index = index.next
        
    return tail
    
def merge_sort_link(head, tail):
    '''
    @brief  2.2.17  实现链表的自然排序
    @param  head    头节点
    @param  tail    尾节点
    '''
    left = head
    right = tail
    mid = find_next_unsorted(head, tail)
    ret = None
    while right != tail:
        right = find_next_unsorted(mid, tail)
        ret = merge_sort.merge_link(left, mid, right)
        ret.next = right
        
    return ret
    
    
def shuffle_part(left, mid, right):
    '''
    @brief  按照50%的概率打乱链表[left, mid](mid, right]
    @param  left
    @param  mid
    @param  right
    '''
    import random
    if random.randint(0,10) < 5:
        return left
        
    head = mid
    mid.next = right.next
    right.next = left
    return head
    
def shuffle_link(head, tail):
    '''
    @brief  2.2.18  使用分治法打乱链表
    @param  head    头节点
    @param  tail    尾节点
    @note   可能有些问题，没有测试
    '''
    left = head
    mid = head
    while left != tail and mid != tail:
        left = left.next
        mid = mid.next
        if mid != tail:
            mid = mid.next
        else:
            break
            
    shuffle_link(left, mid)
    shuffle_link(mid, tail)
    
    ret = shuffle_part(head, left, tail)
    return ret
    
def reverse_merge(l, left, mid, right):
    inversion = 0
    tmp = l.copy()
    i = left
    j = mid
    for k in range(left, right):
        if i < mid and j < right:
            if tmp[i] < tmp[j]:
                l[k] = tmp[i]
                i += 1
            else:
                l[k] = tmp[j]
                j += 1
                inversion += mid - i + 1
        else:
            while i < mid:
                l[k] = tmp[i]
                i += 1
                
            while j < right:
                l[k] = tmp[j]
                j += 1
                
def reverse_count(l, start, end):
    '''
    @brief  2.2.19  统计倒置的数量，要求O(nlogn)
    '''
    if end <= start:
        return 0
        
    mid = start + (end - start)/2
    rst = reverse_count(l, start, mid)
    snd = reverse_count(l, mid, end)
    
    return rst + snd + reverse_merge(l, start, mid, end)
    

def shared_part(rst, snd, thd):
    '''
    @brief  2.2.21  三个list，每个list包含n个key，使用O(nlogn)级别的算法判断三个数组的第一个公共公部分
    '''
    rst.sort()
    snd.sort()
    thd.sort()
    
    i = 0
    j = 0
    k = 0
    while i < len(rst) and j < len(snd) and k < len(thd):
        if rst[i] == snd[j] and snd[j] == thd[k]:
            return rst[i]
        elif rst[i] < snd[j] and rst[i] < thd[j]:
            i += 1
        elif snd[j] < rst[i] and snd[j] < thd[k]:
            j += 1
        else:
            k += 1
    
    return -1       #未找到
    
    
'''
TODO：性能比较2.2.23~2.2.29
'''