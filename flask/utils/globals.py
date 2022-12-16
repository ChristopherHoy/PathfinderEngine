
class Globals:    
    def new(self, **kwargs):
        for name, value in kwargs.items():
            self.__setattr__(name, value)


globals = Globals()