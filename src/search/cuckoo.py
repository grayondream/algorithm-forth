import math


def is_prime(no):
    if no <= 0:
        return False
    else:
        i = 2
        while i <= int(math.sqrt(no)):
            if no % i == 0:
                return False
                
    return True


def get_prime(no):
    while not is_prime(no):
        no += 1
        
    return no
    
class cuckoo_hash(object):
    '''
    @brief  布谷鸟散列
    '''
    def __init__(self, size):
        super().__init__()
        self.bucket = size
        self.hash_table1 = [-1] * size
        self.hash_table2 = [-1] * size
        self.limit = 1000      #阈值
        self.cannotinsert = 0
        
    def hash_rst(self, key):
        return key % self.bucket
        
    def hash_snd(self, key):
        return int(key / self.bucket) % self.bucket
    
    def refresh(self, key, limit):
        id_rst = self.hash_rst(key)
        id_snd = self.hash_snd(key)
        if key == self.hash_table1[id_rst]:
            if self.hash_table2[id_snd] == -1:
                self.hash_table2[id_snd] = key
                return True
            elif self.refresh(self.hash_table2[id_snd], limit - 1):
                self.hash_table2[id_snd] = key
                return True
        elif key == self.hash_table2[id_snd]:
            if self.hash_table1[id_rst] == -1:
                self.hash_table1[id_rst] = key
                return True
            elif self.refresh(self.hash_table1[id_rst], limit - 1):
                self.hash_table1[id_rst] = key
                return True
            
        return False
                
                
    def insert(self, key):
        if self.find(key):
            return
            
        id_rst = self.hash_rst(key)
        id_snd = self.hash_snd(key)
        if self.hash_table1[id_rst] == -1:
            self.hash_table1[id_rst] = key
        elif self.hash_table2[id_snd] == -1:
            self.hash_table2[id_snd] = key
        else:
            if self.refresh(self.hash_table1[id_rst], self.limit):
                self.hash_table1[id_rst] = key
            elif self.refresh(self.hash_table2[id_snd], self.limit):
                self.hash_table2[id_snd] = key
            else:
                self.cannotinsert += 1
                
    def find(self, key):
        id = self.hash_rst(key)
        if key == self.hash_table1[id]:
            return True
        elif key == self.hash_table2[self.hash_snd(key)]:
            return True
            
        return False