#!/bin/bash
# Execute curl, display the available methods for the URL
curl -s -I "$1" | grep -P "Allow:" | cut -c 8-
