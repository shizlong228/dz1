def div(a: float, b: float) -> float | str:
    if b == 0:
        return "Ошибка! Деление на ноль!"
    return a / b

def pow(a: float, b: float) -> float:
    return a ** b

def summ(a: float, b: float) -> float:
    return a + b

def minuse(a: float, b: float) -> float:
    return a - b

def sqrt(a: float) -> float:
    """Возвращает корень числа a"""
    return a ** 0.5

def fact(a: int) -> int:
    """Вычисляет факториал"""
    r = 1
    for i in range(2, a + 1):
        r *= i
    return r

def is_equal(a: float, b: float) -> bool:
    return a == b