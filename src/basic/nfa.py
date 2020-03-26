''''
@brief 非确定性自动机
'''
from src.basic.diagraph import diagraph
from src.basic.stack import stack


def prase_nfa(reg):
    '''
    @brief 使用nfa解析正则表达式
    @param ref  模式串
    @return
    '''
    stk = stack()
    g = diagraph()
    for i in range(len(reg)):
        lp = i
        if reg[i] == '(' or reg[i] == '|':
            stk.push(i)
        elif reg[i] == ')':
            or_id = stk.top()
            stk.pop()
            if(reg[i] == '|'):
                lp = stk.top()
                g.add_edge(lp, or_id + 1)
                g.add_edge(or_id, i)
            else:
                lp = or_id
        
        if i < len(reg) - 1 and reg[i + 1] == '*':
            g.add_edge(lp, i + 1)
            g.add_edge(i + 1, lp)
        
        if reg[i] == '(' or reg[i] == '*' or reg[i] == ')':
            g.add_edge(i, i + 1)
    
    return g
    

def nfa_recognizes(str, g):
    ''''
    @brief 模式识别
    '''
    pass
    
    
def nfa_test():
    g = prase_nfa('*')
    print(g)

