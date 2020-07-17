class randomFuzzer:

    def __init__(self, binary, data):
        self.binary = binary
        self.data = data
        self.makePayload = lambda x: bytes(x)

    #Fuzzing Techniques
