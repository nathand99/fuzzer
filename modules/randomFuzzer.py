from .fuzzerClass import fuzzerClass

class randomFuzzer(fuzzerClass):

    def __init__(self, binary, data):
        super(randomFuzzer,self).__init__(binary, data, lambda x: x)

    #Fuzzing Techniques
    def empty(self):
        print("===>Trying send empty")
        self.usePayload(b'')
    
    def null(self):
        print('===>Trying send NULL')
        self.usePayload(b'\x00')