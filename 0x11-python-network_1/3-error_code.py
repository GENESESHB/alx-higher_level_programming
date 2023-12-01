#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL and
    displays the body of the response (decoded in utf-8), manages
    the exceptions.
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as resp:
            data = resp.read().decode('utf-8')
            print(data)

    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
