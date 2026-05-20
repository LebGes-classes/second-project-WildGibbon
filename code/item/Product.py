class Product:
    def __init__(self, id, name, description, warehouse):
        self._description = description
        self._warehouse = warehouse
        self._name = name
        self._id = id

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def description(self):
        return self._description


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

    @description.setter
    def description(self, value):
        if value is None or value == '':
            raise ValueError('description cannot be empty')

        self._description = value