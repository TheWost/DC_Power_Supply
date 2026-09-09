import json
import pyvisa



class PsuConnection:

    @staticmethod
    def load_config(config_path="config.json"):
        with open(config_path, "r") as f:
            data = json.load(f)
            return data.get("psu")

    @staticmethod
    def save_config(psu_name, config_path="config.json"):
        data = PsuConnection.load_config(config_path)
        data["psu"] = psu_name 
        with open(config_path, "w") as f:
            json.dump(data, f)

    @staticmethod
    def choice(resources):
        if not resources:
            print("No psus found.")
            return None

        for number, resource in enumerate(resources, start=1):
            print(f"{number}. {resource}")

        choice = int(input("Choose psu: "))
        return resources[choice - 1]

    @staticmethod
    def connection_input(rm):
        resources = rm.list_resources()
        return PsuConnection.choice(resources)

    @staticmethod
    def connect():
        rm = pyvisa.ResourceManager()

        psu_name = PsuConnection.load_config()
        if not psu_name:
            psu_name = PsuConnection.connection_input(rm)

        if not psu_name:
            raise RuntimeError("No psu selected or available.")

        PsuConnection.save_config(psu_name)

        psu = rm.open_resource(psu_name)
        return psu




def main():
    print("First time setup")
    PsuConnection.connect()


if __name__ == "__main__":
    main()
