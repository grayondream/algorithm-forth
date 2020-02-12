'''
@brief  无向图
'''
from src.basic import graph, linklist, stack, queue


class digraph(graph.nodigraphd):
    def __init__(self, vecs):
        super(digraph, self).__init__(vecs)
        
    def add_e(self, s, d):
        '''
        @brief  添加边s-->d
        '''
        s_vec = self.find(s)
        d_vec = self.find(d)
        if s_vec is None and d_vec is None:
            s_node = linklist.linklist(s, None)
            s_head = linklist.linklist(None, s_node)
            
            d_node = linklist.linklist(d, None)
            d_head = linklist.linklist(None, d_node)
            
            sd_node = linklist.linklist(d, s_head.next.next)
            s_head.next.next = sd_node
            
            self.append(s_head)
            self.append(d_head)
        elif s_vec is not None and s_vec is not None:
            if self.has_edge(s, d):
                return
            else:
                sd_node = linklist.linklist(d, s_head.next.next)
                s_vec.next.next = sd_node
        elif s_vec is None and d_vec is not None:
            s_node = linklist.linklist(s, None)
            s_head = linklist.linklist(None, s_node)
            self.append(s_head)
            
            sd_node = linklist.linklist(d, s_head.next.next)
            s_head.next.next = sd_node
        else:
            d_node = linklist.linklist(d, None)
            d_head = linklist.linklist(None, None)
            self.append(d_head)
            
            sd_node = linklist.linklist(d, s_vec.next.next)
            s_vec.next.next = sd_node
            
        self.e_len += 1
            
    def reverse(self):
        g = digraph(None)
        for v in self.vs():
            for w in self.adj(v):
                g.add_e(w, v)
                
        return g
        
        
class digraph_cycle(object):
    '''
    @brief  判断有向图有没有环
    @note: TODO:这里和书上的实现不太一样
    '''
    def __init__(self, g):
        super().__init__()
        self.g = g
        self.marked = {}
        self.edge_to = {}
        self.stk_flag = {}  #必须有，如果出现1->2->3 1->3就会误判
        for v in self.g.vs():       #vs返回所有的顶点
            self.marked[v] = False
            self.edge_to[v] = None
            self.stk_flag[v] = False
        
        for v in self.g.vs():
            if not self.marked[v]:
                self.dfs_v(g, v)
                
    def dfs_v(self, g, v):
        self.stk_flag[v] = True
        self.marked[v] = True
        for adj in g.adj(v):        #adj为图g的邻接点
            if not self.marked[adj]:
                self.edge_to[adj] = v
                self.dfs_v(g, adj)
            else self.stk_flag[adj]:
                 i = v
                 self.stk = stack.stack()
                 while i != adj:
                    stk.push(i)
                    i = self.edge_to[i]
                    
                stk.push(adj)
                stk.push(v)
        self.stk_flag[v] = False
                
    def is_cycle(self):
        if hasattr(self, 'stk') and not self.stk.empty()
        
    def get_cycle(self):
        return self.stk
        
        
class dfsorder(object):
    def __init__(self, g):
        super().__init__()
        self.g = g
        self.marked = {}
        for v in self.g.vs():
            self.marked[v] = False
            
        self.pre = queue.queue()
        self.post = queue.queue()
        self.reverse = stack.stack()
        for v in self.g.vs():
            if not self.marked[v]:
                self.dfs_v(self.g, v)
                
    def dfs_v(self, g, v):
        self.marked[v] = True
        self.pre.enqueue(v)
        for adj in self.g.vs():
            if not self.marked[adj]:
                self.dfs_v(g, adj)
                
        self.post.enqueue(v)
        self.reverse.push(v)
        
    def get_pre(self):
        return self.pre
        
    def get_post(self):
        return self.post
        
    def get_reverse(self):
        return self.reverse
        
        
class topolog_dfs(object):
    '''
    @brief  拓步排序
    '''
    def __init__(self, g):
        super().__init__()
        self.g = g
        cycle = digraph_cycle(g)
        if not cycle.is_cycle():
            self.order = dfsorder()
            
    def get_order(self):
        return self.order.get_reverse()
        
    def is_dag(self):
        return hasattr(self, 'order')
        
        
class koasrajuscc(object):
    '''
    @brief  有向图的强连通分量
    '''
    def __init__(self, g):
        super().__init__()
        self.g = g
        self.ids = {}
        self.marked = {}
        for v in self.g.vs():
            self.marked[v] = False
            
        self.count = 0
        order = dfsorder(self.g)
        rever = order.get_reverse()
        while not rever.empty():
            v = rever.pop()
            if self.marked[v] is False:
                self.count += 1
                
    def dfs_v(self, g, v):
        self.marked[v] = True
        self.ids[v] = self.count
        for adj in g.adj(v):
            if not self.marked[v]:
                self.dfs_v(g, adj)
                
    def connect(self, v, w):
        return self.ids[v] == self.ids[w]
        
    def id(self, v):
        return self.ids[v]
        
    def get_count(self):
        return self.count
    
    
class dia_degree(object):
    '''
    @brief  计算有向图的度
    '''
    def __init__(self, g):
        self.marked = {}
        self.indegree = {}
        self.outdegree = {}
        self.stk_flag = {}
        for v in g.vs():
            self.marked[v] = False
            self.indegree[v] = 0
            self.outdegree[v] = 0
            self.stk_flag[v] = False
        self.dfs(g)
        
    def dfs(self, g):
        for v in g.vs():
            if self.mared[v] is False:
                self.dfs_v(g, v)
                
    def dfs_v(self, g, v):
        self.stk_flag[v] = True
        self.marked[v] = True
        adjs = g.adj(v)
        self.outdegree[v] = len(adjs)
        for adj in g.adj(v):
            if not self.marked[adj]:
                self.indegree[adj] += 1
                self.dfs_v(g, adj)
            elif self.stk_flag[adj]:
                self.indegree[adj] += 1
                
        self.stk_flag[v] = False
                
    def sources(self):
        '''
        @brief  所有起点合集，入度为0
        '''
        ret = []
        for v in self.indegree:
            if self.indegree[v] == 0:
                ret.append(v)
                
        return ret
        
    def sinks(self):
        '''
        @brief  所有终点合集，出度为0
        '''
        ret = []
        for v in self.outdegree:
            if self.outdegree[v] == 0:
                ret.append(v)
                
        return ret
        
    def ismap(self):
        '''
        @brief  如果所有顶点的出度均为1
        '''
        for v in self.outdegree:
            if self.outdegree[v] != 1:
                return False
                
        return True
        
        