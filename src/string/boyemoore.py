
def get_right(pat, r=256):
    right = [-1] * r
    for i in range(len(pat)):
        right[ord(pat[i])] = i
        
    return right
    

def boyemoore_search(txt, pat):
    right = get_right(pat)
    skip = 0
    i = 0
    while i <= len(txt) - len(pat):
        skip = 0
        j = len(pat) - 1
        while j >= 0:
            if pat[j] != txt[i + j]:
                skip = j - right[ord(txt[i + j])]
                if skip < 1:
                    skip = 1
                break
            
            j -= 1
            
        if skip == 0:
            return i
        
        i += skip
            
    return len(txt)
        
        
def boyemoore_test():
    txt = 'abcabcabdabcabcabc'
    pat = 'abcabcabc'
    ret = boyemoore_search(txt, pat)
    print(ret)
    print(txt[ret:])
    