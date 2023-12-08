#!/usr/bin/python3
"""
    Module of the (hbnb) command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ defining class for hbnb command interpreter """
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """ When (CTRL+D) exit the program """
        return True
    
    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def help_quit(self):
        """ Quit command to exit the program """
        print ("Quit command to exit the program\n")

    def emptyline(self):
        """ do nothing, give another prompt """
        pass

    def postloop(self):
        """
        print newline when Ctrl+D, to provide a clean
        separation between the cmd prompt and the shell prompt.
        """
        print()

    def default(self, line):
        """ Print unrecognized command """
        print(f"Command '{line}' not recognized."
                "Type 'help' for a list of commands.")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
