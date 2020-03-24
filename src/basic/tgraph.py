from src.basic.graph import graph


class tgraph(graph):
    ''''
    @brief  图结构的邻接表表示，不允许平行边，孤立的节点使用None表示
    @param
    @return
    '''

    def __init__(self, vec=None):
        '''
        @brief vec为二元数组，根据二元数组构建图解钩
        @param
        @return
        '''
        super(tgraph, self).__init__()
        self.data = {}
        if vec is None:
            return

        for edge in vec:
            if len(edge) == 2:
                v, w = edge
                self.add_edge(v, w)
            else:
                v = edge[0]
                self.add_edge(v, None)

    def v(self):
        '''
        @brief 顶点数
        @param
        @return
        '''
        return len(self.data)

    def vs(self):
        ''''
        @brief 获取所有的顶点
        @param
        @return
        '''
        return list(self.data.keys())

    def e(self):
        ''''
        @brief 边数
        @param
        @return
        '''
        cnt = 0
        for v in self.data:
            cnt += len(self.adj(v))
        
        return cnt
        
    def add_edge(self, v, w):
        '''
        @brief  添加边v,w，如果是有向图则v->w
        @param
        @return
        '''
        if v not in self.vs():
            self.data[v] = []

        if w is not None:  #非孤立节点
            self.data[v].append(w)

    def adj(self, v):
        ''''
        @brief  返回顶点v相邻的所有顶点
        @param  
        @return 返回值应该是一个list
        '''
        if v in self.data.keys():
            return self.data[v]

        return None


def tgraph_test():
    vec = [[1, 2], [2, 1], [1, 3], [3, 1], [2, 4], [4, 2], [5]]
    g = tgraph(vec)
    print(g)
    print("顶点数", g.v())
    print("边数", g.e())
    print("最大出度", g.max_degree())
    print("顶点", g.vs())
    
    