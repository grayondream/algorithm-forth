from src.basic.wundiagraph import min_queue, wvector
import sys


class wdiaedge(object):
    ''''
    @brief 加权无向边
    '''
    def __init__(self, v, w, weight):
        super(wdiaedge, self).__init__()
        self.v = v
        self.w = w
        self.weight = weight
        
    def come_from(self):
        return self.v
    
    def to(self, v):
        return self.w
        
    def get_w(self):
        return self.weight
    
    def __str__(self):
        line = str(self.v) + '==' + str(self.weight) + '==>' + str(self.w)
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
        return wdiaedge(self.w, self.v, self.weight)
        
        
class wdiagraph:
    def __init__(self, vectors):
        super(wdiagraph, self).__init__()
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
            
        vw = wdiaedge(v, w, weight)
        if vw not in self.data[v]:
            self.data[v].append(vw)
        else:
            self.data[v][self.data[v].index(vw)] = vw
            
    def vs(self):
        return list(self.data.keys())
    
    def adj(self, v):
        ret = []
        for edge in self.data[v]:
            ret.append(edge)
            
        return ret
        
    
def dijkstra_sp(g, v):
    '''
    @brief  dijkstra最短路径算法
    '''
    edge_to = {}
    dist_to = {}
    min_q = min_queue()
    for p in g.vs():
        dist_to[p] = sys.maxsize
    
    min_q.insert(wvector(v, 0.0))
    dist_to[v] = 0
    while not min_q.empty():
        cur = min_q.del_min()
        dijkstra_releax(g, cur.v, edge_to, dist_to, min_q)
        
    return edge_to
    
def dijkstra_releax(g, v, edge_to, dist_to, min_q):
    for e in g.adj(v):
        w = e.other(v)
        if e.weight + dist_to[v] < dist_to[w]:
            dist_to[w] = e.weight + dist_to[v]
            edge_to[w] = e
            id = min_q.find(wvector(w, 0))
            if id != -1:
                min_q.replace(id, wvector(w, dist_to[w]))
            else:
                min_q.insert(wvector(w, dist_to[w]))
                

def wdiagraph_test():
    vec = [[1, 2, 3], [1, 3, 4], [2, 4, 6], [3, 5, 5], [4, 1, 10]]
    g = wdiagraph(vec)
    print('顶点数 ', g.v(), ' 顶点　', g.vs())
    print('边数', g.e(), ' 边', g.es())
    print('邻接点', g.adj(1))
    print('dijstra最短路径', dijkstra_sp(g, 1))