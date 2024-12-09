# Cookie
> I have a trade offer for you. The challenge is at https://cookies.acmcyber.com

## About the Challenge
We need to find the flag on the website We were given. The website is just a plain website and there is a button to get the cookie


[Image extracted text: normal website
TRADE OFFER
i receive:
you receive:
a cookie
a
flag]



[Image extracted text: go to
for your flag
imgflip com
get cookiel
Iflag]


## How to Solve?
I tried to click the `get cookie!` button and then there is a new cookie on HTTP request


[Image extracted text: cache-control: max-age
cookie:
secret-687
if-modified-since: Mon,]


And then in the one of the image said that I need to go to `/flag` endpoint to get the flag. But when I open that there is just a simple message

```
icky cookie
```

I stuck a little bit and decided to try changing the cookie value from 1 - 75 and luckily I got the flag


[Image extracted text: 2uu
236
33
200
236
35
200
236
35
200
236
36
200
236
37
200
236
38
200
236
200
247
40
200
236
200
236
43
42
200
236
200
236
45
4
200
236
45
200
236
46
200
236
200
236
48
200
236
200
236
50
200
236
52
200
236
52
200
236
200
236
54
200
236
J30
Request
Response
Pretty
Raw
Hex
Render
HTTP / =
200
OK
Lt-Svc:
h3=
443"
ma-_s9_000
Content
Type
text/hcnl
charsetsut f-8
Dat
Thu 
0_
Har
2023
07: 40:12
GIIT
Etag:
V/ "15-#iXR / d8n8ikAHnG} Sh #BnStzk
Server
Caddy
X-Powered-By:
Express
Content
Lengch:
flag(c00k135_
gO_brrr}]


```
flag{c00k135_g0_brrr}
```