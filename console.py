#!/usr/bin/python3
import cmd
class Console(cmd.Cmd):
    prompt = ">>>"
    pass

if __name__ == "__main__":
        Console().cmdloop()

