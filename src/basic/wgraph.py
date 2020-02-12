'''
@brief  加权有向图
'''
from src.basic import linklist, heap, graph, queue


class edge(self):
    '''
    @brief  边的定义
    '''
    def __init__(self, v, w, weight):
        super().__init__()
        self.start = v
        self.end = w
        self.weight = weight

    def other(self, v):
        if v == self.start:
            return self.end
        elif v == self.end:
            return self.start
            
    
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
            ed = edge(v, w, weight)
            ed_node = linklist.linklist(ed, v_head.next)
            v_head.next = ed_node            
            
            w_head = self.head[w]
            ed = edge(w, v, weight)
            ed_node = linklist.linklist(ed, w_head.next)
            w_head.next = ed_node            
            
        elif w in self.edges.keys() and v not in self.edges.keys():
            ed = edge(v, w, weight)
            ed_node = linklist.linklist(ed, None)

            v_head = linklist.linklist(v, ed_node)
            self.heads[v] = v_head
            
            w_head = self.head[w]
            ed = edge(w, v, weight)
            ed_node = linklist.linklist(ed, w_head.next)
            w_head.next = ed_node     
        elif w not in self.edges.keys() and v in self.edges.keys():
            v_head = self.heads[v]
            ed = edge(v, w, weight)
            ed_node = linklist.linklist(ed, v_head.next)
            v_head.next = ed_node
            
            w_head = linklist.linklist(w, None)            
            self.heads[w] = w_head
            ed = edge(w, v, weight)
            ed_node = linklist.linklist(ed, w_head.next)
            w_head.next = ed_node     
        elif w not in self.edges.keys() and v not in self.edges.keys():
            ed = edge(v, w, weight)
            ed_node = linklist.linklist(ed, None)

            v_head = linklist.linklist(v, ed_node)
            w_head = linklist.linklist(w, None)
            
            self.heads[v] = v_head
            self.heads[w] = w_head
            ed = edge(w, v, weight)
            ed_node = linklist.linklist(ed, w_head.next)
            w_head.next = ed_node     
            
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
        

class mst(object):
    '''
    @brief  最小生成树的接口
    '''
    def __init__(self, g):
        super(mst, self).__init__()
        self.g = g
        
    def edges(self):
        '''
        @brief  最小生成树的边
        '''
        
    def weight(self):
        '''
        @brief  最小生成树的权重
        '''
        
class lazy_prim_mst(object):
    '''
    @brief  prim最小生成树的实现
    '''
    def __init__(self, g):
        super().__init__()
        self.q = heap.max_queue_order()
        self.marked = {}
        for v in g.vs():
            self.marked[v] = False
        
        self.mst_q = queue.queue()
        
    def mst(self, g):
        v = g.vs()[0]
        self.mark(v)
        while not self.q.empty():
            e = self.q.delmin()
            if self.marked[e.start] and self.marked[e.end]:
                continue
            
            self.mst_q.enqueue(e)
            if not self.marked[e.start]:
                self.mark(e.start)
            if not self.marked[e.end]:
                self.mark(e.end)
                
    def mark(self, v):
        self.marked[v] = True
        for adj in self.g.adj(v):
            if not self.marked[adj.end]:
                self.mst_q.insert(adj)
        
    def get_mst(self):
        return self.mst_q
        
        
def bigger(rst, snd):
    return rst[1] > snd[1]
    
def equal(rst, snd):
    return rst[0] == snd[0]
    
class prim_mst(object):
    '''
    @brief  prim算法的改进
    '''
    def __init__(self, g):
        super().__init__()
        self.marked = {}        #标记是否访问过
        self.edge_to = {}       #树和当前节点最小距离的边
        self.dst_to = {}        #树的当前结点之间的最小距离
        self.mst_q = heap.max_queue_order()
        for v in g.vs():
            self.marked[v] = False
            self.dst_to[v] = 1000       #should be INT_MAX
            
        self.mst(g)
        
    def mst(self, g):
        v = self.g.vs()[0]
        self.dst_to[v] = 0
        self.mst_q.insert((v, 0.0), bigger)
        while not self.mst_q.empty():
            self.mark(g, self.mst_q.delmin())
    
    def mark(self, g, v):
        v, w = v
        self.marked[v] = True
        for adj_e in g.adj(v):
            end = adj_e.other(v)
            if self.marked[end]:
                continue
            
            if adj_e.weight < self.dst_to[adj_e]:
                self.edge_to[end] = adj_e
                self.dst_to[end] = adj_e.weight
                
            if self.mst_q.contain(end, equal):
                self.mst_q.replace((end, self.dst_to[end]))
            else:
                self.mst_q.insert((end, self.dst_to[end]))
                
                
class kruskalmst(object):
    '''
    @brief  kruskal最小生成树算法
    '''
    def __init__(self, g):
        super().__init__()
        self.mst_q = queue.queue()
        self.min_q = heap.max_queue_order()
        for edage in g.edags():
            self.min_q.insert(edage)
        
        self.marked = {}
        for v in self.vs():
            self.marked[v] = False
            
    def kruskal(self, g):
        while not self.min_q.empty():
            e = self.min_q.delmin()
            v = e.start
            w = e.end
            if self.marked[v] and self.marked[w]:
                continue
            
            self.marked[v] = True
            self.marked[w] = True
            self.mst_q.enqueue(e)
            
    def mst(self):
        return self.mst_q
        