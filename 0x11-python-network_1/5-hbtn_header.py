#!/usr/bin/python3
"""Show X-Request-Id using requests"""
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
