from src.search import binary_search
import sys
from src.basic import stack


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
    l.sort()
    rst = 0
    snd = 0
    for i in range(1, len(l)):
        if abs(rst - snd) > abs(l[i - 1], l[i]):
            rst = l[i - 1]
            snd = l[i]
    
    return rst, snd
    

def farest_pair(l):
    '''
    @brief  1.4.17  设计线性对数级别的算法找出list中距离最远的两个元素
    @param  l   list
    @param  找出最大值和最小值即可
    '''
    max_ele = 0
    min_ele = sys.maxsize
    for ele in l:
        max_ele = max(max_ele, ele)
        min_ele = min(min_ele, ele)
        
    return max_ele, min_ele
    
    
def local_min(l):
    '''
    @brief  1.4.18  寻找出local最小值的index，a[i]<a[i+1] and a[i-1]>a[i]
    @param  l   list
    @return index
    '''
    size = len(l)
    if 1 == size:
        return 0
    elif l[0] < l[1]:
        return 0
    elif l[size - 2] > l[size - 1]:
        return size - 1
        
    left = 1
    right = size - 2
    while left <= right:
        mid = left + (right - left)/2
        if l[mid] < l[mid - 1] and l[mid] < l[mid + 1]:
            return mid
        elif l[mid] > l[mid - 1]:
            right = mid - 1
        elif l[mid] > l[mid + 1]:
            left = mid + 1
            
    return -1
        

def minium_index(l):
    ret = l[0]
    for i in range(1, len(l)):
        if l[i] < ret:
            ret = i
            
    return ret
    
    

def matrix_partition(matrix, row, col):
    '''
    @brief  matrix_local_min的分治部分
    @param  matrix  矩阵
    @param  row 行
    @param  col 列
    '''
    cur_item = matrix[row][col]
    left = matrix[row][col - 1 if col - 1 >= 0 else col]
    top = matrix[row - 1 if row - 1>= 0 else row][col]
    bottom = matrix[row + 1 if row + 1 < len(matrix) else row][col]
    right = matrix[row][col + 1 if col + 1 < len(matrix[0]) else col]
    
    items = [left, top, right, bottom]
    items.sort()
    min_item = items[0]
    
    ret_row = row
    ret_col = col
    if min_item == cur_item:
        return ret_row, ret_col
    elif min_item == left:
        ret_col = col - 1
        matrix_partition(matrix, ret_row, ret_col)
    elif min_item == right:
        ret_col = col + 1
        matrix_partition(matrix, ret_row, ret_col)
    elif min_item == top:
        ret_row = row - 1
        matrix_partition(matrix, ret_row, ret_col)
    elif min_item == bottom:
        ret_row = row + 1
        matrix_partition(matrix, ret_row, ret_col)
    else:
        pass
        
    return ret_row, ret_col
    
    
def matrix_local_min(matrix):
    '''
    @brief  1.4.19 寻找去matrix中的局部最小值，要求算法规模O(n),局部最小值表示当前元素小于四周的元素
    @param  matrix  矩阵
    @return     value
    @note   参照：https://www.jianshu.com/p/b4f5cb071f04
            解法一：找到每一列的局部最小值，然后遍历找到的最小值，判断是不是局部最小值
            解法二：分治算法，将大矩阵拆分为小矩阵,matrix_partition的代码暂时并未完全搞懂
            TODO:
    '''
    mid_row = int(len(matrix) / 2)
    mid_row_array = matrix[mid_row]
    mid_min_index =minium_index(mid_row_array)
    return matrix_partition(matrix, mid_row, mid_min_index)
    
    
def double_tone_search(l, value):
    '''
    @brief  1.4.20  数组是先升后降判断value是否在数组中，要求最坏情况3lgn
    @param  l   list
    @param  value   需要search的值
    @return True or False
    '''
    left = 0 
    right = len(l) - 1
    #先寻找最大值
    mid  = None
    while left <= right:
        mid = left + (right - left)/2
        if mid > 0 and mid < len(l) and l[mid - 1] < l[mid] and l[mid] < l[mid + 1]:
            break
        elif l[mid] > l[mid - 1]:
            left = mid + 1
        elif l[mid + 1] < l[mid]:
            right = mid - 1
        
    if value > l[mid] or value < l[0] or value < l[len(l) - 1]:
        return False
    else:
        ret = binary_search.binary_search(l, 0, mid, value)
        if -1 != ret:
            return ret
        else:
            return -1 != binary_search.binary_search(l, mid, len(l) - 1, value)
            
    return False
    
    
'''
1.4.22 见 binary_search.binary_search_constrain
'''


