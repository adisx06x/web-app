# Unique IP's Script

## Introduction

This small script curls a url, grabs all IP's, and sorts them. It also only keeps unique IP's.

### Getting started: Usage

You can run this script by simply running: `bash unique_ips.sh`

You can also specify the url on the command line.

```bash
bash unique_ips.sh URL_HERE
```

For example:

```bash
bash unique_ips.sh https://bit.ly/3hFzUzs
```

Or:

```bash
bash unique_ips.sh https://raw.githubusercontent.com/linuxacademy/content-elastic-log-samples/master/access.log
```

Caution: This script assumes all logs are the same and that IP's all start as the first field of the log file. On a different log file some form of regex can be a better choice. It also asssumes you're grabbing from URL and not a local file.

```shell
curl -Ss $url | grep -E -o "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)" | sort | uniq
```
