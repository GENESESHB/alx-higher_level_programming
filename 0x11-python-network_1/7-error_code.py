#!/usr/bin/python3
""" Show status code in request """

import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])

    if 400 > r.status_code:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
