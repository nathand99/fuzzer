import json
import copy
import itertools
from .fuzzerClass import fuzzerClass

# Convert python object into json string
def makePayload(data):
    return json.dumps(data)

class jsonFuzzer(fuzzerClass):

    def __init__(self, binary, data, stopAtFirst=False):
        super(jsonFuzzer,self).__init__(binary, data, makePayload, "JSON Mutation", stopAtFirst)

    #Fuzzing Techniques

    def emptyObject(self):
        self.useDirectPayload("{}")

    def lotsOfElements(self):
        print("===>Trying extend JSON with padding elements")
        d=copy.copy(self.data)  
        for i in range(0x100):
            d[i] = "A"
        self.usePayload(d)

    def lotsOfNested(self):
        print("===>Trying lots of nested elements")
        d = copy.copy(self.data)
        elem = {'A': ''}
        for _ in range(0x100):
            new = {}
            new['A'] = elem
            elem = new
        d['A'] = elem
        self.usePayload(d)

    def longTag(self):
        print("===>Trying add long JSON tag")
        d = copy.copy(self.data)
        d['A'*0x80] = 'A'*0x80
        self.usePayload(d)

    # # Try send each possible subset of fields
    # def fuzzSubsets(self):
    #     print("===>Trying each subset of JSON fields")
    #     l = self.data.keys()
    #     for i in range(0, len(l) + 1):  
    #         for subset in itertools.combinations(l, i):
    #             d = {}
    #             for item in subset:
    #                 d[item] = self.data[item]
    #             self.usePayload(d)