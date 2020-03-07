import ctypes
import platform
'''
Windows相关颜色和数据输出流定义
'''
std_dict = {'stdin': -10, 'stdout': -11, 'stderr': -12}
windows_fore_colors = {
    'black': 0x0,
    'blue': 0x01,
    'green': 0x02,
    'red': 0x04,
    'inten': 0x04,
    'reset': 0x07
}
windows_back_colors = {'blue': 0x10, 'green': 0x20, 'red': 0x40, 'inten': 0x80}

linux_fore_colors = {
    'black': 30,
    'red': 31,
    'green': 32,
    'yellow': 33,
    'blue': 34,
    'white': 37
}

linux_back_colors = {
    'black': 40,
    'red': 41,
    'green': 42,
    'yellow': 43,
    'blue': 44,
    'white': 47
}


def printw(line, fore_color, back_color):
    plat = platform.system().lower()
    stream = None
    if plat == 'windows':
        stream = windows_stream('stdout')
    elif plat == 'linux':
        stream = linux_stream()

    stream.out(line, fore_color, back_color)


class linux_stream(object):
    def __init__(self):
        super(linux_stream, self).__init__()

    def out(self, line, fore_color, back_color):
        if back_color is None:
            back_color = 'black'
            
        line = '\033[0;%d;%dm%s\033[0m' % (linux_fore_colors[fore_color],
                                           linux_back_colors[back_color], line)
        print(line)


class windows_stream(object):
    '''
    @brief  windows输出流管理
    @example    
        red self.set_color(FOREGrOUND_RED | FOREGROUND_INTENSITY)
        蓝底红字   FOREGROUND_RED | FOREGROUND_INTENSITY| BACKGROUND_BLUE | BACKGROUND_INTENSITY
    '''

    def __init__(self, stream):
        super(windows_stream, self).__init__()
        self.handle = ctypes.windll.kernel32.GetStdHandle(std_dict[stream])

    def set_color(self, handle, fore_color, back_color=None):
        '''
        @brief  设置颜色
        @param  handle  io流
        @param  fore_color  前景色
        @param  back_color  背景色
        '''
        color = windows_fore_colors[fore_color] | windows_fore_colors['inten']
        if back_color is not None:
            color = color | windows_back_colors[
                back_color] | windows_back_colors['inten']
        bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
        return bool

    def reset(self):
        self.set_color(self.handle, 'reset')

    def out(self, line, fore_color, back_color=None):
        '''
        @brief  输出相关字符
        @param  line    输出的信息
        @param  fore_color  前景颜色
        @param  back_color  背景颜色
        '''
        self.set_color(self.handle, fore_color, back_color)
        print(line)
        self.reset()


if __name__ == "__main__":
    line = 'test'
    for key in windows_fore_colors.keys():
        printw(line, key, None)
