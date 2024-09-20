from syscsim.sc_module import SCModule
from syscsim.sc_event import SCEvent
import simpy 

class ModuleB(SCModule):
    def __init__(self, env, name) -> None:
        super().__init__(env, name)
        self.e1 = SCEvent(env)
        self.e2 = SCEvent(env)
        self.env.process(self.tigger1())
        self.env.process(self.tigger2())

        self.env.process(self.catcher())
        self.env.process(self.catcher2())
        self.env.process(self.catcher3())
        self.env.process(self.catcher4())

    def tigger1(self):
        while True:
            print(f'Trigger1 @{self.env.now}')
            yield self.e1.notify(3)

    def tigger2(self):
        while True:
            print(f'Trigger2 @{self.env.now}')
            yield self.e2.notify(2)

    def catcher(self):
        while True:
            yield self.e1.wait() 
            print(f'Catch @{self.env.now}')

    def catcher2(self):
        while True:
            yield self.e1.wait() | self.env.timeout(1)
            print(f'Catch2 @{self.env.now}')

    def catcher3(self):
        while True:
            yield self.e1.wait() & self.env.timeout(6)
            print(f'Catch3 @{self.env.now}')

    def catcher4(self):
        while True:
            yield self.e1.wait() & self.e2.wait()
            print(f'Catch4 @{self.env.now}')

if __name__ == '__main__':
    '''
    https://github.com/learnwithexamples/learnsystemc/blob/master/basic/08_event/event.cpp
    '''
    env = simpy.Environment()
    m = ModuleB(env, 'b')
    env.run(10)
