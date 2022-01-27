import pandas as pd
from multiprocessing import freeze_support, Pool, Value
import requests
import zlib
import base64
import sys
import socket

timeout = 3
progress = Value('i', 0)
failed = Value('i', 0)


def run_multiprocessing(func, i, n_processors):
    with Pool(processes=n_processors) as pool:
        return pool.map(func, i)


def run_multiprocessing(func, i, n_processors):
    with Pool(processes=n_processors) as pool:
        return pool.map(func, i)


def request_page(domain):
    try:
        r = requests.get("https://" + domain, timeout=timeout,
                         allow_redirects=True)

        return {
            "url": r.url,
            "status_code": r.status_code,
            "html": base64.b64encode(zlib.compress(r.text.encode('utf-8'), 9))
        }

    except:
        try:
            r = requests.get("http://" + domain, timeout=timeout,
                             allow_redirects=True)

            return {
                "url": r.url,
                "status_code": r.status_code,
                "html": base64.b64encode(zlib.compress(r.text.encode('utf-8'), 9))
            }
        except:
            failed.acquire()
            failed.value += 1
            failed.release()
            return {
                "url": "fail",
                "status_code": 0,
                "html": ""
            }
    finally:
        progress.acquire()
        progress.value += 1
        progress.release()
        print("Failed:", failed.value, " Total:",
              progress.value, end="\r", flush=True)


def main():

    df = pd.read_csv(infile)

    domains = df['domain'].tolist()

    n_processors = 24
    x_ls = domains

    results = run_multiprocessing(request_page, x_ls, n_processors)

    final_df = pd.DataFrame(results)
    final_df.to_csv(outfile)

    print("Failed:", failed.value, " Total:",
          progress.value, end="\r", flush=True)


if __name__ == "__main__":
    infile = sys.argv[1]
    outfile = sys.argv[2]
    timeout = int(sys.argv[3])

    freeze_support()   # required to use multiprocessing
    main()
