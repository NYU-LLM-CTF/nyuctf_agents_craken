# WxMCTF Web 2 - Restricted Access
> Legend has it that WLMAC has a super duper secret website, currently being used to plot attacks against MGCI...

> Access the challenge right here: https://weba.jonathanw.dev:3002/

## About the Challenge
We were given a website and we need to change some headers to get the flag


[Image extracted text: Welcome to the SUPER SECRET WLMAC SITE
But wait__you dont look like a lyonbrowser user to me]


## How to Solve?
First, you need to change the `User-Agent` header to `lyonbrowser`


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
HTTP/1-1
padding: :Opx
Host :
Veba-
onathanv
dev: 300_
margin: aut 0
User-Agent
lyonbrovser
26
hl
line
cht
len
input
bucton
textarea(
Padding: Spx ;
font
size
Zpx ;
border: lpxsolidgray;
forn
line
height
len
hr
border:0;
border-top
lpxsolidgray;
style>
fhead>
<body>
<hl>
Velcone
co
che
SUPER
SECRET
FLILLC SITE
</hl>
<h3>
But
walt
ulmac
People
Colne
from
the
maclyonsden_
Com
vebsite,
are YOu
spy?
</h3>
</body>
(hcnl>
Seorcn;
0 matches
Seorcn;
matches
Fhei]


And then you need to add a header called `Referer` and the value is `https://maclyonsden.com/`


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
HTTP/1-1
22
padding: ZOpx
2 Host
Veba
Jonachanv
dev: 3003
23
margin
aut 0
User-Agent
lyonbrovser
Referer:
https:
[maclyonsden
con/
hl
line-height
len ;
28
29
input
bucton
textarea(
padding
Spx
font-
size
Zpx ;
border
lpxsol
dgray;
forn (
line-height
len
hr
border
border
Ipxsolidgray;
style>
~[head>
~hody>
<hl>
F-lcon=
che
SUPER
SECRET
WLILLC
SITE
</hl>
<h3>
But
Jaic
You
are
bere
hortal
Jho
liv-s
in
che
presenc
Are
divin-
beings living
10
Years
the
fucure
are
not
the
se
</h3>
~/body>
~hehly
Sarch 
matches
Sarch 
matches
~cop"]


And then you need to add a header called `Date` and the value is `2043`


[Image extracted text: Request
Response
Pretty
Raw
Hex
Pretty
Raw
Hex
Render
~I
GET
HTTP/1-L
max-Jidch: [20Opx;
Host
veba-jonathanv
dev: 3003
22
Padding: ZOpx
User-
Agent
lyonbrovser
margin: aut o
Re ferer: https:
[maclyonsden
Cm
Date
2043
25
26
27
line-height : len;
28
29
input
button
textarea(
padding: Spx
fonc
size:
Zpx ;
border
Lprsol
dgray;
forn {
line-height
len;
hr {
border:0;
border
lpxsolidgray;
46
<[style>
~fhead>
<body?
<hl>
Welcone
che
SUPER
SECRET
WLILLC
SITE
~</hl>
<h3>
But
hey,
you need
to
explicitly
be
SECURE
</h3>
~[body>
~/hehl>
Sborch
matches
Seorchu
matches
hl (
~cop
Jalt]


Add another header called `Upgrade-Insecure-Requests` and the value is `1`


[Image extracted text: Request
Response
Prethy
Raw
Hex
Pretty
Raw
Hex
Render
083
GET
HTTP / 1
max-vidch:120Opx
Host
Veba-jonathanv. dev: 3003
Padding: ZOpx
User-
Agent
lyonbrovser
margin
aut
Referer
https: / /maclyonsden_
con/
Date
2043
26
Upgrade
Ins-
Cuc
Requescs:
line-height
len ;
28
29
input
but
cextareat
padding: Spx;
font-
size
17pX ;
35
border
Ipxsolidgray;
forn {
line-he
ght
len ;
h {
border: 0
border-cop
lpxsolidgray;
Istyle>
/head>
<bodyz
shl>
Welcone
the
SUPER
SECRET VLILLC
SITE
~fhl>
<h3>
But
valt
imagine having
slou
internet
</h3>
<mbody>
55
~hehly
Sarch 
matches
Sarch 
0 matches]


And the last one you need a header called `Downtime` and set the value into a big number for example 99999999999


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
HTTP /1 -
max-vidch:120OpX
Host
Veba;
jonathanv
dev: 3003
Padding: ZOpx ;
User-Agent
lyonbrovser
margin: aut 0
Re ferer
hctps:
[maclyonsden
Cm
Date
2043
Upgrade
Insecure-Requests:
hl {
Doulink
9999999999999
line-height
len;
29
input
button
textarea(
adding: Spx
fonc
size
ZpX ;
border: lpxsolidgray;
forn {
line-height
Len ;
hr {
border:0;
border-cop
lpxsolidgray;
style>
~fhead?
<body?
<hl>
Welcone
che
SUPER
SECRET
WLILLC
SITE
~</hl>
52
<h3>
Congrats
Here
15
che
flag:
vrhct f (s3cret_sic3_http_head3rs_
cOol}
</h3>
~[body>
{heil>
Seorchu
matches
Seorchu
matches]


```
wxmctf{s3cret_sit3_http_head3rs_r_c0o1}
```