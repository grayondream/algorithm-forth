'''
list相关的工具函数
'''

import random
import sys

def generate_list(count:int , low=0, top=sys.maxsize, sorted=False) -> list:
    '''
    @brief  生成一个随机的int list，可以指定是否经过排序
    @param  count   元素数量
    @param  low     最小值下界
    @param  top     最大值上界
    '''
    assert low < top, 'low >= top, %d >= %d' % (low, top)
    res_list = [random.randint(low, top) for i in range(count)]
    if sorted:
        res_list.sort()

    return res_list


def is_sorted(l:list)->bool:
    '''
    @brief  判断一个list是否已经经过排序
    @param  l  需要经过判断的list
    @return bool, true or false,顾名思义
    '''
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False

    return True

if __name__ == '__main__':
    for i in range(10):
        l = generate_list(10, 0, 20, 1 == i%2)
        print(l)
        print(is_sorted(l))