import os
#表达式解析,计算表达式的值

import src.basic.stack

def add(rst, snd):
    return rst + snd

def dim(rst, snd):
    return rst - snd

def mult(rst, snd):
    return rst * snd

def div(rst, snd):
    return rst / snd

def calc_value(op, rst, snd):
    '''
    @brief  根据操作符计算结果
    @param  op  操作符
    @param  rst 第一个值
    @param  snd 第二个值
    '''
    calc_dict = {'+':add, '-':dim, '*':mult, '/':div}
    return calc_dict[op](rst, snd)

#假定任意两个子表达式都通过()进行界定，比如
#(1+2)
#(2*3)*(3*3)
#(1+(3*3))
#不支持正负号解析
#只支持整数解析
def smi_expression_calc(express):
    '''
    @brief  解析有限定的表达式求值，每个子表达式之间通过()进行区分界定
    @param  express 表达式字符串
    @return
    '''
    op_stk = src.basic.stack.stack()
    num_stk = src.basic.stack.stack()

    index = 0
    while len(express) != index:
        ch = express[index]
        if ch == '(':
            continue
        elif ch == ')' and not op_stk.empty() and not num_stk.empty():      #接触到一个子表达式
            op = op_stk.pop()
            rst = num_stk.pop()
            snd = num_stk.pop()
            value = calc_value(op, rst, snd)

            num_stk.push(value)
        elif ch in ['+', '-', '*', '/']:
            op_stk.push(ch)
        elif ch.isdigit():
            start = index
            while express[index].isdigit():
                index += 1

            num = int(express[start : index])
            num_stk.push(num)
            index -= 1
        else:
            raise Exception("bag character!")

        index += 1

    return num_stk.pop()


def main():
    pass

if __name__ == '__main__':
    main()
