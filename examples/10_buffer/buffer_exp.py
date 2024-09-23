from syscsim.sc_module import SCModule
from syscsim.sc_buffer import SCBuffer
import simpy


class ModuleC(SCModule):
    def __init__(self, env, name) -> None:
        super().__init__(env, name)
        self.buf = SCBuffer(env)
        self.env.process(self.thread1())
        self.env.process(self.thread2())

    def thread1(self):
        '''
        No event triggered, since data does not change 
        '''
        self.buf.write(2)
        while True:
            self.buf.write(2)
            yield self.env.timeout(4)

    def thread2(self):
        while True:
            yield self.buf.event()
            print(f'catch event value @ {self.env.now} value {self.buf.read()}')


if __name__ == '__main__':
    '''
    https://github.com/learnwithexamples/learnsystemc/blob/master/basic/24_buffer/buffer.cpp
    '''

    env = simpy.Environment()
    n = ModuleC(env, 'b')
    env.run(10)
