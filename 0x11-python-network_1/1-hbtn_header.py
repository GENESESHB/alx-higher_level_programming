#!/usr/bin/python3
"""
sends a request to a url and display the value of the X-Request-Id
variable found in the header of the response
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        x_request_id = response.info().get('X-Request-Id')
        print(x_request_id)
