class Proxy:
    def __init__(self, obj):
        self._obj = obj
        self.last_invoked = ""
        self.calls = {}

    def last_invoked_method(self):
        return self.last_invoked

    def count_of_calls(self, method_name):
        return self.calls[method_name]

    def was_called(self, method_name):
       if self.calls[method_name] > 0:
        return True
       else:
        return False
    

    def __getattr__(self , attr):
        if attr in dir(self):
            getattr(self,attr)
            self.last_invoked = attr
            if attr in self.calls.keys():
                self.calls[attr] += 1
            else:
                self.calls[attr] += 1
            return getattr(self,attr)
        else:
            if attr in self.calls.keys():
                self.calls[attr] = 0
            else:
                self.calls[attr] = 0
        
        def f():
            getattr(self,attr,"no method invoked")
            raise Exception('No method Is Invoked')

        return f