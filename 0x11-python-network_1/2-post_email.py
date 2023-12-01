#!/usr/bin/python3
"""a Python script that takes in a URL and an email,
    sends a POST request to the passed URL with the email
    as a parameter, and displays the body of the response
    (decoded in utf-8).
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    data_encoded = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url, data=data_encoded, method='POST')
    with urllib.request.urlopen(request) as response:
        response_data = response.read().decode('utf-8')
        print(response_data)
