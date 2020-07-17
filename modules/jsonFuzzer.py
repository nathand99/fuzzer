import json
import copy
import numbers
from .fuzzerClass import fuzzerClass

# Convert python object into json string
def makePayload(data):
    return json.dumps(data)

class jsonFuzzer(fuzzerClass):

    def __init__(self, binary, data):
        self.binary = binary
        self.data = data
        self.makePayload = makePayload

    #Main class function which runs all the different techniques
    def fuzz(self):
        #TODO
        #self.fuzzNumeric()
        #self.fuzzStrings()
        #self.fuzzEveryNumber()
        self.fuzzFloat()
        return #remove after implementation

    #Other Techniques
    
    # Mess with numeric fields
    def fuzzNumeric(self):
        d=copy.deepcopy(self.data)  
       
        numericFields = []

        for key in d.keys():
            #print(d[key])
            if isinstance(d[key], numbers.Number):
                numericFields.append(key)

        for field in numericFields:
            d[field] = 999999
            self.usePayload(d)
            d[field] = 0
            self.usePayload(d)
            d[field] = -1
            self.usePayload(d)

        #self.usePayload(d)

    # fuzz strings
    def fuzzStrings(self):
        d=copy.deepcopy(self.data)  
       
        stringFields = []

        for key in d.keys():
            if isinstance(d[key], str):
                stringFields.append(key)

        for field in stringFields:
            d[field] = ""
            self.usePayload(d)
            d[field] = "A"*1000
            self.usePayload(d)
            d[field] = "10000000"
            self.usePayload(d)
            d[field] = True
            self.usePayload(d)
            d[field] = False
            self.usePayload(d)
            d[field] = None
            self.usePayload(d)
    
    # fuzz lots of numbers - looks like its too slow
    def fuzzEveryNumber(self):
        d=copy.deepcopy(self.data)  
       
        numericFields = []

        for key in d.keys():
            if isinstance(d[key], numbers.Number):
                numericFields.append(key)
        for num in range(2^63 - 1):
            #2^63 - 1
            for field in numericFields:
                d[field] = num
            self.usePayload(d)

    # fuzz floats
    def fuzzFloat(self):
        d=copy.deepcopy(self.data)  
       
        numericFields = []

        for key in d.keys():
            #print(d[key])
            if isinstance(d[key], numbers.Number):
                numericFields.append(key)

        for field in numericFields:
            d[field] = 0.0
            self.usePayload(d)
            d[field] = 0.1
            self.usePayload(d)
            d[field] = -1.1
            self.usePayload(d)
            d[field] = 0.000000009
            self.usePayload(d)
            d[field] = 0.000000001
            self.usePayload(d)
