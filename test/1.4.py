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
    
    
def list_shared_value(rst, snd):
    '''
    @brief  1.4.12  返回有序数组rst和snd的公共元素
    @param  rst 第一个列表
    @param  snd 第二个列表
    @return list
    '''
    ret = []
    i = 0
    j = 0
    while i < len(rst) and j < len(snd):
        if rst[i] == snd[j]:
            ret.append(rst[i])
            i += 1
            j += 1
        elif rst[i] > snd[j]:
            i += 1
        else:
            j += 1
    
    return ret
    

def four_sum_force(l, target):
    '''
    @brief  1.4.14 寻找出数组中四个数之和为target的组合个数，暴力查找法
    @param  l   list
    @param  target  目标值
    @return 数量
    '''
    count = 0
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                for n in range(k + 1, len(l)):
                    if target == l[i] + l[j] + l[k] + l[n]:
                        count += 1
    
    return count


def four_sum_bin(l, target):
    '''
    @brief  1.4.14 寻找出数组中四个数之和为target的组合个数，二分查找法
    @param  l   list
    @param  target  目标值
    @return 数量
    '''
    count = 0
    l.sort()
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if binary_search.binary_search(l, k + 1, len(l), target - l[i] - l[j] - l[k]) != -1:
                    count += 1
    
    return count
    

def two_sum_faster(l, target):
    '''
    @brief  1.4.15 寻找出有序数组中两个值之和为target的组合的个数，要求算法O(n)
    @param  l   list
    @param  target  目标值
    '''
    left = 0
    right = len(l) - 1
    count = 0
    while left <= right:
        if l[left] + l[right] == target:
            count += 1
        elif l[left] + l[right] < target:
            left += 1
        else:
            right -= 1
        
    return count
    

def three_sum_faster(l, target):
    '''
    @brief  参照two_sum_faster寻找出有序数组中三个数之和为target的个数，要求算法O(n*n)
    @param  l   list
    @param  target  目标值
    '''
    for i in range(len(l)):
        left = i + 1
        right = len(l) - 1
        count = 0
        while left <= right:
            if l[left] + l[right] + l[i] == target:
                count += 1
            elif l[left] + l[right] + l[i] < target:
                left += 1
            else:
                right -= 1
                
    return count 
    
    
def nearest_pair(l):
    '''
    @brief  1.4.16 设计线性对数级别的算法找出list中距离最近的两个元素
    @param  l   list
    '''
    

def farest_pair(l):
    '''
    @brief  1.4.17  设计线性对数级别的算法找出list中距离最远的两个元素
    @param  l   list
    '''
    
if __name__ == '__main__':
    pass