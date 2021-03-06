import csv, io
from .fuzzerClass import fuzzerClass

#HELPER: Applies fn to each element in 2D array and returns 2D array
def map2DList(fn, l):
    return list(map(lambda i: list(map(fn, i)), l))

#returns new csv from list as string
def makePayload(l):
    f = io.StringIO(None)
    writer = csv.writer(f, lineterminator='\n')
    for row in l:
        writer.writerow(row)
    return f.getvalue()

class csvFuzzer(fuzzerClass):

    def __init__(self, binary, data, stopAtFirst=False):
        super(csvFuzzer,self).__init__(binary, data, makePayload, "CSV Mutation", stopAtFirst)

    def _usePayload(self, d):
        self.usePayload(d)
        d[0] = self.data[0]
        self.usePayload(d)

    #Fuzzing Techniques
    def allNull(self):
        print("===>Trying all null...")
        d = map2DList(lambda x: None, self.data)
        self._usePayload(d)

    def longValues(self):
        print("===>Trying making all values long...")
        d = map2DList(lambda x: 'A'*1000, self.data)
        self._usePayload(d)

    def extendHorizontally(self):
        print("===>Trying extending header...")
        d = [x[:] for x in self.data]
        for x in d:
            for _ in range(1000):
                x.append('A')
        self.usePayload(d)

    def dropHeader(self):
        print("===>Trying removing header...")
        d = self.data[1:]
        self._usePayload(d)

    def numericFuzzer(self):
        print("===>Trying numeric fuzzing")
        d = map2DList(lambda x: -1, self.data)
        self._usePayload(d)
        d = map2DList(lambda x: 0, self.data)
        self._usePayload(d)
        d = map2DList(lambda x: 999999, self.data)
        self._usePayload(d)