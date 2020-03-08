import math
from tools import shell_step


                
def shell_sort(l, start, end, hook_func=None):
    '''
    @brief  希尔排序算法[start, end]
    @param  l   需要进行排序的list
    @param  start   开始位置
    @param  end 结束位置
    @param  hook_func   进行可视化的函数
    '''
    k = 1
    size = end - start + 1
    while int(size/3) > k:
        k = 3*k + 1
    
    count = 0
    while k >= 1:
        for i in range(start, end + 1):
            j = i
            while j >= k and l[j] < l[j - k]:
                if hook_func is not None:
                    hook_func(l, i, j, count)
                    count += 1
                    
                l[j], l[j - k] = l[j - k], l[j]
                j -= k
        
        k = int(k/3)
    return l
    

def shell_sort_custom(l, start, end, k_list, hook_func=None):
    '''
    @brief  希尔排序算法使用用户自定义的步长, [start, end]
    @param  l   需要进行排序的list
    @param  start   开始位置
    @param  end 结束位置
    @param  k_list  步进
    @param  hook_func   进行可视化的函数
    '''
    #k_list = [1, 5, 19, 41, 109, 209, 505, 929, 2161, 3905, 8929]   #9*4^k-9*2^k+1,4^k-3*2^k+1
    #k = 1
    #while int((end - start)/3) > k:
    #    k = 3*k + 1
    k = len(k_list) - 1
    count = 0
    while k >= 0:
        for i in range(start, end + 1):
            j = i
            while j >= k_list[k] and l[j] < l[j - k_list[k]]:
                if hook_func is not None:
                    hook_func(l, i, j, count)
                    count += 1
                
                l[j - k_list[k]], l[j] = l[j], l[j - k_list[k]]
                j -= k_list[k]
        
        k -= 1
    return l
    
def shell_sort_custom_sent(l, start, end, k_list, hook_func=None):
    '''
    @brief  希尔排序算法使用用户自定义的步长, [start, end],引入哨兵进行优化
    @param  l   需要进行排序的list
    @param  start   开始位置
    @param  end 结束位置
    @param  k_list  步进
    @param  hook_func   进行可视化的函数
    '''
    #k_list = [1, 5, 19, 41, 109, 209, 505, 929, 2161, 3905, 8929]   #9*4^k-9*2^k+1,4^k-3*2^k+1
    #k = 1
    #while int((end - start)/3) > k:
    #    k = 3*k + 1
    k = len(k_list) - 1
    count = 0
    while k >= 0:
        for i in range(start, end + 1):
            j = i
            sent = l[j]
            while j >= k_list[k] and sent < l[j - k_list[k]]:
                if hook_func is not None:
                    hook_func(l, i, j, count)
                    count += 1
                
                l[j] = l[j - k_list[k]]
                j -= k_list[k]
            
            l[j] = sent
            
        k -= 1
    return l
        

def shell_sort_custom_bin(l, start, end, k_list, hook_func=None):
    '''
    @brief  希尔排序算法使用用户自定义的步长, [start, end],使用二分查找进行搜索
    @param  l   需要进行排序的list
    @param  start   开始位置
    @param  end 结束位置
    @param  k_list  步进
    @param  hook_func   进行可视化的函数
    '''
    #k_list = [1, 5, 19, 41, 109, 209, 505, 929, 2161, 3905, 8929]   #9*4^k-9*2^k+1,4^k-3*2^k+1
    #k = 1
    #while int((end - start)/3) > k:
    #    k = 3*k + 1
    k = len(k_list) - 1
    count = 0
    while k >= 0:
        for i in range(start, end + 1):
            j = i
            sent = l[j]
            right_count = 0                   #引入count是为了方便下面进行mid的计算
            left_count = 0                      #这里的right和left只是表明数组上两个点的位置关系
            #while i - left_count * k_list[k] >= start:    #寻找查找边界
            #    left_count += 1
            left_count = int((i - i % k_list[k])/k_list[k])
            
            #left_count -= 1 
            left = i - left_count * k_list[k]
            #二分查找
            while right_count <= left_count:
                mid_count = int(right_count + (left_count - right_count)/2 )
                mid = i - mid_count * k_list[k] 
                if l[mid] < sent:
                    left_count = mid_count - 1
                else:
                    right_count = mid_count + 1
                
            left = i - left_count * k_list[k]    
            while j > left:
                if hook_func is not None:
                    hook_func(l, i, j, count)
                    count += 1
                
                l[j] = l[j - k_list[k]]
                j -= k_list[k]
            
            l[left] = sent
            
        k -= 1
    return l
        
        
'''
下面是采用不同的step序列的shell排序的实现
'''
def shell_sort_geo_sent(l, start, end, hook_func):
    k_list = shell_step.get_shell_steps(end - start + 1, shell_step.shell_step_geo_inc)
    return shell_sort_custom_sent(l, start, end, k_list, hook_func)
    
def shell_sort_geo_bin(l, start, end, hook_func):
    k_list = shell_step.get_shell_steps(end - start + 1, shell_step.shell_step_geo_inc)
    return shell_sort_custom_bin(l, start, end, k_list, hook_func)

