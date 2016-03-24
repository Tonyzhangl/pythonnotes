#coding=utf-8
def ReturnTest(a):
    try:
        if a <= 0:
            raise ValueError("data can not be negative")
        else:
            return a
    except ValueError as e:
        print e
    finally:
        print "The end!"
        return -1   #实际开发的过程中并不推荐在finally中使用return语句进行返回！

print ReturnTest(0)
print '>'*20
print ReturnTest(2)
