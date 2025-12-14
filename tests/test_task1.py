#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math

import pytest

from tasks.series import calculate_series, get_control_value


@pytest.mark.parametrize(
    "x, eps",
    [
        (2.0, 1e-7),
        (3.0, 1e-8),
        (5.0, 1e-6),
    ],
)
def test_calculate_series_accuracy(x: float, eps: float) -> None:
    total_sum, total_count = calculate_series(x, eps, num_processes=4)
    control_value: float = get_control_value(x)
    error: float = abs(total_sum - control_value)

    assert error < eps, f"Ошибка {error} превышает eps={eps}"
    assert total_count > 0


def test_control_value_known() -> None:
    x: float = 2.0
    expected: float = 0.5 * math.log((x + 1) / (x - 1))
    assert math.isclose(get_control_value(x), expected, rel_tol=1e-12)


def test_series_convergence_monotone() -> None:
    x: float = 3.0
    sum_coarse, _ = calculate_series(x, 1e-4, num_processes=4)
    sum_fine, _ = calculate_series(x, 1e-8, num_processes=4)
    control: float = get_control_value(x)

    assert abs(sum_fine - control) < abs(sum_coarse - control)
