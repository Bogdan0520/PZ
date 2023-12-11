




def variant_4(V_1 : float, V_2: float, S: float, T:float) -> float:
    if isinstance(V_1, (float, int)) != True:
        raise BaseException('Некорректная первая скорость')
    if isinstance(V_2, (float, int)) != True:
        raise BaseException('Некорректная вторая скорость')
    if isinstance(S, (float, int)) != True:
        raise BaseException('Некорректное расстояние')
    if isinstance(T, (float, int)) != True:
        raise BaseException('Некорректное время')
    return S + abs(V_1 + V_2) * T

print(variant_4(1.0,2,3,4))
