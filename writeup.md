# Fuzzer

## Fuzzer Design
The fuzzer works by using a number of modules and classes of fuzzers to break up the work.  
'fuzzerClass' is the main class and defines methods used by all classes such as sendPayload which creates a process, sends the payload and returns the exit code. The subclasses of this fuzzer are the csv, xml, json, txt and random Fuzzers. These define their own fuzzing methods as well as makePayload method which formats the payload for use with sendPayload.  
In order to determine the type of input in the file we use the parser module which analyses the contents to determine the sample input type then returns it as a python object depending on the input (csv returns 2D list, json returns dict ect) depending on which type of input was provided we use that class of fuzzer. If no input is given we skip this step.  
We then use the random fuzzer to generate random inputs.

## Fuzzer Functionality
So far the fuzzer manages to cause segfaults with csv1 and json1 only.  
It took some time to get the design of the fuzzer quite right but use of classes and methods makes it much easier to write new methods and call only those for testing.  
At the moment the only external python package required for the fuzzer to work is pwntools
