from car import Car
import pytest

def test_helloWorld():
    assert "helloworld" == "helloworld"

def test_fillWithGas_error():
    """
    Test that the exception has too much gas
    """
    with pytest.raises(Exception) as excinfo:
        car = Car(3)
        car.fillWithGas(15)
        print (excinfo)
    assert str(excinfo.value) == "The car can't hold that much of gas because you put in 18 gallons, and the max is 12 gallons, and it's 6 gallons over!"
