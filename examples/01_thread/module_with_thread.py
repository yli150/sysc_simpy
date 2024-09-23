from syscsim.sc_module import SCModule
import simpy


class ModuleB(SCModule):
    def __init__(self, env, name) -> None:
        super().__init__(env, name)
        self.env.process(self.thread())

    def thread(self):
        while True:
            print(f'Run @{self.env.now}')
            yield self.env.timeout(1)


if __name__ == '__main__':
    env = simpy.Environment()
    m = ModuleB(env, 'b')
    env.run(10)
