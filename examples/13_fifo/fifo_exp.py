from syscsim.sc_module import SCModule
from syscsim.sc_event_queue import SCEventQueue
from syscsim.sc_fifo import SCFifo
import simpy


class ModuleB(SCModule):
    def __init__(self, env, name) -> None:
        super().__init__(env, name)
        self.fifo = SCFifo(env, 3)
        self.env.process(self.generator())
        self.env.process(self.consumer1())

    def consumer1(self):
        yield self.env.timeout(10)
        while True:
            req = self.fifo.read()
            yield req 
            print(f'get v  {req.value} @ {self.env.now}')
            yield self.env.timeout(2)

    def generator(self):
        v = 1 
        while True:
            yield self.fifo.write(v)
            print(f'put v  {v} @ {self.env.now}')
            v += 1 
            yield self.env.timeout(1)



if __name__ == '__main__':
    '''
    https://github.com/learnwithexamples/learnsystemc/blob/master/basic/18_channel_fifo/fifo.cpp
    '''
    env = simpy.Environment()
    m = ModuleB(env, 'b')
    env.run(16)
