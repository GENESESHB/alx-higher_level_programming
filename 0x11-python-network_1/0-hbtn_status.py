#!/usr/bin/python3
"""a script that fetches https://alx-intranet.hbtn.io/status"""
from urllib.request import urlopen

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urlopen(url) as response:
        response_content = response.read()
        response_type = type(response_content)
        response_utf_content = response_content.decode('utf-8')
    print("Body response:")
    print(f"\t- type: {response_type}")
    print(f"\t- content: {response_content}")
    print(f"\t- utf8 content: {response_utf_content}")
