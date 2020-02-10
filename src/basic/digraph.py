'''
@brief  无向图
'''
from src.basic import graph, linklist


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