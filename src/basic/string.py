class string(object):
    '''
    @brief 只是为了实现细节展示，使用数组保存字符
    '''
    def __init__(self, str):
        super().__init__()
        self.data = list(str)
        
    def size(self):
        return len(self.data)
        
    def to_char(self):
        ret = ''
        for ch in self.data:
            ret += ch
        
        return ret
    