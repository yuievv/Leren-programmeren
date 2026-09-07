from test_lib import test, report
from mijn_functie import mijn_functie

expected = 'gelijk' 
result = mijn_functie(5, 5)
test('TEST nr1=nr2', expected, result)

expected = 'groter' 
result = mijn_functie(10, 5)
test('TEST nr1>nr2', expected, result)

expected = 'kleiner' 
result = mijn_functie(3, 5)
test('TEST nr1<nr2', expected, result)

if __name__ == "__main__":
    report()