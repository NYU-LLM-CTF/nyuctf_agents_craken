# No Expectation of Privacy
> We've been monitoring data coming and going from around campus. Might be worth looking into it to see if anything weird stands out.

> Could be that's how whoever is behind the weird stuff on campus is communicating? We're looking for something from someone named RB.

## About the Challenge
We were given a `pcapng` file (You can get the flag [here](caughtin2023.pcapng)), so we need Wireshark to open the file


[Image extracted text: caughtin2023 pcapng
File
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
Q
6 ?
n
'
No_
Time
Source
Destination
Protocol
Length Info
10568 466
279684253
142
251
40.164
192.167.200_
QUIC
1399 Protected
Payload
(KPO
DCID-92b54b
10569 466. 279684273 142.251
40.164
192.167.200.5
QUIC
1399 Protected
Payload (KPO
DCID-92b54b
10570 466
279684293 142.251
40.164
192.167.200
QUIC
1399 Protected
load
(KPO
DCID-92b54b
10571 466
279684323 142.251.40
164
192.167.200
QUIC
1399 Protected
Payload
(KPO
DCID-92b54b
10572 466
279698727
142.251
40.164
192
167.200
QUIC
1399 Protected
load (KPO
DCID-92b54b
10573 466.279698757
142.251
40.164
192.167.200
QUIC
1399 Protected
Payload (KPO
DCID-92b54b
10574 466
279698787
142.251
40.164
192
167
200
QUIC
1399 Protected
load (KPO
DCID-92b54b
10575 466
279698807
142.251
40.164
192
167
200
QUIC
1399 Protected
Payload (KPO
DCID-92b54b
10576 466. 279698837
142.251
40.164
192.167
200
QUIC
1312 Protected
load (KPO
DCID-92b54b
10577 466.279698857
142.251.40
164
192.167
200
QUIC
1392 Protected
Payload (KPO
DCID-92b54b
10578 466
279698887
142.251
164
192
167
200
QUIC
1399 Protected
load
(KPO
DCID-92b54b
10579 466
279698907
142.251.40
164
192
167
200
QUIC
1399 Protected
Payload
(KPO
DCID-92b54b
10580 466
280146614
142.251
40.164
192
167.200
QUIC
1399 Protected
load
(KPO
DCID-92b54b
10581 466
280147045 142.251
40.164
192.167.200
QUIC
1399 Protected
Payload (KPO
DCID-92b54b
10582 466
280147095
142.251
40.164
192.167
200
QUIC
1399 Protected
load
(KPO
DCID-92b54b
10583 466
280147125
142.251
40.164
192.167.200
QUIC
1399 Protected
Payload
(KPO
DCID-92b54b
10584 466
280147155
142.251
40.164
192
167.200
QUIC
1399 Protected
load
(KPO
DCID-92b54b
10585 466
280147185 142.251
40.164
192.167.200.5
QUIC
1399 Protected
Payload (KPO
DCID-92b54b
Frame
10568 : 1399
bytes
on
Wire
(11192 bits),
1399
bytes captured
(11192 bits)
interface
etho,
id
000
00
27
68
a6
54
35
08
'ha
RT
5 'E
Ethernet
Src:
RealtekU_12:35
(52:54:00
12:35:00 ) ,
Dst :
PcsCcompu
68: fd:a6 (08:00:27:68:fd:a6)
0010
00
8e
28
cO
iZ#.
Internet
Protocol
Version
Src:
142.251
40. 164 ,
Dst :
192.167
200.5
05
55
b5
4f f7
KO .
User
Datagram Protocol,
Src
Port:
443 ,
Dst
Port:
37107
03e
20
QUIC IETF
ab
Y5
53
f2
Wf ,
9b
db
f1
SG
N'
8c
f{
2a
vk
82
UD .
16
20
7>
ab
b5
h W .
c5
8a
29
df
H  )3
4e
cf
8<y
XN
18
co
83
d5
46
08
a0
fe
0140
50
3a
f6
52
b8
62
76
9e
P:
1R
5]
Cbv
0150
ce
d2
6d
18 30
03
46 a2 1a
88 36 9c
m. 0
F.
Sis neither a field nor a protocol name:
Packets: 14939 . Displayed: 14939 (100.0%)
Profile: Default
Pay _
Pay _
Pay _
Pay _
Pay _
Pay _
Pay _
Pay _
II,]


## How to Solve?
First I tried to use `frame contains "nicc"` in the filter and there is 1 packet that contains string `nicc`.


[Image extracted text: Q & +
0
'
7'
frame contains
'nicc"|
No:
Time
Source
Destination
Protocol
Length Info
10948 511.379889879 192.167
200 .
192.167.200.5
TCP
100 57340
1337
[PSH ,
ACK]
Seq-708
Ack.]


Right click the packet and follow TCP stream to get the flag


[Image extracted text: can
nelp
you
OmLe11so
look
up
night
16
see
every
old
man
long
gone
TomLei15
nicc{th3y_
t011
for_th33}6
TomL]


```
nicc{th3y_t011_f0r_th33}
```