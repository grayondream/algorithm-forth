class dfa_kmp(object):
    def __init__(self, pat, txt):
        self.dfa = []
    
    def create_dfa(self, pat):
        pat_len = len(pat)
        r = 256
        self.dfa = [pat_len * [0]] * r
        self.dfa[pat[0]][0] = 1
        i = 0
        j = 1
        while j < pat_len:
            for c in range(r):
                self.dfa[c][j] = self.dfa[c][i]
                
            self.dfa[pat[j]][j] = j + 1
            i = self.dfa[pat[j]][i]
            j += 1
    
    def search(self, txt, pat):
        i = 0
        j = 0
        n = len(txt)
        m = len(pat)
        while i < n and j < m:
            j = self.dfa[txt[i]][j]
            i += 1
        
        if j == m:
            return i - m
        
        return n
        
    