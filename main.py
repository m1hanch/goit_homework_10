from collections import UserDict
class Field:
    pass

class Phone(Field):
    def __init__(self, phone: str):
        self.value = phone
class Name(Field):
    def __init__(self, name: str):
        self.value = name

class Record:
    def __init__(self, Name: Name, *phone: Phone):
        if len(phone)==0:
            phone = []
        self.name = Name
        self.phones = list(phone)

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def remove_phone(self, phone: Phone):
        for ph in self.phones:
            if ph.value == phone.value:
                self.phones.remove(ph)

    def edit_phone(self, old_phone: str, new_phone: str):
        #result = list(filter(lambda contact: contact.get("id") == id, self.data))
        #return result[0] if len(result) > 0 else None
        for phone in self.phones:
            if old_phone == phone.value:
                phone.value = new_phone
class AddressBook(UserDict):
    def list_contacts(self):
        return self.data

    def add_record(self, record: Record):
        self.data.update({record.name.value: record})

    #returns list of phone objects
    def get_contact(self, name: str):
        return self.data.get(name).phones

    def remove_contact(self, name: str):
        self.data.pop(name)


if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    print('All Ok)')