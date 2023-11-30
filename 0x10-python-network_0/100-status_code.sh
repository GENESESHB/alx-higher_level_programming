#!/bin/bash
# send a get request to a give url and desplay the response status code
curl -s -o /dev/null -w "%{http_code}" "$1"
