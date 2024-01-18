#!/usr/bin/python3
"""
Module for console
"""
import cmd
import shlex
from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "State", "City",
                     "Amenity", "Review", "Place"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF (Ctrl+D) signal to exit the program."""
        return True

    def emptyline(self):
        pass

    def help(self, arg):
        if not arg:
            super().do_help("")
        else:
            try:
                getattr(self, "help_" + arg)()
            except AttributeError:
                print("No help available for this command.")

    def do_create(self, arg):
        """
                Create a new instance of BaseModel and
                save it to the JSON file.
                Usage: create <class_name>
                """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print('** class name missing **')
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = globals()["{}".format(commands[0])]()
            storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
               Show the string representation of an instance.
               Usage: show <class_name> <id>
               """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print('** class name missing **')
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.
        Usage: destroy <class_name> <id>
        """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print('** class name missing **')
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                del objects[key]
                storage.save()

    def do_all(self, arg):
        """
                Print the string representation of all
                instances or a specific class.
                Usage: <User>.all()
                        <User>.show()
                """
        objects = storage.all()
        commands = shlex.split(arg)
        if len(commands) == 0:
            for key, value in objects.items():
                print(str(value))
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == commands[0]:
                    print(str(value))

    def do_update(self, arg):
        """
                   Update an instance by
                   adding or updating an attribute.
                   Usage: update <class_name> <id>
                   <attribute_name> "<attribute_value>"
                   """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key not in objects:
                print("** no instance found **")
            elif len(commands) < 3:
                print("** attribute name missing **")
            elif len(commands) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                atr_name = commands[2]
                atr_value = commands[3]
                try:
                    atr_value = eval(atr_value)
                except Exception:
                    pass
                setattr(obj, atr_name, atr_value)
                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
