class Employee:
    def __init__(self, id, name, position):
        self._position = position
        self._name = name
        self._id = id

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def position(self):
        return self._position


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

    @position.setter
    def position(self, value):
        if value is None or value == '':
            raise ValueError('position cannot be empty')

        self._position = value
