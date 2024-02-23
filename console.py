#!/usr/bin/python3
import cmd
import shlex
from models import storage
import sys
from models.base_class import BaseModel
from models.User import User
from air_bnb.models.City import City
from air_bnb.models.Place import Place
from air_bnb.models.Amenity import Amenity
from air_bnb.models.Review import Review
from air_bnb.models.State import State


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "State", "City", "Amenity", "Review", "Place"]

    def do_quit(self):
        """Quit command to exit the program."""
        exit()

    def do_EOF(self):
        """EOF (Ctrl+D) signal to exit the program."""
        return True

    def emptyline(self):
        pass

    def help(self, arg):
        if not arg:
            super().do_help("")
        else:
            try:
                getattr(self, f"help_{arg}")
            except AttributeError:
                print("No help available for this command.")

    def do_create(self, args):
        """
                Create a new instance of BaseModel and save it to the JSON file.
                Usage: create <class_name>
                """
        try:
            commands = args.split(" ")
            if len(commands) == 0:
                print('** class name missing **')
                return
            elif commands[0] not in self.valid_classes:
                print("** class doesn't exist **")
                return
            else:
                class_name = commands[0]
                new_instance = eval(class_name)()
                params = {}
                for i in range(1, len(commands)):
                    key, value = tuple(commands[i].split("="))
                    if value[0] == '"' and value[-1] == '"':
                        value = value[1:-1].replace('_', ' ').replace('"', r'\"')
                    elif '.' in value:
                        value = float(value)
                    else:
                        try:
                            value = int(value)
                        except ValueError:
                            # Skip if not a valid integer
                            continue
                    params[key] = value
                    setattr(new_instance, key, value)
                storage.new(new_instance)
                storage.save()
                print(new_instance.id)
        except ValueError:
            print(ValueError)
            return

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
            key = f"{commands[0]}.{commands[1]}"
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
            key = f"{commands[0]}.{commands[1]}"
            if key in objects:
                del objects[key]

    def do_all(self, arg):
        """
                Print the string representation of all instances or a specific class.
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
                   Update an instance by adding or updating an attribute.
                   Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
