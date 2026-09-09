from connect import PsuConnection
import os
import pyvisa
from promptmanager import PromptManager
import sys

class TUI:
    def __init__(self, psu):
        self.psu = psu

    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    def user_choice(self, prompt = "Enter your choice: ", choices_amount = 4):

        while True:

            choice = input(prompt).strip()

            if choice.isalpha():
                input("invalid choice. Please enter a number")
                continue


            choice = int(choice)

            if choice > choices_amount or choice < 1:
                input(f"invalid choice. Please enter number between 1 - {choices_amount}")
                continue

            return choice

    def print_menu(self):
        self.clear()
        print("""--- Funcitons ---
        1. write - Sends a control command to PSU without asking for a reply.
        2. read - Fetches raw data currently sitting in the PSU output buffer.
        3. query - Combines write and read into one action by sending a command.
        4. settings - Self Explanatory
        5. close - Releases VISA session and closes program.""")


    def _enter_menu_prompt(self, choice_num):

            commands = {
                1: self.write_prompt,
                2: self.read_prompt,
                3: self.query_prompt,
                4: self.settings,
                5: self.cleanup,
            }

            action = commands.get(choice_num)
            if action:
                action()
            else:
                print("Invalid input")



    def write_prompt(self):
        self.clear()
        cmd = PromptManager("write").run()
        psu.write(cmd)

    def read_prompt(self):
        self.clear()
        cmd = PromptManager("read").run()
        psu.read(cmd)

    def query_prompt(self):
        self.clear()
        cmd = PromptManager("query").run()
        psu.query(cmd)


    def settings(self):
        input("Not avaiable")


    def cleanup(self):
        print("Releasing VISA session and closing program...")
        sys.exit(0)

    def run(self):
        while True:

            self.print_menu()
            user_command = self.user_choice(choices_amount = 5)

            self._enter_menu_prompt(user_command)

:


def main():
    psu = PsuConnection.connect()
    TUI(psu).run()
