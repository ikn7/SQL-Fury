import httpx
import sys
import time

##### YOU CAN CHANGE THIS #####

timeout = 2 # Timeout for HTTP requests
wait = 0 # Time to sleep after each request

##### PROGRAM #####
def test_sql(url):
    test_url = url.replace("=", f"='\"")

    try:
        r = httpx.get(test_url, timeout=timeout)
    except httpx.HTTPError as e:
        print(f"\033[91m[ERROR]\033[0m - {test_url} {e}")
        return

    if "sql" in r.text:
        print(f"\033[92m[SQL FOUND]\033[0m - {test_url}")
    else:
        print(f"\033[91m[+]\033[0m - {test_url}")

    time.sleep(wait)

if __name__ == "__main__":
    for line in sys.stdin:
        url = line.strip()
        if not url.startswith("http"):
            print(f"\033[91m[ERROR]\033[0m - '{url}' IS INVALID !")
            continue
        elif "=" in line:
            test_sql(url)

