from src.basic.wundiagraph import min_queue, wvector
from src.basic.queue import queue
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
    
    def to(self):
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
    def __init__(self, vectors=None):
        super(wdiagraph, self).__init__()
        self.data = {}
        if vectors is None:
            return
            
        for vec in vectors:
            v, w, weight = vec
            self.add_edge(v, w, weight)
            
        self.pre = []
        self.post = []
        self.reve = []
        self.tranversal()
        
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
            if not visited[adj.to()]:
                self.dfs_v(adj.to(), visited)

        self.post.append(v)
        self.reve.append(v)
    
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
        for e in self.adj(v):
            w = e.to()
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
        
        if w not in self.vs():
            self.data[w] = []
            
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
    
    
def dijkstra_releax(g, v, edge_to, dist_to, min_q=None):
    for e in g.adj(v):
        w = e.to()
        if e.weight + dist_to[v] < dist_to[w]:
            dist_to[w] = e.weight + dist_to[v]
            edge_to[w] = e
            if min_q is not None:
                id = min_q.find(wvector(w, 0))
                if id != -1:
                    min_q.replace(id, wvector(w, dist_to[w]))
                else:
                    min_q.insert(wvector(w, dist_to[w]))
                

def dijkstra_nocycle_sp(g, v):
    edge_to = {}
    dist_to = {}
    for p in g.vs():
        dist_to[p] = sys.maxsize
    
    dist_to[v] = 0
    order = g.topol_traversal()
    for w in order:
        dijkstra_releax(g, w, edge_to, dist_to)
        
    return edge_to
    
    
def findnegative_cycle(edge_to, dist_to):
    ''''
    @brief 必须配合relax使用，当每个顶点都经过relax后还存在环，则一定是有负权边的环
    '''
    g = wdiagraph(None)
    for w in edge_to.keys():
        e = edge_to[w]
        g.add_edge(e.v, e.w, e.weight)
        
    cycle = g.get_cycle()
    return cycle
    
    
def ford_relax(g, v, dist_to, edge_to, q, onq, cost):
    for e in g.adj(v):
        w = e.to()
        if dist_to[w] > dist_to[v] + e.weight:
            dist_to[w] = dist_to[v] + e.weight
            edge_to[w] = e
            if not onq[w]:
                q.enqueue(w)
                onq[w] = True
        if cost % g.v() == 0:
            findnegative_cycle(edge_to, dist_to)
            
        cost += 1
        
        
def ford_sp(g, v):
    edge_to = {}
    dist_to = {}
    onq = {}
    q = queue()
    for w in g.vs():
        dist_to[w] = sys.maxsize
        onq[w] = False
        
    dist_to[v] = 0.0
    q.enqueue(v)
    onq[v] = True
    cost = 0
    while not q.empty() and not findnegative_cycle(edge_to, dist_to):
        v = q.dequeue()
        ford_relax(g, v, dist_to, edge_to, q, onq, cost)

    return edge_to
    
    
def wdiagraph_test():
    vec = [[1, 2, 3], [1, 3, 4], [2, 4, 6], [3, 5, 5], [4, 1, 10]]
    g = wdiagraph(vec)
    print('顶点数 ', g.v(), ' 顶点　', g.vs())
    print('边数', g.e(), ' 边', g.es())
    print('邻接点', g.adj(1))
    print('dijstra最短路径', dijkstra_sp(g, 1))
    print('无环图dijstra最短路径', dijkstra_nocycle_sp(g, 1))
    print('无环图ford最短路径', ford_sp(g, 1))