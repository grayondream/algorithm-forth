
class wundiaedge(object):
    ''''
    @brief 加权无向边
    '''
    def __init__(self, v, w, weight):
        super(wundiaedge, self).__init__()
        self.v = v
        self.w = w
        self.weight = weight
        
    def either(self):
        return self.v
    
    def other(self, v):
        return self.w if v == self.v else self.v
        
    def get_w(self):
        return self.weight
    
    def __str__(self):
        line = str(self.v) + '<==' + str(self.weight) + '==>' + str(self.w)
        return line
        
    def __repr__(self):
        return str(self)
        
    def equal_to(self, value):
        return self.v == value.v and self.w == value.w
        
    def __eq__(self, value):
        return self.weight == value.weight
        
    def __lt__(self, value):
        return self.weight < value.weight
        
    def __gt__(self, value):
        return self.weight > value.weight
    
    def __ge__(self, value):
        return self.weight >= value.weight
        
    def reverse(self):
        return wundiaedge(self.w, self.v, self.weight)
        
        
class wundiagraph:
    def __init__(self, vectors):
        super(wundiagraph, self).__init__()
        self.data = {}
        for vec in vectors:
            v, w, weight = vec
            self.add_edge(v, w, weight)
            
    def vs(self):
        return list(self.data.keys())
        
    def v(self):
        return len(self.vs())
        
    def e(self):
        return len(self.es())
        
    def es(self):
        ret = []
        for key in self.data.keys():
            for edge in self.data[key]:
                if edge.reverse() not in ret:
                    ret.append(edge)
        
        return ret
        
    def add_edge(self, v, w, weight):
        if v not in self.vs():
            self.data[v] = []
            
        vw = wundiaedge(v, w, weight)
        if vw not in self.data[v]:
            self.data[v].append(vw)
        else:
            self.data[v][self.data[v].index(vw)] = vw
            
        wv = wundiaedge(w, v, weight)
        if w not in self.vs():
            self.data[w] = []
            
        if wv not in self.data[w]:
            self.data[w].append(wv)
        else:
            self.data[w][self.data[w].index(wv)] = wv
        
    def vs(self):
        return list(self.data.keys())
    
    def adj(self, v):
        ret = []
        for edge in self.data[v]:
            ret.append(edge)
            
        return ret


class min_queue:
    ''''
    @brief 结尾为最小值4,3,2,1
    '''
    def __init__(self):
        self.data = []
        
    def empty(self):
        return len(self.data) == 0
        
    def insert(self, val):
        self.data.append(val)
        i = len(self.data) - 1
        while i > 0 and self.data[i - 1] < self.data[i]:
            self.data[i], self.data[i - 1] = self.data[i - 1], self.data[i]
            i -= 1
        
    def del_min(self):
        ret = self.data[-1]
        del self.data[-1]
        return ret
        
    def find(self, val):
        for i in range(len(self.data)):
            if val == self.data[i]:
                return i
        
        return -1
        
    def replace(self, i, val):
        del self.data[i]
        self.insert(val)
        
        
def lazy_prim(g):
    ''''
    @brief prim 算法的lazy版本
    @param
    @return
    '''
    visited = {}
    for v in g.vs():
        visited[v] = False
        
    min_q = min_queue()
    ret = []
    lazy_prim_visit(g, g.vs()[0], visited, min_q)
    while not min_q.empty():
        e = min_q.del_min()
        v = e.either()
        w = e.other(v)
        if visited[v] and visited[w]:
            continue
        
        ret.append(e)
        if not visited[v]:
            lazy_prim_visit(g, v, visited, min_q)
        
        if not visited[w]:
            lazy_prim_visit(g, w, visited, min_q)
        
    return ret
    
    
def lazy_prim_visit(g, v, visited, min_q):
    visited[v] = True
    for e in g.adj(v):
        if not visited[e.other(v)]:
            min_q.insert(e)
            

class wvector:
    def __init__(self, v, weight):
        self.v = v
        self.weight = weight
        
    def __lt__(self, value):
        return self.weight < value.weight
        
    def __eq__(self, value):
        return self.v == value.v


def prim_mst(g):
    import sys
    dst_to = {}
    visited = {}
    edge_to = {}
    min_q = min_queue()
    for v in g.vs():
        dst_to[v] = sys.maxsize
        visited[v] = False
    
    dst_to[g.vs()[0]] = 0.0
    min_q.insert(wvector(g.vs()[0], 0.0))
    while not min_q.empty():
        cur_v = min_q.del_min()
        prim_mst_visit(g, min_q, cur_v.v, visited, dst_to, edge_to)
        
    return [edge_to[key] for key in edge_to]
    
    
def prim_mst_visit(g, min_q, v, visited, dst_to, edge_to):
    for e in g.adj(v):
        w = e.other(v)
        if visited[w]:
            continue
        
        if e.weight < dst_to[w]:
            dst_to[w] = e.weight
            edge_to[w] = e
            id = min_q.find(wvector(w, 0))
            if id == -1:
                min_q.insert(wvector(w, dst_to[w]))
            else:
                min_q.replace(id, wvector(w, dst_to[w]))
                

def kruskal_mst(g):
    ''''
    @brief kruskal最小生成树
    '''
    min_q = min_queue()
    for e in g.es():
        min_q.insert(e)
        
    ret = []
    visited = {}
    for v in g.vs():
        visited[v] = False
        
    while not min_q.empty():
        e = min_q.del_min()
        v = e.either()
        w = e.other(v)
        if visited[v] and visited[w]:
            continue
            
        ret.append(e)
        visited[v] = True
        visited[w] = True
    
    return ret
    
    
def wundiagraph_test():
    vec = [[1, 2, 3], [1, 3, 4], [2, 4, 6], [3, 5, 5], [4, 1, 10]]
    g = wundiagraph(vec)
    print('顶点数 ', g.v(), ' 顶点　', g.vs())
    print('边数', g.e(), ' 边', g.es())
    print('邻接点', g.adj(1))
    print('lazy prim 最小生成树', lazy_prim(g))
    print('mst prim最小生成树', prim_mst(g))
    print('krusal 最小生成树', kruskal_mst(g))