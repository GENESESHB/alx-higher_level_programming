#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status."""
import urllib.request


url = 'https://intranet.hbtn.io/status'
request = urllib.request.Request(url)
request.add_header('User-Agent', 'Mozilla/5.0')

try:
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print(f"HTTPError: {e}")
