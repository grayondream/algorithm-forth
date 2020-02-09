from src.basic import linklist


'''
稀疏矩阵的实现
'''
class matrix_ele(object):
    def __init__(self, key, value):
        super().__init__()
        self.key = key
        self.value = value
        
        
class sprase_matrix(object):
    def __init__(self, array):
        super().__init__()
        self.rows = [linklist.linklist(None, None)] * len(array)
        self.col = len(array[0])
        self.row = len(self.rows)
        
    def build(self, array):
        for i in range(len(array)):
            head = self.rows[i]
            for j in range(len(array[0])):
                if array[i][j] != 0:
                    node = linklist.linklist(matrix_ele(j, array[i][j]), head.next)
                    head.next = node
                    
    def find(self, key):
        for i in range(len(self.rows)):
            index = self.rows(i)
            while index.next is not None:
                if index.next.data.value == value:
                    return (i, index.next.data.key)
                
                index = index.next
                
        return None
        
    def get(self, i, j):
        if i < self.row and i >= 0 and j < self.col and j >= 0:
            head = self.rows[i]
            while head.next is not None:
                if head.next.data.key == i:
                    return head.next.data.value
                head = head.next
            
            return 0