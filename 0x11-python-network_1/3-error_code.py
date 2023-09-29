#!/usr/bin/python3
"""  using Except in request """

import urllib.request
from sys import argv

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            html = response.read().decode("UTF-8")
            print(html)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
