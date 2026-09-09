#!/usr/bin/python3
"""This module defines the entry point of the command interpreter
for the AirBnB clone project.
"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone project."""

    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program."""
        print("")
        return True

    def do_create(self, line):
        """Creates a new instance of a class, saves it and prints
        the id. Usage: create <class name>
        """
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[args[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on
        the class name and id. Usage: show <class name> <id>
        """
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        print(all_objs[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id.
        Usage: destroy <class name> <id>
        """
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        del all_objs[key]
        storage.save()

    def do_all(self, line):
        """Prints all string representations of all instances, based
        or not on the class name. Usage: all [<class name>]
        """
        args = shlex.split(line)
        all_objs = storage.all()
        if len(args) > 0 and args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        result = []
        for key, obj in all_objs.items():
            if len(args) == 0 or key.split(".")[0] == args[0]:
                result.append(str(obj))
        print(result)

    def do_update(self, line):
        """Updates an instance based on the class name and id by
        adding or updating an attribute. Usage:
        update <class name> <id> <attribute name> "<attribute value>"
        """
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = all_objs[key]
        attr_name = args[2]
        attr_value = args[3]
        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
            try:
                attr_value = attr_type(attr_value)
            except (TypeError, ValueError):
                pass
        setattr(obj, attr_name, attr_value)
        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
