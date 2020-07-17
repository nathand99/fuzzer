#!/usr/bin/python3
import sys, os
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
            fuzzers = jsonFuzzer(binary, data)
        elif fileType == 'xml':
            fuzzers = xmlFuzzer(binary, data)
        else:
            fuzzers = txtFuzzer(binary, data)

    except:
        print("##########Couldn't read supplied input")
        print("##########Continuing with random generated inputs...")

if fuzzer is not None:
    fuzzer.fuzz()
    if not fuzzer.success:
        print("##########Couldn't crash program with input mutation")
        print("##########Continuing with random generated inputs...")

fuzzer = randomFuzzer(binary, data)
fuzzer.fuzz()
if not fuzzer.success:
    print("##########Couldn't crash program :(")