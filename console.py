#!/usr/bin/python3
import cmd
"""
AirBnB Console Class
"""


class HBNBCommand(cmd.Cmd):

    """
    The command prompot interpreter
    Attributes:
        prompt:  prompt string
    """
    prompt = "(hbnb)"

    def do_quit(self, args):
        """
        to quit the program
        """
        return True

    def do_EOF(self, arg):
        """exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
