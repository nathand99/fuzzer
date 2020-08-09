import json
import csv
from xml.etree import ElementTree

#returns two values data, type ('json', 'csv', 'xml', 'txt')
#JSON returns Dict
#XML  returns ElementTree
#CSV  returns 2D Array/List
#TXT  returns String

def parseFile(file):
    data = None
    t = None
    try:
        data = json.load(file)
        t = 'json'
    except:
        file.seek(0)
        try:
            data = ElementTree.parse(file).getroot()
            t = 'xml'
        except:
            file.seek(0)
            try:
                csv.Sniffer().sniff(file.read(), delimiters=",") #checks csv format
                file.seek(0)
                data = list(csv.reader(file))
                t = 'csv'
            except:
                t = 'txt'
    file.seek(0)
    return data, t