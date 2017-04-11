#!/bin/bash
# Execute curl with a POST request containing some information
curl -s -d 'email=hr@holbertonschool.com' -d \
    'subject=I will always be here for PLD' "$1"
