import os

def makesure_path(path):
    if not os.path.exists(path):
        os.mkdir(path)
        
    
def get_func_name(func):
    return str(func)[10:-23]