

class graph_bridge(object):
    def __init__(self, g):
        super().__init__()
        self.marked = {}
        for v in self.g.vs():
            self.marked[v] = False
            
        self.edages = self.get_edages(g)
        
    def get_edages(self, g):
        self.edages = {}
        for v in g.vs():
            if not self.marked[v]:
                self.dfs_v(g, v)
        
        return self.edages
        
    def dfs_v(self, g, v):
        for adj in g.adj(v):
            if not self.marked[v]:
                self.marked[v] = True
                self.dfs_v(g, adj)
                self.edages[(v, adj)]  = False           
    
    def dfs_ve(self, g, v):
        for adj in g.adj(v):
            if not self.marked[v] and (v, adj) in self.edages.keys() and self.edages[(v, adj)] is False:
                self.marked[v] = True
                self.dfs_v(g, adj)
    
    def bridge(self, g):
        for key in self.edages:
            for key in self.marked:
                self.marked[key] = False
                
            self.edages[key] = True
            self.dfs_ve(g, key[0])
            for key in self.marked:
                if not self.marked[key]:
                    return True
        
        return False
            
            