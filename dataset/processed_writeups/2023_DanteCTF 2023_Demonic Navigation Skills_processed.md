# Demonic Navigation Skills
> A friend told me that they are creating a new celestial network, way better than our Internet even though it is based on some long forgotten tech. Do you have the skills to find the Holy Record? Start your search at gates.hell.dantectf.

## About the Challenge
We were given a server, and we need to check the records of the server, for example `NS`, `A`, etc.

## How to Solve?
Well, this is how I solved the challenge: first, I checked the `gates.hell.dantectf` using the `dig` command. You will see there is a subdomain in the `ANSWER SECTION`, and you need to look up that subdomain and find more information by checking another records. Repeat that step until you obtain the flag.

```
dig @challs.dantectf.it -p 31553 gates.hell.dantectf
dig @challs.dantectf.it -p 31553 tesssss.purgatory.dantectf NS
dig @challs.dantectf.it -p 31553 skies.paradise.dantectf CLASS9
dig @challs.dantectf.it -p 31553 flag.paradise.dantectf CLASS9
```


[Image extracted text: <<>> DiG
9.18.1-lubuntul
2-Ubuntu
<<>>
@challs.dantectf
it
~p
31553 flag.paradise.dantectf CLASS9
(13
servers
found)
global options
+cmd
Got
answer
~>>HEADER<<- opcode
QUERY
status
NOERROR
id:
61387
flags
qr
aa rd ad; QUERY
1 ,
ANSWER :
1,
AUTHORITY:
ADDITIONAL:
WARNING
recursion requested
but
not
available
OPT
PSEUDOSECTION:
EDNS
version:
flags:
udp :
1232
COOKIE
a9badc60_
du8d0bl
(echoed)
QUESTION
SECTION
paradise.dantectf
CLAsS9
ANSWER
SECTION:
paradise.dantectf
CLAsS9
TXT
"DANTE {who_r3m3mb3r5_ch4osn3t_
4nd_
h3slOd}
Query
time
200
msec
SERVER
188. 166.77.196#31553(challs.dantectf
it)
(UDP)
WHEN
Tue
Jun
06
07: 04: 46
WIB
2023
MSG
SIZE
rcvd:
138
flag_
lag]


```
DANTE{wh0_r3m3mb3r5_ch405n3t_4nd_h3s10d}
```