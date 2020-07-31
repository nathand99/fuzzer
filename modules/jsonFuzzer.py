import json
import copy
import numbers
import itertools
from .fuzzerClass import fuzzerClass

# Convert python object into json string
def makePayload(data):
    return json.dumps(data)

class jsonFuzzer(fuzzerClass):

    def __init__(self, binary, data):
        super(jsonFuzzer,self).__init__(binary, data, makePayload)

    #Fuzzing Techniques
    
    # Mess with numeric fields
    def fuzzNumeric(self):
        print("===>Trying numeric fuzzing")
        d = copy.deepcopy(self.data)  
        numericFields = []

        for key in d.keys():
            #print(d[key])
            if isinstance(d[key], numbers.Number):
                numericFields.append(key)


        
        for field in numericFields:

            d[field] = 0x7FFFFFFF
            self.usePayload(d)
            d[field] = 0
            self.usePayload(d)
            d[field] = -1
            self.usePayload(d)
            d[field] = 0xFFFFFFFF
            self.usePayload(d)
        
        #self.usePayload(d)
        # Do every combination of test values on every subset of numeric fields
        # Will take too long if there are too many numeric fields.
        # Fix this later (OSError: [Errno 24] Too many open files)

        testValues = [0, -1, 0x7FFFFFFF, 0xFFFFFFFF]
        n = len(testValues)
        i = 0

        limit = n**len(numericFields)
        if (limit > 100):
            limit = 100

        while i < (limit):
            d = copy.deepcopy(self.data)  

            for i2 in range(0, len(numericFields)):
                d[numericFields[i2]] = testValues[ int(i /(n**i2))  %n]
            self.usePayload(d)
            #print(d)
            i += 1


    # fuzz strings
    def fuzzStrings(self):
        print("===>Trying string fuzzing")
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
            d[field] = "%n" * 100
            self.usePayload(d)
    
    # fuzz floats
    def fuzzFloat(self):
        print("===>Trying float fuzzing")
        d=copy.deepcopy(self.data)  
       
        numericFields = []

        for key in d.keys():
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

        

    
    # fuzz list
    def fuzzList(self):
        print("===>Trying fuzz lists")
        d = copy.deepcopy(self.data)  
        listFields = []

        for key in d.keys():
            if isinstance(d[key], list):
                listFields.append(key)
        #default length is 12 - give 13
        for field in listFields:
            d[field] = d[field].append["A"]
            self.usePayload(d)
            d[field] = []
            self.usePayload(d)
            d[field] = ["a"]
            self.usePayload(d)
            d[field] = [1]
            self.usePayload(d)
            d[field] = [True]
            self.usePayload(d)
            d[field] = ["AAAAAAAAAAAAAAAAAAAAAAA"]
            self.usePayload(d)
            d[field] = ["A"]*100
            self.usePayload(d)
    
    # default input
    def fuzzDefault(self):
        print("===>Trying default input")
        ret = self.data
        self.usePayload(ret)


    # Try send each possible subset of fields
    def fuzzSubsets(self):

        l = self.data.keys()
        for i in range(0, len(l) + 1):  
            for subset in itertools.combinations(l, i):
                d = {}
                for item in subset:
                    d[item] = self.data[item]
                self.usePayload(d)
                #print(d)


    # Add additonal fields?
    # Send format strings?
    #

