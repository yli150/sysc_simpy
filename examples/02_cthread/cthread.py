from syscsim.sc_module import SCModule
from syscsim.sc_clock import SCClock
from simpy import Environment
import simpy


class ModuleB(SCModule):
    def __init__(self, env: Environment, clk: SCClock, name: str) -> None:
        super().__init__(env, name)
        self.clk = clk
        self.env.process(self.cthread())

    def cthread(self):
        while True:
            # wait for clock
            yield self.clk.wait()
            print(f'CThread Run @{self.env.now}')


if __name__ == '__main__':
    env = simpy.Environment()
    m = ModuleB(env, clk=SCClock(env, 'clk'), name='b')
    env.run(10)
