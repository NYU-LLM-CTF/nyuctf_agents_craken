# Auth
> I just started learning about a new authentication method called JWT. This is my first website with it, could you check if its secure?

## About the Challenge
We were given a plain website and we need to find the flag there


[Image extracted text: 213.133.103.186.6400/
213.133.103.186.6400
Getting Started
#519502 Name Link B
#927384 Race Conditi_.
#502758 RCE and Co.
ExpE
username or
password; register using /register and the username and password params
Wrong]


## How to Solve?
First, we need to create an account by using the `/register` endpoint.


[Image extracted text: 213.133.103.186.6400/register?usern X
213.133.103.186.6400/register?username=
&password-testing
Getting Started
#519502 Name Link B.
#927384 Race Conditi_.
#502758 RCE and Co_
Exploit Database
Ex _
User created
-testinge]


And then login again and you will see JWT token on the HTTP response body


[Image extracted text: Request
Response
Pretty
Raw
Hex
Pretty
Raw
Hex
Render
GET
HTTP / 1.
HTIP/11
200
OK
Host :
213
133-103
186: 6400
X-Povered-By:
Express
User-Agent
Hozilla/5
(Vindous
IT
Vin64;
{64;
rv:109
Gecko/:O1OO101
Info
check
info
Firefor/1l1
Content
Type
cext /htnl ;
charset-ut f-8
Accept
Content
Lengch:
133
ext /htzl
applicat
on / xhcultxul
application/xnl
4F-0
9 , image/ avif ,inage /vebp ,* /*;4F-0
ETag:
0/
85-34Arcao8qhvBUhEfT4G30c1HBcl:"
Aecept-Language
en-US
en;4-0 -
Dat e
Sun ,
09
ApI
2023
15 : 50:13
GHT
Accept
Encoding:
gzip
deflace
Connect
on -
close
Authorizat
on =
Basic
dGVzdGluzzpOz MOalSn
Connect
On -
close
eyJhbGcidiJIUzIlMilsInRSCCIGIlpXVCJ9
eyJ[c-VybnFtZSIGInBle3PpbnciLCJprxoi JEZODE-NTUOH
ade
Ins
cure-Ree
quests:
LPrHQOtoEqziJYUUID_IWE-vrCWijjg-hESLGcThhFO
Upgr =
INS _]


Copy that JWT token, and then try to brute-force the key from the token (Without the key, we won't be able to modify the token's contents). In this case im using this [tool](https://github.com/Sjord/jwtcrack) (Especially `jwt2john` script). Im using this command to bruteforce the JWT token

```shell
python3 jwt2john.py eyJ...... > hash.txt
john -w=/usr/share/wordlist/rockyou.txt
```

First, we need to convert the JWT token to john format, and then johntheripper will bruteforce the token


[Image extracted text: (kaliokali)-[~/Tools/ jwtcrack]

python3 jwtzjohn.py eyJhbGci0iJIUZIINiIsInRScCI6IkpXVC J9.eyJlc2VybmFtZSI6InRlc3QiLCJpYXQiojEZODA4OTABMjh9 . OBkpmOpWOZseyZrVniBp-ZuwIS2rGKd4a9INFmVhzVU
hash
txt
(kaliokali)-[~/Tools/ jwtcrack]

john
~Welusr
Share/wordlists/rockyou
txt
hash
txt

Created directory
/home/kalil . john
Using default input encoding
UTF-8
Loaded
password
hash (HMAC-SHA256 [password is
SHA256 128/128
AVX 4x])
Will
run
OpenMP
threads
Press
or Ctrl-C
abort ,
almost
any other key for
status
1
s3cret
(2)
0:00
00 DONE (2023-04-07 14:10) 2.127g/5 2823Kp/s 2823Kc/s 2823KC/s sackhead
rxygurl
Use the
show"
option
to display all of
the cracked passwords reliably
Session
completed_
3
key,]


After that, we know the key is `s3cret`. Now use https://jwt.io to change the username to `admin` and then set the key in the `VERIFY SIGNATURE` section


[Image extracted text: Encoded
PASTE _
TOKEN HERE
Decoded
EDIT THE PAYLOAD AND SECRET
HEADER: ALGORITHM & TOKEN TYPE
eyJhbGciOiJIUZIINilsInRScCI6IkpXVCJ9 .ey
JIcZVybmFtZSI6ImFkbWluliwiaWFOIjoxNjgxM
"alg'
'HS256"
DU1MTcwfQ. ZqnlQIn2pUDAtWTI8kgvQwUMFccsf
'typ
JWT
uleqLZOaJkxG8E
PAYLOAD: DATA
username
admin
'iat
1681055170
VERIFY SIGNATURE
HMACSHA256
base64UrlEncode(header)
base64UrlEncode (payload)
s3cret
secret base64
encoded]


You will notice in the HTTP response header there is a header called `Info` and in the header written we need to access `/info` endpoint


[Image extracted text: Response
Pretty
Raw
Hex
Render
HTTP/ 1. 1
200
OF
X-Povered-By:
Express
Info
chec}
linfo
Content
Type
text /htul
charsetzut €-8
Content
Lengch
133
ETag:
D/
85-341rcao8qhuBUffT4G30clHBcl
Dat e
Sun ,
09 Apr
2023
15 : 50:13
GHT
Connection-
close]


and then in the HTTP response body we need to access `/validate` endpoint also we need to provide the JWT token that we have signed before


[Image extracted text: Response
Pretty
Raw
Hex
Render
HTIP/11
200
OK
X-Povered-By:
Express
Content
Type
exc /hcnl
charset-ut f-8
Content
ength:
ETag:
V/ E
zZnvTvZei4RfPgk UjkHUdjG81v4
Date
Su 
09
Lpr
2023
15: 59:23
GIT
Connect
on :
close
check
che /validace
rout =
use
Eoken
che
query
Paran]


Now, go to the `/validate` endpoint and add the JWT token to the `token` parameter in order to obtain the flag.


[Image extracted text: 213.133.103.186.6400/validate?toke
213.133.103.186.6400/validate?token=eyJhbGciOiJIUzl  NilsInRScCl6IkpXVCJ9 eyJIc2VybmFtZSiGImFkbWluliwiaWFOljoxNjgxMDUIMTcwfQ ZqnlQlnZpUDAtl
Getting Started
#519502 Name Link B_
#927384 Race Conditi_.
#502758 RCE and Co_
Exploit Database
Ex .
Vulnerable Android Br_
#289000 Vulnerable e_
Android App Security
bucket{1_lOv3_jwtW!lll!}]


```
bucket{1_l0v3_jwt!!!1!!!!1!!!!!1111!}
```