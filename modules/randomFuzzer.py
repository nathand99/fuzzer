from .fuzzerClass import fuzzerClass

class randomFuzzer(fuzzerClass):

    def __init__(self, binary, stopAtFirst=False):
        super(randomFuzzer,self).__init__(binary, None, lambda x: x, "Random Generated Inputs", stopAtFirst)

    #Fuzzing Techniques
    def spam(self):
        print("===>Trying spam A")
        self.usePayload(b'A'*0x1000)

    def formatString(self):
        print("===>Trying send format string")
        self.usePayload(b'%p%s%x%n'*0x50)

    def empty(self):
        print("===>Trying send empty")
        self.usePayload(b'')
    
    def null(self):
        print('===>Trying send NULL')
        self.usePayload(b'\x00')