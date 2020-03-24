class graph:
    ''''
    @brief  图结构的基本抽象
    @param
    @return
    '''

    def __init__(self, vec=None):
        '''
        @brief vec为二元数组，根据二元数组构建图解钩
        @param
        @return
        '''
        super().__init__()

    def v(self):
        '''
        @brief 顶点数
        @param
        @return
        '''

    def vs(self):
        ''''
        @brief 获取所有的顶点
        @param
        @return
        '''

    def e(self):
        ''''
        @brief 边数
        @param
        @return
        '''

    def add_edge(self, v, w):
        '''
        @brief  添加边v,w，如果是有向图则v->w
        @param
        @return
        '''

    def adj(self, v):
        ''''
        @brief  返回顶点v相邻的所有顶点
        @param  
        @return 返回值应该是一个list
        '''

    def __str__(self):
        ret = str(self.v()) + " vertices," + str(self.e()) + " edges\n"
        for v in self.vs():
            cur_adj = self.adj(v)
            if len(cur_adj) == 0:
                ret += str(v) + ' '
            else:
                for w in cur_adj:
                    ret += str(v) + '-->' + str(w) + '  '

            ret += '\n'

        return ret

    def degree(self, v):
        ''''
        @brief　顶点v的出度
        @param
        @return
        '''
        return len(self.adj(v))

    def max_degree(self):
        '''
        @brief 图中顶点最大出度数
        @param
        @return
        '''
        max_d = 0
        for v in self.vs():
            cur_degree = self.degree(v)
            if max_d < cur_degree:
                max_d = cur_degree

        return max_d

    def self_loops(self):
        ''''
        @brief 自环个数
        @param
        @return
        '''
        cnt = 0
        for v in self.vs():
            for w in self.adj(v):
                if w == v:
                    cnt += 1

        return cnt


