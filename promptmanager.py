import json
from pathlib import Path
import re


class PromptManager:

    def __init__(self, prompt, config_path=None, doc_path="commands.json"):
        self.prompt = (
            f"{prompt}_commands" if not prompt.endswith("_commands") else prompt
        )
        self.available_prompts = {"write", "query", "read"}


        #Load settings
        if not config_path:
            current_dir = Path(__file__).resolve().parent
            config_path = current_dir / "config.json"

        # Load config and documentation using Path
        config_path = Path(config_path)
        if config_path.exists():
            with open(config_path, "r") as f:
                self.config = json.load(f)
        else:
            self.config = {
                "hints": True
            }


        doc_path = Path(doc_path)
        if doc_path.exists():
            with open(doc_path, "r") as f:
                self.doc = json.load(f).get(self.prompt, {})
        else:
            self.doc = {}


    def has_digit(self, text):
        return bool(re.search(r'\d', text))

    def run(self):
        print("\n--- Command Helper ---")


        show_hints = self.config['hints']

        if "overview" in self.doc and show_hints:
            print(f"Overview: {self.doc['overview']}")
            print(f"Example: {self.doc['example']}\n")

        cmd = input("Enter command name: ").strip().upper()

        if cmd.startswith("*") or cmd.endswith("?"):
            return cmd

        if self.has_digit(cmd):
            command, value = cmd.split( )

            value = float(value)

            return f"{command} {value}"



        # Show doc info if command exists in JSON
        if cmd in self.doc:
            info = self.doc[cmd]
            print(f"Meaning: {info['meaning']}")
            print(f"Doc Example: {info['example']}\n")

        value = input(f"{cmd} ").strip()

        # Format integer values as floats (e.g., 5 -> 5.0)
        if value.isdigit():
            value = f"{float(value):.1f}"

        return f"{cmd} {value}".strip()
