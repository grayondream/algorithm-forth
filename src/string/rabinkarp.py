class rabinkarp:
    def __init__(self, pat):
        self.m = len(pat)
        self.pat = pat
        self.q = 0#longrandomprime()
        self.rm = 1
        i = 1
        while i <= self.m -1:
            self.rm = (self.r * self.rm) % self.q
            i += 1
        self.pat_hash = self.hash(self.pat, self.m)
        
    def check(self, i):
        return True
        
    def search(self, txt):
        n = len(txt)
        txt_hash = self.hash(txt, self.m)
        if self.pat_hash == self.txt_hash and self.check(0):
            return 0
        
        for i in range(self.m, n):
            txt_hash = (txt_hash + self.q - self.rm * txt[i - self.m] % self.q) % self.q
            txt_hash = (txt_hash * self.r + txt[i]) % self.q
            if self.pat_hash == self.txt_hash:
                if self.check(i -m + i):
                    return i - m + 1
                    
        return n