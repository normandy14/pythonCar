class Car:
    def __init__(self, gallonsOfGas):
        print ("car created")
        self.gallonsOfGas = gallonsOfGas
        self.maxGallonOfGas = 12

    def turnOn(self):
        print ("Battery OK")
        print ("Ignition Switch OK")
        print ("Resistor OK")
        print ("Ignition Coil OK")
        print ("Rotor OK")
        print ("Spark Plugs OK")
        print ("Engine OK")

    def fillWithGas(self, numToFillBy):
        newAmountOfGas = self.gallonsOfGas + numToFillBy
        if newAmountOfGas > self.maxGallonOfGas:
            raise Exception("The car can't hold that much of gas because you put in {}, and it's {} gallons over".format(newAmountOfGas, newAmountOfGas - self.maxGallonOfGas))

if __name__ == "__main__":
    car = Car(3)
    car.turnOn()
    try:
        car.fillWithGas(15)
    except Exception as e:
        print (e)
        print ("the max gallons in the tank is {}".format(car.maxGallonOfGas))
