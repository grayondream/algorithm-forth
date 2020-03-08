from src.sort import quick_sort


def bucket_sort(l, left, right, hook_func, bucketsize=4):
    ''''
    @brief  桶排序，l中排序范围[left, right]
    @param  bucketsize  每个桶的大小
    @return
    '''
    max_val = l[0]
    min_val = l[0]
    for val in l:
        if val < min_val:
            min_val = val
        if val > max_val:
            max_val = val

    bucket_cnt = (max_val - min_val + 1) // bucketsize + 1  #计算桶的数量
    bucket_list = [[] for _ in range(bucket_cnt)]  #创建桶

    #将数据存放入对应的桶中
    for val in l:
        id = (val - min_val) // bucketsize
        bucket_list[id].append(val)

    #对每个桶内的数据进行排序
    for i in range(len(bucket_list)):
        bucket_list[i] = quick_sort.quick_sort(bucket_list[i], 0,
                                               len(bucket_list[i]) - 1)

    ret = []
    for ele in bucket_list:
        if ele is not None:
            ret.extend(ele)

    return ret


# 计数排序
def count_sort(l, left, right, hook_func):
    ''''
    @brief  排序范围l[left, right]
    @param  hook_func   只是为了接口一致
    @return
    '''
    max_val = l[0]
    min_val = l[0]
    for val in l:
        if val < min_val:
            min_val = val
        if val > max_val:
            max_val = val

    count = [0] * (max_val - min_val + 1)  #确定统计数组长度
    for val in l:
        count[val - min_val] += 1

    ret = []
    for i in range(len(count)):
        for j in range(count[i]):
            ret.append(i + min_val)

    l = ret
    return l


# 基数排序
def radix_sort(l, left, right, hook_func):
    ''''
    @brief  
    @param  hook_func   只是为了接口一致
    @return
    '''
    max_val = max(l)
    n = 1
    #找到最大数的位数
    while max_val > 10**n:
        n += 1

    i = 0
    while i <= n:
        bucket = [[] for _ in range(10)]
        for val in l:
            id = int((val / (10**i)) % 10)
            bucket[id].append(val)

        h = 0
        for j in range(10):
            if len(bucket[j]) != 0:
                for val in bucket[j]:
                    l[h] = val
                    h += 1
        i += 1
    return l


def bucket_sort1(l, left, right, hook_func):
    return bucket_sort(l, left, right, hook_func, 1)


def bucket_sort2(l, left, right, hook_func):
    return bucket_sort(l, left, right, hook_func, 2)


def bucket_sort3(l, left, right, hook_func):
    return bucket_sort(l, left, right, hook_func, 3)


def bucket_sort4(l, left, right, hook_func):
    return bucket_sort(l, left, right, hook_func, 4)


def bucket_sort5(l, left, right, hook_func):
    return bucket_sort(l, left, right, hook_func, 5)


def bucket_sort6(l, left, right, hook_func):
    return bucket_sort(l, left, right, hook_func, 6)


def bucket_sort7(l, left, right, hook_func):
    return bucket_sort(l, left, right, hook_func, 7)


def bucket_sort8(l, left, right, hook_func):
    return bucket_sort(l, left, right, hook_func, 8)


def bucket_sort9(l, left, right, hook_func):
    return bucket_sort(l, left, right, hook_func, 9)


def bucket_sort10(l, left, right, hook_func):
    return bucket_sort(l, left, right, hook_func, 10)


all = [count_sort, bucket_sort, radix_sort]
buckets = [
    bucket_sort1, bucket_sort2, bucket_sort3, bucket_sort4, bucket_sort5,
    bucket_sort6, bucket_sort7, bucket_sort8, bucket_sort9, bucket_sort10
]
