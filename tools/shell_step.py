'''
希尔排序相关的step获取函数，部分函数提供多一个无用的参数t是为了保证函数的接口一致性
'''
import math


def shell_step_normal(k, t=2):
    return int(3 * k + 1)
    
    
def shell_step_geo_inc(k, t=2):
    '''
    @breif  k_list为1, t, t^2, ..., t^n    
    '''
    return int(math.pow(t, k))

def shell_step_poly1(k, t):
    '''
    @brief  9*4^k-9*2^k+1,4^k-3*2^k+1
    '''
    return int(9 * math.pow(4, k) - 9 * math.pow(2, k) + 1)
    

def shell_step_poly2(k, t=2):
    '''
    @brief  9*4^k-9*2^k+1,4^k-3*2^k+1
    @note   这个不能使用，index会出现负值
    '''
    return int(math.pow(4, k) - 3 * math.pow(2, k) + 1)
    
    
def shell_step_poly12(k, t):
    '''
    @brief  将poly1和poly2结合起来，主要来自于algorithm4上
    '''
    k_list = [1, 5, 19, 41, 109, 209, 505, 929, 2161, 3905, 8929]   
    return int(k_list[k])
    
    
def get_shell_steps(n, func, t=2):
    '''
    @brief  n   数组元素数量
    @param  t   职位shell_step_geo_inc准备的t参数
    @return 返回shell排序的步进数组
    '''
    k_list = []
    i = 0
    while True:
        k =  int(func(i, t))
        if k >= n:
            return k_list
            
        k_list.append(k)
        i += 1
        
    return k_list