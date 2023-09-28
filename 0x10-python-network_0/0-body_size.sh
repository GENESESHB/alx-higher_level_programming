#!/bin/bash
# takes in a URL, sends a request to that URL, displays the size of the body of the response
# curl: This is the command used to make HTTP requests.
# -s: This option stands for "silent" mode, which makes curl operate in a quiet mode, suppressing unnecessary output.
# -I: This option tells curl to fetch only the HTTP headers of the response, not the body.
# GET "$1": This specifies the HTTP method (GET) and uses the first command-line argument ($1) as the URL to request.
# |: The pipe symbol (|) is used to pass the output of one command as input to another.
# grep: This command is used to search for text patterns within the input.
# -i: This option makes grep perform a case-insensitive search.
# "Content-Length": This is the text pattern that grep is searching for in the input. It's looking for the line that contains the text "Content-Length."
# cut: This command is used to extract specific parts of each line of input.
# -d " ": This option specifies that the delimiter used to separate fields is a space.
# -f2: This option tells cut to extract the second field (word) from each line of input. In this case, it extracts the value of the "Content-Length" header, which represents the size of the response body.

curl -sI GET "$1" | grep -i "Content-Length" | cut -d " " -f2
