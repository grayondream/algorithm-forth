from src.sort import insert_sort
import random
from src.basic import stack

count = 0


def partition(l, start, end, hook_func):
    '''
    @brief  选择一个锚点将所有元素分割为两部分[start, end]，以第一个元素为锚点
    @param  l   list
    @param  start
    @param  end
    @param  hook_func   hook函数
    @return 锚点
    '''
    if end <= start:
        return end

    value = l[start]
    i = start
    j = end
    while i < j:
        if hook_func is not None:
            global count
            count += 1
            hook_func(l, i, j, count)

        while l[j] > value and i < j:
            j -= 1

        l[i] = l[j]
        while l[i] <= value and i < j:  #结束之后i指向的是大于value的index
            i += 1

        l[j] = l[i]
        if hook_func is not None:
            global count
            count += 1
            hook_func(l, i, j, count)
    l[i] = value
    return i


def quick_sort(l, start, end, hook_func=None):
    '''
    @brief  快速排序[start, end]
    @param  l   list
    @param  start    左边边界
    @param  end   右边边界
    @param  hook_func   hook用function
    '''
    if end <= start:
        return l

    if hook_func is not None:
        global count
        count += 1
        hook_func(l, start, end, count)
    anchor = partition(l, start, end, hook_func)
    if hook_func is not None:
        global count
        count += 1
        hook_func(l, start, end, count)

    quick_sort(l, start, anchor - 1, hook_func)
    quick_sort(l, anchor + 1, end, hook_func)
    return l


def quick_sort_II(l, start, end, hook_func=None):
    '''
    @brief  快速排序[start, end)，当问题规模足够小时，使用插入排序代替
    @param  l   list
    @param  start    左边边界
    @param  end   右边边界
    @param  hook_func   hook用function
    '''
    if start >= end:
        return l

    if end - start < 16:
        insert_sort.insert_sort(l, start, end, None)
        return l

    anchor = partition(l, start, end, hook_func)
    quick_sort(l, start, anchor - 1)
    quick_sort(l, anchor + 1, end)
    return l


def partition3way(l, start, end, hook_func):
    '''
    @param  三取样切分，将整个数组分成，小于当前元素，等于当前元素和大于当前元素三个部分[start, end)
    @param  l
    @param  start
    @param  end
    @param  hook_func
    @note   [start, lt]  lower
            [lt + 1, i - 1] equal
            [gt + 1, end]   bigger
    '''
    value = l[start]
    i = start
    lt = start - 1
    gt = end
    while i <= gt:
        if hook_func is not None:
            hook_func(l, lt, gt, count)
            global count
            count += 1

        if l[i] < value:
            l[i], l[lt + 1] = l[lt + 1], l[i]
            lt += 1
        elif l[i] > value:
            l[i], l[gt] = l[gt], l[i]
            gt -= 1
        else:
            i += 1

    return lt, gt + 1


def quick_sort3way(l, start, end, hook_func=None):
    '''
    @brief  快速排序[start, end)，当问题规模足够小时，使用插入排序代替
    @param  l   list
    @param  start    左边边界
    @param  end   右边边界
    @param  hook_func   hook用function
    '''
    if start < end:
        lt, gt = partition3way(l, start, end, hook_func)
        quick_sort3way(l, start, lt, hook_func)
        quick_sort3way(l, gt, end, hook_func)
    return l


def partition3way_faster(l, start, end, hook_func):
    '''
    @param  三取样切分，将整个数组分成，小于当前元素，等于当前元素和大于当前元素三个部分[start, end)
    @param  l
    @param  start
    @param  end
    @param  hook_func
    @note   将start和end分为四段=anchor,<anchor,>anchor,=anchor    [start,p,i,j,q,end]
            [start, p)   =v
            [p, i)      <v
            [i,j)       ?
            [j,q)       >v
            [q,end)   =v
    '''
    anchor = l[start]
    i = start + 1
    j = end
    p = i
    q = j

    while i < j:
        if l[i] == anchor:
            l[i], l[p] = l[p], l[i]
            i += 1
            p += 1
        elif l[i] < anchor:
            i += 1
        else:
            l[i], l[j] = l[j], l[i]
            j -= 1

        if i >= j:
            break

        if [j] == anchor:
            l[j], l[q] = l[q], l[j]
            j -= 1
            q -= 1
        elif l[j] < anchor:
            j -= 1
        else:
            l[i], l[j] = l[j], l[i]
            i += 1

        #结束之后
        #[start, p, ij, q, end]
        while p != start:
            l[p - 1], l[i - 1] = l[i - 1], l[p - 1]
            p = p - 1
            i = i - 1

        while q != end:
            l[q + 1], l[j + 1] = l[q + 1], l[j + 1]
            q = q + 1
            j = j + 1

    return i, j


def quick_sort3way_faster(l, start, end, hook_func=None):
    '''
    @brief  快速排序[start, end)，当问题规模足够小时，使用插入排序代替
    @param  l   list
    @param  start    左边边界
    @param  end   右边边界
    @param  hook_func   hook用function
    '''
    if start < end:
        lt, gt = partition3way(l, start, end, hook_func)
        quick_sort3way_faster(l, start, lt, hook_func)
        quick_sort3way_faster(l, gt, end, hook_func)
    return l


def partition5sample(l, start, end, hook_func, sample_no=5):
    '''
    @brief  五取样切分使用从数组中采样的五个数的中位数进行parition
    @param  l   
    @param  start
    @param  end
    @param  hook_func
    @param  sample_no   采样数
    '''

    def get_mid(l, part_list):
        '''
        @brief  返回中位数对应的value在l中的索引，如果l的数组为偶数则选择len(l)/2
        '''
        part_values = [l[i] for i in part_list]
        mid_value = part_values[int(len(part_values) / 2)]
        for i in part_list:
            if l[i] == mid_value:
                return i, mid_value

    part_index_list = [random.randint(start, end) for i in range(sample_no)]
    anchor, _ = get_mid(l, part_index_list)

    l[anchor], l[start] = l[start], l[anchor]

    return partition(l, start, end, hook_func)


def quick_sort5sample(l, start, end, hook_func=None):
    '''
    @brief  快速排序[start, end)，parition时使用从数组中随机采样的五个数的中位数进行切分
    @param  l   list
    @param  start    左边边界
    @param  end   右边边界
    @param  hook_func   hook用function
    '''
    if start < end:
        anchor = partition5sample(l, start, end, hook_func)
        quick_sort5sample(l, start, anchor - 1, hook_func)
        quick_sort5sample(l, anchor + 1, end, hook_func)
    return l


def quick_sort_cyc(l, start, end, hook_func=None):
    '''
    @brief  快速排序非递归版本
    @param  l   list
    @param  start
    @param  end
    @parma  hook_func
    @note   建立一个容器，容器的每个元素是一个tuple表示需要进行partition的start和end
    '''
    rst = stack.stack()
    snd = stack.stack()
    rst.push((start, end))
    while not rst.empty():
        while not rst.empty():
            start, end = rst.pop()
            if end < start:
                continue

            anchor = partition(l, start, end, hook_func)
            snd.push((start, anchor - 1))
            snd.push((anchor + 1, end))

        rst, snd = snd, rst
    return l


all = [
    quick_sort, quick_sort_II, quick_sort3way, quick_sort3way_faster,
    quick_sort5sample, quick_sort_cyc
]
