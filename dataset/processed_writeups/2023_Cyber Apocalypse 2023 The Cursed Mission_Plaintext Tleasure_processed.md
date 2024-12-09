# Plaintext Tleasure
> Threat intelligence has found that the aliens operate through a command and control server hosted on their infrastructure. Pandora managed to penetrate their defenses and have access to their internal network. Because their server uses HTTP, Pandora captured the network traffic to steal the server's administrator credentials. Open the provided file using Wireshark, and locate the username and password of the admin.

## About the Challenge
We were given a zip file (You can download the file [here](forensics_plaintext_treasure.zip)). If we unzip the file, there is a file called `capture.pcap`


[Image extracted text: Name
capture pcap]


## How to Solve?
Open `capture.pcap` using Wireshark and enter `frame containing "HTB"` in the filter section to find packets containing the words `HTB`


[Image extracted text: trame contains
"HTB"sS
No
Time
Source
Destination
Protocol
Length Info
969 36
041586
192.168.1.35
192.168.1.30
HTTP
855 POST
token
HTTP/1.1
Frame
969 :
855
bytes
on wire
(6840 bits) ,
855
bytes
captured
6840
bits)
Dc
7E  7 .
Cs '
Ethernet
I,
Src:
PcsCompu_43
73:bc (08
00:27:43.73:bc ) ,
Dst :
Tp-Linkt
ee: 37:b1
(do:37:45.ee: 37:b1)
a8
a8
I @ @'
b .
Internet
Protocol
Version
Src:
192.168.1.35
Dst
192.168
1.30
18
P . 9C6
fJ..1
Transmission
Control
Protocol,
Src
Port
53840 ,
Dst
Port:
1337 ,
Seq:
Ack:
Len :
789
e8
Hyper
ext
Transfer
Protocol
POST
token HT
MIME
Multipart
Media Encapsulation,
Type:
multipart/form-data,
Boundary:
TP/1.1
Host:
19
38
2.168.1 _
30:1337
User-Ag
ent :
Moz
illa/5.0
(X11;
inux X86
64 ;
rv :
102
0 )
ecko/201
00101 Fi
refox/10
Acc
ept :
app
lication
Ijson,
ext/plai
Accept-L
anguage
en-US,
n;q-0.5
Accept-
Encoding
gzip,
deflate
Content
~Type:
ultipart
Iform-da
150
ta;
boun dary=-
160
42360219
80508159
70860674
9430 .
ntent-Le
O1a0
ngth:
Origi
0100
20
2f
2f
39
2e 31
36
http: //192
16
O1c0
38
2e
31
2e 33
30 3a
37
33 Od
6e
8.1.30:4
173
Con
33]


Right click the packet and then choose `Follow TCP Stream` to get the flag


[Image extracted text: Host:
192.168.1.30:1337
User
Agent
Mozilla/5
(X1l;
Linux x86_64;
rv:102.0 )
Gecko/20100103
Accept
application/json,
text/plain_
Accept-Language
en-US , en;q-0.5
Accept-Encoding:
gzip,
deflatel
Content-Type
multipart/form-data;
boundary=
Content-Length:
332
Origin:
http:/ /192.168
1.30
4173
Connection:
keep-alive
Referer
http://192.168.1.30:41737
-4236021980508159708606749430
Content
Disposition:
form-data;
name=
username
cOSmic
operator
4236021980508159708606749430
Content
Disposition:
form-data;
name=
password"
HTB{th3s3_
4113n5_
still_us3_HTTP}
4236021980508159708606749430 -
HTTP/1.1
200
OK
Idate: Thu,
Mar
2023 10:11:21
GMT]


```
HTB{th3s3_4l13ns_st1ll_us3_HTTP}
```