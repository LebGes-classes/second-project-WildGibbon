from code.entities.employee.Employee import Employee
from code.menu_system.factories.LeafItemFactory import create_leaf_item
from code.menu_system.actions.DelegateAction import DelegateAction
from code.menu_system.menu.item.MenuItem import MenuItem
from code.menu_system.menu.Menu import IMenu


class EmployeeMenu(IMenu):
    def __init__(self, menu: IMenu, employees: list[Employee]):
        self.__employees = employees
        self.__menu = menu

        self.__build_menu()

    def open(self):
        self.__menu.open()

    def close(self):
        self.__menu.close()

    def append_item(self, item):
        self.__menu.append_item(item)

    def insert_item(self, menu_item, index):
        self.__menu.insert_item(index, menu_item)

    def remove_item(self, index):
        self.__menu.remove_item(index)

    def length(self):
        return self.__menu.length()


    def __build_menu(self):
        self.__menu.insert_item(0, MenuItem("Добавить сотрудника", DelegateAction(self.__add_employee)))
        self.__menu.insert_item(0, MenuItem("Удалить сотрудника", DelegateAction(self.__remove_employee)))

        for employee in self.__employees:
            product_item = create_leaf_item(employee.id,
                                            employee.name,
                                            employee.position)

            self.__menu.append_item(product_item)

    def __add_employee(self):
        id = input("Enter ID: ")
        name = input("Enter name: ")
        position = input("Enter position: ")

        menu_item = create_leaf_item(name, id, position)

        self.__employees.append(Employee(id, name, position))
        self.__menu.append_item(menu_item)

    def __remove_employee(self):
        num = int(input("Enter number: "))
        self.__menu.remove_item(num - 1)
        self.__employees.pop(num - 4)
