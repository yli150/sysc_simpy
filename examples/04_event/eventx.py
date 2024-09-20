from syscsim.sc_module import SCModule
from syscsim.sc_event import SCEvent
import simpy 

class ModuleB(SCModule):
    def __init__(self, env, name) -> None:
        super().__init__(env, name)
        self.xevent = SCEvent(env)
        self.env.process(self.tigger())
        self.env.process(self.catcher())

    def tigger(self):
        while True:
            print(f'Trigger @{self.env.now}')
            yield self.xevent.notify(3)

    def catcher(self):
        while True:
            yield self.xevent.wait() 
            print(f'Catch @{self.env.now}')


if __name__ == '__main__':
    '''
    https://github.com/learnwithexamples/learnsystemc/blob/master/basic/08_event/event.cpp
    '''
    env = simpy.Environment()
    m = ModuleB(env, 'b')
    env.run(10)
