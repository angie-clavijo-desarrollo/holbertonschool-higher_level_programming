#!/bin/bash
#  cURL POST parameters
curl -s -o /dev/null -I -w "%{http_code}" "$1"