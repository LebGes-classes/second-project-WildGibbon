class Customer:
    def __init__(self, id, name, email):
        self._email = email
        self._name = name
        self._id = id

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def email(self):
        return self._email


    @id.setter
    def id(self, value):
        if value is None or value == '':
            raise ValueError('id cannot be empty')

        self._id = value

    @name.setter
    def name(self, value):
        if value is None or value == '':
            raise ValueError('name cannot be empty')

        self._name = value

    @email.setter
    def email(self, value):
        if value is None or value == '':
            raise ValueError('email cannot be empty')

        self._email = value
