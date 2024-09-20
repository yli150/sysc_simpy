from simpy import Environment
import simpy 
from simpy import Resource, Event
from simpy.resources.resource import Request
import functools

class SCMutex():
    '''
    SCMutex is wrap of a simpy resource   
    '''
    def __init__(self, env: Environment) -> None:
        self.env = env
        self._token = simpy.Resource(self.env, capacity=1)

    def lock(self) -> Request:
        '''
        blocks until mutex could be locked
        return token
        '''
        return self._token.request()

    def unlock(self, req:Request) -> Event:
        return self._token.release(req)