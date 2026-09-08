import pyvisa





class Connect:

    @staticmethod
    def choice(resources):
        for number, resource in enumerate(resources, start=1):
            print(f"{number}. {resource}")

        choice = int(input("Choose instrument: "))
        return resources[choice - 1]

    @staticmethod
    def connect():
        rm = pyvisa.ReasourceManager()

        resources = rm.list_resources()

        print("Available instruments:")
        resource = Connect.choice(resources)

        instrument = rm.open_resource(resource)

        print(instrument.query("*IDN?"))

        return instrument
