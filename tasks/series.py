#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math
from multiprocessing import Manager, Process


class SeriesProcess(Process):
    def __init__(self, x, eps, start_idx, step, results, pos):
        super().__init__()
        self.x = x
        self.eps = eps
        self.start_idx = start_idx
        self.step = step
        self.results = results
        self.pos = pos

    def _term(self, n):
        try:
            return 1.0 / ((2 * n - 1) * (self.x ** (2 * n - 1)))
        except OverflowError:
            return 0.0

    def run(self):
        partial_sum = 0.0
        count = 0

        n = self.start_idx
        while True:
            term = self._term(n)
            if abs(term) < self.eps:
                break
            partial_sum += term
            count += 1
            n += self.step

        self.results[f"sum_{self.pos}"] = partial_sum
        self.results[f"count_{self.pos}"] = count


def calculate_series(x, eps, num_processes=4):
    with Manager() as manager:
        results = manager.dict()
        processes = []

        for i in range(num_processes):
            p = SeriesProcess(x, eps, i + 1, num_processes, results, i)
            processes.append(p)
            p.start()

        for p in processes:
            p.join()

        total_sum = sum(results[f"sum_{i}"] for i in range(num_processes))
        total_count = sum(results[f"count_{i}"] for i in range(num_processes))

    return total_sum, total_count


def get_control_value(x):
    return 0.5 * math.log((x + 1) / (x - 1))
