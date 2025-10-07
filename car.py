class Car:
    def __init__(self, currentGallonsOfGas):
        print ("car created")
        self.currentGallonsOfGas = currentGallonsOfGas
        self.maxGallonOfGas = 12
        # number of miles per gallon. Then howMuchToDrive (amountOfMIles), then costs of gallons of gasoline, then newAmountOfGasoline = self.currentAmountOfGas - numOfGallons it took to  move

    def turnOn(self):
        print ("Battery OK")
        print ("Ignition Switch OK")
        print ("Resistor OK")
        print ("Ignition Coil OK")
        print ("Rotor OK")
        print ("Spark Plugs OK")
        print ("Engine OK")

    def fillWithGas(self, numToFillBy):
        newAmountOfGas = self.currentGallonsOfGas + numToFillBy
        if newAmountOfGas > self.maxGallonOfGas:
            raise Exception("The car can't hold that much of gas because you put in {} gallons, and the max is {} gallons, and it's {} gallons over!".format(newAmountOfGas, self.maxGallonOfGas, newAmountOfGas - self.maxGallonOfGas))

if __name__ == "__main__":
    car = Car(3)
    car.turnOn()
    try:
        car.fillWithGas(15)
    except Exception as e:
        print (e)
