from typing import List, Tuple
from multiprocessing import Pool
from inflect import engine
from functools import lru_cache

p = engine()

@lru_cache(maxsize=None)
def fibonnaci_value(n: int) -> int:
    if n <= 1:
        return n
    return fibonnaci_value(n - 1) + fibonnaci_value(n - 2)

def fibonnaci(n: int) -> List[int]:
    print(f"Calculating fibonnaci sequence for {n}")
    sequence = map(fibonnaci_value, list(range(n)))
    return sequence

def format_fibonnaci_sequence(n: int) -> Tuple[str, str]:
    return (f"Sequência de {n} digitos", ", ".join(map(str, fibonnaci(n))))