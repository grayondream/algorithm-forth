import os


#1.1.28
#移除数组中的重复元素
def remove_repeat_ele(l:list):
    '''
    @brief  移除数组中重复元素
    @param  l   目标数组
    '''
    l = l.copy()
    count = 0
    for i in range(len(l) - 1):
        if l[i] == l[i + 1]:
            count += 1

        l[i] = l[i + count]

    return l[:-count]

#1.1.29
#返回数组中小于target的元素数量
def get_lower_num(l:list, start:int, end:int, target:int):
    '''
    @brief  返回start:end+1之间小于target的元素的数量
    @param  l   目标数组
    @param  start   开始位置
    @param  end 结束位置
    @param  target  目标值
    @return 小于target的数量
    '''
    copy_start = start
    while start <= end:
        mid = start + (end - start)/2
        if target == l[mid]:
            while mid > start and l[mid] == target :
                mid -= 1

            return mid - copy_start + 1
        elif target > l[mid]:
            if mid < end and l[mid + 1] > target:
                return mid - copy_start

            start = mid + 1
        else:
            end = mid - 1


#1.1.33
class matrix(object):
    def __init__(self):
        super(matrix, self).__init__()

    @staticmethod
    def dot(v1:list, v2:list):
        '''
        @brief  向量点×
        @param  v1  向量1   1*n
        @param  v2  向量2   1*n
        @return 向量
        '''
        assert len(v1) == len(v2)
        return [v1[i] * v2[i] for i in range(len(v1))]

    @staticmethod
    def transpose(m:list):
        '''
        @brief  矩阵转置
        @param  m   矩阵，暂时用list代替，二维的list
        @return 矩阵
        '''
        row = len(m)
        col = len(m[0])
        res = [[0] * row] * col     #预先分配转置后的空间
        for i in range(row):
            for j in range(col):
                res[j][i] = m[i][j]

    @staticmethod
    def mult_mm(m1:list, m2:list):
        '''
        @brief  矩阵相乘
        @param  m1  第一个矩阵s * n
        @param  m2  第二个矩阵n * m
        '''
        s, n = len(m1), len(m1[0])
        n, m = len(m2), len(m2[0])
        res = [[0] * s] * m
        for i in range(s):
            for j in range(m):
                for k in range(n):
                    res[i][j] += m1[i][k] * m2[k][j]

        return res

    @staticmethod
    def mult_vm(v:list, m:list):
        '''
        @brief  向量和矩阵相乘
        @param  v   向量1*n
        @param  m   矩阵n * m
        '''
        assert len(v) == len(m), 'len(v) != len(m)'
        row, col = len(m), len(m[0])
        res = [[0] * row]
        for i in range(row):
            for index in range(col):
                res[i][0] += v[i] * m[row][i]

        return res

def main():
    pass
if __name__ == '__main__':
    main()