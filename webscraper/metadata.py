import pandas as pd
from multiprocessing import freeze_support, Pool, Value
import zlib
import base64
import sys

def run_multiprocessing(func, i, n_processors):
    with Pool(processes=n_processors) as pool:
        return pool.map(func, i)


def run_multiprocessing(func, i, n_processors):
    with Pool(processes=n_processors) as pool:
        return pool.map(func, i)

count = Value('i', 0)

def extractor(str_compressed):
    zlib.decompress(base64.b64decode(str_compressed))
    count.acquire()
    count.value += 1
    count.release()
    print("Count: ", end="\r", flush=True)
    return "y"

def main():
    df = pd.read_csv(infile)
    print ("Read CSV")
    html_content = df['html'].tolist()

    n_processors = 24
    x_ls = html_content

    results = run_multiprocessing(extractor, x_ls, n_processors)
    print("LE\r\n", len(results) ,flush=True)

if __name__ == "__main__":
    infile = sys.argv[1]
    
    freeze_support()   # required to use multiprocessing
    main()

