# Containerized Web Application

## Introdcution

This app uses Nginx and directs all traffic to a Flask app.

### Getting started

`git clone`

`docker-compose up`

To test app, go to your browser: `https://localhost`

You can also use curl: `curl -i -k -L http://localhost` using the same options to see a full output and redirection.

```
HTTP/1.1 301 Moved Permanently
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

You can also use `curl -H "User-Agent: h4ck3r" -i -k -L https://localhost` to test user agent defined as h4ck3r.

```
HTTP/1.1 403 FORBIDDEN
Server: nginx/1.19.0
Date: Thu, 25 Jun 2020 01:34:39 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 234
Connection: keep-alive

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>403 Forbidden</title>
<h1>Forbidden</h1>
<p>You don't have the permission to access the requested resource. It is either read-protected or not readable by the server.</p>
```

## TODO

This app needs CI:

- 
