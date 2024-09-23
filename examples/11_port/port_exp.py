from syscsim.sc_module import SCModule
from syscsim.sc_port import SCPort
from syscsim.sc_singnal import SCSingnal
import simpy


class ModuleB(SCModule):
    def __init__(self, env, name) -> None:
        super().__init__(env, name)
        self.out_port = SCPort(env)
        self.env.process(self.thread1())

    def thread1(self):
        v = 1 
        while True:
            self.out_port.write(v)
            yield self.env.timeout(2)
            v += 1 

class ModuleC(SCModule):
    def __init__(self, env, name) -> None:
        super().__init__(env, name)
        self.in_port = SCPort(env)
        self.env.process(self.thread2())

    def thread2(self):
        while True:
            yield self.in_port.event()
            print(f'catch event value @ {self.env.now} value {self.in_port.read()}')


if __name__ == '__main__':
    '''
    https://github.com/learnwithexamples/learnsystemc/blob/master/basic/25_port/port.cpp
    '''
    env = simpy.Environment()
    m = ModuleB(env, 'b')
    n = ModuleC(env, 'b')

    s = SCSingnal(env)
    m.out_port.bind(s)
    n.in_port.bind(s)

    env.run(10)
