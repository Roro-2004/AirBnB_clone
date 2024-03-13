#!/usr/bin/python3
"""
AirBnB Console Class
"""
import cmd
import shlex
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    The command prompot interpreter

    Attributes:
        prompt:  prompt string
        classes: list of classes of airbnb
    """

    prompt = "(hbnb)"
    classes = ["BaseModel"]

    def do_quit(self, args):
        """
        to quit the program
        """
        return True

    def do_EOF(self, arg):
        """
        exit the program
        """
        return True

    def emptyline(self):
        """
        handles empty prompot
        """
        return False

    def do_create(self, arg):
        """
        creates a new instance
        """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """
        show the data of an instance
        """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(commands) == 1:
            print("** instance id missing **")
        else:
            loaded = storage.all()
            key = commands[0] + '.' + commands[1]
            if key in loaded:
                print(loaded[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        deletes an instance
        """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(commands) == 1:
            print("** instance id missing **")
        else:
            new = FileStorage()
            new.reload()
            loaded = new.all()
            key = commands[0] + '.' + commands[1]
            if key in loaded:
                loaded.pop(key)
                new.edit(loaded)
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        prints all instances in a list
        """
        commands = shlex.split(arg)
        loaded = storage.all()
        temp = []
        if len(commands) == 1:
            if commands[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                for v in loaded.values():
                    temp.append(str(v))
                print(temp)
        else:
            for v in loaded.values():
                temp.append(str(v))
            print(temp)

    def do_update(self, arg):
        """"
        updates an existing instance
        """
        commands = shlex.split(arg)
        new = FileStorage()
        new.reload()
        loaded = new.all()
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(commands) == 1:
            print("** instance id missing **")
        elif len(commands) == 2:
            key = commands[0] + '.' + commands[1]
            if key not in loaded:
                print("** no instance found **")
            else:
                print("** attribute name missing **")
        elif len(commands) == 3:
            print("** value missing **")
        else:
            key = commands[0] + '.' + commands[1]
            object = loaded[key]
            att_name = commands[2]
            att_val = commands[3]
            try:
                att_val = eval(att_val)
            except Exception:
                pass
            setattr(object, att_name, att_val)
            object.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
