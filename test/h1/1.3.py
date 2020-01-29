from src.basic import stack, linklist


def is_left_bracket(ch):
    '''
    @brief  1.3.4 括号匹配，判断字符是不是左括号
    @param  ch  字符
    @return ture or false
    '''
    return ch == '(' or ch == '[' or ch == '{'


def is_right_bracket(ch):
    '''
    @brief  判断字符是不是右括号
    @param  ch  字符
    @return ture or false
    '''
    return ch == ')' or ch == ']' or ch == '}'


def match_bracket(rst, snd):
    '''
    @brief  匹配括号
    @param  rst  左括号
    @param  snd  右括号
    @return     ture or false
    '''
    b_dict = {'(': ')', '[': ']', '{': '}'}
    if snd != b_dict[rst]:
        return False
    else:
        return True


def bracket_match(line):
    '''
    @brief  括号匹配，支持(),[],{}，对于不是相关字符接略过
    @param  line    括号字符串
    '''
    stk = stack.stack()
    for ch in line:
        if is_left_bracket(ch):
            stk.push(ch)
        elif is_right_bracket(ch):
            if not match_bracket(ch, stk.pop()):
                return False
        else:
            continue


def complete_left_brackets(line):
    '''
    @brief  1.3.9 补全表达式中的左括号,表达式中只有右括号而没有左括号，将左括号补全
    @param  line    表达式
    @return 补全后的表达式字符串
    '''
    val_stk = stack.stack()
    op_stk = stack.stack()
    for ch in line:    
        if ch.isdigit():
            val_stk.push(ch)
        elif ch in '+-*/':
            op_stk.push(ch)
        elif ch == ')':
            cur_value = '(' + op_stk.pop() + val_stk.pop() + ch
            val_stk.push(cur_value)
        else:
            raise Exception('bad character')
            
    return val_stk.pop()
    
    
def get_prior(rst):
    '''
    @brief  获取操作符的优先级
    @param  rst 操作符， + - × /
    @return     
    '''
    ret = 0
    if rst in '+-':
        ret = 1
    elif rst in '*/':
        ret = 2
    else:
        ret = 0
    
    return ret


def in2post(line):
    '''
    @brief  1.3.10  中序表达式转换为后序表达式，不含括号的表达式转换
    @param  line    中序表达式
    '''
    op_stk = stack.stack()
    ret_line = ''
    for ch in line:
        if ch.isdigit():
            ret_line += ch
        elif ch == '(':
            op_stk.push(ch)
        elif ch == ')':
            tmp = op_stk.pop()
            ret_line += tmp
            while tmp != ')':
                tmp = op_stk.pop()
        else:
            while get_prior(op_stk.top()) > get_prior(ch):
                ret_line += op_stk.pop()
                
            op_stk.push(ch)
    
    while not op_stk.empty():
        ret_line += op_stk.pop()
    
    return op_stk
            
        else:
            raise Exception('bad characters!')

def link_delete_tail(link):
    '''
    @brief  1.3.19 删除单链表的尾节点
    @param  link    链表对象
    '''
    if link is None or link.next is None:
        return None
    else:
        index = link
        while index.next is not None:
            index = index.next

        del index.next
        index.next = None

    return link


def link_delete_kth(link, k):
    '''
    @brief  1.3.20 删除链表的第k个元素
    @param  link    链表对象
    @param  需要删除的元素的index，取值从0开始
    '''
    if None is link:
        return None
    else:
        index = link
        count = 0
        while count < k and index.next is not None:
            count += 1
            index = index.next

        if index.next is None:  
            return link
        else:
            tmp = link.next
            link.next = tmp.next
            del tmp
    return link


def link_find_value(link, value):
    '''
    @brief  1.3.21  判断value是否在链表link中
    @param  link    链表
    @param  value   item的value值
    @return Ture or False
    '''
    if None is link:
        return False
    else:
        index = link
        while index is not None:
            if value == index.data:
                return True
            index = index.next

    return False


def link_remove_after(link):
    '''
    @brief  1.3.24  删除节点link之后的所有节点
    @param  link    目标节点
    '''
    if None is link:
        return None
    else:
        index = link.next
        link.next = None
        while None is not index:
            tmp = index
            index = index.next
            del tmp

    return link


def link_insert_after(link, item):
    '''
    @brief  1.3.25  向link节点之后插入节点item
    @param  link    插入的位置节点
    @param  item    需要插入的节点
    '''
    if None is link or None is item:
        return None
    else:
        item.next = link.next
        link.next = item

    return link


def link_remove(link, value):
    '''
    @brief  1.3.26  删除链表link中所有值为value的item
    @param  link    需要进行操作的链表
    @param  value   目标值
    '''
    head = linklist.linklist(next=link, data=0) 
    index = head
    while index.next is not None:
        if index.next.data == value:
            tmp = index.next
            index.next = index.next.next    
            del tmp
            

    link = head.next
    del head
    return link


def link_max(link):
    '''
    @brief  1.3.27  返回链表中最大的value,假设链表上的值全是正整数
    @param  link    目标链表
    '''
    index = link
    max_item = 0
    while index is not None:
        if index.data > max_item:
            max_item = index.data

        index = index.next

    return max_item


def link_max_recur(link):
    '''
    @brief  1.3.28  使用递归姐姐1.3.27问题返回链表中最大的value
    @param  link    目标链表
    '''
    if link is None:
        return 0

    max_item = max(link.data, link_max_recur(link.next))
    return max_item


def main():
    pass


