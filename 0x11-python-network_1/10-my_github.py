#!/usr/bin/python3
""" a script that takes your GitHub credentials
    (username and password) and uses the GitHub API
    to display your id
"""
import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    url = "https://api.github.com/user"
    session = requests.Session()
    session.auth = (user, pwd)
    r = requests.get(url=url, auth=session.auth)
    print(f"{r.json().get('id')}")
