#!/usr/bin/python3
""" a Python script that takes in a URL, sends a request to the
    URL and displays the value of the X-Request-Id variable
    found in the header of the response.
"""
import requests
import sys

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        resp = requests.get(url)
        x_request_id = resp.headers.get("X-Request-Id")
        print(x_request_id)
    except Exception as e:
        print(f"An error occurred: {e}")
