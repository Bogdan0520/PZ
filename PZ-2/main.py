

def variant_4(V_1 : float, V_2: float, S: float, T:float) -> float:
    if isinstance(V_1, float):
        print('Некорректная первая скорость')
    return S + abs(V_1 + V_2) * T

variant_4(1,2,3,4)
