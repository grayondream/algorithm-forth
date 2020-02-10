from src.basic import queue


class graph_properties(object):
    '''
    @brief  离心率：当前结点离最远节点的最短距离
            直径： 所有顶点的最大离心率
            半径：所有顶点的最小离心率
            中心：离心率和半径相等的顶点
            周长：最短环的长度
    '''
    def __init__(self, g):
        super().__init__()
        self.eccentricities = {}        #离心率
        self.dst_to = {}                #当前顶点到各个顶点的距离,同时用来mark
        self.edge_to = {}
        for v in self.g.vs():
            self.dst_to[v] = -1
            self.edge_to[v] = None
            self.eccentricities[v] = 0
        
        for v in self.g.vs():
            self.bfs_v(self.g, v)
            
        self.diam = self.get_diameter()
        self.radi = self.get_radius()
        self.centers = self.get_centers()
        
    def bfs_v(self, g, v):
        self.dst_to[v] = 0
        q = queue.queue()
        q.enqueue(v)
        eccent = 0
        cyc = 100
        while not q.empty():
            v = q.dequeue()
            for adj in g.adj(v):
                if self.dst_to[adj] is not -1:
                    q.enqueue(adj)
                    self.dst_to[adj] = self.dst_to[v] + 1
                    eccent = self.dst_to[adj]   
                    self.edge_to[adj] = v
                elif v != self.edge_to[adj]:
                    d = self.dst_to[v] + self.dst_to[adj] + 1
                    if d < cyc:
                        cyc = d
                        
        self.eccentricities[v] = eccent
        if self.cyc > cyc:
            self.cyc = cyc
        
    def eccentricity(self, v):
        '''
        @brief  离心率
        '''
        return self.eccentricities[v]       
        
    def get_diameter(self):
        max_ecc = 0
        for ecc in self.eccentricities:
            if max_ecc < self.eccentricities[ecc]:
                max_ecc = self.eccentricities[ecc]
                
        return max_ecc
        
    def diameter(self):
        '''
        @brief  直径
        '''
        return self.diam
        
    def get_radius(self):
        min_ecc = 100
        for ecc in self.eccentricities:
            if min_ecc > self.eccentricities[ecc]:
                min_ecc = self.eccentricities[ecc]
            
        return min_ecc
        
    def radius(self):
        '''
        @brief  半径
        '''
        return self.radi
    
    def get_centers(self):
        ret = []
        for ecc in self.eccentricities:
            if self.eccentricities[ecc] == self.radi:
                ret.append(ecc)
        return ret
        
    def center(self):
        '''
        @brief  中心点
        '''
        return self.centers
        
    def girth(self):
        '''
        @brief  返回周长
        '''
        return self.cyc