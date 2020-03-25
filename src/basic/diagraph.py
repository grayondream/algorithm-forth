from src.basic.tgraph import tgraph
from src.basic import graph, stack


class diagraph(tgraph):
    '''
    @brief  无向图邻接表
    @param
    '''

    def __init__(self, vec=None):
        super(diagraph, self).__init__(vec=vec)
        self.pre = []
        self.post = []
        self.reve = []
        
    def tranversal(self):
        visited = {}
        for v in self.vs():
            visited[v] = False

        for v in self.vs():
            if not visited[v]:
                self.dfs_v(v, visited)

        self.reve.reverse()

    def dfs_v(self, v, visited):
        visited[v] = True
        self.pre.append(v)
        for adj in self.adj(v):
            if not visited[adj]:
                self.dfs_v(adj, visited)

        self.post.append(v)
        self.reve.append(v)

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

    def reverse(self):
        ''''
        @brief 当前图的反向图
        @param
        @return
        '''
        g = diagraph()
        for v in self.vs():
            adjs = self.adj(v)
            if len(adjs) == 0:
                g.add_edge(v, None)
            else:
                for w in adjs:
                    g.add_edge(w, v)

        return g

    def diagraph_arrived(self, v):
        '''
        @brief 从顶点v到其他顶点的可达性
        @param
        @return
        '''
        visited = {}
        for p in self.vs():
            visited[p] = False

        graph.dfs_v(self, v, visited)
        return visited

    def get_cycle(self):
        '''
        @brief 获取图中的环
        @param
        @return
        '''
        stk = {}  #维护一个stak更加高效
        visited = {}
        edge_to = {}
        for v in self.vs():
            stk[v] = False
            visited[v] = False

        for v in self.vs():
            if not visited[v]:
                cycle = self.cycle_dfs(v, stk, visited, edge_to)
                if cycle is not None:
                    return cycle

        return None

    def cycle_dfs(self, v, stk, visited, edge_to):
        stk[v] = True
        visited[v] = True
        cycle = None
        for w in self.adj(v):
            if not visited[w]:
                edge_to[w] = v
                cycle = self.cycle_dfs(w, stk, visited, edge_to)
            elif stk[w]:
                cycle = []
                id = v
                while id != w:
                    cycle.append(id)
                    id = edge_to[id]

                cycle.append(w)
                cycle.append(v)

        stk[v] = False
        return cycle

    def pre_traversal(self):
        return self.pre

    def post_traversal(self):
        return self.post

    def reverse_traversal(self):
        return self.reve

    def topol_traversal(self):
        ''''
        @brief　拓扑排序
        @param
        @return
        '''
        cycle = self.get_cycle()
        if cycle is not None:  #有环
            return None

        return self.reverse_traversal()

    def isdag(self):
        ''''
        @brief 是不是有向无环图
        @param
        @return
        '''
        return self.get_cycle() == None

    def get_kosaraju_scc(self):
        ''''
        @brief 获得图的连通图的id表格
        @param
        @return
        '''
        ids = {}
        visited = {}
        for v in self.vs():
            visited[v] = False
            ids[v] = 0

        count = 0
        g = self.reverse()
        g.tranversal()
        order = g.reverse_traversal()
        for v in order:
            if not visited[v]:
                self.kosaraju_scc_dfs(v, visited, ids, count)
                count += 1
        
        return ids

    def kosaraju_scc_dfs(self, v, visited, ids, count):
        visited[v] = True
        ids[v] = count
        for adj in self.adj(v):
            if not visited[adj]:
                self.kosaraju_scc_dfs(adj, visited, count)

    def scc_connected(self, v, w):
        '''
        @brief v 和w是不是联通的
        @param
        @return
        '''
        scc = self.get_kosaraju_scc()
        return scc[v] == scc[w]

    def get_scc_count(self):
        ''''
        @brief 获得连通图的数量
        @param
        @return
        '''
        return len(self.get_kosaraju_scc())


def print_g(v):
    print(v, end='\t')


def diagraph_test():
    vec = [[1, 2], [1, 3], [3, 4], [4, 5], [6]]
    #vec = [[1, 2], [2, 3], [3, 1], [5]]
    g = diagraph(vec)
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
    print("reverse:")
    print(g.reverse())
    print('可达性:', g.diagraph_arrived(1))
    print('环', g.get_cycle())
    print("pre", g.pre_traversal())
    print('post', g.post_traversal())
    print('reverse', g.reverse_traversal())
    print("拓扑排序:", g.topol_traversal())
    print("联通性:", g.get_kosaraju_scc())
    