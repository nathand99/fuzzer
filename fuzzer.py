#!/usr/bin/python3
import sys, os
import json
import csv
from xml.etree import ElementTree
from pwn import process
from modules import *

binaryName = sys.argv[1]

if not os.path.isfile(binaryName):
    exit("Couldn't find binary please use format: python fuzzer.py <binary> [supplied input]")

if (len(sys.argv) > 2):
    try:
        suppliedInput = open(sys.argv[2])
        data, fileType = parseFile(suppliedInput) #Check modules/parser for doc on return
        print("Supplied input of type: {}".format(fileType))
    except:
        print("Couldn't read supplied input. Continuing without...")


try:
    p = process(binaryName)
    #TODO
except Exception as e:
    exit("Couldn't run binary") #TODO