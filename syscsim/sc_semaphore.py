from simpy import Environment
import simpy 
from simpy import Resource, Event
from simpy.resources.resource import Request
import functools

class SCSemaphore():
    '''
    SCSemaphore is wrap of a simpy resource with capacity 
    '''
    def __init__(self, env: Environment, capacity:int) -> None:
        self.env = env
        self._token = simpy.Resource(self.env, capacity=capacity)

    def wait(self) -> Request:
        return self._token.request()

    def post(self, req:Request) -> Event:
        return self._token.release(req)

    def get_value(self):
        return self._token.count 