from multiprocessing import Pool
from typing import List
from fastapi import FastAPI, Query

from fibonnaci import fibonnaci

app = FastAPI()


@app.get("/fibonnaci")
def listFibonnaciSequences(ns: List[int] = Query()):
    sequences = [
        (f"Sequência de {n} digitos", ", ".join(map(str, fibonnaci(n)))) for n in ns
    ]

    return dict(sequences)
