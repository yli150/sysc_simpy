from syscsim.sc_module import SCModule
from syscsim.sc_event_queue import SCEventQueue
from syscsim.sc_semaphore import SCSemaphore
import simpy


class ModuleB(SCModule):
    def __init__(self, env, name) -> None:
        super().__init__(env, name)
        self.semaphore = SCSemaphore(env, 3)
        self.env.process(self.thread1())
        self.env.process(self.thread2())
        self.env.process(self.thread3())

    def thread2(self):
        while True:
            req = self.semaphore.wait()
            yield req
            print(f'2 get lock {self.env.now} {self.semaphore.get_value()}')
            yield self.env.timeout(1)
            yield self.semaphore.post(req)

    def thread1(self):
        while True:
            req = self.semaphore.wait()
            yield req
            print(f'1 get lock {self.env.now} {self.semaphore.get_value()}')
            yield self.env.timeout(1)
            yield self.semaphore.post(req)

    def thread3(self):
        while True:
            req = self.semaphore.wait()
            yield req
            print(f'3 get lock {self.env.now} {self.semaphore.get_value()}')
            yield self.env.timeout(1)
            yield self.semaphore.post(req)


if __name__ == '__main__':
    '''
    https://github.com/learnwithexamples/learnsystemc/blob/master/basic/17_channel_semaphore/semaphore.cpp
    '''
    env = simpy.Environment()
    m = ModuleB(env, 'b')
    env.run(6)