def binary_search_rational(l, value):
    '''
    @brief  1.4.23  比较l中是否存在和有理数value相同的值，比较规则，abs(value - item) < 1/n*n即可
    @param  l   list
    @param  value   值
    @return     index
    '''
    left = 0
    right = len(l) - 1
    while left <= right:
        mid = left + (right - left)/2
        if abs(l[mid] - value) < 1 / (len(l) * len(l)):
            return mid
        elif l[mid] > value:
            right = mid - 1
        else:
            left = mid + 1


def single_egg(n):
    '''
    @brief  1.4.24 一个鸡蛋判断鸡蛋不摔坏的楼层，O(F),F为目标楼层
    @param  n   楼层数目
    @return 目标楼层F
    @note   一层一层的试
    '''
    
    

def double_egg(n):
    '''
    @brief  1.4.25 两个鸡蛋判断楼层，O(cF^1/2)
    @param  n   楼层高度
    @return 目标楼层F
    @note   https://www.jianshu.com/p/165570d1696a
    14次
    [14, 27, 39, 50, 60, 69, 77, 84, 90, 95, 99, 100]
    '''
    pass
    

'''
1.4.27  两个栈实现一个队列   1.3做过
1.4.28  队列实现栈，简单懒得写
1.4.29  两个栈实现stqueue，不重复造轮子
1.4.30  单个栈和stqueue实现双向队列，不多说
'''

class double_queue_with_stack(object):
    '''
    @brief  1.4.31  使用三个栈实现双向队列
    @note   left和right分别作为left和right操作栈，mid作为缓冲栈进行元素的调整,mid_type表示栈中元素类型，false表示为left的元素否则为right的元素
    '''
    def __init__(self):
        super(double_queue_with_stack, self).__init__()
        self.left = stack.stack()
        self.right = stack.stack()
        self.mid = stack.stack()
        self.mid_type = True     
        self.len = 0
        
    def push_left(self, item):
        self.left.push(item)
        self.len += 1
        
    def pop_left(self):
        if self.empty():
            return None
        else:
            if not self.left.empty() and not self.mid.empty() and not self.mid_type:
                self.len -= 1
                return self.mid.pop()
            elif not self.left.empty() and self.mid.empty() and not self.mid_type:
                self.mid_type = False
                while not self.left.empty():
                    self.mid.push(self.left.pop())
                self.len -= 1
                return self.mid.pop()
            elif not self.left.empty() and not self.mid.empty() and self.mid_type:
                #mid  --> left
                #right --> mid
                #left--> mid
                #mid --> right
                count = 0
                while not self.mid.empty():
                    self.left.push(self.mid.pop())
                    count += 1    
                
                while not self.right.empty():
                    self.mid.push(self.right.pop())
                    
                while count != 0:
                    count -= 1
                    self.mid.push(self.left.pop())
                    
                while not self.mid.empty():
                    self.right.push(self.mid.pop())
                    
                return self.pop_left()
            elif self.left.empty() and self.mid.empty() and not self.right.empty():
                self.pop_right()
                
    def push_right(self, item):
        self.right.push(item)
        self.len += 1
        
    def pop_right(self):
        if self.empty():
            return None
        else:
            if not self.right.empty() and not self.mid.empty() and self.mid_type:
                self.len -= 1
                return self.mid.pop()
            elif not self.right.empty() and self.mid.empty() and self.mid_type:
                self.mid_type = True
                while not self.right.empty():
                    self.mid.push(self.right.pop())
                self.len -= 1
                return self.mid.pop()
            elif not self.right.empty() and not self.mid.empty() and not self.mid_type:
                #mid  --> right
                #left --> mid
                #right--> mid
                #mid --> left
                count = 0
                while not self.mid.empty():
                    self.right.push(self.mid.pop())
                    count += 1    
                
                while not self.left.empty():
                    self.mid.push(self.left.pop())
                    
                while count != 0:
                    count -= 1
                    self.mid.push(self.right.pop())
                    
                while not self.mid.empty():
                    self.left.push(self.mid.pop())
                    
                return self.pop_right()
            elif self.right.empty() and self.mid.empty() and not self.left.empty():
                self.pop_left()
        
    def size(self):
        return self.len
        
    def empty(self):
        return 0 == self.size()
    
def secret_number(n, value):
    '''
    @brief  1.4.34  每次猜测一个1-n的数，每次系统会反馈改数离目标数远还是近，使用O(2logn)和O(logn)算法实现
    @param  value   目标值，假设程序不知道
    '''
if __name__ == '__main__':
    pass