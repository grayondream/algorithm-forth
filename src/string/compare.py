from tools import string_tool
from src.string import boyemoore, rabinkarp, kmp
import time
import matplotlib.pyplot as plt


def algorithm_ana(func, slen, plen, times):
    cost_time = 0.0
    for i in range(times):
        txt = string_tool.random_str(slen=slen)
        pat = string_tool.random_str(slen=plen)
        start = time.clock()
        func(txt, pat)
        end = time.clock()
        cost_time += end - start
        
    return cost_time / times
    

def get_func_name(func):
    return str(func)[10:-19]
    
    
def compare_test():
    funcs = [kmp.kmp, kmp.kmp_dfa, boyemoore.boyemoore_search, rabinkarp.rabinkarp_m, rabinkarp.rabinkarp_l]
    all_times = {get_func_name(func):[] for func in funcs}
    x = list(range(10,1000, 10))
    for i in x:
        print(i)
        for func in funcs:
            cost_time = algorithm_ana(func, slen=1000, plen=i, times=10)
            all_times[get_func_name(func)].append(cost_time)
            
    plt.figure()
    for key in all_times.keys():
        plt.plot(x, all_times[key], label=key)
        
    plt.legend()
    plt.show()