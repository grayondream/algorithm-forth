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
    op_stk = stack.stack()
    value_stk = stack.stack()
    index = 0
    for ch in line:
        if is_right_bracket(ch):
            op_stk.push(ch)
        elif ch.isdigit():
            start = index
            while line[index].isdigit():
                index += 1
            value = int(line[start:index])
            value_stk.push(value)
            index -= 1
        else:
            raise Exception("unknown character!")

        index += 1

    '''
    TODO:尚未完成
    '''
    
    
def op_is_prior(rst, snd):
    '''
    @brief  1.3.10 判断操作符rst是否比操作符snd的优先级高
    @param  rst 操作符， + - × /
    @param  snd 同rst
    @return     True or False
    '''
    pass


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


def extend_link(link, size):
    '''
    @brief  扩展link节点，如果link为空则默认创建一个的链表
    @param  link链表需要插入的节点
    '''
    is_none = False
    if link is None:
        is_none = True
    
    index = link
    while size != 0:
        node = linklist.linklist(data=0, next=None)
        if index.next is not None:
            node.next = index.next.next
            
        index.next = node
        index = index.next
        size -= 1
    
    if is_none:
        index.next = link
            
    return link
    
    
class circle_queue(object):
    '''
    @brief  1.3.29 环形链表queue实现
    '''
    def __init__(self):
        super(circle_queue, self).__init__()
        self.head = extend_link(None, 4)        #magic number 4,默认链表长度
        self.tail = self.head
        self.len = 0
        
    def enqueue(self, item):
        if self.full():
            extend_link(self.head, self.len * 2)
            
        self.head = self.head.next
        self.head = item
        self.len += 1
    
    def dequeue(self):
        if self.empty():
            return None
        
        value = self.head.data
        self.tail = self.tail.next
        self.len -= 1
        return value
    
    def empty(self):
        return self.tail == self.head and self.len == 0
    
    def size(self):
        return self.len
    
    def full(self):
        return self.head.next == self.tail and self.len != 0


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



if __name__ == '__main__':
    main()
