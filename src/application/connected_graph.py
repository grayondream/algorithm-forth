#1.5 连通图
#每一次给定连通图中连个节点的连接状况，判断有多少个连通图
#例如1 2, 2 3, 4 5,表示两个连通图，123为一个，45为一个
class union_find(object):
    '''
    @brief  第一版实现，通过父节点关系
    '''
    def __init__(self, max_no):
        super(union_find, self).__init__()
        self.list = [i for i in range(max_no)]  
        self.count = max_no
        
    def get_parent(self, id):
        return self.list[id]
        
    def is_connect(self, rst, snd):
        return self.get_parent(rst) == self.get_parent(snd)
        
    def union(self, rst, snd):
        p_rst = self.get_parent(rst)
        p_snd = self.get_parent(snd)
        if (p_rst == p_snd):
            return
        else:
            for ele in self.list:
                if ele == p_snd:
                    self.list[self.list.index(ele)] = p_rst
                    
            self.count -= 1
        

class union_find_tree(object):
    '''
    @brief  第二版实现，通过树结构
    @note   缺陷无法生成最优树结构
    '''
    def __init__(self, max_no):
        super(union_find_tree, self).__init__()
        self.list = [i for i in range(max_no)]  
        self.count = max_no
        
    def get_parent(self, id):
        '''
        @note   根节点的parent为自身
        '''
        while id != self.list[id]:
            id = self.list[id]
            
        return id
        
    def union(self, rst, snd):
        p_rst = self.get_parent(rst)
        p_snd = self.get_parent(snd)
        if p_rst == p_snd:
            return
        else:
            self.list[p_rst] = p_snd
            self.count -= 1
        

class union_find_wtree(object):
    '''
    @brief  第二版实现，通过树结构
    @note   通过引入weight因子保证整个树结构的最优化
    '''
    def __init__(self, max_no):
        super(union_find_wtree, self).__init__()
        self.list = [i for i in range(max_no)]  
        self.weight = [1] * max_no
        self.count = max_no
        
    def get_parent(self, id):
        '''
        @note   根节点的parent为自身
        '''
        while id != self.list[id]:
            id = self.list[id]
            
        return id
        
    def union(self, rst, snd):
        p_rst = self.get_parent(rst)
        p_snd = self.get_parent(snd)
        if p_rst == p_snd:
            return
        else:
            if self.weight[p_rst] < self.weight[p_snd]:
                self.list[p_rst] = p_snd
                self.weight[p_snd] += self.weight[p_rst]
            else:
                self.list[p_snd] = p_rst
                self.weight[p_rst] += self.weight[p_snd]
        
            self.count -= 1
        