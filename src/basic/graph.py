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
    
    def has_edge(self, v, w):
        '''
        @brief  判断v和w之间是否有边
        '''
        
    def find(self, v):
        '''
        @brief  找到v对应的节点
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
        
    
class nodigraph(graph):
    '''
    @brief  无向图的邻接表表示
    '''
    def __init__(self, vecs):
        self.vecs = []      #存储带头节点的链表
        self.es_len = 0
        super(nodigraph, self).__init__(vecs)
        if vecs is None:
            self.build(self.vecs)
        
    def build(self, vecs):
        for vec in vecs:
            self.add_e(vec[0], vec[1])
            
    def find(self, v):
        for vec in self.vecs():
            if v == vec.next.data:
                return vec
                
        return None
        
    def has_edge(self, v, w):
        vec = self.find(v)
        for vec.next is not None:
            if vec.next.data == w:
                return True
                
        return False
        
    def add_e(self, v1, v2):
        v1_vec = self.find(v1)
        v2_vec = self.find(v2)
        if v1_vec is None and v2_vec is not None:
            node = linklist.linklist(v1, None)
            head = linklist.linlist(None, node)
            self.vecs.append(head)
            
            #向v2中添加v1
            v1_node = linklist.linklist(v1, v2_vec.next.next)
            v2_vec.next.next = v1_node
        elif v2_vec is None and v1_vec is not None:
            node = linklist.linklist(v2, None)
            head = linklist.linlist(None, node)
            self.vecs.append(head)
                
            #向v1中添加v2
            v2_node = linklist.linklist(v2, v1_vec.next.next)
            v1_vec.next.next = v2_node
        elif v1_vec is None and v2_vec is None:
            v1_node = linklist.linklist(v1, None)
            v1_head = linklist.linlist(None, v1_node)
            self.vecs.append(v1_head)

            #向v2中添加v1
            v1_node = linklist.linklist(v1, v2_node.next.next)
            v2_node.next.next = v1_node

            v2_node = linklist.linklist(v2, None)
            v2_head = linklist.linlist(None, v2_node)
            self.vecs.append(v2_head)
            
            #向v1中添加v2
            v2_node = linklist.linklist(v2, v1_node.next.next)
            v1_node.next.next = v2_node
        else:
            if self.has_edge(v1, v2):
                return
            else:
                v1_node = linklist.liklist(v1, v2_vec.next.next)
                v2_node = linklist.liklist(v2, v1_vec.next.next)
                
                v2_vec.next.next = v1_node
                v1_vec.next.next = v2_node
                
        
        
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
            self.edge_to[v] = None
            
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
                
    def dst_to(self, v):
        '''
        @brief  返回s和v之间的路径长度
        '''
        count = 0
        while v != self.s:
            v = self.edge_to[v]
            count += 1
            
        return count
        
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
            elif w != adj:
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
                self.color[adj] = !self.colors[v]
            elif self.color[adj] == self.color[v]:
                return False
                
        return True