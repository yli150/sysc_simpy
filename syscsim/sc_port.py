from simpy import Environment
from .sc_singnal import SCSingnal

class SCPort():
    '''
    SCPort can bind SCSingal or other SC object  
    '''
    def __init__(self, env: Environment) -> None:
        self.env = env
        self._singnal = None 
     
    def bind(self, singnal:SCSingnal):
        self._singnal = singnal 

    # proxy to command class
    def __getattr__(self, name):
        if self._singnal is None:
            raise RuntimeError(f'{self} need to bound to sc singnal first')

        # redirect to singal interface 
        if hasattr(self._singnal, name):
            return getattr(self._singnal, name)