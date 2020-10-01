#!/usr/bin/env python3
''' Console '''

from cmd import Cmd
from datetime import datetime
import models
from models.base_model import BaseModel
from models.project import Project
import shlex
from models import storage

classes = {
    'Project': Project
}


class Command(Cmd):
    ''' Command Console '''
    prompt = '[Portfolio] '

    def do_EOF(self, arg):
        """Exits console"""
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def _key_value_parser(self, args):
        """creates a dictionary from a list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except Exception:
                        try:
                            value = float(value)
                        except Exception:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, argv):
        '''Creates a new instance of a passed class '''
        args = argv.split()

        if not len(args):
            print('-*-[ Class name missing ]-*-')
            return None
        elif args[0] in classes:
            new_dict = self._key_value_parser(args[1:])
            id = new_dict.get('id')
            if storage.exists(args[0], id):
                print('-*-[ Id already exists ]-*-')
                return None

            instance = classes[args[0]](**new_dict)
        else:
            print('-*-[ Class doesn\'t exist ]-*-')
            return None

        print(instance.id)
        print(instance, '\n\n\n')
        instance.save()

    def do_all(self, arg):
        '''Prints string representations of instances'''
        args = shlex.split(arg)
        list_ = []
        if len(args) == 0:
            obj_dict = storage.all()
        elif args[0] in classes:
            obj_dict = storage.all(args[0])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            header = key.split('.')
            list_.append(
                '[' + header[0] + '] (' + header[1] + ') ' + str(obj_dict[key])
            )
        print("(", end="")
        print(", ".join(tuple(list_)), end="")
        print(")")

    def do_show(self, arg):
        """Prints an instance as a string based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    print(storage.all().get(key))
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == "__main__":
    Command().cmdloop()
