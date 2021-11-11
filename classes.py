class Cars:
    power = 200
    __slots__ = ['brand', 'model', 'year', 'efficiency', 'color']
    def __init__(self, brand, model, year, efficiency, color):
        self.brand = brand            #this is the car's brand name
        self.model = model            #this is the car's model name
        self.year = year              #this is the car's model year
        self.efficiency = efficiency  #this is the car's fuel efficiency
        self.color = color            #this is the car's color

def printerCars(A):                       #this function prints the class object
    print(A.brand, A.model, A.year, A.efficiency, A.color)

def effCompare(x, y):                 #this function compares fuel efficiency of two cars 
    if x.efficiency > y.efficiency:
        print(x.brand, x.model, "has higher fuel efficiency.")
    elif x.efficiency < y.efficiency:
        print(y.brand, y.model, "has higher fuel efficiency.")
    else:
        print("Equal efficiency.")

def main():
    car1 = Cars('Toyota', 'Camry', 2012, 14.3, 'White')
    car2 = Cars('Mazda', 'MX-5', 2018, 11, 'Red')
    printerCars(car2)
    printerCars(car1)
    print(car2.color)
    effCompare(car1, car2)
    print(car1.power)

main()
