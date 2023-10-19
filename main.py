def div(a: float, b: float) -> float | str:
    if b == 0:
        return "Ошибка! Деление на ноль!"
    return a / b

def pow(a: float, b: float) -> float:
    return a ** b

def summ(a, b):
    return a + b