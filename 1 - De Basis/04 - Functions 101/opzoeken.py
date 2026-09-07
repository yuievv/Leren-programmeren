from test_lib import test, report

def get_value(data: str, separator: str, position: int) -> str:
    splitted_strings = data.split(separator)
    
    if 0 <= position < len(splitted_strings):
        return splitted_strings[position]
    else:
        return None

def test_get_value():
    test('get_value - normaal geval', 'kat', get_value('muis,kat,hond', ',', 1))
    
    test('get_value - eerste positie', 'Sofie:8', get_value('Sofie:8,Emma:7,Ahmed:9', ',', 0))
    test('get_value - laatste positie', 'Ahmed:9', get_value('Sofie:8,Emma:7,Ahmed:9', ',', 2))
    test('get_value - ongeldige positie', None, get_value('muis,kat,hond', ',', 5))
    test('get_value - lege string', '', get_value('muis,,hond', ',', 1))
    test('get_value - andere separator', 'Emma:7', get_value('Sofie:8;Emma:7;Ahmed:9', ';', 1))

test_get_value()
report()