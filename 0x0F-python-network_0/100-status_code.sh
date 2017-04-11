#!/bin/bash
# Execute curl and display the response code
curl -s -o /dev/null -w "%{http_code}" "$1"
