#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        payload = {'q': sys.argv[1]}
        r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    else:
        print("No result")
