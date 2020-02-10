from src.basic import linklist, stack, queue


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
    
   
class dfs_graph(object):
    '''
    @brief  深度优先搜索图
    @param  g   进行搜索的图
    @param  marked_flags    图中结点是否进行搜索的标志
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
        
    def dfs(self):
        for vec in self.gs.vs():
            if not self.marked(vec):
                self.dfs_v(vec)
                
    def dfs_v(self, v):
        for adj in self.g.adj(v):
            if not self.marked(adj):
                self.count += 1
                self.marked_flags[v] = True
                self.dfs_v(adj)
                        
                        
class dfs_paths(object):
    '''
    @brief 从已知的graph中搜索出顶点s相关路径，只能保证找到路径
    @param g    进行搜索的图
    @param  s   图中进行搜索的顶点
    @param  marked_flags    顶点和s之间是否有path的标志
    @param  edge_to key为节点，value为当前结点的父节点
    '''
    def __init__(self, g, s):
        self.s = s
        self.marked_flags = {}
        self.edge_to = {}
        self.g = g
        for v in self.g.vs():
            self.marked_flags[v] = False
            
        self.dfs(self.g, s)
        
    def dfs(self, g, v):
        self.marked_flags[v] = True
        for w in g.adj(v):
            if self.marked_flags[w]:
                self.edge_to[w] = v
                dfs(g, w)
                
    def has_path_to(self, v):
        '''
        @brief  s->v是否有路径
        '''
        return self.marked_flags[v]
        
    def path_to(self, v):
        '''
        @brief  s到v的路径
        '''
        if self.has_path_to(v):
            path = stack.stack()
            while v != self.s:
                path.push(v)
                v = self.edge_to[v]
                
            path.push(self.s)
        
        return path
        
        
class bfs_graph(object):
    '''
    @brief  图的广度优先搜索算法
    @param  marked  是否访问过
    @param  s 起点
    @note   类似于树的按层遍历
    '''
    def __int__(self, g):
        self.marked = {}
        self.g = g
        self.count = 0
        for v in g.vs():
            self.marked[v] = False
            
    def bfs(self):
        q = queue.queue()
        for v in self.v.vs():
            if self.marked[v]:
                continue
                
            q.enqueue(v)
            self.marked[v] = True
            while not q.empty():
                v = q.dequeue()
                for adj in self.g.adj(v):
                    if not self.marked[adj]:
                        self.marked[adj] = True
                        q.enqueue(adj)
                        self.count += 1
                        
                        
class bfs_paths(object):
    '''
    @brief 从已知的graph中搜索出顶点s相关路径，只能保证找到路径
    @param g    进行搜索的图
    @param  s   图中进行搜索的顶点
    @param  marked_flags    顶点和s之间是否有path的标志
    @param  edge_to key为节点，value为当前结点的父节点
    '''
    def __init__(self, g, s):
        self.s = s
        self.marked_flags = {}
        self.edge_to = {}
        self.g = g
        for v in self.g.vs():
            self.marked_flags[v] = False
            
        self.bfs(self.g, s)
        
    def bfs(self, g, v):
        q = queue.queue()
        q.enqueue(v)
        self.marked[v] = True
        while not q.empty():
            v = q.dequeue()
            for adj in g.adj(v):
                if not self.marked[adj]:
                    self.edgs_to[adj] = v
                    self.marked[adj] = True
                    q.enqueue(adj)
                
    def has_path_to(self, v):
        '''
        @brief  s->v是否有路径
        '''
        return self.marked_flags[v]
        
    def path_to(self, v):
        '''
        @brief  s到v的路径
        '''
        if self.has_path_to(v):
            path = stack.stack()
            while v != self.s:
                path.push(v)
                v = self.edge_to[v]
                
            path.push(self.s)
        
        return path
        
        
class graph_cc(object):
    '''
    @brief  
    @param  g   进行搜索的图
    @param  count   联通分量个数
    '''
    
    def __init__(self, g):
        self.g = g
        self.cc_ids = [0] * self.g.v_len()
        self.count = 0
        self.marked = {}
        for v in self.g.vs():
            self.marked[v] = False

        self.dfs(self.g)
            
    def connect(self, v, w):
        '''
        @brief  v和w是否联通
        '''
        return self.cc_ids[v] == self.cc_ids[w]
    
    def dfs(self, g):
        for v in g.vs():
            if not self.marked[v]:
                self.count += 1
                self.dfs_v(g, v)
                self.id[v] = self.count
                
    def dfs_v(self, g, vec):
        self.marked[v] = True
        for adj in g.adj(v):
            if not self.marked[adj]:
                self.dfs(g, adj)
                

class graph_cycle(object):
    '''
    @brief  判断图中是否包含环，假定不包含自环和平行边
    '''
    def __init__(self, g):
        self.marked = {}
        self.g = g
        for v in self.g.vs():
            self.marked[v] = False
            
    def dfs(self, g):
        for v in g.vs():
            if not self.marked[v]:
                if self.dfs_v(g, v, v):
                    return True
            
    def dfs_v(self, g, v, w):
        self.marked[v] = True
        for adj in g.adj():
            if not self.marked[v]:
                self.dfs_v(g, w, v)
            elif w == adj:
                return True
                
        return False
        
        
class graph2color(object):
    '''
    @brief  双色问题，将每个节点染色，是否能够保证相邻节点的颜色不同
    '''
    def __init__(self, g):
        self.marked = {}
        self.colors = {}
        self.g = g
        for v in self.g.vs():
            self.marked[v] = False
            self.colors[v] = False
            
    def dfs(self, g):
        for v in g.vs():
            if not self.marked[v]:
                if not self.dfs_v(g, v):
                    return False
            
    def dfs_v(self, g, v):
        self.marked[v] = True
        for adj in g.adj():
            if not self.marked[v]:
                self.dfs_v(g, adj)
                self.color[adj] = !self.color[v]
            elif self.color[adj] == self.color[v]:
                return False
                
        return True