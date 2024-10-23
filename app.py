import datetime
from multiprocessing import Pool
from typing import List
from fastapi import FastAPI, Query

from fibonnaci import format_fibonnaci_sequence

app = FastAPI()


@app.get("/fibonnaci")
def listFibonnaciSequences(ns: List[int] = Query()):
    print(f"Request time for {ns} {datetime.datetime.now()}")
    with Pool() as pool:
        sequences = pool.map(
            format_fibonnaci_sequence,
            ns,
        )

        return dict(sequences)