def shell_sort_normal(l, start, end, hook_func):
    k_list = shell_step.get_shell_steps(end - start + 1, shell_step.shell_step_normal)
    return shell_sort_custom(l, start, end, k_list, hook_func)
    
    
def shell_sort_poly1(l, start, end, hook_func):
    k_list = shell_step.get_shell_steps(end - start + 1, shell_step.shell_step_poly1)
    return shell_sort_custom(l, start, end, k_list, hook_func)
    
    
def shell_sort_poly2(l, start, end, hook_func):
    k_list = shell_step.get_shell_steps(end - start + 1, shell_step.shell_step_poly2)
    return shell_sort_custom(l, start, end, k_list, hook_func)
    
    
def shell_sort_poly12(l, start, end, hook_func):
    '''
    @brief  这个版本有缺陷，因为k_list有限，元素不能过多
    '''
    k_list = shell_step.get_shell_steps(end - start + 1, shell_step.shell_step_poly12)
    return shell_sort_custom(l, start, end, k_list, hook_func)
    
    
def shell_sort_geo(l, start, end, hook_func):
    k_list = shell_step.get_shell_steps(end - start + 1, shell_step.shell_step_geo_inc)
    return shell_sort_custom(l, start, end, k_list, hook_func)
    
'''
t^k 2-10相关函数定义
'''
def shell_sort_geo2(l, start, end, hook_func):
    k_list = shell_step.get_shell_steps(end - start + 1, shell_step.shell_step_geo_inc, t=2)
    return shell_sort_custom(l, start, end, k_list, hook_func)

def shell_sort_geo3(l, start, end, hook_func):
    k_list = shell_step.get_shell_steps(end - start + 1, shell_step.shell_step_geo_inc, t=3)
    return shell_sort_custom(l, start, end, k_list, hook_func)

def shell_sort_geo4(l, start, end, hook_func):
    k_list = shell_step.get_shell_steps(end - start + 1, shell_step.shell_step_geo_inc, t=4)
    return shell_sort_custom(l, start, end, k_list, hook_func)

def shell_sort_geo5(l, start, end, hook_func):
    k_list = shell_step.get_shell_steps(end - start + 1, shell_step.shell_step_geo_inc, t=5)
    return shell_sort_custom(l, start, end, k_list, hook_func)

def shell_sort_geo6(l, start, end, hook_func):
    k_list = shell_step.get_shell_steps(end - start + 1, shell_step.shell_step_geo_inc, t=6)
    return shell_sort_custom(l, start, end, k_list, hook_func)
    
def shell_sort_geo7(l, start, end, hook_func):
    k_list = shell_step.get_shell_steps(end - start + 1, shell_step.shell_step_geo_inc, t=7)
    return shell_sort_custom(l, start, end, k_list, hook_func)
    
def shell_sort_geo8(l, start, end, hook_func):
    k_list = shell_step.get_shell_steps(end - start + 1, shell_step.shell_step_geo_inc, t=8)
    return shell_sort_custom(l, start, end, k_list, hook_func)
    
def shell_sort_geo9(l, start, end, hook_func):
    k_list = shell_step.get_shell_steps(end - start + 1, shell_step.shell_step_geo_inc, t=9)
    return shell_sort_custom(l, start, end, k_list, hook_func)

def shell_sort_geo10(l, start, end, hook_func):
    k_list = shell_step.get_shell_steps(end - start + 1, shell_step.shell_step_geo_inc, t=10)
    return shell_sort_custom(l, start, end, k_list, hook_func)

def shell_test(dat, k_list):
    while k_list[len(k_list) - 1] > len(dat):
        del k_list[len(k_list) - 1]
        
    import time
    start = time.clock()
    shell_sort_custom(dat, 0, len(dat), k_list)
    end = time.clock()
    return end - start
    
    
def main():
    '''
    3k+1 0.7175969126842866
    159 0.007275240319850496
    2 0.027542164490908516
    3 0.026061200628479497
    4 0.029292122367044593
    5 0.03206374431114012
    6 0.029257054784971537
    7 0.0331268907627712
    8 0.04672712545897906
    9 0.03632659380022252    
    '''
    import random
    n = 2000
    dat = [random.randint(0, n) for i in range(n)]
    
    k_list = [3 * i + 1 for i in range(n)]
    print('3k+1', shell_test(dat, k_list))

    k_list = [1, 5, 19, 41, 109, 209, 505, 929, 2161, 3905, 8929]   #9*4^k-9*2^k+1,4^k-3*2^k+1
    print('159', shell_test(dat, k_list))
    
    for t in range(2, 10): 
        k_list = [t^20 for i in range(200)]
        print(str(t), shell_test(dat, k_list))
    
    
shell_sort_opt = [shell_sort_geo,
                    shell_sort_geo_sent,
                    shell_sort_geo_bin
                    ]
                    
all = [shell_sort_normal,
            shell_sort_poly1, 
            shell_sort_poly12,
            shell_sort_geo]
            
shell_sort_tk = [shell_sort_geo2,
                shell_sort_geo3,
                shell_sort_geo4,
                shell_sort_geo5,
                shell_sort_geo6,
                shell_sort_geo7,
                shell_sort_geo8,
                shell_sort_geo9,
                shell_sort_geo10
                ]
                
if __name__ == '__main__':
    main()