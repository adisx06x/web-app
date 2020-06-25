# Containerized Web Application

## Introdcution

This app uses Nginx and directs all traffic to a Flask app.

### Getting started

`git clone`

`docker-compose up`

To test app, go to your browser: `https://localhost`

You can also use curl: `curl -i -k -L http://localhost` using the same options to see a full output and redirection.

```HTTP/1.1 301 Moved Permanently
Server: nginx/1.19.0
Date: Thu, 25 Jun 2020 01:17:10 GMT
Content-Type: text/html
Content-Length: 169
Connection: keep-alive
Location: https://localhost/

HTTP/1.1 200 OK
Server: nginx/1.19.0
Date: Thu, 25 Jun 2020 01:17:10 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 73
Connection: keep-alive
```

## TODO

This app needs CI:

- 
