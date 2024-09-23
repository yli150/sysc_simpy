from simpy import Environment
import simpy


class SCClock():
    '''
    Clock is a particular event which runs in one cycle 
    '''
    def __init__(self, env: Environment, name: str) -> None:
        self.env = env
        self.name = name
        self.env.process(self.run())

    def run(self):
        while True:
            self.event = self.env.timeout(1)
            yield self.event

    def wait(self):
        return self.event
