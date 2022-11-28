#!/usr/bin/python3
"""
    AirBnB_Clone ommand Line Interpreter
"""

import cmd
import json

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

# EOF command exits out of the comand line interpreter
    def do_EOF(self, args):
        print()
        return True
    def help_EOF(self):
        print("EOF (End Of File): Command to terminate process and exit the program")

# quit command exits the program
    def do_quit(self, args):
        return True
    def help_quit(self):
        print("Quit: Command to exit the program. Similar to EOF")

# Empty_line + enter would not execute
    def emptyline(self):
        pass
    

if __name__ == "__main__":
        HBNBCommand().cmdloop()

