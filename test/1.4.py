from src.search import binary_search


def three_sum_force(l, target):
    '''
    @brief  在l中查找三个值之和为target的个数暴力解法,时间复杂度O(n^3)
    @param  l   list
    @param  target  目标值
    @return 数量
    '''
    count = 0
    size = len(l)
    for i in range(size):
        for j in range(i + 1, size):
            for k in range(j + 1, size):
                if l[i] + l[j] == target - l[k]:
                    count += 1
    
    return count


def three_sum_bin(l, target):
    '''
    @brief  在l中查找三个值之和为target的个数利用二分查找发解法,时间复杂度O(n^2logn)
    @param  l   list
    @param  target  目标值
    @return 数量
    '''
    count = 0
    size = len(l)
    l.sort()
    for i in range(size):
        for j in range(i + 1, size):
            if binary_search.binary_search(l, j + 1, size, target - l[i] - l[j]) != -1:
                count += 1
    
    return count
    
    
def binary_search_min(l, start, end, target):
    '''
    @brief  1.4.10 二分查找法，返回的是对应元素的最小下标
    @param  l   list
    @param  start   开始位置
    @param  end     结束位置
    @param  target  目标值
    @return -1 or index
    '''
    while start <= end:
        mid = start + (end - start)/2
        if l[mid] > target:
            end = mid - 1
        elif l[mid] < target:
            start = mid + 1
        else:
            #以当前[start, mid]为区域寻找使用二分查找算法查找最小的index
            if mid == 0 or l[mid] != l[mid - 1]:
                return mid
            else:
                end = mid - 1
                while start <= end:
                    mid = start + (end - start)/2
                    if mid == 0 or l[mid] != l[mid - 1]:
                        return mid
                    elif l[mid] < target:
                        start = mid + 1
                    elif l[mid] == target:
                        end = mid - 1
                    else:
                        raise Exception('data error')
    
    return -1
    
    
if __name__ == '__main__':
    pass