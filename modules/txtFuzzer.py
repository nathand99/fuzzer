from .fuzzerClass import fuzzerClass

#Refer to csv fuzzer for idea of whats supposed to happen
def makePayload():
    #TODO
    return

class txtFuzzer(fuzzerClass):

    def __init__(self, binary, data):
        super(txtFuzzer,self).__init__(binary, data, makePayload, "Input mutation")

    #Fuzzing Techniques
