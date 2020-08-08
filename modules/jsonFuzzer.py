import json
import copy
import numbers
from .fuzzerClass import fuzzerClass

# Convert python object into json string
def makePayload(data):
    return json.dumps(data)

class jsonFuzzer(fuzzerClass):

    def __init__(self, binary, data):
        super(jsonFuzzer,self).__init__(binary, data, makePayload, "JSON Mutation")

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
            d[field] = 999999
            self.usePayload(d)
            d[field] = 0
            self.usePayload(d)
            d[field] = -1
            self.usePayload(d)

        #self.usePayload(d)

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

    # default input
    def fuzzDefault(self):
        print("===>Trying default input")
        ret = self.data
        self.usePayload(ret)

    # fuzz list
    def fuzzList(self):
        print("===>Trying fuzz lists")
        d = copy.deepcopy(self.data)  
        self.usePayload(d)
        listFields = []

        for key in d.keys():
            if isinstance(d[key], list):
                listFields.append(key)
        #default length is 12 - give 13
        for field in listFields:
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
    

