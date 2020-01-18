import os
from src.basic import stack


'''
1.3.4 括号匹配
'''
def is_left_bracket(ch):
    '''
    @brief  判断字符是不是左括号
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
    b_dict = {'(':')', '[':']', '{':'}'}
    if snd != b_dict[rst]:
        return False
    else:
        return True


#括号匹配[](){}匹配问题
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

'''
1.3.9
表达式中只有右括号而没有左括号，将左括号补全
例如：
1+2)*3-4)*5+6))) ((1+2)*((3-4)*(5+6)))
'''
def complete_left_brackets(line):
    '''
    @brief  补全表达式中的左括号
    @param  line    表达式
    @return 补全后的表达式字符串
    '''
    op_stk = stack.stack()
    value_stak = stack.stack()
    index = 0
    for ch in line:
        if is_right_bracket(ch):
            op_stk.push(ch)
        elif ch.isdigit():
            start = index
            while line[index].isdigit():
                index += 1
            value = int(line[start:index])
            index -= 1
        else:
            raise Exception("unknown character!")

        index += 1


    #上面的代码将所有的括号和字符串全部放入了栈中

'''
1.3.10
中序表达式 == 》 后序表达式
        1+2*3   ==> 1 2 3 * +           (1+2)*3 ==> 1 2 + 3 *
        1*2+3   ==> 1 2 * 3 +           1*(2+3) ==> 1 2 3 + *
'''
def op_is_prior(rst, snd):
    '''
    @brief  判断操作符rst是否比操作符snd的优先级高
    @param  rst 操作符， + - × /
    @param  snd 同rst
    @return     True or False
    '''
    pass


def main():
    pass

if __name__ == '__main__':
    main()
