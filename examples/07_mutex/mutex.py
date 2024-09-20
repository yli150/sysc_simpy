from syscsim.sc_module import SCModule
from syscsim.sc_event_queue import SCEventQueue
from syscsim.sc_mutex import SCMutex
import simpy 

"""
SC_MODULE(MUTEX) {
  sc_mutex m;
  int value = 0;
  SC_CTOR(MUTEX) {
    SC_THREAD(thread_1);
    SC_THREAD(thread_2);
  }
  void thread_1() {
    while (true) {
      m.lock();
      value += 1;
      wait(1, SC_SEC);
      m.unlock();
    }
  }
  void thread_2() {
    while (true) {
      m.lock();
      value += 1;
      wait(1, SC_SEC);
      m.unlock();
    }
  }
};
"""
class ModuleB(SCModule):
    def __init__(self, env, name) -> None:
        super().__init__(env, name)
        self.mutex = SCMutex(env)
        self.m = 0 
        self.env.process(self.thread1())
        self.env.process(self.thread2())

    def thread2(self):
        while True:
            req = self.mutex.lock()
            yield req 
            print(f'thread2 get lock {self.m}')
            self.m += 1 
            yield self.mutex.unlock(req)
            yield self.env.timeout(1)

    def thread1(self):
        while True:
            req = self.mutex.lock()
            yield req 
            print(f'thread1 get lock {self.m}')
            self.m += 1 
            yield self.mutex.unlock(req)
            yield self.env.timeout(1)

if __name__ == '__main__':
    '''
    https://github.com/learnwithexamples/learnsystemc/blob/master/basic/16_channel_mutex/mutex.cpp
    m increamented by two threads from 0 to 16 
    '''
    env = simpy.Environment()
    m = ModuleB(env, 'b')
    env.run(8)
    print(m.m)

