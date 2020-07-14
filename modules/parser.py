import json
import csv
import sys
from xml.etree import ElementTree

#returns two values data, type ('json', 'csv', 'xml', 'txt')
#JSON returns Dict
#XML  returns ElementTree
#CSV  returns Dict
#TXT  returns String

def parseFile(file):
    try:
        data = json.load(file)
        return data, 'json'
    except:
        file.seek(0)
        try:
            data = ElementTree.parse(file)
            return data, 'xml'
        except:
            file.seek(0)
            try:
                dialect = csv.Sniffer().sniff(file.read(), delimiters=",")
                file.seek(0)
                data = csv.DictReader(file, fieldnames=None)
                return data, 'csv'
            except:
                file.seek(0)
                return file.read(), 'txt'