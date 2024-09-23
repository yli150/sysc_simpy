from syscsim.sc_module import SCModule
from syscsim.sc_port import SCPort
from syscsim.sc_singnal import SCSingnal
import simpy


class SubModuleB(SCModule):
    def __init__(self, env, name) -> None:
        super().__init__(env, name)
        self.out_port = SCPort(env)
        self.env.process(self.thread1())

    def thread1(self):
        v = 1 
        while True:
            self.out_port.write(v)
            yield self.env.timeout(1)
            v += 1 

class TopModuleB(SCModule):
    def __init__(self, env, name) -> None:
        super().__init__(env, name)
        # connect port from top module to submodule 
        self.out_port = SCPort(env)
        self.submodule_b = SubModuleB(self.env, 'sub_b')
        self.submodule_b.out_port = self.out_port



class SubModuleC(SCModule):
    def __init__(self, env, name) -> None:
        super().__init__(env, name)
        self.in_port = SCPort(env)
        self.env.process(self.thread2())

    def thread2(self):
        while True:
            yield self.in_port.event()
            print(f'catch event value @ {self.env.now} value {self.in_port.read()}')


class TopModuleC(SCModule):
    def __init__(self, env, name) -> None:
        super().__init__(env, name)
        # connect port from top module to submodule 
        self.in_port = SCPort(env)
        self.submodule_c = SubModuleC(self.env, 'sub_c')
        self.submodule_c.in_port = self.in_port



if __name__ == '__main__':
    '''
    https://github.com/learnwithexamples/learnsystemc/blob/master/basic/27_port2port/port2port.cpp
    '''
    env = simpy.Environment()
    m = TopModuleB(env, 'b')
    n = TopModuleC(env, 'b')

    s = SCSingnal(env)
    m.out_port.bind(s)
    n.in_port.bind(s)

    env.run(10)
