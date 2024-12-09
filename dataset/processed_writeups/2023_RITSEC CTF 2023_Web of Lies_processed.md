# Web of Lies
> We found more weird traffic. We're concerned he's connected to a web of underground criminals.

## About the Challenge
We were given a `pcapng` file (You can download the file [here](weboflies.pcapng)). And here is the preview


[Image extracted text: 6 7
0
Apply-
display filter
<Ctrl-I>
No_
Time
Source
Destination
Protoco
Length  Info
8 3.914163
127
0.1
127
HTTP
205 GET /flag
HTTP/1.1
12 3.915625
127 . 0
127
0 .0
HTTP
72 HTTP/1.1
400
BAD REQUEST
(text/html)
22 3.925083
127
127
HTTP
205 GET
1f14g
HTTP/1.1
26 3.926283
127
127
HTTP
71 HTTP/1.1
401
UNAUTHORIZED
(text/html)
36 3.934066
127
127
HTTP
205 GET /flag
HTTP/1.1
40 3.935186
127
127
HTTP
72 HTTP/1.1
400
BAD REQUEST
(text/html)
50 3
944673
127
127
HTTP
205 GET /f14g
HTTP/1.1
54 3.945874
127
127
HTTP
71 HTTP/1.1
401
UNAUTHORIZED
(text/html)
3. 953191
127
127
0.0 _
HTTP
205 GET
Iflag
HTTP/1.1
66 3.954402
127
127
HTTP
72 HTTP/1.1
400
BAD REQUEST
(text/html)
74 3.964630
127.0. 0
127.0.0.1
HTTP
205 GET /flag
HTTP/1.1
783,966144
127
127
HITP
72 HTTPL1 1
400
BAID
REOUEST
Ltext Zhtml
Frame
1: 361
bytes
on wire
((2888
bits) ,
361
bytes captured
2888 bits)
on
interface
loo ,
id
000
3d 11
ff
80
Null/Loopback
0010
00
d3
68 ff
00
h.
Internet
Protocol
Version
Src:
fe8o::941C:45ff:fed3:9468,
Dst : ffoz:
fb
e9
User Datagram
Protocol,
Src
Port:
5353
Dst
Port:
5353
Multicast
Domain
Name
System
(response)
CLink-f
0478478a
02b
com panion-
ink
tcp
local
0S
32
2724c2cd
6993-4c
20-aa39 - 397b97bc
lebe
00
rpBA=
3B: 7F: C9
4E : 8F : 8
1 rpFI-0
X800 rpA
D-6cdc54
00442dr
pVr-410_
servi
ces
dns
sd .
udp
00
130
d3
E . h
40
co
08
4b
X' -
0150
00
00
0160
CO
00
00
80
1e]


There are a lot of requests to `/flag` and `/fl4g` endpoints

## How to Solve?
As there were only requests to the `/flag` and `/fl4g` endpoints, I decided to represent them in binary code. Therefore, `/flag` is equivalent to 0 and `/fl4g` is equivalent to 1.

```shell
tshark -r weboflies.pcapng -Y http | grep -oP "/fl.* HTTP" | sed 's/\/flag.*/0/g' | sed 's/\/fl4g.*/1/g' | tr -d '\n'
```

To easier myself, im using `tshark` command to print all the HTTP packet, and then change them to binary code using `sed` command


[Image extracted text: (kaliokali)-[~/Desktop]
tshark
Weboflies.pcapng
~Y http
grep
"If1.*
HTTP"
sed
's/Vflag.*/0/g'
sed
s/V/f14g.*/1/g'
tr -d
An
01010010010100110111101101010010011001010110011001110010001100110111001101101000010101000110100000110011010100000011
0100011001110011001101111101]


Use binary code translator to obtain the flag


[Image extracted text: Recipe
Input
+ O9
01010010010100110111101101010010011001010110011001110010001100110111001101101000010101000110100000
From
1100110101000000110100011001110011001101111101
Delimiter
Byte Length
144
Raw Bytes
Output
0 0
M
{
IRS{Refr3shTh3P4g3}
Binary
Space]


```
RS{Refr3shTh3P4g3}
```