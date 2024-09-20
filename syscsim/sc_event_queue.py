from simpy import Environment
import simpy 
import functools

class SCEventQueue():
    '''
    SCEventQueue is wrap of a simpy event  
    '''
    def __init__(self, env: Environment) -> None:
        self.env = env
        self._e = self.env.event()

    def notify(self, delay:int) -> simpy.Event:
        # Separate the time delay of events from caller process 
        self.env.process(self._notify(delay))

    def _notify(self, delay:int) -> simpy.Event:
        '''
        Return a timeout event with a callback func to release event 
        '''    
        def _callback(*args):
            self._e.succeed()
            self._e = self.env.event()

        t = self.env.timeout(delay)
        t.callbacks.append(_callback)   
        yield t 

    def triggered(self):
        return self._e.triggered()

    def wait(self) -> simpy.Event:
        '''
        Return event with callback to reset event
        '''
        return self._e 
