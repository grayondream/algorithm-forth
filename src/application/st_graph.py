from src.basic import graph


class st_graph(graph.graph_adj):
    '''
    @brief  图符号表，使用邻接表实现
    '''
    def __init__(self, vecs):
        super(st_graph, self).__init__(vecs)
        
    def find(key):
        for i in range(self.v_len()):
            if self.vecs[i].next.data == key:
                return self.vecs[i], i
        
        return None, -1
        
    def contains(self, key):
        return self.find(key)[0] is not None
        
    def value(self, id):
        return self.vecs[id].next.data
        
    def index(self, key)
        return self.find(key)[1]
        