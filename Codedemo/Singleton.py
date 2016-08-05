print '-------------- 方法1 ----------'
# 方法1 实现__new__方法
#将一个类的实例绑定到类变量_instance上

class Singletn(object):

    def __new__(cls, *args, **kwargs):
        if not cls.hasattr(cls, '_instance'):
            orgi = super(singleton,cls):
                cls._instance = orgi.__new__(cls, *args, **kwargs)
        return cls._instance



print '-------------- 方法2 ----------'
#方法2 所谓单例就是所有引用(实例和对象)拥有相同的状态和行为
#只需保证类的所有实例拥有相同的状态（属性）即可

class Someobject(object):

    _state = {}

    def __new__(cls, *args, **kwargs):
        ob = super(Someobject, cls).__new__(cls, *args, **kwargs)
        ob.__dict__ = cls._state
        return ob



print '-------------- 方法3 ----------'
#方法3 本质上是方法1的升级（或者是高级）版
#使用__metaclass__元类的高级python用法

class Someobject(object):

    def __init__(cls, name, bases, dict):
        super(Someobject, cls).__init__(name, bases, dict)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Someobject, cls).__call__(*args, **kwargs)
            return cls._instance
