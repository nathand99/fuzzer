from .fuzzerClass import fuzzerClass

#Refer to csv fuzzer for idea of whats supposed to happen
def makePayload():
    #TODO
    return

class xmlFuzzer(fuzzerClass):

    def __init__(self, binary, data, stopAtFirst=False):
        super(xmlFuzzer,self).__init__(binary, data, makePayload, "XML Mutation", stopAtFirst)

    #Fuzzing Techniques
