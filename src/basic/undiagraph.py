from src.basic.tgraph import tgraph
from src.basic import graph


class undiagraph(tgraph):
    '''
    @brief  无向图邻接表
    @param
    '''

    def __init__(self, vec=None):
        super(undiagraph, self).__init__(vec=vec)

    def add_edge(self, v, w):
        '''
        @brief  添加边v,w，如果是有向图则v->w
        @param
        @return
        '''
        if v not in self.vs():
            self.data[v] = []

        if w is not None and w not in self.data[v]:  #非孤立节点
            self.data[v].append(w)

        if w is not None and w not in self.vs():
            self.data[w] = []
        
        if w is not None and v is not None and v not in self.data[w]:
            self.data[w].append(v)


'''
@brief 无向图相关算法
'''


def print_g(v):
    print(v, end='\t')


def undiagraph_test():
    vec = [[1, 2], [1, 3], [3, 4], [4, 5], [6]]
    #vec = [[1, 2], [2, 3], [3, 1], [5]]
    g = undiagraph(vec)
    print(g)
    print()
    graph.dfs(g, print_g)
    print()
    graph.bfs(g, print_g)
    print()
    print(graph.path_to(g, 1, 5))
    print(graph.path_to_bfs(g, 1, 5))
    print(graph.connected_part(g))
    print(graph.has_cycle(g))