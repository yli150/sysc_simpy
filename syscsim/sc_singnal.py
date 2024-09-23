from simpy import Environment
import simpy
from simpy import Resource, Event
from simpy.resources.resource import Request
from typing import Any


class SCSingnal():
    '''
    SCMutex is wrap of a simpy resource   
    '''
    def __init__(self, env: Environment) -> None:
        self.env = env
        self.value = None
        self._e = self.env.event()

    def read(self):
        return self.value

    def write(self, v: Any):
        if self.value == v:
            return
        self.value = v
        # tirgger event and create a new one
        self._e.succeed()
        self._e = self.env.event()

    def event(self):
        return self._e