'''
1.3.29  见cyc_queue的实现
'''


def reverse_link(head):
    '''
    @brief  1.3.30 反转链表
    @param  head    链表的头结点
    @return     翻转之后的头结点
    '''    
    if head is None:
        return head
    elif head.next is None:
        tmp = head.next
        head.next = None
        tmp.next = head
        return tmp
    else:
        last = head
        cur = last.next
        next = cur.next
        
        last.next = None
        while next is not None:
            cur.next = last
            last = cur
            cur = next
            next = next.next

        cur.next = last
        return cur
    
    
'''
1.3.31  见doublelink的实现
'''


'''
1.3.32  见stkqueue实现
'''


'''
1.3.33 见doublequeue实现
'''


'''
1.3.34  见randombag实现
'''


'''
1.3.25  见randomqueue实现
'''


def josephus(n, m):
    '''
    @brief  1.3.37 josephus问题，排队送死
    @param  n   人数
    @param  m   数数的次数
    @note   更加符合实际情况的实现应该是使用标志位进行标记这个人已经死了，这里懒得写就这样用python写的快
    '''
    l = [i for i in range(n)] #0 , 1, 2, , 3, ...
    cur = 0
    res = []
    while True:
        cur += m
        cur = cur % n
        res.append(cur)
        del l[cur]
        
    return res
        
    
class generalize_queue(object):
    '''
    @brief  1.3.38  删除第K个元素
    '''
    def __init__(self):
        super(generalize_queue, self).__init__()
        
        self.data = []
    
    def empty(self):
        return 0 == len(self.data)
        
    def size(self):
        return len(self.data)
        
    def insert(self, data):
        '''
        @brief  插入一个元素
        @param  data    插入的元素
        '''
        self.data.append(data)
        
    def delete(self, k):
        '''
        @brief  删除第k个元素
        @param  k
        '''
        if k > self.size():
            return None
            
        res = self.data[self.size() - k - 1]
        del self.data[self.size() - k - 1]
        return res
        
       
def move_front(line):
    '''
    @brief  1.3.40 前移编码，创建一个链表，遍历line，每次遇到表中存在的元素将新元素插入到表头，删除表中存在的节点
    '''
    head = linklist.linklist()
    for ch in line:
        node = linklist.linklist.find(head, ch)
        if node == None:
            node = linklist.linklist(head, ch)
            head = node
        elif head == node and head.data == ch:
            continue
        else:
            tmp = node.next
            node.next = node.next.next
            tmp.next = head
            head = tmp
            
    return head
    

'''
1.3.41    参见queue的clone实现
'''


'''
1.3.43  参见stk的clone实现
'''
            
    
class read_buffer(object):
    '''
    @brief  1.3.44  文件读写buffer
    @param  data    数据区
    @param  cur     贯标位置
    '''
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.data = list(f.readlines())
        self.cur = 0
    
    def delete(self):
        '''
        @brief  删除并返回光标处的字符
        '''
        res = self.data[self.cur]
        del self.data[self.cur]
        return res
        
    def insert(self, ch):
        '''
        @brief  在光标处插入字符，插入后的字符的索引为self.cur
        @param  ch  插入的字符
        '''
        self.data.insert(self.cur, ch)
        
    def left(self, k):
        '''
        @brief  光标向左移动k个位置
        @param  k   光标移动的尺度
        '''
        self.cur = max(self.cur - k, 0)
        
    def right(self, k):
        '''
        @brief  光标向右移动k个位置
        @param  k   移动的位置尺度
        '''
        self.cur = min(self.size() - 1, self.cur + k)
        
    def size(self):
        return len(self.data)
        

def is_stk_overflow(line):
    '''
    @brief  1.3.45 给定一系列的操作判定操作是否导致栈溢出，其中push为数字，pop为-
    @param  line    操作定义字符串
    '''
    cur = 0
    for ch in line:
        if ch.isdigit():
            cur += 1
        elif ch == '-':
            cur -= 1
            if cur < 0:
                return False        #overflow
                
    return True
    
    
def is_stkop_legal(push_line, pop_line):
    '''
    @brief  1.3.46 给定push的序列，判断pop序列是否合法
    @param  push_line   push序列
    @param  pop_line    pop序列
    @return True or False
    @example:   
    1 2 3 -- > 3 2 1 True
               2 3 1 False 
    @note:  算法实现的基本思路是，之前pop的元素在pushline中的位置一定比当前元素的位置靠前 1 2 3  2 1 3 ，也就是说之前元素的index小于当前元素的index
    '''
    indexs = [push_line.index(ch) for ch in pop_line]
    for i in range(len(indexs)):
        for j in [i - x - 1 for x in range(i)]:
            if i == 0:
                continue
            else:
                if indexs[i] > indexs[j]:
                    break
                else:
                    if indexs[i] < indexs[j]:
                        return False
    
    return True
        
    
    
'''
1.3.47 见queue和stack的catenation操作
'''


class queue_with_stack(object):
    '''
    @brief  1.3.49  双栈实现队列
    '''
    def __init__(self):
        self.rst = stack.stack()
        self.snd = stack.stack()
        
    def enqueue(self, data):
        '''
        @brief  入队
        @param  data    入队的数据
        '''
        self.rst.push(data)
        
    def dequeue(self):
        '''
        @brief  出队
        '''
        if self.snd.empty():
            while not self.rst.empty():
                self.snd.push(self.rst.pop())
                
        return self.snd.pop()
        
        
if __name__ == '__main__':
    main()
