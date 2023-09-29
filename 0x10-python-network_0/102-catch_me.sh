#!/bin/bash
# This script sends a POST request to 0.0.0.0:5000/catch_me causing the server to respond with "You got me!"
curl -sLX POST 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin:  X-School"

