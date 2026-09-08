import pyvisa

class InstrumentCLI:

    def __init__(self, instrument):
        self.instrument = instrument

    def run(self):
        while True:
            print("\n--- Instrument Control ---")
            print("1. write")
            print("2. query")
            print("3. read")
            print("4. exit")

            choice = input("Choose: ")

            if choice == "1":
                command = input("SCPI command: ")
                self.instrument.write(command)

            elif choice == "2":
                command = input("SCPI query: ")
                print(self.instrument.query(command))

            elif choice == "3":
                print(self.instrument.read())

            elif choice == "4":
                break
