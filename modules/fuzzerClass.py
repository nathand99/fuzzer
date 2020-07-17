from pwn import process, context
import sys

#HELPER: formats output to console
def logPayload(code, payload):
    print("SUCCESS! Process crashed with code {}".format(code))
    print("PAYLOAD:")
    print("=========================================")
    print(payload)
    print("=========================================")

#Turns off pwn logging
context.log_level = 'warn'

class fuzzerClass:

    success = False

    def __init__(self, binary, data, payloadFormatter):
        self.binary = binary
        self.data = data
        self.makePayload = payloadFormatter

    def fuzz(self):
        attributes = list(filter(
            lambda x: not x.startswith("_")
            and not x.endswith("Payload")
            and not x == "fuzz",
            dir(self)))
        for attribute in attributes:
            method = getattr(self, attribute)
            if callable(method):
                method()


    #Returns the exit code of the process or 0 if process didn't exit
    def sendPayload(self, payload):
        p = process(self.binary)
        p.send(payload)
        p.sendline()
        p.wait_for_close(timeout=0.2)
        code = p.poll()
        if code is None:
            code = 0
            p.kill()    #Kill proc if doesn't stop on its own
            # print("Process did not exit")
        return code

    #Runs the process with payload and prints if error
    def usePayload(self, data):
        payload = self.makePayload(data)
        exitCode = self.sendPayload(payload)
        if exitCode != 0:
            self.success = True
            logPayload(exitCode, payload)
