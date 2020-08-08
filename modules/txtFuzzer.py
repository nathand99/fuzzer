from .fuzzerClass import fuzzerClass
import re

#Refer to csv fuzzer for idea of whats supposed to happen
def makePayload():
    #TODO
    return

metachars = ["|", ">", "<", "/", "%", "-", "?", "}", "..", "../"]

class txtFuzzer(fuzzerClass):

    def __init__(self, binary, data, stopAtFirst=False):
        super(txtFuzzer,self).__init__(binary, data, makePayload, "Input mutation", stopAtFirst)

    #Fuzzing Techniques
    def dropMeta(self):
        print("===>Trying drop meta char")
        for meta in metachars:
            payload = "".join(self.data.rsplit(meta, 1))
            self.usePayload(payload)
            payload = self.data.replace(meta, "", 1)
            self.usePayload(payload)
            payload = self.data.replace(meta, "", 1)
            self.usePayload(payload)