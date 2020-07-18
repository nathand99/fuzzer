from pwn import process, context
import sys, glob

outputFormat = """SUCCESS! Process crashed with code {}
PAYLOAD:
=========================================
{}{}
========================================="""

#Turns off pwn logging
context.log_level = 'warn'

class fuzzerClass:

    def __init__(self, binary, data, makePayload):
        self.binary = binary
        self.data = data
        self.makePayload = makePayload
        self.success = False

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
            self._logPayload(exitCode, payload)

    #Logs output to console and bad and sets success true
    def _logPayload(self, code, payload):
        ellipsis = "\n..." if len(payload) > 200 else ""
        out = outputFormat.format(code, payload[0:200], ellipsis)
        print(out)
        suffix = len(glob.glob("bad*.txt"))
        suffix = suffix + 1 if suffix > 0 else ""
        f = open("bad{}.txt".format(suffix), "w")
        f.write(payload)
        f.close
        self.success = True
