# SadQL
> I do not know whether I should say that or not, but you must bypass the login in any way, but remember that forcing does not always work. (Make Your Choice)

## About the Challenge
We were given a website (without the source code) and we need to bypass the login page


[Image extracted text: Login
Login Form
CYBER WARGAMES
Arad
Security Championship
Email
EmaillUsername
Password:
Password
Login]


## How to Solve?
At first I tried to change to add `[]` on each parameter to see the error message. First i want to test `email` parameter


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
[ sadql /
HTTP/1.1
HTTP/1-1
200
2 Host:
34
18
16-17
2 Dace:
Sat
Lug
2023 12.40.28
GHT
User-Agent
Hozilla/5
(Vindous
IT
10
Vine4 ;
264;
17:109
Gecko/FO1OO101
Server:
Apache/ 2 =
(Vine4)
OpenSSL/1-1It
PHP / 8 - 1.17
Firefox/115
X-Povered-By:
PHP /8 _
1.17
Accept
Cont ent
ength:
317
cexc/htrl
applicat
on / xhcaltxnl
applicat
on/xhl
47-0
9 ,image/avif
inage /vebp ,* /*;4-0
Conn
on:
close
Accept-Language
en-US
en ;
Cont ent -
Type
cexc
/htnl ;
charset=UTF -8
Lecept-Encoding:
gzip ,
deflace
Content-Type
applicat
on/ *-
UF
form-urlencoded
sbr
Content
Lengch:
Origin:
http: / /34
atal
error
Connect
on :
close
<b>
Re ferer
http
1/34- 18 _
16 _
17 /sadql/
Uncaught
TypeError:
addslashes ! :
Arcent
(sstring)
hust
be
of type
string,
12 Upgrade
Ins
cure-Requeses:
array
given
in
xanppx
hedocs
sadql index-php
Stack
crace:
email(ifcescepassvord-test
subnit-Login
xappx
hedocs
sadql
index-php ( 11 ,
addslashes (Array)
(main}
chroi
in
Kb >
C:xamppx htdocs
sadql
index
php
<b
on
line
<b>
Kfb
9F0 .]


As you can see, the source code use `addslashes()` function in email parameter, now lets try to add `[]` in the password parameter


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
Isadql/ HTTP/1.1
HTTP/1-1
200
Host :
34-
18
16
Dace
Sat
2023
13.43.46
GHT
User-Agent
Hozilla/5
(Vindous
HT
Vine4;
364;
rv:109
Gecko/ZO1OO1OI
Server
Apache/ 2 _
(Vine4)
OpenSSL/1-1.lt
PHP / 8 - 1 - 17
Firefox/115
X-Povered-BY:
PHP /8 -1.17
Accept
Cont ent -
Length:
303
cext/htrl
applicat
on / xhcultxul
application/xnl
9 ,image/ avif,inage /vebp ,* /*;4-0
Conneccion:
close
Accept-Language
en-US
en; 4F0
Cont ent
Type:
cert/html;
charset=UTF-8
1ccept
Encoding:
gzip
deflace
Content-
Type
applicat
on / *-U-form-urlencoded
<p1
Content
Lengch:
Origin
http
1/34
Fatal
error
Connect
on :
close
4b>
Referer
1/34 _
18 _
16-17/sadql/
Uncaught
TypeError:
md5 ( :
Ar cuent
(sstring)
must
be
of
type
string,
array
Upgrade
Ins
cure-Requeses:
given
in
C: xamppx
hedoes
sadql
index.php
13
Stacl
crace:
email-testEpassvord[ ]-test
subnic-Login
12
appx
hedocs
adql
index-php (121
nd5 (Array)
(main}
chrox
1n
C: xamppx htdocs
sadql
index-php
4/b>
line
4o>
</b>
<b1
Aug
4-0
hetp-]


And in the password parameter, the source code using `md5()` function. And I searched on google about SQL injection if the program using `addslashes()` and I found this useful [website](http://www.securityidiots.com/Web-Pentest/SQL-Injection/addslashes-bypass-sql-injection.html). So I added `%af` into the SQL injection payload


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
[ sadql /
HTTP/1.1
HTTP/1-1
200
Host
34
18.16-17
2 Dace:
Sat
Lug
2023 12:50; 36
GHT
User-Agent
Hozilla/5 - 0
(Vindous
IT
10
Vine4;
264;
17:109
Gecko/FO1OO101
Server:
Apache/ 2 =
(Vine4)
OpenSSL/1-1
lt
PHP / 8 . 1 -17
Firefox/115
X-Povered-By:
PHP /8 _
17
Accept
Cont ent
ength:
496
cexc/htrl
application/xhcnltxnl, applicat
on / xhl
47-0 ,9
image/ avif
inage /vebp ,* /*;4-0
Connect
on;
Accept-Language
En _
US
en ;
Cont ent -
Type
cert/htul
charset=UTF -8
1ccept -
Encoding:
gzip ,
deflace
Content
Type
applicat
on / *--form-ur lencoded
sbr
Concent-Lengch:
Origin:
http
1/34
Fatal
error
Connect
on :
close
<b>
Referer
http
1/34- 18 _
16.17/sadql/
Uncaught
nysqli
sql
except
on:
You have
error
in
your
SQL syntax;
check
che
Upgrade
Insecure-Requescs:
anual
chac
corresponds
your HariaDB
server
Version
for
che
right
syntax
0
4se
near
crue-
AI
passuord
098fEbcd46214373cade4e83262764f6
line
1n
enail-taf
crue
Fpassword-cestesubnit-Login
xacpp%
hcdocs
sadql
index-php
Stacl
crace:
xappx
hedocs
sadql
index-php ( 15 |
Lysqli
query (Object (#ysqli) _
SELECT
FROH
(hain}
throw
in
C:xanppx hedocs
sadql
index-php
Kfb>
on
line
15
4/b>
Sbr
close
4=0]


But that's weird, why the website output was like this?

```
:  Uncaught mysqli_sql_exception: You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'true---' AND `password`='098f6bcd4621d373cade4e832627b4f6'' at line 1 in C:\xamppx\htdocs\sadql\index.php:15
```

It looks like there are another filter that we needed to bypass again. I tried to stack the query, so for example from `or` to `oorr` and I changed the space into `/**/`. And in the end we also need to change the comment from `-- -` to `#`


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
[sadql/
HTTP/1.1
HTTP/ 1-1
200
Host :
34
18
16
17
2 Date:
Fri
Lug
2023
18:12.43
GHT
User-Agent
Hozilla/5
(Vindous
IT
10.0;
Vin64;
{64;
17:109
Geclo/:O100101
Server:
Apache/ 2 _
(Vin64)
OpenSSL/I-1It
PHP / 8 - 1.17
Firefor/115
X-Povered-By:
PHP / 8 _
Aecept
Content
engch:
2117
cext / html
applicat
on / xhthltxul , applicat
on/ <ul
F0
image / avif
1nage /vebp
1*{9=0
Connection:
close
Content -
Type
cexc/henl;
charset-UTF-8
Lccept-Language
en-US
en ;
Aecept
Encoding:
szip
deflace
aduinlSCVG
SqL_INj 3ctlon
1s
VaBy_Esay_AId_Funyyyyry! } < !DOCTTPE
hcml?
Content
Type
applicat
on / *-IU -
IorMcUL
encoded
10
chtml>
Content-
Lengch:
shead>
Origin:
http: / /34
17
<neta
charset=
u f-8 "
Connect
on:
close
scitle>
Re ferer: http
1/34 _
18_
16-17/sadql/
Login Page
Upgrade
Ins
cue-
Requests:
<[cicle
style>
emailstaf
1**[oorr/t* /true
Epassvord-dasubnit-Login
15
body (
16
background-color
Ff7f7f7;
font
fahily:sans
serif;
18
19
container {
max-vidth: 40Opx
margin: SOpxauco
padding: ZOpx
23
background-color
#fff;
24
border
adius
Spx
25
box-shadou
OO1Opxrgba(0
0,0,0.21
26
9-0]


```
adminASCWG{SqL_1Nj3ct1on_1s_V3Ry_Esay_ANd_Funyyyyyy!}
```