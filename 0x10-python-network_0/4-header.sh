#!/bin/bash
# takes in a URL as an argument send a GET request to the URL , and dsplay the body the response
curl -sH "X-School-User-Id: 98" "$1"
