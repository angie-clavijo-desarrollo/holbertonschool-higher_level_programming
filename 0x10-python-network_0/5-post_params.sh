#!/bin/bash
#  cURL POST parameters
curl -sd "email=hr@holbertonschool.com&subject=I will always be here for PLD" -X POST "${1}"
