# Backup
> This company has an interesting approach to backuping their routers. I sniffed the network traffic while they conducted a backup. Check if you find something interesting.

## About the Challenge
We got a gzip file (You can download the file [here](backup.tar.gz)) and that file contain a PCAP file called `traffic.pcap`


[Image extracted text: trafficpcap
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
Apply
display filter
Ctrl-/ >
Time
Source
Destination
Protocol
Length
Info
000000
192.168 _
239.255.255
250
SSDP
209 M-SEARCH
HTTP /1.1
2 1.006784
192.168.56 _
239.255.255.250
SSDP
209 M-SEARCH
HTTP /1.1
3 2.014853
192.168.56 _
239.255.255.250
SSDP
209 M-SEARCH
HTTP /1.1
4 3.023183
192.168.56 _
239.255.255.250
SSDP
209 M-SEARCH
HTTP /1.1
5 14.828872
192.168.56.3
192.168.56.4
TCP
74 38534
[SYN]
Seq-0
Win-64240
Len=0
MSS-1460
SACK
PERM TSval-2259716122 TSecr-0
NS-128
14.829155
192.168.56 _
192.168.56 _
TCP
74 23
38534
[SYN,
ACK]
Seq-0
Ack-1 Hin-65160
Len-0 MSS-1460
SACK PERM TSval-3129789828
TSecr-2259716122 WS-128
7 14.829164
192.168.56.3
192.168
TCP
66 38534
[ACK]
Seq-1
Ack-1 Win-64256
Len=0
TSval-2259716123
TSecr-3129789828
8 14.829226
192.168.56 _
192.168.56
TELNET
90 Telnet
Data
9 14.829366
192.168.56 _
192.168.56
TCP
66 23
38534 [ACK]
Seq-l Ack-25 Win-65152
Len=0
TSval-3129789829
TSecr-2259716123
10 14.838269
192.168.56 _
192.168.56
TELNET
87 Telnet
Data
11 14.838275
192.168.56 _
192.168.56
TCP
66 38534
23 [ACK] Seq-25 Ack-22 Win-64256
Len=0
TSval-2259716132
TSecr-3129789837
12 14.838335
192.168.56 _
192.168
TELNET
78 Telnet
Data
13 14.838549
192.168.56 _
192.168.56
TELNET
89 Telnet
Data
14 14.838565
192.168.56 _
192.168
TCP
66 38534
23 [ACK]
Seq-37
Ack-45 Win-64256
Len=0
TSval-2259716132
TSecr-3129789838
15 14.838811
192.168.56 _
192.168.56
TELNET
84 Telnet
Data
16 14.838815
192.168.56 _
192.168
TELNET
132 Telnet
Data
17 14.881930
192.168.56 _
192.168.56
TCP
66 23
38534 [ACK]
Seq-63 Ack-103 Win-65152
Len=0
TSval-3129789881
TSecr-2259716132
18 14.881941
192.168.56 _
192.168
TELNET
109 Telnet
Data
19 14.882198
192.168.56 _
192.168.56
TCP
66 23
38534 [ACK]
Seq-63 Ack-146 Win-65152
Len-0 TSval-3129789881
TSecr-2259716175
20 14.882662
192.168.56 _
192.168
TELNET
69 Telnet
Data
Frame
209
bytes
Nire
(1672
bits) ,
209
bytes
captured
(1672
0000
00 5e 7f ff fa 0a 00
27 00 00 00 08 00
Ethernet
II,
Src:
00:27:00:00
00:27
00:
Dst:
IPv4ncast 7f:ff:fa
(01:00:5e:7f:ff:fa)
0010
00 <3 73 30 40 00 01
ld 56 c0 a8 38 01 ef
s0@
V.8 .
Internet
Protocol
Version 4,
Src:
192.168.56.1,
Dst:
239.255.255.250
0020
ff fa a4 e2
07 6c 00 af
4c Jc 4d 2d 53 45 41 52
LIM-SEAR
User Datagram Protocol,
Src
Port: 42210,
Dst
Port:
1900
0030
48 20 2a 20 48 54 54
50 2f 31 2e 31 0d 0a
HTT
P/1.1 .H
0040
4f 53 54 3a 20 32 33 39
2e 32 35 35 2e 32 35 35
OST: 239
255.255
Simple
Service Discovery
Protocol
0050
2e 32 35 30 3a 31 39 30
30 Od Oa 4d 41 4e 3a
250:190
0..MAN:
9060
22 73 73 64 70 3a
73 63 6f 76 65 72 22
ssdp:di
scover
4d 58 3a 20 31 Od Oa
53 54 3a 20 75 72 6e 3a
MX:
ST:
urn:
59 61 6c 2d 6d 75 6c
74 69 73 63 72 65 65 6e
dial-mul
tiscreen
2d 6f 72 67 3a 73 65 72
76 69 63 65 3a 64 69
-org:ser
vice:dia
0a0
Sc 3a 31 0d 0a 55 53 45
52 2d 41 47 45 4e 54 3a
1:1 .USE R-AGENT:
20 43 68 72 6f 6d 69 75
6d 2f 31 30 39 2e 30 2e
Chromiu m/109.0
@0c0
35 34 31 34 2e 37 34 20
4c 69 6e 75 78 0d 0a 0d
5414.74
Linux
00d0
bits)
00
00) ,]


## How to Solve?
If you analyze the traffic, you will see there are a lot of FTP traffic here, you can filter it using `ftp`


