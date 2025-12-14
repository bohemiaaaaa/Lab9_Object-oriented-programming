#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from multiprocessing import Process


def func():
    print("Hello from child Process")


if __name__ == "__main__":
    print("Hello from main Process")
    proc = Process(target=func)

    proc.start()

    print(f"Proc is_alive statis: {proc.is_alive()}")

    proc.join()

    print("Goodbye")
    print(f"Proc is_alive status: {proc.is_alive()}")
