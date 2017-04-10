#!/bin/bash
# Display length of response body
curl -o /dev/null -s -w "%{size_download}\n" "$1"
