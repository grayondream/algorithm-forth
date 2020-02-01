import os

def makesure_path(path):
    if not os.path.exists(path):
        os.mkdir(path)
        
    
def get_func_name(func):
    return str(func)[10:-23]
    
    
def get_file_ext(filename):
    return filename.split('.')[-1]
    
    
def get_all_files(path, ext):
    '''
    @brief  获取path下所有后缀名为ext的文件名称的列表
    @param  path    制定的目录
    @param  ext     文件后缀
    '''
    files = os.listdir(path)
    ret = []
    for file in files:
        filename = os.path.join(path, file)
        if os.path.isfile(filename):
            if get_file_ext(filename) == ext:
                ret.append(filename)
        elif os.path.isdir(filename):
            ret.extend(get_all_files(filename, ext))
        
    return ret