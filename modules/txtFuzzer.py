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

    def numericFuzzer(self):
        print("===>Numeric fuzzing")
        self.usePayload(re.sub(r"(\d+)", r"-\1", self.data))
        self.usePayload(re.sub(r"\d+", r"0", self.data))
        self.usePayload(re.sub(r"\d+", r"999999999", self.data))

    def bitFlip(self):
        print("===>Trying random bit flips")
        for i in range(len(self.data)):
            if random.random() > 0.95:
                d = bytearray(self.data, 'utf-8')
                d[i] ^= random.randint(1, 255)
                self.usePayload(d)

    def removeNUll(self):
        print("===>Trying remove all NULL")
        d = self.data.encode()
        self.usePayload(d.replace(b"\x00", b""))

    def repeat(self):
        print("===>Trying repeat input")
        d = self.data
        for _ in range(8):
            d += d
        self.usePayload(d[:50000])