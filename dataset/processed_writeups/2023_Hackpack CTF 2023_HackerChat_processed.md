# HackerChat
> HackerChat is the hottest new chat app for hackers. Can you recover the secret message sent to the HackerChat admin?

## About the Challenge
We are given a website that has multiple functionality such as send msg to another user, login, register, etc.


[Image extracted text: HackerChat
Home
Register
Login
Dashboard
Welcome to HackerChat]


## How to Solve?
Register first and then login to the website and you will see this page


[Image extracted text: HackerChat
Home
Register
Login
Dashboard
Inbox
Profile
Recipient:I
Message]
Send
Username:
testim
Role:
member
Date created:
2023-04-15 16.16.29]


You will notice there are 2 API endpoints when accessing dashboard page
* /api/chat
* /api/search

There is a SQL injection vulnerability on `/api/search` endpoint on `search_term` parameter. Input `' or true--` in that parameter to print all the user information


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
[apilsearch
HTTP / =
usernane
Ghost InShell"
Host
hackerchat
cha-haclpack_
club
Cookie
access
Coken=
eyJhbGcidiJIUzIlMilsInRScCIGIlpXVCJ9
eyJzdulioiJOzxlOallplivizxhuIjoxIJgxITgYODI-LCJpY
date
created"
2023-04-05
12: 56:18"
xQiOjEZODEIIzU2Hjz9
PFLSKAUF
1OOHZRxYziYst_PuIxOUX2ozY4Opualk
id":null
User
Agent
Hozilla/5
(Vindous
IT
Vin64 ;
364;
rV: 109
Gecko/ZOlOO1ol
notes
Firefox/lll
Password"
null
Accept :
role
member
Accept-Language
en-US
en;
UCernAne
"Blacl Hatlinja"
Lecept-Encoding:
gzip
deflace
Re ferer
https:
[hackerchat
cha hackpack
club / dashboard
Content
Type
app
Cat
on /
son
date
created"
2023-04-05
13.27: 51"
Authorizat
on =
Bearer
id"
null
eyJhbGcioiJIUzI NilsInRScCIEIlpXVCJ9.eyJzduliOiJOz lOallpliviz ivIjoxlJgxITgYODI-LCJpr
notes
xQiOjEZODEINzUZHjz9
PFISKAUF_
OOHZRxYzirstZPvIxOUUXzoZT4Opvalk
Password"
null
Content
Lengch:
role
member
Origin:
https:
{hackerchat
cha haclpacl:
club
usernae
"CyberPunk404"
Sec--
etch-
Dest
empty
Sec-
etch-Hode
cors
Sec-
etch-Sice
sae
origin
date
created"
2023-04-10
14.20:45 "
crailers
id"
null
notes
secret
reminder:
8vqB Sxhr TdPzPDXpSpOTYSoTB3ExpZJdrsFGn /hc/YE="
Password
null
search
term
true-=
role
adu1n
UCernAne
adnin"
date
created"
2023-04-14
22: 53:27"
id"
null
notes
Password"
null
role
member
usernae
date
created"
2023-04-14
22: 53: 57"
id"
null
notes
Password"
null
role
'member"
ne A
Seorcni
matches
Seorcne
matches
4-0
JA
aa]


As we can see, we found admin username and there is an interesting notes there

```
secret reminder: 8vqB5xhrTdPzPDXpSpOTY3oTB3ExpZJdrsFGm/hq/yE=
```

The `secret reminder` refers to the JWT secret, which is required in order to modify the value of the `Authorization` token from your username (For example testiiii) to `admin`


[Image extracted text: Encoded
PASTE A TOKEN HERE
Decoded
EDIT THE PAYLOAD AND SECRET
HEADER: ALGORITHM & TOKEN TYPE
eyJhbGciOiJIUZI NilsInRScCI6IkpXVCJ9 . ey
JzdWiOiJhZG pbiIsImV4cCI6MTYAMTUAMjgyN
alg"
'HS256 "
iwiaWFOIjoxNjgxNTc1NjIZfQ.MQ4Rowtq3aCXL
'typ'
JWT
LHvMBtJEY1459pEHOdySBX3MEOog0
PAYLOAD: DATA
sub"
admin"
exp"
1681582826
'iat"
1681575626
VERIFY SIGNATURE
HMACSHA256
base64UrlEncode( header)
base64UrlEncode(payload) _
8vqBSxhrTdPzPDXp SpoTy:|
secret
base64
encoded]


Now, go to `/api/chat` history and don't forget to change the `Authorization` token and voilà you will obtain the flag


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
[apilchat
HTTP / =
HTTP / 2
200
Or
Host
hackerchat
cha-hackpack
club
Content
Type
applicat-
on/ Json
User-Agent
Hozilla/5
(Vindous
IT
0; Vin64 ;
*64;
rv:109
Gecko/:O1OO101
Dat
Sat
15
ApI
2023
16: 26: 39
GHT
Fire
(11
Server:
nginx/ 1
Accept
applicat
on/json,
Eext/plain,
77"
Content
Lengch:
158
Lccept-Language
En
US
en ;
Aecept
Encoding:
szip
deflace
Luthorizat
on -
Bearer
eyJhbGcidiJIUzIlNilsInRScCIEIFpXVCJ9. eyJzdWlioiJhZGlpbilsInV4cCIEHTT4HTUAHjgyliviaWFOI
messages
oxMjgxMTcINjISfQ
HOARGvt q3aCXLLHvIt JEY114SSp EHOdySBXZMEOogo
Re ferer
https:
[hackerchat
cha hackpack
club
dashboard
dat e
2023-04-10 18:27:47"
Sec-
etch-Dest
empty
recipi
adhin
Sec--
etch-Hode
cors
"cext
Elag{Unbr341-4613
Chlt
S3curity_ulu_flgla}
Sec--
etch-Sice:
5ae
origin
usernane
aduin"
crailers
recipient
adhin
fox
9-0
ent]


```
flag{Unbr34k4bl3_Ch@t_S3curity_uWu_2lgla}
```