from simpy import Environment
import simpy 
import functools

class SCEvent():
    '''
    SCEvent is wrap of a simpy event  
    '''
    def __init__(self, env: Environment) -> None:
        self.env = env
        self._e = self.env.event()

    def notify(self, delay:int) -> simpy.Event:
        '''
        Return a timeout event with a callback func to release event 
        '''
        def _callback(*args):
            self._e.succeed()

        t = self.env.timeout(delay)
        t.callbacks.append(_callback)
        return t

    def triggered(self):
        return self._e.triggered()

    def wait(self) -> simpy.Event:
        '''
        Return event with callback to reset event
        '''
        def _callback_reset(*args):
            self._e = self.env.event()

        self._e.callbacks.append(_callback_reset)
        return self._e 
