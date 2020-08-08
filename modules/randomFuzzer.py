from .fuzzerClass import fuzzerClass

class randomFuzzer(fuzzerClass):

    def __init__(self, binary, stopAtFirst=False):
        super(randomFuzzer,self).__init__(binary, None, lambda x: x, "Random Generated Inputs", stopAtFirst)

    #Fuzzing Techniques
    def empty(self):
        print("===>Trying send empty")
        self.usePayload(b'')
    
    def null(self):
        print('===>Trying send NULL')
        self.usePayload(b'\x00')