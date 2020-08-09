from .fuzzerClass import fuzzerClass
import random, re

class binFuzzer(fuzzerClass):

    def __init__(self, binary, data, stopAtFirst=False):
        super(binFuzzer,self).__init__(binary, data, lambda x: x, "Binary input mutation", stopAtFirst)

    def bitFlip(self):
        print("===>Trying random bit flips")
        for i in range(len(self.data)):
            if random.random() > 0.95:
                d = bytearray(self.data)
                d[i] ^= random.randint(1, 255)
                self.usePayload(bytes(d))

    def removeNUll(self):
        print("===>Trying remove all NULL")
        self.usePayload(self.data.replace(b"\x00", b""))
