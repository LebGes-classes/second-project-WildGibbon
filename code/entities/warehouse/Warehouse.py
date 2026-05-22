class Warehouse:
    def __init__(self, id, name, location):
        self.__location = location
        self.__name = name
        self.__id = id

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @property
    def location(self):
        return self.__location


    @id.setter
    def id(self, value):
        if value is None or value == '':
            raise ValueError('id cannot be empty')

        self.__id = value

    @name.setter
    def name(self, value):
        if value is None or value == '':
            raise ValueError('name cannot be empty')

        self.__name = value

    @location.setter
    def location(self, value):
        if value is None or value == '':
            raise ValueError('location cannot be empty')

        self.__location = value
