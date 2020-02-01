'''
list相关的工具函数
'''

import random
import sys
import numpy as np


def random_same(low, high, count):
    '''
    @brief  生成完全相同的随机数
    '''
    return [low for i in range(count)]
    

def random_int(low, high, count):
    '''
    @brief  生成随机数
    @param  low 下界
    @param  high    上界
    @param  count   数量
    '''
    return [random.randint(low, high) for i in range(count)]
    
    
def random_poisson(low, high, count):
    '''
    @brief  生成正态高斯分布的数据
    @param  low     lambda
    @param  high    
    '''
    return np.random.poisson(lam=low,size=count)
    

def random_normal(mean, std, count):
    '''
    @brief  生成正太分布的数据
    '''
    return np.random.normal(mean, std, count)
    
    
def random_bin(low, high, count):
    '''
    @brief  生成二值随机数
    @param  low 二值得第一个值
    @param  high    二值的第二个值
    '''
    low_list = [low] * int(count/2)
    high_list = [high] * int(count/2)
    ret = low_list + high_list
    if len(ret) != count:
        ret.append(high)
        
    random.shuffle(ret)
    return ret
    
    
random_dict = {'same' : random_same, 'bin' : random_bin, 'int' : random_int, 'norm' : random_normal, 'poiss' : random_poisson}
    
def generate_list(count:int , low=0, top=sys.maxsize, random_index='int', sorted=False, reverse=False) -> list:
    '''
    @brief  生成一个随机的int list，可以指定是否经过排序
    @param  count   元素数量
    @param  low     最小值下界
    @param  top     最大值上界
    @param  random_index    生成数据的方式
    @param  sorted  是否需要进行排序
    @param  reverse 是否进行反转
    '''
    assert low < top, 'low >= top, %d >= %d' % (low, top)
    res_list = list(random_dict[random_index](low, top, count))
    res_list = [int(ele) for ele in res_list]
    
    if sorted:
        res_list.sort()

    if reverse:
        res_list.reverse()
        
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