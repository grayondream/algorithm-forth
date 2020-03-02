class boyemoore:
    def __init__(self, pat):
        self.pat = pat
        m = len(pat)
        r = 256
        self.right = [-1] * r
        for i in range(m):
            self.right[pat[i]] = j
            
    def search(self, txt):
        n = len(txt)
        m = len(self.pat)
        skip = 0
        i = 0
        while i <= n - m:
            skip = 0
            j = m - 1
            while j >= 0:
                if self.pat[j] != txt[i + j]:
                    skip = j - self.right[txt[i + j]]
                    if skip < 1:
                        skip = 1
                    break
                j -= 1
            
            if 0 == skip:
                return i
                
            i += skip
            
        return n