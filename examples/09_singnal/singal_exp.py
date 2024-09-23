from syscsim.sc_module import SCModule
from syscsim.sc_singnal import SCSingnal
import simpy


class ModuleB(SCModule):
    def __init__(self, env, name) -> None:
        super().__init__(env, name)
        self.singnal = SCSingnal(env)
        self.env.process(self.thread1())
        self.env.process(self.thread2())

    def thread1(self):
        self.singnal.write(2)
        while True:
            v = self.singnal.read()
            print(f'Set value to {self.env.now}')
            self.singnal.write(self.env.now)
            yield self.env.timeout(4)

    def thread2(self):
        while True:
            yield self.singnal.event()
            print(f'catch event value @ {self.env.now} value {self.singnal.read()}')


class ModuleC(SCModule):
    def __init__(self, env, name) -> None:
        super().__init__(env, name)
        self.singnal = SCSingnal(env)
        self.env.process(self.thread1())
        self.env.process(self.thread2())

    def thread1(self):
        '''
        No event triggered, since data does not change 
        '''
        self.singnal.write(2)
        while True:
            v = self.singnal.read()
            self.singnal.write(2)
            yield self.env.timeout(4)

    def thread2(self):
        while True:
            yield self.singnal.event()
            print(f'catch event value @ {self.env.now} value {self.singnal.read()}')


if __name__ == '__main__':
    '''
    https://github.com/learnwithexamples/learnsystemc/blob/master/basic/20_signal_event/signal_event.cpp
    '''
    env = simpy.Environment()
    m = ModuleB(env, 'b')
    env.run(10)

    env = simpy.Environment()
    n = ModuleC(env, 'b')
    env.run(10)
