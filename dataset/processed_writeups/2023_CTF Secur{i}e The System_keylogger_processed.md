# keylogger

> So, here's the thing. I just came to the Internet caffee (warnet) and after several minutes using the computer, I found a strange process running in the backround. Then i found out it was a keylogger. Luckily I can stop the process and don't let the attacker get this keylogger file. Because i just logged in to my server before.

> flag = STS23{`<my server password>`}

## About the Challenge
We were given a pcapng file (You can downlod the file [here](log.pcapng)) and we need to find the flag inside this packet capture file


[Image extracted text: Time
Source
Destination
Protocol
Length | Leftover Capt | Info
2023-12-06 14:04:28.231664
host
2.3.0
USB
36
GET DESCRIPTOR Request DEVICE
2
2023-12-06 14:04:28.231664
2.3.0
host
USB
46
GET DESCRIPTOR Response DEVICE
3
2023-12-06 14:04:28.231664
host
2.3.0
USB
36
GET DESCRIPTOR Request CONFIGURATION
2023-12-06 14:04:28.231664
2.3.0
host
USB
87
GET DESCRIPTOR Response CONFIGURATION
5
2023-12-06 14:04:28.231664
host
2.3.0
USB
36
SET CONFIGURATION Request
2023-12-06 14:04:28.231664
2.3.0
host
USB
28
SET CONFIGURATION Response
2023-12-06 14:04:28.231664
host
2.1.0
USB
36
GET DESCRIPTOR Request DEVICE
8
2023-12-06 14:04:28.231664
2.1.0
host
USB
46
GET DESCRIPTOR Response DEVICE
9
2023-12-06 14:04:28.231664
host
2.1.0
USB
36
GET DESCRIPTOR Request CONFIGURATION
10
2023-12-06 14:04:28.231664
2.1.0
host
USB
62
GET DESCRIPTOR Response CONFIGURATION
11
2023-12-06
14:04:28.231664
host
2.1.0
USB
36
SET CONFIGURATION Request
12
2023-12-06 14:04:28.231664
2.1.0
host
USB
28
SET CONFIGURATION Response
13
2023-12-06 14:04:28.231664
host
2.2.0
USB
36
GET DESCRIPTOR Request DEVICE
14
2023-12-06 14:04:28.231664
2.2.0
host
USB
46
GET DESCRIPTOR Response DEVICE
15
2023-12-06
14:04:28.231664
host
2.2.0
USB
36
GET DESCRIPTOR Request CONFIGURATION
16
2023-12-06 14:04:28.231664
2.2.0
host
USB
94
GET DESCRIPTOR Response CONFIGURATION
17
2023-12-06 14:04:28.231664
host
2.2.0
USB
36
SET CONFIGURATION Request
18
2023-12-06 14:04:28.231664
2.2.0
host
USB
28
SET CONFIGURATION Response
19
2023-12-06 14:04:38.371981
2.3.1
host
USB
35
URB_
INTERRUPT
in
20
2023-12-06 14:04:38.372027
host
2.3.1
USB
27
URB_
INTERRUPT
in
21
2023-12-06 14:04:38. 487979
2.3.1
host
USB
35
URB_
INTERRUPT
in
22
2023-12-06 14:04:38. 488020
host
2.3.1
USB
27
URB_
INTERRUPT
in
23
2023-12-06 14:04:38. 550985
2.3.1
host
USB
35
URB_
INTERRUPT
in
24
2023-12-06 14:04:38.551042
host
2.3.1
USB
27
URB_
INTERRUPT
in
25
2023-12-06 14:04:38.649990
2.3.1
host
USB
35
URB_INTERRUPT
in
26
2023-12-06 14:04:38. 650049
host
2.3.1
USB
27
URB_INTERRUPT
in
77
7073-1)-06
14-04.38 677080
7 ?
hoct
MCR
36
MPR
Tntfpiipt]


## How to Solve?
Im using this [writeup](https://ctftime.org/writeup/27675) as a reference because they have the same solution method. First filter the data first to get the usbhid data

```
((usb.transfer_type == 0x01) && (frame.len == 35)) && !(usb.capdata == 00:00:00:00:00:00:00:00)
```

And then put this filter into this [repository](https://github.com/WangYihang/UsbKeyboardDataHacker) to convert the usbhid data into a character and voila!


[Image extracted text: <RET>sshh<SPACE>kyruuu@2mydomain. id<RET>thlsmys3cre<DEL>etp@sSWwo<DEL Ord<RET>thls
mys3cretpa<DEL @SSwO<DEL>O<DEL>Ord<RET><RET><RET><RET><RET><RET><RET>ls<SPACE>-
laa<RET>ccatt<SPACE>.ssh/auth
<RET><RET>
<RET>ccdd<SPACE> /vvar/wwwlhtmml/<DEL>/<RET>vviim<SPACE>iindex. htmml<RET>]


> `<DEL>` means we need to delete the character

```
STS23{th1smys3cretp@ssw0rd}
```