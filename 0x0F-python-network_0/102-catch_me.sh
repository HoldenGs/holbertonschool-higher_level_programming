#!/bin/bash
# Execute a curl request that receives a specific message
curl -X PUT -L -H 'Origin:HolbertonSchool' -d 'user_id=98' 0.0.0.0:5000/catch_me
