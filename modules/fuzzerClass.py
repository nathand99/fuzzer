from pwn import process, context
import glob

outputFormat = """SUCCESS! Process crashed with code {}
PAYLOAD:
=========================================
{}{}
========================================="""

#Turns off pwn logging
context.log_level = 'warn'

class fuzzerClass:

    def __init__(self, binary, data, makePayload, name, stopAtFirst=False):
        self.binary = binary
        self.data = data
        self.makePayload = makePayload
        self.name = name
        self.stopAtFirst = stopAtFirst
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
                if self.success and self.stopAtFirst:
                    return


    #Returns the exit code of the process or 0 if process didn't exit
    def sendPayload(self, payload):
        nullPadding = False
        p = process(self.binary)
        p.send(payload)
        p.sendline()

        p.wait_for_close(timeout=0.1)
        code = p.poll()
        if code is None:
            p.send(b'\x00'*10000)
            p.clean(timeout=0.001)
            nullPadding = True

        p.wait_for_close(timeout=0.2)
        code = p.poll()
        if code is None: #Process still has not exited
            code = 0
            p.kill()    #Kill proc if doesn't stop on its own
            print("Process did not exit")
        
        return code, nullPadding

    #Runs the process with payload and prints if error
    def usePayload(self, data):
        payload = self.makePayload(data)
        exitCode, nullPadding = self.sendPayload(payload)
        if exitCode != 0:
            self._logPayload(exitCode, payload, nullPadding)

    #Logs output to console and bad and sets success true
    def _logPayload(self, code, payload, nullPadding):
        ellipsis = "\n..." if len(payload) > 200 else ""
        out = outputFormat.format(code, payload[0:200], ellipsis)
        print(out)
        suffix = len(glob.glob("bad*.txt"))
        suffix = suffix + 1 if suffix > 0 else ""
        f = open("bad{}.txt".format(suffix), "w")
        f.write(payload)
        if nullPadding:
            f.write('\x00'*10000)
        f.close
        self.success = True
