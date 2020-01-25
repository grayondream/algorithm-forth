'''
@brief  2.1.13  将一副所有牌背面朝上排成一列的扑克牌按照花色排序，每次只能翻看两张或者交换两张
@note:  使用插入排序，不同花色的扑克牌的具体区间是固定的，每次查看后将相应的花色插入到对应的位置处
'''


def move2last(l):
    '''
    将第一个元素移动到最后的位置
    '''
    l.append(l[0])
    del l[0]
    
    
def ensuer_first(l, size):
    '''
    @brief  查看前面两个数，保证第一个数比较小否则交换
    @param  l   数组
    @param  size    循环次数
    '''
    for i in range(size):
        if l[1] < l[0]:
            l[1], l[0] = l[0], l[1]
            
        move2last(l)
        
        
def queue_sort(l, start, end):
    '''
    @brief  2.1.13  排序扑克，每次只能查看最上面的两张或者交换最上面的两张，或者将最上面的一张放到最底下
    @param  l   需要进行排序的数据
    @param  start   开始位置
    @param  end 结束为止
    @note   
            TODO:尚未进行测试
    '''
    for i in range(len(l) - 1):
        ensuer_first(l, len(l) - i);
        move2last(l);
        
        
'''
2.1.15  使用选择排序即可，将空出的位置作为存储选择出来的最小值进行选择排序
'''


'''
2.1.16  将经过官方提供的排序算法的结果和sort的结果做对比
'''


'''
2.1.25  见insert_sort.insert_sort_II实现性能提升了
'''

'''
2.1.28  限制数据只有01两种值查看不同的性能
TODO:   在等所有的排序算法整理结束后一起做
'''