#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import isfile
from json import dump, load


class JSonManager:
    def create_json(self, filepath, *args):
        data = {"username": "", "password": ""}
        if args:
            data = {f"username": f"{args[0]}", "password": f"{args[1]}"}
        with open(filepath, "w") as f:
            dump(data, f, indent=2, separators=(",", ": "))
        return True

    def read_json(self, filepath):
        if isfile(filepath):
            with open(filepath) as f:
                data = load(f)
            return data
        else:
            return False

    def update_json(self, filepath, data):
        with open(filepath, "w") as f:
            dump(data, f, indent=2, separators=(",", ": "))


if __name__ == "__main__":
    jmanager = JSonManager()
    jmanager.create_json("data/data.json")
    print(jmanager.read_json("data/data.json")["username"])
