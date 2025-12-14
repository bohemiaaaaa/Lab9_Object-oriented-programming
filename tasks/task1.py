#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from series import calculate_series, get_control_value

if __name__ == "__main__":
    x = 3.0
    eps = 1e-7

    print("Ряд: S = Σ [1/((2n-1)*x^(2n-1))], n=1..∞")
    print(f"x = {x}, ε = {eps}")

    total_sum, total_count = calculate_series(x, eps)
    control_value = get_control_value(x)
    error = abs(total_sum - control_value)

    print("\nРезультаты:")
    print(f"Вычисленная сумма: {total_sum:.10f}")
    print(f"Контрольное значение: {control_value:.10f}")
    print(f"Абсолютная погрешность: {error:.2e}")
    print(f"Учтено членов ряда: {total_count}")

    if error < eps:
        print("Точность достигнута (погрешность < ε)")
    else:
        print("Погрешность превышает ε")
