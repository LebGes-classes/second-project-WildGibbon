class Store:
    def __init__(self, id, name, address):
        self._address = address
        self._name = name
        self._id = id

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def address(self):
        return self._address


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

    @address.setter
    def address(self, value):
        if value is None or value == '':
            raise ValueError('address cannot be empty')

        self._address = value
