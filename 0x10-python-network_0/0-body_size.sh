#!/bin/bash

# Send a request to the provided URL and display the size of the body of the response in bytes
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
