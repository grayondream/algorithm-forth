from src.basic.queue import queue


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


''''
@brief  图相关算法
'''


def dfs(g, visit_func):
    '''
    @brief 深度优先搜索
    @param　起始顶点为v
    @return
    '''
    visited = {}
    for v in g.vs():
        visited[v] = False

    for v in g.vs():
        if not visited[v]:
            dfs_v(g, v, visited, visit_func)


def dfs_v(g, v, visited, visit_func=None):
    visited[v] = True
    if visit_func is not None:
        visit_func(v)
        
    for w in g.adj(v):
        if not visited[w]:
            dfs_v(g, w, visited, visit_func)


def bfs(g, visit_func=None):
    ''''
    @brief 广度优先搜索
    @param
    @return
    '''
    visited = {}
    for v in g.vs():
        visited[v] = False
    for v in g.vs():
        if not visited[v]:
            q = queue()
            if visit_func is not None:            
                visit_func(v)
                
            visited[v] = True
            q.enqueue(v)
            while not q.empty():
                v = q.dequeue()
                for adj in g.adj(v):
                    if not visited[adj]:
                        visit_func(adj)
                        visited[adj] = True
                        q.enqueue(adj)


def path_to(g, v, w):
    ''''
    @brief 找出v->w的路径
    @param
    @return
    '''
    visited = {}
    edge_to = {}  #存储当前访问节点可达顶点的上一个顶点
    for p in g.vs():
        visited[p] = False
        edge_to[p] = 0

    find_path_to(g, v, visited, edge_to)
    if visited[w]:  #表示有路径
        ret = []
        while w != v:
            ret.append(w)
            w = edge_to[w]

        ret.append(v)
        return ret

    return None


def find_path_to(g, v, visited, edge_to):
    ''''
    @brief 这里的代码是找到v能达到的所有点的路径本不应如此复杂，但是懒得写第二个函数就公用一个了，如果仅仅是找出v->w的路径直接记录edge_to然后当找到节点w就停止
    @param
    @return
    '''
    visited[v] = True
    for adj in g.adj(v):
        if not visited[adj]:
            edge_to[adj] = v
            find_path_to(g, adj, visited, edge_to)


def path_to_bfs(g, v, w):
    ''''
    @brief 使用广度优先搜索算法找出v->的路径
    @param
    @return
    '''
    visited = {}
    edge_to = {}  #存储当前访问节点可达顶点的上一个顶点
    for p in g.vs():
        visited[p] = False
        edge_to[p] = 0

    q = queue()
    visited[v] = True
    q.enqueue(v)
    while not q.empty():
        vector = q.dequeue()
        for adj in g.adj(vector):
            if not visited[adj]:
                q.enqueue(adj)
                visited[adj] = True
                edge_to[adj] = vector

        if vector == w:
            break

    if visited[w]:  #表示有路径
        ret = []
        while w != v:
            ret.append(w)
            w = edge_to[w]

        ret.append(v)
        return ret

    return None


def connected_part(g):
    ''''
    @brief 返回每个点的联通分量编号
    @param
    @return
    '''
    visited = {}
    ids = {}
    for p in g.vs():
        visited[p] = False
        ids[p] = 0

    id = 0
    for v in g.vs():
        if not visited[v]:
            id += 1
            cc_dfs(g, v, visited, ids, count=id)

    return ids


def cc_dfs(g, v, visited, ids, count):
    visited[v] = True
    ids[v] = count
    for adj in g.adj(v):
        if not visited[adj]:
            cc_dfs(g, adj, visited, ids, count)


def has_cycle(g):
    ''''
    @brief 判断图是不是有环
    @param
    @return
    ''' 
    visited = {}
    for v in g.vs():
        visited[v] = False

    for v in g.vs():
        if not visited[v]:
            ret = cycle_dfs(g, visited, v, v)
            if ret:
                return ret
    
    return False


def cycle_dfs(g, visited, v, w):
    ''''
    @brief w->v
    @param
    @return
    '''
    visited[v] = True
    for adj in g.adj(v):
        if not visited[adj]:
            ret = cycle_dfs(g, visited, adj, v) 
            if ret:
                return ret
        elif w != adj:
            return True
    
    return False
