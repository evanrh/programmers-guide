from argparse import ArgumentParser as AP

class CLIView:
    def __init__(self):
        self.parser = AP(description='Store and retrieve contact info')
        self.parser.add_argument('contacts', metavar='database',
                type=str,
                help='a database file to use as the contact book')
        self.parser.add_argument('-a', '--add', action='store_true',
                help='add a new contact to the database')
        self.parser.add_argument('-u', '--update', action='store_true',
                help='update an existing contact in the database')
        self.parser.add_argument('-d', '--delete', action='store_true',
                help='delete an existing contact from the database')

        self.args = self.parser.parse_args()

    def getDB(self):
        """ Get database file for contact information """
        return self.args.contacts

    def getCmd(self):
        """ Return input command """
        if self.args.add:
            return 'add'
        elif self.args.update:
            return 'update'
        elif self.args.delete:
            return 'delete'
        else:
            return ''

    def show(self, s):
        """ Print a string to the screen """
        print(s)

    def getInput(self, s=None):
        """ Get a value from the user """
        return input(s)
