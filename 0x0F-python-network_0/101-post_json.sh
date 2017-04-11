#!/bin/bash
# Execute a curl POST request using data from a file in argument #2
curl -H "Content-Type: application/json" -d @"$2" "$1"
