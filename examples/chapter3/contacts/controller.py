from model import ContactBook
from view import CLIView

class Controller:
    def __init__(self):
        self.view = CLIView()
        self.model = ContactBook()

    def run(self):
        db = self.view.getDB()
        self.model.loadBook(db)
        cmd = self.view.getCmd()

        if cmd == 'add':
            self._add()
        elif cmd == 'delete':
            self._delete()
        elif cmd == 'update':
            self._update()
        else:
            self._showContacts()

    def _add(self):
        nameStr = "Enter the contact's name: "
        phoneStr = "Enter the contact's phone number: "
        addrStr = "Enter the contact's address: "
        emailStr = "Enter the contact's email: "

        name = self.view.getInput(nameStr)
        while not name:
            name = self.view.getInput(nameStr)
        phone = self.view.getInput(phoneStr)
        while not phone:
            phone = self.view.getInput(phoneStr)
        addr = self.view.getInput(addrStr)
        email = self.view.getInput(emailStr)

        self.model.addContact(name, phone, addr, email)

    def _delete(self):
        s = "Enter the contact to be deleted's name OR phone number: "
        np = self.view.getInput(s)
        if self.model.deleteContact(np):
            st = "The contact identified by {} was deleted".format(np)
            self.view.show(st)
        else:
            self.view.show("No matching contacts found")

    def _update(self):
        pass

    def _showContacts(self):
        conts = self.model.getAllContacts()
        for c in conts:
            hdrs = ['Phone', 'Address', 'Email', '']
            hdrs = ['\t' + x for x in hdrs]
            s = "{}:\n" + ": {}\n".join(hdrs)
            self.view.show(s.format(*c))
