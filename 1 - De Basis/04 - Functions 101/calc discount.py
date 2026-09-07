from test_lib import test, report

month_discount_brands = 'Vespa,Kymco,Yamama'
MONTH_DISCOUNT_PERC = 10

def calc_discount(price: float, brand: str, month_discount_brands: str) -> float:
    try:
        price = float(price)
        brand = str(brand).strip().lower()
        discount_brands = [b.strip().lower() for b in month_discount_brands.split(',')]
    except ValueError:
        return 0.0  

    if brand in discount_brands:
        discount = price * (MONTH_DISCOUNT_PERC / 100)
        return round(discount, 2)
    else:
        return 0.0

def test_calc_discount():
    test('calc_discount - merk met korting', 100.00, calc_discount(1000, 'Vespa', month_discount_brands))
    test('calc_discount - merk zonder korting', 0.00, calc_discount(1000, 'Honda', month_discount_brands))
    test('calc_discount - hoofdlettergevoeligheid', 50.00, calc_discount(500, 'kYmCo', month_discount_brands))
    test('calc_discount - ongeldige prijs', 0.00, calc_discount('niet een prijs', 'Vespa', month_discount_brands))
    test('calc_discount - lege merklijst', 0.00, calc_discount(1000, 'Vespa', ''))

test_calc_discount()
report()