[Image extracted text: trafficpcap
File
Edit
Go
Capture
Analyze
Statistics
Telephony
Wireless
Tools
Help
Time
Source
Destination
Protocol
Length
Info
158 41.783077
192.168_
192.168.56
FTP
100 Response:
220
Helcone
to 1337
FTP service_
160 45.271620
192.168.56.3
192.168.56
FTP
82 Request: USER
anonymous
162 45.272082
192.168.56.4
192.168.56
FTP
100 Response:
331
Please
specify
the password-
164
48.311683
192.168.56 _
192.168
FTP
76 Request:
PASS
XXX
165 48.313398
192.168.56.4
192.168.56
FTP
Response:730
Login_Successtil
167 48.313428
192.168.56 _
192.168
FTP
72 Request:
SYST
168 48.313574
192.168.56 _
192.168.56
FTP
85 Response: 215
UNIX Type:
170 50.119479
192.168.56 _
192.168.56
FTP
93 Request:
PORT
192,168,56,3,188,253
171 50.119809
192.168.56 _
192.168.56
FTP
117 Response:
200
PORT
command successful.
Consider using
PASV _
173 50.119853
192.168.56 _
192.168.56
FTP
72 Request:
LIST
177 50.120398
192.168.56 _
192.168.56
FTP
105 Response: 150
Here
comes
the directory listing.
184 50.120608
192.168.56 _
192.168.56
FTP
90 Response: 226 Directory
send
186 54.450898
192.168.56.3
192.168.56
FTP
74 Request:
TYPE
187 54.451402
192.168.56 _
192.168
FTP
97 Response: 200
Switching
to Binary
mode _
189 54.451551
192.168.56.3
192.168.56
FTP
93 Request:
PORT
192,168,56,3,213,243
190 54.451712
192.168.56 _
192.168
FTP
117 Response:
200 PORT
command successful.
Consider using
PASV _
192 54.451740
192.168.56.3
192.168.56
FTP
83 Request:
RETR
backup.zip
196 54.452135
192.168.56 _
192.168
FTP
135 Response: 150
Opening BINARY
mode
data
connection
for
backup.zip
(411
bytes) .
203 54.452489
192.168.56.4
192.168.56
FTP
90 Response:
226
Transfer
complete_
205 57
897801
192.168 _
56 ..
192.168
FTP
72 Request: QUIT
Frame
165:
bytes
on wire
(712
bits) ,
bytes
captured (712
J000
08 00 27 76 5f 41 08
27 8c 3b 95 08 00 45
v_A;
Ethernet
II,
Src: PcsCompu_
8c:3b:95
00:27:8c: 3b:95) ,
Dst: PcsCompu_76:5f:41 (08:00:27:76:5f:41)
0010
bc af 40 00 40
8c a5 c0 a8 38 04 c0 a8
Internet
Protocol
Version
Src:
192.168.56.4,
Dst:
192.168.56.3
0020
38 03 00 15 c} 76 96
27 32 21 bb
bc eb 80
2! .
Transmission
Control
Protocol,
Src
Port:
21 ,
Dst
Port:
50038 ,
Seq:
69 ,
Ack: 27 ,
Len: 23
0030
fe a5 Sd 00 00 01
ba 8d 50 61 86 b1
0040
0a e5 32 33 30 20 4c 6f
69 6e 20 73 75 63 63
230 Lo gin
succ
File Transfer
Protocol (FTP)
0050
65 73 73 66 75 6c 2e Od
essful
[Current working
directory:
View
bits)]


Choose one of the packet, right click and then choose `Follow TCP stream`. In stream `0` there is a user password


[Image extracted text: Wireshark
Follow TCP Stream (tcp.stream eq 0)
traffic pcap
#..$
38400,38400_
xterm-256color
1337router
login:
rroooott
Password
sup3rs3cur
Login
incorrect
1337router
login:
rroooott
Password:
sup3rs3cur3
Welcome
to 1337router!
Last
login:
Wed
Jan 25 17
00:37
UTC 2023
from 192
168.56.3
on
pts/2
[?2004h. ]o;root@1337router
root@1337router
~# aaccttiivvaattee_
-ffttpp
[?20041
ftp
server
activated
[?2004h. ]o;root@1337router:
root@1337router:~#
[?20041
logout]


And in stream `3` there is a zip file that we can extract


[Image extracted text: Wireshark
Follow TCP Stream (tcp.stream eq 3)
trafficpcap
PK_
9V_
backup/UT
SI-cn | -
cux _
PK_
9Vk
XA _
backup/secrets. jsonUT
SI-cn | -
cux _
-AT/ .
~~K.ya.W.
5.Y&.W.
~J-1.
^oWw _
01_
KQ:
LPK..k
XA _
5 ._
PK _
9V _
backup/UT_
-Sl-cux_
PK _
9Vk
XA .
backup/secrets.jsonUT
-SI-cux _
PK]


Extract the zip file first and you will find a file called `secrets.json`. To open the file we need to know the key.


[Image extracted text: Name
Type
Compressed size
Password p=
Size
Ratio
Date modified
secretsjson
JSON Source File
1 KB
Yes
KB
0%
1/25/2023 5.44 PM
Password needed
File 'secrets json' is password protected_
Please enter the password in the box below:
Skip File
Password:
Cance]


Use the password that you have found in stream `0` (The password is `sup3rs3cur3`)


[Image extracted text: masterkey"
flag{TelnetAndFTPAreSoVErySecure}"]


```
flag{TelnetAndFTPAreSoVErySecure}
```