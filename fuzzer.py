#!/usr/bin/python3
import sys
import json
from pwn import *
from modules.parser import parseFile

try:
    p = process(sys.argv[1])
except:
    exit("Couldn't run or find binary please use format: python fuzzer.py <binary> [supplied input]")

if (len(sys.argv) > 2):
    try:
        suppliedInput = open(sys.argv[2])
        data, fileType = parseFile(suppliedInput) #Check modules/parser for doc on return
        print("Supplied input of type: {}".format(fileType))
    except:
        print("Couldn't read supplied input. Continuing without...")