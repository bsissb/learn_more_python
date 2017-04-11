# coding:utf-8
__metaclass__ = type

class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print 'Ahhhh...'
            self.hungry = False
        else:
            print 'No,thanks'


class SongBird(Bird):
    def __init__(self):
        super(SongBird, self).__init__()
        self.sound = True
    def sing(self):
        print self.sound

########################################################################
#接下来创建一个无穷序列
def checkIndex(key):
    """
    所给的键是能够接受的索引吗？
    
    类型不对就弹出TypeError
    是负数就引发IndexError，因为是无穷序列
    """
    if not isinstance(key,(int, long)):raise TypeError
    if key<0: raise IndexError

class ArithmeticSequence:
    """
    初始化算术序列
    
    起始值——序列中的第一个值
    步长——两个相邻值之间的差别
    改变——用户修改的值的字典
    """
    def __init__(self,start=0,step=1):
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        checkIndex(key)

        try: return self.changed[key]
        except KeyError:
            return self.start + key*self.step

    def __setitem__(self, key, value):
        checkIndex(key)
        self.changed[key] = value

###########################################################

#带有访问计数的表
class CounterList(list):
    def __init__(self,*args):
        super(CounterList, self).__init__(*args)
        self.counter = 0

    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)
##########################
#访问器方法 - 属性

class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def setSize(self,size):
        self.width,self.height = size
    def getSize(self):
        return self.width, self.height
    size = property(getSize,setSize)

##############################################
# 装饰器-静态方法和类成员方法
class MyClass:
    @staticmethod
    def smeth():
        print 'THis is a static method'

    @classmethod
    def cmeth(cls):
        print 'This is a class method of', cls