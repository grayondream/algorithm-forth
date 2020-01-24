import imageio
import os
from matplotlib import pyplot as plt
from tools import file_tools
import cv2
import numpy as np


def generate_gif(file_list:list, target_file, fps=1):
    '''
    @brief  根据图片的路径生成gif图片
    @param  file_list   图片的路径列表
    @param  target_file 目标图片路径
    @param  fps         顾名思义
    '''
    img_list = [imageio.imread(file) for file in file_list]
    imageio.mimsave(target_file, img_list, fps=fps)

def generate_gif_dir(path:str, target_file, fps=1):
    '''
    @brief  根据图片的路径将路径中的图片制作成gif，顺序会根据图片名称的字典排序进行排序
    @param  path    原图片路径
    @param  target_file 生成图片文件名
    @param  fps     顾名思义
    '''
    files = os.listdir(path)
    files.sort()
    file_list = [os.path.join(path, file) for file in files]
    generate_gif(file_list, target_file, fps=fps)


def rgb2bgr(rgb):
    '''
    @brief  将rgb颜色转换成bgr
    @return bgr
    '''
    return (rgb[2], rgb[1], rgb[0])
    
    
def search_visualization_hook(data, start, mid, end, target, count):
    '''
    @brief  可视化相关hook函数，暂时未想到完全和API脱离的实现
    @param  data    数据域
    @param  start   开始节点
    @param  mid     中间节点
    @param  end     结束节点
    @param  target  目标值
    @param  count   用来统计当前算法调用了多少次
    '''
    h, w, v_border, w_border = 600, 800, 100, 5   #长宽边界,opencv左上角为0，0
    gap_ratio = (2,1)   #设置gap的比例,数据的条目宽度和之间的间隔只比
    
    ratio = (h - v_border) / max(data)
    item_w = ((w - w_border)/len(data))
    item_width = int(item_w * gap_ratio[0]/sum(gap_ratio))
    item_gap = int(item_w * gap_ratio[1]/sum(gap_ratio))

    #border修正
    w_border = int( (w - (item_width + item_gap) * len(data)) / 2)
    
    img = np.zeros((h, w, 3), dtype=np.uint8)
    img = img + 255
    
    for i in range(len(data)):
        color = rgb2bgr((240,121,81))
        liner = -1
        cur_h = int(data[i] * ratio)
        minxy = (w_border + i * (item_width + item_gap), h - cur_h)
        maxxy = (w_border + i * (item_gap + item_width) + item_width, h)
        if mid == i:
            liner = -1
            color = rgb2bgr((97,134,163))
        elif start == i:
            liner = -1
            color = rgb2bgr((168,61,103))
        elif end == i:
            liner = -1
            color = rgb2bgr((168,61,103))
        else:
            color = rgb2bgr((240,121,81))
            liner = -1
        
        cv2.rectangle(img, minxy, maxxy, color, liner)
        
    path = './img/binary_search'
    file_tools.makesure_path(path)
    cv2.imwrite(os.path.join(path, str(count) + '.png'), img)


def sort_visualization_hook(data, indexi, indexj, count, desc, img_ratio=20):
    '''
    @brief  可视化相关hook函数，暂时未想到完全和API脱离的实现，由于如果按照遍历的方式生成图片，图片生成太多，现在设置img_ratio进行图片筛选
    @param  data    数据域
    @param  indexi
    @param  indexj
    @param  count   用来进行图片的记名
    @param  desc    描述信息
    '''
    if count % img_ratio != 0:
        return
        
    h, w, v_border, w_border = 600, 800, 100, 5   #长宽边界,opencv左上角为0，0
    gap_ratio = (2,1)   #设置gap的比例,数据的条目宽度和之间的间隔只比
    
    ratio = (h - v_border) / max(data)
    item_w = ((w - w_border)/len(data))
    item_width = int(item_w * gap_ratio[0]/sum(gap_ratio))
    item_gap = int(item_w * gap_ratio[1]/sum(gap_ratio))

    #border修正
    w_border = int( (w - (item_width + item_gap) * len(data)) / 2)
    
    img = np.zeros((h, w, 3), dtype=np.uint8)
    img = img + 255
    
    for i in range(len(data)):
        color = rgb2bgr((240,121,81))
        liner = -1
        cur_h = int(data[i] * ratio)
        minxy = (w_border + i * (item_width + item_gap), h - cur_h)
        maxxy = (w_border + i * (item_gap + item_width) + item_width, h)
        if indexi == i:
            liner = -1
            color = rgb2bgr((97,134,163))
        elif indexj == i:
            liner = -1
            color = rgb2bgr((97,134,163))
        else:
            color = rgb2bgr((240,121,81))
            liner = -1
        
        cv2.rectangle(img, minxy, maxxy, color, liner)
        
    path = './img/' + desc
    file_tools.makesure_path(path)
    cv2.imwrite(os.path.join(path, str(count) + '.png'), img)


def bubble_sort_visualization(data, i, j, count):
    sort_visualization_hook(data, i, j, count, 'bubble_sort')
    

def selection_sort_visualization(data, i, j, count):
    sort_visualization_hook(data, i, j, count, 'selection_sort')
    
    
def insert_sort_visualization(data, i, j, count):
    sort_visualization_hook(data, i, j, count, 'insert_sort')
    
    
def shell_sort_visualization(data, i, j, count):
    sort_visualization_hook(data, i, j, count, 'shell_sort', img_ratio=1)
    
    
def main():
    src = '/home/altas/Pictures/imgs'
    target = '/home/altas/Pictures/1.gif'
    generate_gif_dir(src, target)

if __name__ == '__main__':
    main()