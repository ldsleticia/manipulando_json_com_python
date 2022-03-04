from os.path import dirname, realpath, join
from getpass import getpass
from passlib.hash import pbkdf2_sha256 as cryp

from jlogin.utils.jlibs import JSonManager


class Jlogin(JSonManager):
    def __init__(self):
        self.root = dirname(realpath(__file__))
        self.path_data = join(self.path, "data/data.json")

    def sing_in(self):
        print("### Sing In")
        username = input("Enter your username: ")
        password = getpass("Enter your password: ")
        password_verify = getpass("Repeat your password: ")

        while password != password_verify:
            print("Password not equal")
            password_verify = getpass("Repeat your password: ")

        JSonManager.create_json(self.path_data, username, cryp(password_verify))
        print("Registration done!")
