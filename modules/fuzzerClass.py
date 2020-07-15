from pwn import process, context

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

    #Returns the exit code of the process or 0 if process didn't exit
    def sendPayload(self, payload):
        p = process(self.binary)
        p.send(payload)
        p.wait_for_close(timeout=0.5)
        code = p.poll()
        if code is None:
            p.kill()    #Kill proc if doesn't stop on its own
        return code

    #Runs the process with payload and prints if error
    def usePayload(self, data):
        payload = self.makePayload(data)
        exitCode = self.sendPayload(payload)
        if exitCode != 0:
            self.success = True
            logPayload(exitCode, payload)

        