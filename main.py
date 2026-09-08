import pyvisa
from connecting import Connect
from instrumentalCLI import InstrumentCLI


def main():

    instrument = Connect.connect()
    InstrumentCLI(instrument).run()

