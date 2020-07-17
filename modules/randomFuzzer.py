from .fuzzerClass import fuzzerClass

class randomFuzzer(fuzzerClass):

    def __init__(self, binary, data):
        self.binary = binary
        self.data = data
        self.makePayload = lambda x: x

    #Fuzzing Techniques
    def empty(self):
        print("===>Trying send empty")
        self.usePayload(b'')
    
    def null(self):
        print('===>Trying send NULL')
        self.usePayload(b'\x00')