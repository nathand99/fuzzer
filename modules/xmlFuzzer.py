
#Refer to csv fuzzer for idea of whats supposed to happen
def makePayload():
    #TODO
    return

class xmlFuzzer:

    def __init__(self, binary, data):
        super(xmlFuzzer,self).__init__(binary, data, makePayload)

    #Fuzzing Techniques
