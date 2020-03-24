from src.basic.graph import graph


class mgraph(graph):
    ''''
    @brief  图结构的邻接矩阵表示，不允许平行边，孤立的节点使用None表示
    @param
    @return
    '''

    def __init__(self, vec=None):
        '''
        @brief vec为二元数组，根据二元数组构建图解钩，实现使用映射实现，每个元素和对应下标的映射，否则添加元素开销会过大
        @param
        @return
        '''
        super(mgraph, self).__init__()

        if vec is None:
            return

        self.ids = {}
        self.keys = {}
        self.data = None
        for vector in vec:
            v, w = None, None
            if len(vector) == 2:
                v, w = vector
            else:
                v = vector[0]

            self.add_edge(v, w)

    def v(self):
        '''
        @brief 顶点数
        @param
        @return
        '''
        return len(self.ids)

    def vs(self):
        ''''
        @brief 获取所有的顶点
        @param
        @return
        '''
        return list(self.ids.keys())

    def e(self):
        ''''
        @brief 边数
        @param
        @return
        '''
        cnt = 0
        for v in self.vs():
            cnt += len(self.adj(v))

        return cnt

    def add_edge(self, v, w):
        '''
        @brief  添加边v,w，如果是有向图则v->w
        @param
        @return
        '''
        if v not in self.vs():
            self.ids[v] = len(self.vs())
            self.keys[self.ids[v]] = v
            if self.data is None:
                self.data = []
                
            self.data.append([0] * self.v())
            
        if w is not None and w not in self.vs():
            self.data.append([0] * self.v())
            self.ids[w] = len(self.vs())
            self.keys[self.ids[w]] = w
            [self.data[i].append(0) for i in range(len(self.data))]
            self.data[self.ids[w]][self.ids[v]] = 1
            self.data[self.ids[v]][self.ids[w]] = 1

    def adj(self, v):
        ''''
        @brief  返回顶点v相邻的所有顶点
        @param  
        @return 返回值应该是一个list
        '''
        if v not in list(self.ids.keys()):
            return None

        line = self.data[self.ids[v]]
        ret = []
        for i in line:
            if i != 0:
                ret.append(self.keys[i])
        
        return ret


def mgraph_test():
    vec = [[1, 2], [2, 1], [1, 3], [3, 1], [2, 4], [4, 2], [5]]
    g = mgraph(vec)
    print("顶点数", g.v())
    print("边数", g.e())
    print("最大出度", g.max_degree())
    print("顶点", g.vs())
    print(g)
