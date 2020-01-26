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
    @brief  2.1.15  队列归并排序
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
2.1.16  自然归并排序，归并的分组不再是预先定义的而是使用目前数组的有序状态进行区分
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
    @brief  2.1.17  实现链表的自然排序
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