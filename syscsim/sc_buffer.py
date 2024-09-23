from simpy import Environment
from typing import Any


class SCBuffer():
    '''
    SCBuffer is similar as SCSingnal
    Only difference is that event is triggred no matter the value changed or not.  
    '''
    def __init__(self, env: Environment) -> None:
        self.env = env
        self.value = None
        self._e = self.env.event()

    def read(self):
        return self.value

    def write(self, v: Any):
        self.value = v
        # tirgger event and create a new one
        self._e.succeed()
        self._e = self.env.event()

    def event(self):
        return self._e
