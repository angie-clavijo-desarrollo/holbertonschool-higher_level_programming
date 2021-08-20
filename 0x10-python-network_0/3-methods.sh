#!/bin/bash
#  cURL method ALL
curl -sI "${1}" | grep Allow
