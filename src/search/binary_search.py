
def force_search(l:list, start:int, end:int, target:int, hook_func=None) -> int:
    '''
    @brief  暴力遍历查找法
    @param  l   目标数组，必须有序
    @param  start   起始位置，指向元素的起始位置，一般为0
    @param  end     结束位置，指向元素的结尾位置，一般为len(list) - 1
    @param  target  查找的value
    @param  hook_func   相关hook函数，对算法进行可视化需要
    @return 对应目标值的索引，如果没有则返回-1
    '''
    assert start < end, 'end < start, check the value please'
    count = 0
    for i in range(start, end + 1):
        if None != hook_func:
            hook_func(data=l, start=start, mid=i, end=end, target=target, count=count)
            count += 1

        if l[i] == target:
            return i

        count +=1

    return -1


def binary_search(l:list, start:int, end:int, target:int, hook_func=None) -> int:
    '''
    @brief  二分查找法
    @param  l   目标数组，必须有序
    @param  start   起始位置，指向元素的起始位置，一般为0
    @param  end     结束位置，指向元素的结尾位置，一般为len(list) - 1
    @param  target  查找的value
    @param  hook_func   相关hook函数，对算法进行可视化需要
    @return 对应目标值的索引，如果没有则返回-1
    '''
    assert start < end, 'end < start, check the value please'
    count = 0
    while (start <= end):
        mid = int(start + (end - start) / 2)
        if None != hook_func:
            hook_func(data=l, start=start, mid=mid, end=end, target=target, count=count)
            count += 1

        if l[mid] == target:
            return mid
        elif l[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1       #没有找到对应的元素

def main():
    from tools import list_tools

    import random
    for i in range(10):
        l = list_tools.generate_list(10 , 0, 20, True)
        print(l)
        print(binary_search(l, 0, len(l) - 1, random.randint(0, 20)))

if __name__ == '__main__':
    main()