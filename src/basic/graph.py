from src.basic import linklist


'''
图的不同表示
'''
class graph(object):
    '''
    @brief  接口定义
    '''
    def __init__(self, vecs):
        super().__init__()
        self.build(vecs)
        
    def build(self, vecs):
        '''
        @brief  使用vecs数组构建图
        '''
        
    def v_len(self):
        '''
        @brief 顶点数
        '''
        
    def vs(self):
        '''
        @brief 所有顶点
        '''
        
    def e_len(self):
        '''
        @brief  边数
        '''
        
    def es(self):
        '''
        @brief 所有边
        '''
        
    def adj(self, v):
        '''
        @brief  返回和v相邻的顶点
        '''
        
    def add_e(self, v1, v2):
        '''
        @brief  向图中添加边
        '''
        
    def degree(self, v):
        '''
        @brief  返回点v的度
        '''
        return len(self.adj(v))
        
    def max_degree(self):
        '''
        @brief  计算最大度数
        '''
        max_d = 0
        for v in self.vs():
            d = self.degree(v)
            if d > max_d:
                max_d = d
                
        return max_d
        
    def avg_degree(self):
        '''
        @brief  平均度数
        '''
        return 2 * self.e_len() / self.v_len()
        
    def loops_no(self):
        '''
        @brief  自环个数
        '''
        count = 0
        for v in self.vs():
            for adj_v in self.adj(v):
                if v == adj_v:
                    count += 1
                    
        return count
        
    
class graph_adj(graph):
    '''
    @brief  无向图的邻接表表示
    '''
    def __init__(self, vecs):
        self.vecs = []      #存储带头节点的链表
        self.es_len = 0
        super().__init__(vecs)
        
    def build(self, vecs):
        for vec in vecs:
            self.add_e(vec)
            
    def add_e(self, v1, v2):
        head = None
        v1_added = False
        v2_added = False
        for vec in self.vecs:
            add_vec = None
            if vec.next.data == v1 or vec.next.data == v2:
                head = vec
                add_vec = v1 if vec == v1 v2
                while head.next is not None:
                    if head.next.data == add_vec:
                        return
                    
                    head = head.next
                
                node = linklist.linklist(add_vec, None)
                self.es_len += 1
                if add_vec == v1:
                    v1_added = True
                elif add_vec == v2:
                    v2_added = True
                    
                head.next = node
                
        if not v1_added:        
            node = linklist.linklist(v2, None)
            head = linklist.linklist(None, node)
            self.vecs.append(head)
            self.es_len += 1
        
        if not v2_added:
            node = linklist.linklist(v1, None)
            head = linklist.linklist(None, node)
            self.vecs.append(head)
            self.es_len += 1
        
        def v_len(self):
            return len(self.vecs)
            
        def e_len(self):
            return self.es_len
                
        def vs(self):
            return [vec.next.data for vec in self.vecs]
            
        def es(self):
            ret = []
            for head in self.vecs:
                index = head
                while index.next is not None:
                    ret.append((head.next.data, index.next.data))
                    index = index.next
                    
            return ret
            
        def adj(self, v):
            for vec in self.vec:
                if vec.next.data == v:
                    i = vec:
                    ret = []
                    while i.next is not None:
                        ret.append(i.next.data)
                        i = i.next
                        
                    return ret
            
            return []
    
    
def dfs_graph(object):
    '''
    @brief  深度优先搜索图
    '''
    def __init__(g):
        self.count = 0
        self.marked_flags = {}
        self.g = g
        for v in g.vs():
            self.marked_flags[v] = False
        
    def marked(self, v):
        return self.marked[v]
        
    def get_count(self):
        return self.count
        
    def dfs(self, v):
        for vec in self.g.vs():
            if not self.marked(vec):
                for adj in self.g.adj():
                    if not self.marked(adj):
                        self.count += 1
                        self.marked_flags[v] = True
                        dfs(adj)