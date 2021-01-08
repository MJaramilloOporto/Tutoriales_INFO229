import pytest

@pytest.fixture
def fibonacci():
    fib_list = [0, 1]
    for i in range (2, 100):
        fib_list.append(fib_list[i-1]+fib_list[i-2])
    return fib_list

def test_fibo5(fibonacci):
   assert fibonacci[5] == 5

def test_fibo2(fibonacci):
   assert fibonacci[2] == 1

def test_fibo8(fibonacci):
    #Es 21, pero pondremos 22 para que falle
    assert fibonacci[8] == 22

def test_fibo10(fibonacci):
   assert fibonacci[10] == 55
