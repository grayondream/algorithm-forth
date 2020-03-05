

def get_primes(n):
    '''
    @brief  埃拉托斯特尼筛法,生成素数表
    '''
    origin = [1] * n
    origin[0], origin[1] = 0, 0
    for i in range(2, int(pow(n, 0.5)) + 1):
        if origin[i] == 1:
            origin[i * i::i] = [0] * len(origin[i * i::i])
    return [idx for idx, i in enumerate(origin) if i == 1]


def long_random_prime():
    return 121461810980405772771175611270843884000507802617010592057054218483258626678101103820926110565823269240433607391822175172403272239136199088141179467742900111960579379552996372680978058346702525397940161911461633009865733654996981492831594146175519276801093888903332607532190216271689437619073359758499365149323
    
    
def hash(line, big_prime, r=256):
    hcode = 0
    for i in range(0, len(line)):
        hcode = (r * hcode + ord(line[i])) % big_prime
        
    return hcode
    
    
def alwayes_matched(txt, pat):
    return True
    
    
def check_matched(txt, pat):
    return txt == pat
    

def rabinkarp(txt, pat, is_matched_func, r=256):
    big_prime = long_random_prime()
    txt_code = hash(txt[0:len(pat)], big_prime, r)
    pat_code = hash(pat, big_prime, r)
    if txt_code == pat_code and is_matched_func(txt, pat):
        return 0        #pat == txt
    
    rm = 1
    for i in range(1, len(pat)):
        rm = (r * rm) % big_prime
        
    for i in range(len(pat), len(txt)):
        txt_code = (txt_code + big_prime - rm * ord(txt[i - len(pat)]) % big_prime) % big_prime
        txt_code = (txt_code * r + ord(txt[i])) % big_prime
        if pat_code == txt_code and is_matched_func(txt[i - len(pat) + 1:i + 1], pat):
            return i - len(pat) + 1
            
    return len(txt)
            
    
def rabinkarp_m(txt, pat):
    '''
    @brief  蒙特卡洛方法
    '''
    return rabinkarp(txt, pat, alwayes_matched)
    

def rabinkarp_l(txt, pat):
    '''
    @brief  拉斯维加斯算法
    '''
    return rabinkarp(txt, pat, check_matched)
    
    
def rabinkarp_test():
    txt = 'abcabcabdabcabcabc'
    pat = 'abcabcabc'
    ret = rabinkarp_l(txt, pat)
    print(ret)
    print(txt[ret:])