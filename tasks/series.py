#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from multiprocessing import Manager, Process


class SeriesProcess(Process):
    def __init__(
        self, x: float, eps: float, start_idx: int, step: int, results: dict, pos: int
    ) -> None:
        super().__init__()
        self.x: float = x
        self.eps: float = eps
        self.start_idx: int = start_idx
        self.step: int = step
        self.results: dict = results
        self.pos: int = pos

    def _term(self, n: int) -> float:
        try:
            return 1.0 / ((2 * n - 1) * (self.x ** (2 * n - 1)))
        except OverflowError:
            return 0.0

    def run(self) -> None:
        partial_sum: float = 0.0
        count: int = 0

        n: int = self.start_idx
        while True:
            term: float = self._term(n)
            if abs(term) < self.eps:
                break
            partial_sum += term
            count += 1
            n += self.step

        self.results[f"sum_{self.pos}"] = partial_sum
        self.results[f"count_{self.pos}"] = count


def calculate_series(x: float, eps: float, num_processes: int = 4) -> tuple[float, int]:
    with Manager() as manager:
        results: dict = manager.dict()
        processes: list = []

        for i in range(num_processes):
            p = SeriesProcess(x, eps, i + 1, num_processes, results, i)
            processes.append(p)
            p.start()

        for p in processes:
            p.join()

        total_sum: float = sum(results[f"sum_{i}"] for i in range(num_processes))
        total_count: int = sum(results[f"count_{i}"] for i in range(num_processes))

    return total_sum, total_count


def get_control_value(x: float) -> float:
    return 0.5 * math.log((x + 1) / (x - 1))
