from code.entities.warehouse.Warehouse import Warehouse

a = Warehouse(13, 434, 54)

print({i[0].split("_")[-1]: i[1] for i in a.__dict__.items()})