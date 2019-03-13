import threading as t

class Task:
    def __init__(self,fnTarget,*args,**kwargs):
        self._fnTarget=fnTarget
        self._args=args
        self._kwargs=kwargs
        self._thread=t.Thread(target=self._run)
        self._result=None #this will finally hold the result
        self._thread.start()
        

    def _run(self):
        self._result=self._fnTarget(*self._args,**self._kwargs)

    @property
    def thread(self):
        return self._thread

    @property
    def result(self):
        if self._thread.isAlive():
            self._thread.join()
        return self._result

    @property
    def isAlive(self):
        return self._thread.isAlive()

    def wait(self):
        self._thread.join()
        return self._result



def asynchronous(fnTarget):
    def inner(*args,**kwargs): #parameters for fnTarget
        t=Task(fnTarget,*args,**kwargs)
        return t

    return inner

    


