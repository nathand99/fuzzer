Fuzzer
======

## Fuzzer Design

The fuzzer works through the implementation of a number of modules which handle different cases of input. The overall flow of the program through the different modules is as follows.

#### Flow
1. If an input has been supplied we call the `parser` module which converts CSV, JSON, and XML inputs into Python objects that can be more easily worked with. If no input is passed we skip to step 4.
2. We initialise the fuzzer module corresponding to the input type as well as a text, and binary fuzzer which perform general operations.
3. Each fuzzer module runs its permutations on the supplied input and attempts to cause an error state in the program.
4. We initialise the `randomFuzzer` which makes up input and attempts to crash the program.

*Note: The main fuzzer program contains a variable `stopAtFirst` which when set to **True** will halt fuzzing at the first case where an error occurs.*

#### Structure 
`fuzzerClass` is the main class and defines methods used by all classes, such as `sendPayload` which creates a process, sends the payload and returns the exit code. The subclasses of `fuzzerClass` are the CSV, JSON, XML, text, binary, and random fuzzers. These define their own fuzzing methods as well as the `makePayload` method that converts the payload to the required format (e.g XML ElemenTree to text). This structure makes adding new techniques to each fuzzer very simple.

As the text fuzzer is called in all the cases where an input is passed this fuzzer does a lot of the general legwork mostly with the use of RegEx to make changes. The other fuzzers are more specialised to targeting input specific exploits. An example of this is the XML fuzzer which tries a number of techniques such as sending an XML Bomb, embedding PHP, and inserting meta characters.

## Fuzzer Functionality

As mentioned above the fuzzer applies some general techniques (using the text fuzzer) on all input types as well as input type specific attacks (eg XML Bomb). This approach has worked quite well and has allowed us to cause SEGFAULTS in all of the provided inputs save for XML3. So let's take a look at some of the general techniques and the bugs they find.

#### General Techniques

- **Length extension:** Possibly the simplest technique, we simply pad out the input with text horizontally (each line) and vertically (whole input).
- **Format string attack:** This technique involves inserting strings such as `"%p%s%x%n"` into the input. This targets poorly written printf statements in the binary and tends to cause a segfault when `"%s"` is encountered as  it causes the program to attempt to read a string from the pointer at the current stack location.
- **Numeric fuzzing:** In this technique we simply look for numbers in the supplied input and replace them with values that may cause an internal error for example negative numbers, zero, or large positive numbers. This targets programs which have insufficient checking on their inputs, negative numbers in particular are quite useful at finding these errors.
- **Meta character removing:** We define some general meta characters found across different input types and attempt to remove or replace them.
- **Byte operations:** The last general technique involves operations on the byte formatted input such as random bit flips and stripping all null characters.

These general techniques implemented by the text and binary fuzzers alone are able to cause faults in the majority of the supplied programs, including CSV1, JSON 1 and 2, all plaintext, and XML1. However we implement some more techniques for more input specific faults.

#### Input specific techniques

- **Nesting Elements (XML,JSON):** We attempt to create a large number of nested elements in the hope that we can exceed recursion depth or cause an overflow.
- **Adding Many Elements (CSV,XML,JSON):** A variation of length extension where we add many elements to the supplied input (this may be necessary to fool the parser).
- **Inserting malicious tags (XML):** We attempt to insert scripts, XML bombs and large images into the XML to try to get code execution or a SEGFAULT.
- **Empty elements: (CSV,XML,JSON)** We attempt to send NULL values in the place of existing well formed elements. (Works for CSV1)

## Improvements and Pitfalls

There are a large number of improvements that could be made to the Fuzzer. One key area of concern is that currently we rely on many arbitrary static values assigned for length extension attacks. In many cases we might not hit the required length or we may go too far overboard. A large improvement would be to look at the length of the supplied input and take that into account, or dynamically adjust according to the return from the binary.

Another area which still needs a lot of work are the random fuzzer which generates inputs and the binary fuzzer. These fuzzers as they currently stand are more of a last ditch effort to cause something to happen rather than well thought out and implemented modules which try to cover specific cases.

Overall however the Fuzzer does a decent job on the supplied binaries and the text Fuzzer has promising performance on these so hopefully it will be able to handle the unseen cases.