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

def sqrt(a: float):
    return a ** 0.5