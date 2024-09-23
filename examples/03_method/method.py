from syscsim.sc_module import SCModule
from syscsim.sc_clock import Clock
from simpy import Environment
import simpy


class ModuleC(SCModule):
    def __init__(self, env: Environment, name: str) -> None:
        super().__init__(env, name)
        self.env.process(self.method())

    def method(self):
        print(f'method triggered @ {self.env.now}')


if __name__ == '__main__':
    '''
    https://github.com/learnwithexamples/learnsystemc/blob/master/basic/04_simu_process/simu_process.cpp
    Have not figuered out way to handel this method 
    '''
    env = simpy.Environment()
    m = ModuleC(env, clk=Clock(env, 'clk'), name='b')
    env.run(10)
