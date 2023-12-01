#!/usr/bin/python3
""" a Python script that takes in a URL, sends a request to the
    URL and displays the value of the X-Request-Id variable
    found in the header of the response.
"""
from urllib.request import urlopen
import sys

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        with urlopen(url) as resp:
            x_request_id = resp.getheader("X-Request-Id")
            print(x_request_id)
    except Exception as e:
        print(f"An error occurred: {e}")
