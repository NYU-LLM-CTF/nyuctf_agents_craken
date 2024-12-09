# Pollution
> Flag is on the admin side.

## About the Challenge
Given a website file along with the source code (You can get the source code [here](web_pollution_fix.zip)). On the website there is 1 endpoint named `/register` where if we can set the role to Admin and we know the secret web, then we can get the flag


[Image extracted text: Register
here!
Usenname
admin
Secrel
admin
Submit
Wrong secret!
no Admin!]


## How to Solve?
To solve this chall, according to the title we have to do a pollution prototype. By using this reference https://portswigger.net/web-security/prototype-pollution, the request will look like this


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
[register HTTP/l-1
HTTP/ 1.1
200
OF
Host
103
52-242
116.4137
X-Povered-By: Express
User-Agent
Hozilla/ 5
(Vindous
IT
10
Vin64;
{64;
17:109
Geclo/:O100101
Content
Type
applicat_
on/Json;
charset-uc f-8
Firefor/1l0
Content
Length:
Aecept
ETag:
V/
4d-/TbgE/ InLiEYqu-UOFMF8IxCi8"
ext /html
applicat
on / xhtaltxnl
application/xnl;q-0
image / avif
inage /vebp ,* /*;4F-0
Date
Su ,
26
Feb
2023
11.49.42
GHT
Accept -
aguage
en-US
en;
Connection:
close
1ccept-
Encoding:
gzip ,
deflace
Connect
on:
close
Upgrade
Ins
cure
Requests:
message
Here
your
flad!
Content-
Type
ext/plain
secret
APA2023 {e4sy_Pro70typ3_pOllutloll}
Content
Lengch:
0c0
usernane
"cest
cret
testh
role
Ldnin "
4-0
SPr]


```
ARA2023{e4sy_Pro70typ3_p0llut1oN}
```