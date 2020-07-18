#!/usr/bin/python3
import sys, os, glob
import json
import csv
from xml.etree import ElementTree
from modules import *

binary = sys.argv[1]
fuzzer = None
success = False

if not os.path.isfile(binary):
    exit("Couldn't find binary please use format: python fuzzer.py <binary> [supplied input]")

if (len(sys.argv) > 2):
    try:
        suppliedInput = open(sys.argv[2])
        data, fileType = parseFile(suppliedInput) #Check modules/parser for doc on return
        print("##########Supplied input of type: {}".format(fileType))

        if fileType == 'csv':
            fuzzer = csvFuzzer(binary, data)
        elif fileType == 'json':
            fuzzer = jsonFuzzer(binary, data)
        elif fileType == 'xml':
            fuzzer = xmlFuzzer(binary, data)
        else:
            fuzzer = txtFuzzer(binary, data)

    except:
        print("##########Couldn't read supplied input")
        print("##########Continuing with random generated inputs...")

#remove previous bad outputs
bads = glob.glob("bad*.txt")
for bad in bads:
    os.remove(bad)

if fuzzer is not None:
    fuzzer.fuzz()
    success = success or fuzzer.success
    if not success:
        print("##########Couldn't crash program with input mutation")

print("##########Trying random generated inputs...")

fuzzer = randomFuzzer(binary, data)
fuzzer.fuzz()
success = success or fuzzer.success
if not success:
    print("##########Couldn't crash program :(")
else:
    print("##########Managed to crash program :)")