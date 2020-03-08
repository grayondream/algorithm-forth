from src.search import binary_search


def insert_sort(l, start, end, hook_func=None):
    '''
    @brief  插入排序，排序范围[start, end]
    @param  l   进行排序的list
    @param  start   开始位置
    @param  end 结束位置
    @param  hook_func   hook函数
    '''
    count = 0
    for i in range(start, end + 1):
        j = min(end, i + 1)
        while j > start and l[j - 1] > l[j]:
            if hook_func is not None:
                hook_func(l, i, j, count)
                count += 1

            l[j], l[j - 1] = l[j - 1], l[j]
            j -= 1

    return l


def insert_sort_II(l, start, end, hook_func=None):
    '''
    @brief  插入排序，排序范围[start, end]，排序时使用哨兵，减少对数组的访问
    @param  l   进行排序的list
    @param  start   开始位置
    @param  end 结束位置
    @param  hook_func   hook函数
    '''
    count = 0
    for i in range(start + 1, end + 1):
        tmp = l[i]
        j = i - 1
        while j >= start and l[j] > tmp:
            if hook_func is not None:
                hook_func(l, i, j, count)
                count += 1

            l[j + 1] = l[j]
            j -= 1

        l[j + 1] = tmp
    return l


def insert_sort_III(l, start, end, hook_func=None):
    '''
    @brief  插入排序，排序范围[start, end]，排序时使用哨兵，减少对数组的访问
    @param  l   进行排序的list
    @param  start   开始位置
    @param  end 结束位置
    @param  hook_func   hook函数
    @note   使用二分查找法优化    
    '''
    count = 0
    for i in range(start + 1, end + 1):
        j = i
        left = start
        right = i
        while left <= right:
            mid = int(left + (right - left) / 2)
            if l[mid] < l[j]:
                left = mid + 1
            else:
                right = mid - 1

        j = i
        value = l[j]
        while j > left:
            l[j] = l[j - 1]
            j -= 1

        l[j] = value

    return l


if __name__ == '__main__':
    import random
    dat = [random.randint(0, 10) for i in range(10)]
    print(dat)
    insert_sort_II(dat, 0, len(dat))
    print(dat)

all = [insert_sort, insert_sort_II, insert_sort_III]
