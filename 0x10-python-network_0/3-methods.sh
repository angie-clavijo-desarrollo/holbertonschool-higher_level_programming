#!/bin/bash
#  cURL method ALL
curl -sI -X OPTIONS "${1}" | grep "Allow:" | cut -d " " -f2-
