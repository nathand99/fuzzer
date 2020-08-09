from .fuzzerClass import fuzzerClass
from xml.etree import ElementTree as ET
import re
import copy

#Refer to csv fuzzer for idea of whats supposed to happen
def makePayload(d):
    return ET.tostring(d)

class xmlFuzzer(fuzzerClass):

    def __init__(self, binary, data, stopAtFirst=False):
        super(xmlFuzzer,self).__init__(binary, data, makePayload, "XML Mutation", stopAtFirst)
        self.textData = makePayload(data)

    #Fuzzing Techniques
    def lotsOfElements(self):
        print("===>Trying extend XML with padding elements")
        d = copy.deepcopy(self.data)
        padding = ET.Element('a')
        padding.text = "A"
        for _ in range(0x900):
            d.append(padding)
        self.usePayload(d)

    def lotsOfNested(self):
        print("===>Trying lots of nested elements")
        d = copy.deepcopy(self.data)
        elem = ET.Element('div')
        for _ in range(0x300):
            new = ET.Element('a')
            new.text = "A"
            new.append(elem)
            elem = new
        d.append(elem)
        self.usePayload(d)


    def greaterMeta(self):
        self.useDirectPayload(re.sub(b">", b">" * 0x900, self.textData))

    def longTag(self):
        print("===>Trying add long xml tag")
        d = copy.deepcopy(self.data)
        padding = ET.Element('A' * 0x9000)
        d.append(padding)
        self.usePayload(d)

    def insertQuote(self):
        d = copy.deepcopy(self.data)
        img = ET.Element('a', {'a': "\""})
        for _ in range(10):
            d.append(img)
        self.usePayload(d)

    def addImG(self):
        print("===>Trying insert img")
        d = copy.deepcopy(self.data)
        img = ET.Element('img', {'src': "https://images.unsplash.com/photo-1567261584818-a98331941ef1"})
        for _ in range(10):
            d.append(img)
        self.usePayload(d)

    def addPhP(self):
        print("===>Trying insert php")
        d = copy.deepcopy(self.data)
        php = ET.Element('script', {'language': "php"})
        php.text = "die(-88);"
        d.append(php)
        self.usePayload(d)
