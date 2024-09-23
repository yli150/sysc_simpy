from syscsim.sc_module import SCModule
from syscsim.sc_event import SCEvent
import simpy


class ModuleB(SCModule):
    def __init__(self, env, name) -> None:
        super().__init__(env, name)
        self.xevent = SCEvent(env)
        self.env.process(self.tigger())
        self.env.process(self.catcher())
        self.env.process(self.catcher2())

    def tigger(self):
        while True:
            print(f'Trigger @{self.env.now}')
            self.xevent.notify(3)
            yield self.env.timeout(5)

    def catcher(self):
        while True:
            yield self.xevent.wait()
            print(f'Catch @{self.env.now}')

    def catcher2(self):
        while True:
            yield self.xevent.wait()
            print(f'Catch2 @{self.env.now}')


if __name__ == '__main__':
    '''
    https://github.com/learnwithexamples/learnsystemc/blob/master/basic/08_event/event.cpp
    '''
    env = simpy.Environment()
    m = ModuleB(env, 'b')
    env.run(10)
