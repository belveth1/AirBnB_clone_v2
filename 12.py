#!/usr/bin/python3
import cmd
import shlex
from models import base_model

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "State", "City", "Amenity", "Review", "Place"]

    def do_quit(self, arg):
        """Quit command to exit the program."""
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
                getattr(self, "help_{}".format(arg))
            except AttributeError:
                print("No help available for this command.")
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
if __name__ == "__main__":
    HBNBCommand().cmdloop()
