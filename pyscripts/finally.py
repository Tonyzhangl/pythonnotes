def Finally():
    print 'i am starting....'
    while True:
        try:
            print 'i am running'
            raise IndexError("r")
        except NameError,e: #except 中没有捕获到对应的异常，则将异常临时保存起来了
            print 'NameError happened %d' % e
            break
        finally: #若在此产生新的异常或者使用了break或者return 上次临时保存的异常将被丢弃，从而到时异常屏蔽了
            print 'finally executed'
            break

Finally()
