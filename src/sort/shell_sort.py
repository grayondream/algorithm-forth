def shell_sort(l, start, end, hook_func=None):
    '''
    @brief  希尔排序算法
    @param  l   需要进行排序的list
    @param  start   开始位置
    @param  end 结束位置
    @param  hook_func   进行可视化的函数
    '''
    k = 1
    while int((end - start)/3) > k:
        k = 3*k + 1
    
    count = 0
    while k >= 1:
        for i in range(start, end):
            j = i
            while j >= k and l[j] < l[j - k]:
                if hook_func is not None:
                    hook_func(l, i, j, count)
                    count += 1
                    
                tmp = l[j]
                l[j] = l[j - k]
                l[j - k] = tmp
                
                j -= k
        
        k = int(k/3)
    

def shell_sort_custom(l, start, end, k_list, hook_func=None):
    '''
    @brief  希尔排序算法使用用户自定义的步长
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
        for i in range(start, end):
            j = i
            while j >= k_list[k] and l[j] < l[j - k_list[k]]:
                if hook_func is not None:
                    hook_func(l, i, j, count)
                    count += 1
                    
                tmp = l[j]
                l[j] = l[j - k_list[k]]
                l[j - k_list[k]] = tmp
                
                j -= k_list[k]
        
        k -= 1
    

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
    
    
if __name__ == '__main__':
    main()