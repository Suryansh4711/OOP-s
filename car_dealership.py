class Car:
    def __init__(self, car_maker, car_name, car_model, manufacturing_year, car_price):
        self.maker = car_maker
        self.name = car_name
        self.model = car_model
        self.year = manufacturing_year
        self.price = car_price
        self.available = True

    def display_car(self):
        return f'''Maker: {self.maker}
Car Name: {self.name}
Car Model: {self.model}
Car Production Year: {self.year}
Car Price: {self.price}'''


class dealership:
    def __init__(self, name) -> None:
        self.name = name
        self.inventory = []

    def add_car_to_inventory(self, car):
        self.inventory.append(car)

    def display_available_car(self):
        count = 1
        for car in self.inventory:
            if car.available:
                print(count)
                print(car.display_car())
                print('----------------------\n')
                count += 1

    def sell_car(self, c, index):
        if 0 < index <= len(self.inventory) and self.inventory[index-1].available:
            c.purchase(self.inventory[index-1])
            return self.inventory[index-1]



class customer:
    def __init__(self, name):
        self.name = name
        self.purchased_car = []

    def purchase(self, car):
        self.purchased_car.append(car)
        car.available = False


# main code
car1 = Car('BMW', 'BMW', 'Q7', 2021, '88 Lakhs')
car2 = Car('Audi', 'Audi', 'R8', 2023, '2.72 Crores')
car3 = Car('Tata', 'Jaguar', 'XF', 2015, '87.79 Lakhs')


d1 = dealership('United Cars')
d1.add_car_to_inventory(car1)
d1.add_car_to_inventory(car2)
d1.add_car_to_inventory(car3)
d1.display_available_car()

cname = input('Enter the Customer Name: ')
cnum = int(input(f'Enter the car number from [1-{len(d1.inventory)}]:- '))
c1 = customer(cname)
ret = d1.sell_car(c1, cnum)
if ret:
    print(f'{c1.name} purchase car\n{ret.display_car()}')
else:
    print('car is not available')

print('\nAfter selling available cars')
d1.display_available_car()