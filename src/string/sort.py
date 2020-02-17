'''
字符串排序
'''
def lsb(str_list, w):
    '''
    @brief  低位优先的字符串排序
    @param  str_list    字符串数组
    @param  w   单个字符串的长度
    @note   只适用于长度相同的键值
    '''
    size = len(str_list)
    r = 256;
    aux = [''] * size
    d= w - 1
    while d >= 0:
        count = [0] * (r + 1)
        for i in range(size):
            count[str_list[i][d] + 1] += 1
            
        for i in range(0, r):
            count[r + 1] += count[r]
            
        for i in range(size):
            aux[count[str_list[i][d]]] = str_list[i]
            count[str_list[i][d]] += 1
            
        for i in range(size):
            str_list[i] = aux[i]
            
        d -= 1
        

class msd(object):
    '''
    @brief  高位优先字符串排序
    '''
    def __init__(self, str_list)
        self.r = 256
        self.aux = [''] * len(str_list)
        self.m = 15
        self.sort(0, len(l) - 1, 0)    
        
    def chart_at(self, l, id):
        if d < len(l):
            return l[id]
        else:
            return -1
    
    def sort(self, l, low, high, d):
        if high <= low + self.m:
            
        count  = [0] * self.r
        for i in range(low, high + 1):
            count[self.chart_at(l[i], d) + 2] += 1
            
        for i in range(0, self.r + 1):
            count[r + 1] += count[r]
            
        for i in range(low, high + 1):
            self.aux[count[self.chart_at(l[i], d) + 1]] = l[i]
            count[self.chart_at(l[i], d)] += 1
            
        for i in range(low, high + 1):
            l[i] = self.aux[i - low]
            
        for i in range (0, self.r):
            self.sort(l, low + count[i], low + count[i + 1] - 1, d + 1)
            
    def insert_sort(self, l, low, high, d):
        for i in range(low, high + 1):
            j = i
            while j > low and self.less(l[j], l[j - 1], d):
                l[j], l[j - 1] = l[j - 1], l[j]
                j -= 1
                
    def less(self, rst, snd, d):
        return rst[d:] < snd[d:]
        
class quick3string(object):
    '''
    @brief  算法原理类似于快速三项切分
    '''
    def __init__(self, l):
    
    def chart_at(self, l, id):
        if d < len(l):
            return l[id]
        else:
            return -1
    
    def sort(self, l, low, high, d):
        if low >= high:
            return
            
        lt = low
        gt = high
        v = self.chart_at(l[low], d)
        i = low + 1
        while i <= gt:
            t = self.chart_at(l[i], d)
            if t < v:
                l[lt], l[i] = l[i], l[lt]
                i += 1
                lt += 1
            elif t > v:
                l[i], l[gt] = l[gt], l[i]
                gt -= 1
            else:
                i += 1
                
        self.sort(l, low, lt - 1, d)
        if v > 0:
            self.sort(l, lt, gt, d + 1)
        
        self.sort(l, gt + 1, high, d)