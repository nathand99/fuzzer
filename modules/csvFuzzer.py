import csv, io
from .fuzzerClass import fuzzerClass

#HELPER: Applies fn to each element in 2D array and returns 2D array
def map2DList(fn, l):
    return list(map(lambda i: list(map(fn, i)), l))

#returns new csv from list as string
def makePayload(l):
    f = io.StringIO(None)
    writer = csv.writer(f)
    for row in l:
        writer.writerow(row)
    return f.getvalue()

class csvFuzzer(fuzzerClass):

    def __init__(self, binary, data):
        self.binary = binary
        self.data = data
        self.makePayload = makePayload

    #Main class function which runs all the different techniques
    def fuzz(self):
        self.allNull() #Just running one technique for now 

    #Fuzzing Techniques
    def allNull(self):
        d = map2DList(lambda x: None, self.data)
        self.usePayload(d)
        