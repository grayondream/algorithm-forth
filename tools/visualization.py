import imageio
import os
from matplotlib import pyplot as plt
from tools import file_tools

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
    plt.figure()
    color_list = []
    for i in range(len(data)):
        if start == i:
            color_list.append('r')
        elif end == i:
            color_list.append('r')
        else:
            color_list.append('black')

    plt.text(0,max(data),str(data[:10]) + '...')
    plt.text(0,max(data) - 10,"start=%d,end=%d" % (start, end))
    plt.text(0,max(data) - 20,"target=%d" % target)

    plt.bar(range(len(data)), data, color=color_list)

    path = '/home/altas/altas/algorithm/algorithm-forth/img/binary_search'
    file_tools.makesure_path(path)
    plt.savefig(os.path.join(path, str(count) + '.png'))

def main():
    src = '/home/altas/Pictures/imgs'
    target = '/home/altas/Pictures/1.gif'
    generate_gif_dir(src, target)

if __name__ == '__main__':
    main()