from abc import ABC, abstractmethod
from simpy import Environment


class SCModule(ABC):
    def __init__(self, env: Environment, name: str) -> None:
        self.env = env
        self.name = name
        self.thread_methods = []
