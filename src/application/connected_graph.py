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
        

class union_find_tar_tree(object):
    '''
    @brief  第三版实现，树结构带路压缩，在find的时候将每个节点的parent定位到parent
    @note   缺陷无法生成最优树结构
    '''
    def __init__(self, max_no):
        super(union_find_tar_tree, self).__init__()
        self.list = [i for i in range(max_no)]  
        self.count = max_no
        
    def get_parent(self, id):
        '''
        @note   根节点的parent为自身
        '''
        id_rst = id
        while id_rst != self.list[id_rst]:
            id_rst = self.list[id_rst]
            
        id_snd = id
        #将各个节点的parent指向跟节点
        while id_rst != self.list[id_snd]:
            cur = id_snd
            id_snd = self.list[id_snd]
            self.list[cur] = id_rst
            
        return id_rst
        
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
            
        
class union_find_tar_wtree(object):
    '''
    @brief  第二版实现，通过树结构
    @note   通过引入weight因子保证整个树结构的最优化，引入带路压缩
    '''
    def __init__(self, max_no):
        super(union_find_tar_wtree, self).__init__()
        self.list = [i for i in range(max_no)]  
        self.weight = [1] * max_no
        self.count = max_no
        
    def get_parent(self, id):
        '''
        @note   根节点的parent为自身
        '''
        id_rst = id
        while id_rst != self.list[id_rst]:
            id_rst = self.list[id_rst]
            
        id_snd = id
        #将各个节点的parent指向跟节点
        while id_rst != self.list[id_snd]:
            cur = id_snd
            id_snd = self.list[id_snd]
            self.list[cur] = id_rst
            
        return id_rst
        
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
       

class union_find_whtree(object):
    '''
    @brief  第二版实现，通过树结构
    @note   通过引入weight因子保证整个树结构的最优化，引入带路压缩，权重因子使用树的高度进行计算，不能带压缩如果带压缩所有的height为小于2
    '''
    def __init__(self, max_no):
        super(union_find_whtree, self).__init__()
        self.list = [i for i in range(max_no)]  
        self.height = [1] * max_no
        self.count = max_no
        
    def get_parent(self, id):
        '''
        @note   根节点的parent为自身
        '''
        id_rst = id
        while id_rst != self.list[id_rst]:
            id_rst = self.list[id_rst]
            
        id_snd = id
        #将各个节点的parent指向跟节点
        while id_rst != self.list[id_snd]:
            cur = id_snd
            id_snd = self.list[id_snd]
            self.list[cur] = id_rst
            
        return id_rst
        
    def union(self, rst, snd):
        p_rst = self.get_parent(rst)
        p_snd = self.get_parent(snd)
        if p_rst == p_snd:
            return
        else:
            if self.height[p_rst] < self.height[p_snd]:
                self.list[p_rst] = p_snd
                self.height[p_snd] = max(self.height[p_snd], self.height[p_rst] + 1)
            else:
                self.list[p_snd] = p_rst
                self.height[p_rst] = max(self.height[p_rst], self.height[p_snd] + 1)
        
            self.count -= 1
        

class dymnaic_union_find(object):
    '''
    @brief  事先并不知道具体的点数，每次动态的进行添加
    '''
    def __init__(self):
        self.data = []          #使用动态数组
        
    def get_root(self, id):
        for graph in self.data:
            if id in graph:
                return self.data.index(graph)
        
        return None
        
    def union(self, rst, snd):
        g_rst_id = self.get_root(rst)
        g_snd_id = self.get_root(snd)
        g_rst = self.data[g_rst_id]
        g_snd = self.data[g_snd_id]
        if g_rst_id is None and g_snd_id is None:
            self.data.append([g_rst, g_snd])
        elif g_rst_id is None:
            self.data[g_snd_id].append(g_rst)
        elif g_snd_id is None:
            self.data[g_rst_id].append(g_snd)
        else:
            self.append([ele for ele in self.data[g_rst_id] if ele in self.data[g_snd_id]])
            self.data.remove(self.data[g_rst_id])
            self.data.remove(self.data[g_snd_id])
            
            
            
        