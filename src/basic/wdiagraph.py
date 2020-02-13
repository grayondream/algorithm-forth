from src.basic import linklist, heap, digraph

class wedge(self):
    '''
    @brief  边的定义
    '''
    def __init__(self, v, w, weight):
        super().__init__()
        self.start = v
        self.end = w
        self.weight = weight

class wgraph(object):
    '''
    @brief  加权有向图,只实现了部分方法大部分和graph方法类似
    '''
    def __init__(self, vecs):
        super().__init__()
        self.edges = {}     #每个顶点和相连的边的映射
        self.heads = {}     #每个定点和head的映射
        
    def add_e(self, v, w, weight):
        if v in self.edges.keys() and w in self.edges.keys():
            adjs = self.adj(v)
            for adj in adjs:
                if adj.start == v and adj.end == w:#已经存在一条边
                    return
                    
            v_head = self.heads[v]
            ed = wedge(v, w, weight)
            ed_node = linklist.linklist(ed, v_head.next)
            v_head.next = ed_node            
        elif w in self.edges.keys() and v not in self.edges.keys():
            ed = wedge(v, w, weight)
            ed_node = linklist.linklist(ed, None)

            v_head = linklist.linklist(v, ed_node)
            self.heads[v] = v_head
        elif w not in self.edges.keys() and v in self.edges.keys():
            v_head = self.heads[v]
            ed = wedge(v, w, weight)
            ed_node = linklist.linklist(ed, v_head.next)
            v_head.next = ed_node
            
            w_head = linklist.linklist(w, None)            
            self.heads[w] = w_head
                    
        elif w not in self.edges.keys() and v not in self.edges.keys():
            ed = wedge(v, w, weight)
            ed_node = linklist.linklist(ed, None)

            v_head = linklist.linklist(v, ed_node)
            w_head = linklist.linklist(w, None)
            
            self.heads[v] = v_head
            self.heads[w] = w_head
            
        self.edges[v].extend(ed_node)
        
    def adj(self, v):
        return self.edges[v]
        
    def get_edges(self):
        '''
        @brief  返回图的所有的边
        '''
        ret = []
        for key in self.edges:
            ret.extend(self.edges[key])
            
        return ret
        
    
class shortest_path(object):
    '''
    @brief  最短路径api定义
    '''
    def __init__(self, g, s):
        super().__init__()
        self.distto = {}
        self.edage_to = {}
        
    def dist_to(self, v):
        '''
        @brief  点s-->v的距离
        '''
        
    def has_path_to(self, v):
        '''
        @brief  s->v是否有路径
        '''
        
    def path_to(self, v):
        '''
        @brief  s->v的路径
        '''
        
    def e_relax(self, e):
        if self.distto[e.start] + e.weight < self.distto[e.end]:
            self.distto[e.end] = self.distto[e.start] + e.weight
            self.edage_to[e.end] = e
        
    def v_relax(self, g, v):
        for e in g.adj(v):
            if self.distto[v] + e.weight < self.distto[e.end]:
                self.distto[e.end] = self.distto[v] + e.weight
                self.edage_to[e.end] = e
            
            
def equal(rst, snd):
    return rst[0] == snd[0]
    
class dijkstra_sp(shortest_path):
    '''
    @brief  dijkstra最短路径算法
    '''
    def __init__(self, g, s):
        super().__init__(g, s)
        self.edage_to = {}
        self.dist_to = {}
        self.sp_q = heap.max_queue_order()
        
    def sp(self, g, s):
        for v in self.vs():
            self.dist_to[v] = 1000#should be INT_MAX
        
        self.dist_to[s] = 0
        self.sp_q.insert((s, 0))
        while not self.sp_q.empty():
            self.v_relax(g, self.sp_q.delmin())
            
    def v_relax(self, g, v):
        for e in g.adj(v):
            if self.distto[v] + e.weight < self.distto[e.end]:
                self.distto[e.end] = self.distto[v] + e.weight
                self.edage_to[e.end] = e
                if self.sp_q.contain(e.end):
                    self.sp_q.replace((e.end, self.dist_to[e.end]), equal)
                else:
                    self.sp_q.insert((e.end, self.dist_to[e.end]))
    
    
class acycleic_sp(object):
    '''
    @brief  有向无环最短路径
    '''
    def __init__(self, g, s):
        super().__init__()
        self.edage_to = {}
        self.dist_to = {}
        for v in g.vs():
            self.dist_to[v] = 10000 #should be MAX_INT
        
        self.dist_to[s] = 0
        topo = digraph.topolog_dfs(g)
        order = topo.get_order()
        for v in order:
            self.v_relax(g, v)
            
    def v_relax(self, g, v):
        for e in g.adj(v):
            if self.distto[v] + e.weight < self.distto[e.end]:
                self.distto[e.end] = self.distto[v] + e.weight
                self.edage_to[e.end] = e
                if self.sp_q.contain(e.end):
                    self.sp_q.replace((e.end, self.dist_to[e.end]), equal)
                else:
                    self.sp_q.insert((e.end, self.dist_to[e.end]))
                    

class dijkstra_cpm(shortest_path):
    '''
    @brief  dijkstra最长路径算法，关键路径
    '''
    def __init__(self, g, s):
        super().__init__(g, s)
        self.edage_to = {}
        self.dist_to = {}
        self.sp_q = heap.max_queue_order()
        
    def sp(self, g, s):
        for v in self.vs():
            self.dist_to[v] = 1000#should be INT_MAX
        
        self.dist_to[s] = 0
        self.sp_q.insert((s, 0))
        while not self.sp_q.empty():
            self.v_relax(g, self.sp_q.delmin())
            
    def v_tight(self, g, v):
        for e in g.adj(v):
            if self.distto[v] + e.weight > self.distto[e.end]:
                self.distto[e.end] = self.distto[v] + e.weight
                self.edage_to[e.end] = e
                if self.sp_q.contain(e.end):
                    self.sp_q.replace((e.end, self.dist_to[e.end]), equal)
                else:
                    self.sp_q.insert((e.end, self.dist_to[e.end]))
                    
                    
class ford_sp(shortest_path):
    '''
    @brief  dijkstra最短路径算法
    @note:  TODO:很多还没弄明白
    '''
    def __init__(self, g, s):
        super(ford_sp, self).__init__(g, s)
        self.edage_to = {}
        self.dist_to = {}
        self.sp_q = heap.max_queue_order()
        
    def sp(self, g, s):
        for v in self.vs():
            self.dist_to[v] = 1000#should be INT_MAX
        
        self.dist_to[s] = 0
        self.sp_q.insert((s, 0))
        for i in g.vs():
            for v in g.vs():
                for adj in g.adj(v):
                    self.e_relax(adj)
            
    def e_relax(self, e):
        if self.distto[e.start] + e.weight < self.distto[e.end]:
            self.distto[e.end] = self.distto[e.start] + e.weight
            self.edage_to[e.end] = e
            if self.sp_q.contain(e.end):
                self.sp_q.replace((e.end, self.dist_to[e.end]), equal)
            else:
                self.sp_q.insert((e.end, self.dist_to[e.end]))