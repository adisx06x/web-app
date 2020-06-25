#!/bin/bash

set -euo pipefail

# Default url for ease of use
DEFAULT_URL="https://raw.githubusercontent.com/linuxacademy/content-elastic-log-samples/master/access.log"

url="${1:-$DEFAULT_URL}"

curl -sSL $url | awk '{ print $1 }' | sort | uniq
