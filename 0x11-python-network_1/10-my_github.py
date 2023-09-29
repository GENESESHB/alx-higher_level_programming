#!/usr/bin/python3
"""show id of an user in github"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    login = requests.get('https://api.github.com/user', auth=(username, token))
    print(login.json().get("id"))
