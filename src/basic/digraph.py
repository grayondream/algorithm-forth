'''
@brief  无向图
'''
from src.basic import graph, linklist, stack


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
        for v in self.g.vs():       #vs返回所有的顶点
            self.marked[v] = False
            self.edge_to[v] = None
            
    def dfs_v(self, g, v):
        for adj in g.adj(v):        #adj为图g的邻接点
            if not self.marked[adj]:
                self.edge_to[adj] = v
                self.dfs_v(g, adj)
            else:
                 i = v
                 self.stk = stack.stack()
                 while i != adj:
                    stk.push(i)
                    i = self.edge_to[i]
                    
                stk.push(adj)
                stk.push(v)
                
    def is_cycle(self):
        if hasattr(self, 'stk') and not self.stk.empty()
        
    def get_cycle(self):
        return self.stk