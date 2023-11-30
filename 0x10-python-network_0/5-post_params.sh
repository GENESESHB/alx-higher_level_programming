#!/bin/bash
#takes in the url sends a POST request to the possed URL and dispaly the body of response
curl -s "$1" -X POST -d "email=test@gmail.&subject=I will always be here for PLD"
