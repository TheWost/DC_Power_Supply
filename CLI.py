import sys

from connect import PsuConnection


def main():
    psu = PsuConnection.connect()

    if len(sys.argv) < 2:
        print("No command provided. e.g. python3 cli.py '*IDN?'")
        return

    command = " ".join(sys.argv[1:])

    response = psu.query(command)
    print(response)

    psu.close()


if __name__ == "__main__":
    main()
