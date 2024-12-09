# Hello
> Sir vignere came to my dreams and sent me this packet capture and told me to find the flag from it which is the key to my success. I am a noob in these cases. So I need your help. Please help me find the flag. Will you?

## About the Challenge
We were given a `pcapng` file and we need to open the file in wireshark

## How to Solve?
If we open the file in wireshark and if we check on the DNS packet, there is a single character on each packet


[Image extracted text: Kali Linux
VMware Workstation 17 Player (Non-commercial
use oniy)
Player
@ 4
10.35
find-mepcapng
Eile
Edit
View
Go
Capture
Analyze
Statistics
Telephony
Wireless
Tools
Help
Apply
display
<Ctrl-I>
No
Time
Source
Destination
Protocol
Length  Info
50 8.920119450
104.21.72.32
10.0.2.15
ICMP
60 Echo (ping)
reply
id-Oxoooo
seq-0/0 ,
ttl=54
(request
49
52 9.185207545
8 . 8 . 8 . 8
10.0.2.15
DNS
136 Standard
query
response
Oxoooo
such
name
V.knightctf
com
SOA
brenda
ns
cloudflare
com
55 9.390731665
8 . 8
10.0.2.15
DNS
136 Standard
query
response
Oxooo
such
name
V.knightctf
com
SOA
brenda.ns .
cloudflare
com
58 9.697815962
8 . 8 . 8 . 8
10.0.2.15
DNS
136 Standard
query
response
Oxooo
such
name
B.knightctf
com
SOA
brenda.ns.cloudflare
com
9 . 903672671
8 . 8
10.0.2.15
DNS
136 Standard
query
response
Oxooo
such
name
knightctf
com
SOA
brenda .ns
cloudflare
com
64 10
107182784
8 . 8 . 8 
10 . 0 . 2
DNS
136 Standard
query
response
Oxoooo
such
name
T.knightctf
com
SOA
brenda.ns
cloudflare
com
10
311858316
10.0.2
DNS
136 Standard
query
response
such
name
knightctf
com
SOA
brenda .ns. cloudflare
com
70 10.517299771
8 . 8 . 8 . 8
10 .0.2.15
DNS
136 Standard
query
response
Oxoooo
such
name
t.knightctf
com SOA brenda.ns.cloudflare
com
73 10.721727397
8 . 8
10.0.2.15
DNS
136 Standard
query
response
Xooo
such
name
knightctf
com
SOA
brenda .ns
cloudflare
com
75 10
928565809
10 .0.2.15
DNS
136 Standard
query
response
Oxoooo
such
name
knightctf
com
SOA
brenda
ns
cloudflare
com
77 11.139197213
10 .0.2.15
DNS
136 Standard
query
response
000
such
name
V.knightctf
com
SOA
brenda .ns
cloudflare
com
79 11.341178605
8 . 8
10.0.2.15
DNS
136 Standard
query
response
Oxoooo
such
name
9. knightctf
com SOA
brenda.ns.cloudflare
com
82 11.540771419
8 . 8
10.0.2.15
DNS
136 Standard
query
response
Xoooo
such
name
knightctf
com SOA
brenda .ns. cloudflare
com
84 11.747396713
10 .0.2.15
DNS
136 Standard
query
response
Oxoooo
such
name
knightctf
com
SOA
brenda
ns
cloudflare
com
86 11
951803190
10.0.2.15
DNS
136 Standard
query
response
000
such
name
j knightctf
com
SOA
brenda .ns
cloudflare
com
88 12.258200632
10 .0.2.15
DNS
136 Standard
query
response
Oxoooo
such
name
N.knightctf
com SOA brenda.ns.cloudflare
com
91 12.464155596
8 . 8
10.0.2.15
DNS
136 Standard
query
response
Xoooo
such
name
h.knightctf
com
SOA
brenda .ns
cloudflare
com
93 12
667536900
10.0.2.15
DNS
136 Standard
query
response
Oxoooo
such
name
knightctf
com
SOA
brenda
ns
cloudflare
com
95 12
872431933
10.0.2.15
DNS
136 Standard
query
response
000
such
name
2.knightctf
com
SOA
brenda .ns
cloudflare
com
13.079248120
10.0.2.15
DNS
136 Standard
query
response
Oxoooo
such
name
V.knightctf
com SOA
brenda.ns.cloudflare
com
99 13
283535618
8 . 8
10.0.2.15
DNS
136 Standard
query
response
Xoooo
such
name
knightctf
com
SOA
brenda .ns. cloudflare
com
102
13
487665832
10 .0.2.15
DNS
136 Standard
query
response
Oxoooo
such
name
knightctf
com
SOA
brenda
ns
cloudflare
com
104 13
691696858
10.0.2.15
DNS
136 Standard
query
response
000
such
name
F.knightctf
com
SOA
brenda .ns
cloudflare
com
106 13
897719326
10 .0.2.15
DNS
136 Standard
query
response
Oxoooo
such
name
9. knightctf
com SOA brenda.ns.cloudflare
com
108 14
100673634
8 . 8
10.0.2.15
DNS
136 Standard
query
response
Xoooo
such
name
knightctf
com
SOA
brenda .ns
cloudflare
com
110 14
307559588
10.0.2.15
DNS
136 Standard
query
response
Oxoooo
such
name
knightctf
com
SOA
brenda
ns
cloudflare
com
113 14
511448395
10.0.2.15
DNS
136 Standard
query
response
000
such
name
z.knightctf
com
SOA
brenda .ns
cloudflare
com
115 14.715386589
10.0.2.15
DNS
136 Standard
query
response
Oxoooo
such
name
N.knightctf
com SOA
brenda.ns.cloudflare
com
117 14.919268070
8 . 8
10.0.2.15
DNS
136 Standard
query
response
Xoooo
such
name
knightctf
com SOA
brenda .ns. cloudflare
com
119 15.125389592
10 .0.2.15
DNS
136 Standard
query
response
Oxoooo
such
name
knightctf
com
SOA
brenda.ns
cloudflare
com
121 15
229863461
10.0.2.15
DNS
136 Standard
query
response
Xoooo
such
name
T.knightctf
com
SOA
brenda .ns
cloudflare
com
124 15.639292244
8 . 8 . 8 
10.0.2.15
DNS
136 Standard
query
response Oxooo0
such
name
B.knightctf
com SOA
brenda.ns.cloudflare
com
126 15.843648723
8 . 8 . 8 
10
0.2.15
DNS
136 Standard
query
response
Xoooo
such
name
knightctf
com SOA
brenda .ns
cloudflare
com
128 16.047001845
8 . 8 . 8 _
10
.0.2.15
DNS
136 Standard
query
response
Oxoooo
such
name
f.knightctf
com
SOA
brenda.ns
cloudflare
com
130 16
252973081
10.0.2.15
DNS
136 Standard
query
response
0000
such
name
Q.knightctf
com SOA
brenda .ns
cloudflare
com
133 16. 456688279
8 . 8 . 8 . 8
10.0.2.15
DNS
136 Standard
query
response
Oxoooo
such
name
=.knightctf
com
SOA
brenda.ns. c loudflare
com
135 16
662529884
8 . 8
10.0.2.15
DNS
136 Standard
query
response
Oxoooo
such
name
knightctf
com
SOA
brenda.ns. c loudflare
com
17 2.951855902
10.0.2.15
104.21.72.32
ICMP
43 Echo
(ping)
request
id-Oxoooo
seq-0/0
ttl=64
(reply
in
18
Frame
73
bytes
Wire
(584
bits),
73
bytes captured (584 bits)
on
interface
etho
id
0000
52
54
00 12
02
00
27 22
46 4f
08
00
45
RT.5
"FO E
Ethernet
II,
Src:
PcsCompu_22:46
4f (08
00 : 27 : 22
46: 4f ) ,
Dst
RealtekU_12:35
02 (52
54:00:12:35:02)
0010
3b
2b
40 00
40 11
c5
Oa
00 02
cO
+0 @
find-me pcapng
Packets: 135
Displayed: 135 (100.0%)
Profile: Default
10.35 PM
Search
63
10
1/24/2023
filter]


After we arrange the character, here is the result
```
VVBCTHtvMV9tcjNhX2VuMF9oazNfaTBofQ==
```
And we know that's base64 encode! But after we decode the encoded text the result is
```
UPBL{o1_mr3a_en0_hk3_i0h}
```
And then because there is a hint in the question "`Sir vignere came to ...`". Decode the msg with vigenere cipher and the key is `KNIGHT`
```
KCTF{h1_th3n_wh0_ar3_y0u}
```