import json
import copy
import numbers
from .fuzzerClass import fuzzerClass

# Convert python object into json string
def makePayload(data):
    return json.dumps(data)

class jsonFuzzer(fuzzerClass):

    def __init__(self, binary, data, stopAtFirst=False):
        super(jsonFuzzer,self).__init__(binary, data, makePayload, "JSON Mutation", stopAtFirst)

    #Fuzzing Techniques

    def emptyObject(self):
        self.usePayload('\{\}')

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
    

