from simpy import Environment, Store
from typing import Any


class SCFifo():
    '''
    SCFifo is similar as simpy Store  
    1. data_written_event()/data_read_event() is not provided.
    2. nb_write()/nb_read(): non blocking interface is not provided.
    '''
    def __init__(self, env: Environment, n:int) -> None:
        self.env = env
        self._store = Store(env, capacity=n)

    def read(self):
        return self._store.get()

    def write(self, v: Any):
        return self._store.put(v)
