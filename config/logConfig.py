import logging

class LogCustom():

    def __init__(self,level = logging.DEBUG):
        self.lg = logging.getLogger('myLog')
        self.lg.level = level
    def logger(self):
        fmt = logging.Formatter(fmt='%(asctime)s [%(pathname)s:%(lineno)d 行]| %(levelname)s | %(message)s | %(funcName)s',
                                datefmt='%Y/%m/%d/%X')
        myHandler = logging.StreamHandler()
        self.lg.addHandler(myHandler)
        myHandler.setFormatter(fmt)
        # lg.debug('我是你们的女王!')
        return self.lg



if __name__ == '__main__':
    LogCustom(logging.DEBUG).logger().debug('dasdasdasdasda')
 