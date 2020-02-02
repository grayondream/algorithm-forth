from src import sort


def dedup(line):
    '''
    @brief  2.5.4   返回一个有序的数组，删除其中的重复元素
    '''
    sort.insert_sort.insert_sort(line, 0, len(line) - 1)
    count = 0
    for i in range(1, len(line)):
        if line[i - 1] == line[i]:
            count += 1
            
        line[i] = line[i + count]
        
    line = line[-1 * count:]
    return line
    
    
def frequency(lines):
    '''
    @brief  2.5.8   根据字符串出现的次数从高到低排序输出
    '''
    sort.insert_sort.insert_sort(lines, 0, len(lines) - 1)
    ret = {}
    for i in range(len(lines)):
        if lines[i] in ret.keys():
            ret[lines[i]] += 1
        else:
            ret[lines[i]] = 1
            
    return ret
    
    
def spt_shortest_first(tasks):
    '''
    @brief  2.5.12 最短时间优先原则, tasks是一个[]，每个成员[]第一个是元素是任务名称，第二个是执行时间
    '''
    for i in range(len(tasks)):
        min_index = i       
        for j in range(i + 1, len(tasks)):
            if tasks[min_index][1] > tasks[j][1]:
                min_index = j

        tasks[i], tasks[min_index] = tasks[min_index], tasks[i]
        
    return tasks
    
    
def spt_longest_first(tasks):
    '''
    @brief  2.5.13 最长时间优先原则
    '''
    for i in range(len(tasks)):
        max_index = i       
        for j in range(i + 1, len(tasks)):
            if tasks[max_index][1] < tasks[j][1]:
                min_index = j

        tasks[i], tasks[min_index] = tasks[min_index], tasks[i]
        
    return tasks
    
        
def domain_sort(domains):
    '''
    @brief  2.5.14  将域名按照每个域名自身的逆序进行排序，www.baidu.com的逆序为com.baidu.www
    @note   domains 每个元素是一个字符串,如www.baidu.com
    '''
    def reverse_domain(domain):
        lines = domain.split('.')
        ret = ''
        for i in range(len(lines)):
            ret += '.' + lines[i]
        
        return ret[1:]
    
    for i in range(len(domains)):
        max_index = i       
        for j in range(i + 1, len(domains)):
            if reverse_domain(domains[max_index]) < reverse_domain(domains[j]):
                min_index = j

        domains[i], domains[min_index] = domains[min_index], domains[i]
        
    return domains
    
    
def califormia(names):
    '''
    @brief  按照seq中的字母大小顺序排序姓名列表
    seq = [r, w, q, o, j, m, v, a, h, b, s, g, z, x, n, t, c, i, e, k, u, p, d, y, f, l]
    '''
    def lesser(rst, snd):
        seq = {'r':0, 'w':1, 'q':2, 'o':3, 'j':4, 'm':5, 'v':6, 'a':7, 'h':8, 'b':9, 's':10, 'g':11, 'z':12, 'x':13, 'n':14, 't':15, 'c':16, 'i':17, 'e':18, 'k':19, 'u':20, 'p':21, 'd':22, 'y':23, 'f':24, 'l':25}
        rst = rst.lower()
        snd = snd.lower()
        for i in range(min(len(rst), min(len(snd)))):
            if seq[rst[i]] < seq[snd[i]]:
                return 1    #<
            elif seq[rst[i]] > seq[snd[i]]:
                return 2    #>
                
        if len(rst) == len(snd):
            return 0
        elif len(rst) < len(snd):
            return 1
        else:
            return 2
            
            
    for i in range(len(names)):
        max_index = i       
        for j in range(i + 1, len(names)):
            if lesser(names[max_index], names[j]) != 2:
                min_index = j

        names[i], names[min_index] = names[min_index], names[i]
        
    return names
    
    
def kendall_tau(rst, snd):
    '''
    @brief  2.5.19  两组排列之间的kendall_tau距离
    @note   Kendall tau距离就是两个排列之间的逆序数，它反映了两个排列的相似程度。
            例如两个在区间[ 0 , 6 ]的排列:
                                        a = { 0, 3, 1, 6, 2, 5, 4 }
                                        b = { 1, 0, 3, 6, 4, 2, 5 }
                                        两个排列之间的逆序{ 0，1 }，{ 3，1 }，{ 2，4 }，{ 5，4 }，一共为4对，故Kendall tau距离为4。
                                        也就是说列出的数对，在第一个数组中为[rst, snd]，第二个数组中为[snd, rst]
    '''
    tmp = [0] * len(rst)
    for i in range(len(rst)):
        tmp[rst[i]] = i
        
    tmp2 = [0] * len(snd)
    for i in range((len(snd))):
        tmp2[i] = tmp[snd[i]]
        
    def insert_sort(l):
        count = 0
        for i in range(1, len(l)):
            j = i
            while j > 0 and l[j] < l[j - 1]:
                l[j], l[j - 1] = l[j - 1], l[j]
                count += 1
        return count
        
    return insert_sort(tmp2)
    
def free_time(tasks):
    '''
    @brief  2.5.20  给定多个任务的起始和结束时间，返回期间cpu空闲的最长时间
    @param  tasks   每个元素是一个长度为2的list，[0] start, [1] end
    '''
    def sort_task(tasks):
        for i in range(len(tasks)):
            min_index = i       
            for j in range(i + 1, len(tasks)):
                if tasks[min_index][1] > tasks[j][1]:
                    min_index = j
    
            tasks[i], tasks[min_index] = tasks[min_index], tasks[i]
        
        return tasks
    
    tasks = sort_task(tasks)
    free_time = 0
    for i in range(1, len(tasks)):
        if tasks[i - 1][1] < tasks[i][1] and tasks[i][1] - tasks[i - 1][1] > free_time:
            free_time = tasks[i][1] - tasks[i - 1][1]
    
    return free_time
    
    
def sort_mult_vector(l):
    '''
    @brief  2.5.21  多维数组排序
    '''
    if not isinstance(l, list):
        return
    
    for i in range(len(l)):
        sort_mult_vector(l[i])
    
    def lesser(rst, snd):
        if isinstance(rst, list) and isinstance(snd, list):
            size_rst, size_snd = len(rst), len(snd)
            for i in range(min(size_rst, size_snd)):
                if rst[i] < snd[i]:
                    return True
                elif rst[i] > snd[j]:
                    return False
                else:
                    pass
                
            return size_rst < size_snd
        else:
            return rst < snd
            
    def sort_sub(l):
        for i in range(len(l)):
            min_index = i
            for j in range(i + 1, len(l)):
                if lesser(l[min_index], l[j]):
                    min_index = j
            
            l[min_index], l[i] = l[i], l[min_index]
        
    sort_sub(l)
    
    
def loyd(l, x, y):
    '''
    @brief  2.5.32  九宫格只空出一个位置将其他八个排序，每个棋子只要旁边有空位就可以向空位移动
    @param  l   九宫格的数组
    @param  x,y 空位的坐标
    @note   TODO:unsolved
    '''
    
    
if __name__ == '__main__':
    pass
    
