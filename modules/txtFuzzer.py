from .fuzzerClass import fuzzerClass
import random
import re

metachars = ["|", ">", "<", "/", "%", ",", "}", ".."]

class txtFuzzer(fuzzerClass):

    def __init__(self, binary, data, stopAtFirst=False):
        super(txtFuzzer,self).__init__(binary, data, lambda x: x, "Input mutation", stopAtFirst)

    #Fuzzing Techniques
    def dropMeta(self):
        print("===>Trying drop meta char")
        for meta in metachars:
            # d = "".join(self.data.rsplit(meta, 1))
            # if self.usePayload(d):
            #     return
            d = self.data.replace(meta, "", 1)
            self.usePayload(d)
            # d = self.data.replace(meta, "")
            # self.usePayload(d)

    def makeEmpty(self):
        print("===>Tring remove text")
        self.usePayload(re.sub(r"(\w+)|(\d+)", "", self.data))

    def addFormatString(self):
        print("===>Trying insert format string")
        if self.usePayload(re.sub(r"\".*?\"", "\"%s%p%x%n\"", self.data)):
            return
        if self.usePayload(re.sub(r"\<.*?\>", "<%s%p%x%n>", self.data)):
            return
        self.usePayload(re.sub(r"(\w+)|(\d+)", "%s%p%x%n", self.data))

    def numericFuzzer(self):
        print("===>Numeric fuzzing")
        self.usePayload(re.sub(r"(\d+)", r"-\1", self.data))
        self.usePayload(re.sub(r"\d+", "0", self.data))
        self.usePayload(re.sub(r"\d+", "-1", self.data))
        self.usePayload(re.sub(r"\d+", "2147483647", self.data)) # max 32 bit signed int
        self.usePayload(re.sub(r"\d+", "-2147483648", self.data)) # min 32 bit singed int
        self.usePayload(re.sub(r"\d+", "4294967295", self.data)) # max 32 bit unsigned int
        self.usePayload(re.sub(r"\d+", "9223372036854775807", self.data)) # max 64 bit signed int
        self.usePayload(re.sub(r"\d+", "-9223372036854775808", self.data)) # min 64 bit signed int
        self.usePayload(re.sub(r"\d+", "18446744073709551615", self.data)) # max 64 bit unsigned int

        for _ in range(5):
            r = random.randint(0, 99999999)
            if self.usePayload(re.sub(r"\d+", "-{}".format(r), self.data)):
                return
            if self.usePayload(re.sub(r"\d+", "{}".format(r), self.data)):
                return

    def extendLines(self):
        print("===>Trying extend lines")
        self.usePayload(re.sub(r"\n", "A" * 0x100 + "\n", self.data))

    def repeat(self):
        print("===>Trying repeat input")
        d = self.data
        for _ in range(8):
            d += d
        self.usePayload(d[:100000])