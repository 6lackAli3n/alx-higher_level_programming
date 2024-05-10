#!/bin/bash
# Send a request to the provided URL
curl -s "${1}" | wc -c
