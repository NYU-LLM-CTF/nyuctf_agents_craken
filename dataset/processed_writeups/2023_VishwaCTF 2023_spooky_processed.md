# spooky
> I forgot my login credentials again!!

## About the Challenge
We were given a website that has a login form


[Image extracted text: Username
Password
LOGIN]


## How to Solve?
I have trying every single payload to bypass the admin login (SQL and NoSQL) and the result is nothing. And then my friend, @DimasMaulana found an interesting endpoint called `sitemap.xml`


[Image extracted text: This XML file does not appear to have any style information associat
urlset >
Curl>
<loc>Icredslusers.txt<Iloc >
<lastmod-2023-03-29T09:12.48+01.00</lastmod >
~priority>1.0<Ipriority>
url>
url>
<loc>Icredslpass txt< /loc>
<lastmod>2023-03-29T09:12.48+01.00</lastmod>
<priority>1.0<Ipriority>
clurl>
<lurlset >]


As you can see, we found another endpoint that contain users and password.

### User:
```
user
guest
root
admin
kali
raspberry
support
fiona
charles
alice
pinocchio
shrekop
dragon
donkey
wolf
```

### Pass:
```
R4YPLtCnaMc8GhWy
fX9maZjLNdqKG8wH
r6GUEungvhXqVFyY
WZLNBAdkXc6Yu8rh
ny7Z2jpMT36CBwLH
VmU5gnXKYN2vLp48
VGUtajxuq6KeNk5J
XZTEVmd6AcFN3j84
ydfkG8YS7WMwpQNC
emcYJrGFVMakw5UN
G9fBSNbgmhTduKEU
KctkRurdy4vSMGWF
Ggc6qyrVdDzWhEea
DKaYNZug9ELCzRAy
NwCGR69ZceHu8tmT
```

Im using that username and password wordlist to bruteforce the form and we got 1 correct combination

```
User: shrekop
Pass: VmU5gnXKYN2vLp48
```

Now we can login to the web, but we still didn't get the flag.


[Image extracted text: 7
C
https://ch39906117599.ch eng run/login php
Getting Started
#519502 Name Link B.
#927384 Race Conditi_.
#502758 RCE and Co_
Logged in as
shrekop (user)]


As you can see the role is `user`. We need to do privilege escalation from `user` to `admin` roles. To do that, when we login to the website, add `admin` parameter and the value is `true`


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
HTTP / 2
200
OK
2 Host:
ch39906117599
eng
FLT
Date
Sun ,
0_
Apr
2023
10: 02:22
GIIT
User-Agent
Hozilla/ 5
(Vindous
IT
Vin64;
{64;
17:109
Geclo/:O100101
Content-
Type:
text/hcal
charset-UTF-8
Firefor/1ll
Content
Lengch
148
Aecept
Server:
nginx/ 1
23 .
cext / html
applicat
on / xhcmltxnl
applicat
on/ *ul
F0
1mage/
inage /vebp ,* /*{9=
X-Povered-By:
PHP / 7
0 -33
0 . 8
Vary: Accept
Encoding
Lccept-Language
en-US
en ;
Aecept
Encoding:
szip ,
deflace
Content
Type
applicat
on / *-IU -
IorMcUL
encoded
Logged
1n
Content-
Lengch:
So>
Origin
https: / /ch39906117599_
ch
eng
rt
shrelop
aduin
<script>
Re ferer
https: / /ch39906117599
eng
run/
alert
Congratulations
Tou
che
flag!
Upgrade
Ins-
Cure=
Requests:
script>
Sec--
etch-Dest
docuent
script
Sec--
etch-
Hode
navigate
alert
VishuaCTF (hldd3n
P@ralIs}
2 ;
Sec-
etch-Sice
gin
script>
Sec-Fetch-User:
16
Te:
crailers
user
shrekopepass-VnUS gnXKIEvLp48€ adnin-truel
401
4-0
Sot
a]


```
VishwaCTF{h1dd3n_P@raMs}
```