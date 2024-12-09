# Blue Baby Shark
> Hello Stranger!

> I got recomendation from one of our common acquaintance. I’m a new into all of this CTF stuff. I got stuck with one challange and I’m not that skilled wit the network traffic analysis. Would you be able to help me out with this partiucalr CTF and find the flag? Only hint I have so far is that one machine was compromised.

## About the Challenge
We were given a pcapng file and we need to find the flag there (You can find the file [here](Blue%20Baby%20Shark.pcapng))

## How to Solve?
I open the file using `Wireshark` and using `frame contains "vu"` filters to find the packet that contains `vu` string. And then there are 4 packets that contains `vu` string.


[Image extracted text: 11656 4.604931208
192.168.56.3
192.168.56.3
TCP
60 53978
8086
[SYN]
Seq-0
Win-1024 Len-0 MSS-1460
18554 8
685860119
192.168.56.1
192.168.56
TCP
62 2007
64559
[RST ,
ACK]
Seq-1
Ack-1
Win-0
Len-0
32835 29.222041713
192.168.56.2
192.168.56.3
TCP
3275 1337
52094
[PSH ,
ACK]
Seq-40
Ack-20 Win-32
Len-3207
TSval-1380163497
TSecr-943633313
36350 47.987257033
192.168
56.2
192.168.56.3
TCP
62 53997
6006
[SYN]
Seq-0
Win-1024
Len-0 MSS-1460
Frame
32835:
3275
bytes
on wire
(26200 bits),
3275
bytes captured
26200 bits)
interface
any ,
id 0
0010
bb
00
Oe
CO
38
Linux
cooked capture
0020
a8
03
43 f5
Se
82
"9 ~
hc
Internet
Protocol
Version 4,
Src
192.168. 56.2 ,
Dst :
192.168. 56.3
0030
18
03
08
52
9f
RC
0100
Version:
3a
3a
8>
root
'Xo:0:
0101
Header
Length:
20 bytes
(5)
D
6f
2f
oot :/roo
t /usr/b
Differentiated
Services
Field:
Oxoo
(DSCP 
CSO ,
ECN:
Not-ECT)
in/zsh d aemon:x:
73
1-1:daem
on : /usr/
Total Length:
3259
Identification:
Oxzdfa (11764)
69
2f
sbin:/us rlsbinln
3a
3a
ologin b
in:X:2:2
010
Flags:
Ox2
Don
t fragment
2f
:bin: /bi
n:/usr/s
Ooo0
Ooo0
Ooo0
Fragment
Offset :
bin/nolo
gin  sys
Time
Live
64
3a
X:33:Sy
5 : /dev:
Protocol:
TCP (6)
69
usr/sbin
Inologin
Header
Checksum: Oxoef3 [validation
disabled]
34
sync:X:
4:65534:
[Header
checksum
status
Unverified]
2f
sync: /bi
n: /bin/s
Source
Address
192.168. 56.2
0100
35
36
ync   game s:x:5:60
Destination
Address:
192.168. 56.3
0110
6d
:games:
usr /game
Transmission
Control Protocol,
Src
Port:
1337 ,
Dst
Port:
52094 ,
Seq:
40 ,
Ack:
20 ,
Len :
3207
0120
3a
6e
6e
6c
lusrls binlnolo
Data
3207
bytes)
0130
Oa
3a
36
3a
gin
man :
X:6:12:m
Data: 726f6f743a783a303a303a726f6f743a2f726f6f743a2f7573722f62696e2f7a73680a64_
0140
6e
3a 2f
72
an: Ivar /
cache/ma
[Length: 3207]
0150
3a
75
73
2f
62
6e 2f
6e
6c
n: /usr/s bin/nolo
0160
69
Oa
3a 37
3a
3a
70
gin lp:x
:7:7:lp:
Differentiated Services Field (ip.dsfield); 1 byte
Packets: 40434
Displayed:
(0.0%)]


I press the `Follow TCP` on packet 32835 and we will find the flag on `vu` user


[Image extracted text: rpc:X:117:65534:
[run/rpcbind: /usr/ sbin/nologin
geoc lue:x:118:126
Ivar/ lib/geoclue
lusr/ sbin/nologi
vu:x:1337:bAby_Shark_fly
Aw4y
Debian-snmp:X:119:127 :
Ivar / lib/ snmp
[binffalse
ss Zh:x:120:129: : /nonexistent : /usr/sbin/nologin
ntpsec:X:121:132:
[nonexistent
rusr/ sbinfnologin
FOCCCAV 0
409
499
ao
t OCi Cl @
Vucr/clin /0]


```
VU{b4by_5h4rk_fly_4w4y}
```