from syscsim.sc_module import SCModule
from syscsim.sc_event_queue import SCEventQueue
import simpy 

class ModuleB(SCModule):
    def __init__(self, env, name) -> None:
        super().__init__(env, name)
        self.eq = SCEventQueue(env)
        self.env.process(self.tigger())
        self.env.process(self.catcher())

    def tigger(self):
        while True:
            print(f'Trigger @{self.env.now}')
            self.eq.notify(2)
            self.eq.notify(1)
            yield self.env.timeout(10)

    def catcher(self):
        while True:
            yield self.eq.wait() 
            print(f'Catch @{self.env.now}')

if __name__ == '__main__':
    '''
    https://www.learnsystemc.com/basic/event_queue
    https://github.com/learnwithexamples/learnsystemc/blob/master/basic/14_event_queue/event_queue.cpp

    Expected Results 
    Trigger @0
    Catch @1
    Catch @2
    Trigger @10
    Catch @11
    Catch @12
    '''
    env = simpy.Environment()
    m = ModuleB(env, 'b')
    env.run(20)

