import copy

class Delicacy:
    def __init__(self, name = '', price = 0, weight = 0):
        self.name = name
        self.price = price
        self.weight = weight
    
    def __str__(self):
        return 'name: {}, price: {}, weight: {}'.format(self.name, self.price, self.weight)

warehouse = list()
warehouse.append(Delicacy(name='Lolly Pop', price=0.4, weight=133))
warehouse.append(Delicacy(name='Licorice', price=0.1, weight=251))
warehouse.append(Delicacy(name='Chocolate', price=1, weight=601))
warehouse.append(Delicacy(name='Sours', price=0.01, weight=513))
warehouse.append(Delicacy(name='Hard candies', price=0.3, weight=433))

discount_warehouse_01 = copy.deepcopy(warehouse)

for item in discount_warehouse_01:
    if item.weight > 300:
        item.price = item.price * 0.8

discount_warehouse_02 = copy.copy(warehouse)

for item in discount_warehouse_01:
    if item.weight > 300:
        item.price = item.price * 0.8

print('Source list of candies')
for item in warehouse:
    print(item)
    
print('******************')
print('Price proposal 01')
for item in discount_warehouse_01:
    print(item)

print('******************')
print('Price proposal 02')
for item in discount_warehouse_02:
    print(item)