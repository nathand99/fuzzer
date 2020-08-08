from .fuzzerClass import fuzzerClass
import random
import re

metachars = ["|", ">", "<", "/", "%", "-", "?", "}", "..", "../", "\""]

class txtFuzzer(fuzzerClass):

    def __init__(self, binary, data, stopAtFirst=False):
        super(txtFuzzer,self).__init__(binary, data, lambda x: x, "Input mutation", stopAtFirst)

    #Fuzzing Techniques
    def dropMeta(self):
        print("===>Trying drop meta char")
        for meta in metachars:
            d = "".join(self.data.rsplit(meta, 1))
            self.usePayload(d)
            d = self.data.replace(meta, "", 1)
            self.usePayload(d)
            # d = self.data.replace(meta, "")
            # self.usePayload(d)

    def bitFlip(self):
        print("===>Trying random bit flips")
        for i in range(len(self.data)):
            if random.random() > 0.95:
                d = bytearray(self.data, 'utf-8')
                d[i] ^= random.randint(1, 255)
                self.usePayload(d)
        
    def repeat(self):
        print("===>Trying repeat input")
        d = self.data
        for _ in range(10):
            d += d
        self.usePayload(d)