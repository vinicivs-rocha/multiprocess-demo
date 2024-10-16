from typing import List
from multiprocessing import Pool
from inflect import engine
from functools import lru_cache

p = engine()

@lru_cache(maxsize=None)
def fibonnaci_value(n: int) -> int:
    if n <= 1:
        return n
    return fibonnaci_value(n - 1) + fibonnaci_value(n - 2)


def fibonnaci_sequence(n: int) -> int:
    print(f"Calculating fibonnaci {p.ordinal(n)} value of sequence")
    return fibonnaci_value(n)


def fibonnaci(n: int) -> List[int]:
    print(f"Calculating fibonnaci sequence for {n}")
    with Pool() as pool:
        sequence = pool.map(fibonnaci_sequence, list(range(n)))
    print(f"Calculated fibonnaci sequence for {n}")
    return sequence
