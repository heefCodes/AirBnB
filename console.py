#!/usr/bin/python3
"""
command interpreter for the AirBnB application
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class
    """
    prompt = "(hbnb)"

    def preloop(self):
        """
        Introduction to command interpreter
        """
        print('----------------------------')
        print('| Welcome to hbnb CLI!      |')
        print('| for help, input \'help\'    |')
        print('| to quit, input \'quit\'     |')
        print('----------------------------')

    def postloop(self):
        """
        To exit the command interpreter
        """
        print('---------------------------')
        print('| Well, that sure was fun! |')
        print('---------------------------')

    def emptyline(self):
        """
        method called when an empty line is entered in response to the prompt
        """
        return cmd.Cmd.emptyline(self)

    def default(self, line):
        """
        default response for unknown command
        """
        print("This \"{}\" is invalid, run \"help\" "
              "for more informations".format(line))

    def do_quit(self, line):
        """
        To quit the command interpreter
        """
        return True

    # def lastcmd(self, line):
    #     """
    #     last nonempty command prefix seen
    #     """
    #     pass
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()    