from threading import Timer

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        company = kwargs.get('company').id
        if company not in cls._instances:
            cls._instances[company] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[company]
        

class RepeatingAsyncTimer(metaclass=Singleton):
    def __init__(self, cb, interval=5, *args, **kwargs):
        self.interval = interval
        self.cb = cb
        self.args = args
        self.kwargs = kwargs
        self.aio_timer = None
        self.start_timer()
    
    def start_timer(self):
        self.aio_timer = Timer(self.interval, 
                               self.cb_wrapper, 
                               args=self.args, 
                               kwargs=self.kwargs
                              )

        self.aio_timer.start()
    
    def cb_wrapper(self, *args, **kwargs):
        self.cb(*args, **kwargs)
        self.start_timer()
