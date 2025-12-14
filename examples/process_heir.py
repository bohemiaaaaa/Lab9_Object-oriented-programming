#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from multiprocessing import Process


class CustomProcess(Process):
    def __init__(self, limit):
        Process.__init__(self)
        self._limit = limit

    def run(self):
        for i in range(self._limit):
            print(f"From CustomProcess: {i}")


if __name__ == "__main__":
    cpr = CustomProcess(3)
    cpr.start()
