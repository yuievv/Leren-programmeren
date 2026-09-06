def vergelijk_getallen(nr1: int, nr2: int) -> str:
    if nr1 > nr2:
        return f'Maximum: {nr1} en minimum: {nr2}'
    elif nr1 < nr2:
        return f'Maximum: {nr2} en minimum: {nr1}'
    else:
        return 'Beide getallen zijn even groot'

# Voorbeelden van gebruik
print(vergelijk_getallen(5, 3))  # Output: Maximum: 5 en minimum: 3
print(vergelijk_getallen(3, 5))  # Output: Maximum: 5 en minimum: 3
print(vergelijk_getallen(5, 5))  # Output: Beide getallen zijn even groot