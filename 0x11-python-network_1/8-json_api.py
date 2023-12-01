#!/usr/bin/python3
""" a script that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a
    parameter.
"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': q}
    try:
        r = requests.post(url, data)
        json = r.json()
        if json:
            print(f"[{json.get('id')}] {json.get('name')}")
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
