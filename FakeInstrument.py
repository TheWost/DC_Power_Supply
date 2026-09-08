class FakeInstrument:
    def write(self, command):
        print(f"→ Instrument received: {command}")

    def read(self):
        return "FAKE RESPONSE"

    def query(self, command):
        self.write(command)
        return self.read()
