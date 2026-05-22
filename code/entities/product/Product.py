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

    @property
    def warehouse(self):
        return self._warehouse


    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError('id must be an integer')
        if value <= 0:
            raise ValueError('id must be a positive integer')

        self._id = value

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('name must be a string')
        if not value:
            raise ValueError('name cannot be empty')

        self._name = value

    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise TypeError('description must be a string')
        if not value:
            raise ValueError('description cannot be empty')

        self._description = value

    @warehouse.setter
    def warehouse(self, value):
        if not isinstance(value, int):
            raise TypeError('warehouse must be an integer')
        if value <= 0:
            raise ValueError('warehouse must be a positive integer')

        self._warehouse = value