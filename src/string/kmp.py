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
        
    
def get_next(pat):
    i = 0
    j = -1
    next = (len(pat)) * [-1]
    while i < len(next) - 1:
        if j == -1 or pat[i] == pat[j]:
            i += 1
            j += 1
            next[i] = j
        else:
            j = next[j]
            
    return next
    

def kmp(txt, pat):
    next = get_next(pat)
    i = 0
    j = 0
    while i < len(txt) and j < len(pat):
        if j == -1 or txt[i] == pat[j]:
            i += 1
            j += 1
        else:
            j = next[j]
            
    if j == len(pat):
        return i - j
    else:
        return -1
        
        
def kmp_next_test():
    txt = 'abcabcabdabcabcabc'
    pat = 'abcabcabc'
    ret = kmp(txt, pat)
    print(ret)
    print(txt[ret:])
    

def kmp_test():
    kmp_next_test()