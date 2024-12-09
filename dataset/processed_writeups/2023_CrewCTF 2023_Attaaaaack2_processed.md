# Attaaaaack2
> Q2. How many processes were running ? (number)

> ( doesnt follow format)

## About the Challenge
We got `raw` image and we need to determine the total number of processes that were running

## How to Solve?
To solve this, we need to find the list of process using `pslist` plugin. Here is the command I used

```
vol.py -f /path/to/memdump.raw --profile=Win7SP1x86_23418 pslist
```


[Image extracted text: daffainfo@dapos
$ vol.py
~f
Ihome/daffainfo
forensic/memdump
raw
profile-Win7SPlx86_23418 pslist
Volatility
Foundation Volatility
Framework
2.6
Offset(v)
Name
PID
PPID
Thds
Hnds
Sess
Wow64 Start
Exit
0x8419c020 System
89
536
2023-02-20
19:01:19 UTC+OOOO
0x962f2020
smsS. exe
268
29
2023-02-20
19:01:19 UTC+OOOO
0x860a8c78
csrss.exe
352
344
2
462
2023-02-20
19:01:20 UTC+OOOO
Ox855dfd20
Wininit.exe
404
344
3
76
2023-02-20
19:01:20 UTC+OOOO
0x8550b030
csrss.exe
416
396
268
2023-02-20
19:01:20 UTC+OOOO
0x85ea2368
services
exe
480
404
220
0
2023-02-20
19:01:20 UTC+OOOO
Ox85ea8610 Lsass.exe
488
404
568
0 2023-02-20
19:01:20 UTC+OOOO
Ox85eab718
Lsm.exe
496
404
10
151
2023-02-20
19:01:20
UTC+OOOO
Ox85eacb8o Winlogon. exe
508
396
5
115
0 2023-02-20
19:01:20 UTC+OOOO
0x85f4d030 svchost
exe
632
480
10
357
0
0 2023-02-20
19:01:21 UTC+OOOO
Ox85efoa90 svchost
exe
700
480
280
0 2023-02-20
19:01:21 UTC+OOOO
0x919e2958 svchost
exe
752
480
22
507
0 2023-02-20
19:01:21 UTC+OOOO
Ox85f9c3a8 svchost
exe
868
480
13
309
0 2023-02-20
19:01:21 UTC+OOOO
Ox85fae030 svchost
exe
908
480
18
715
0 2023-02-20
19:01:21 UTC+OOOO
0x85fb7670 svchost
exe
952
480
34
995
0 2023-02-20
19:01:22 UTC+OOOO
0x85ff1380 svchost
exe
1104
480
18
391
2023-02-20
19:01:22 UTC+OOOO
0x8603a030 spoolsv
exe
1236
480
13
270
2023-02-20
19:01:22 UTC+OOOO
0x86071818
svchost
exe
1280
480
19
312
2023-02-20
19:01:22 UTC+OOOO
0x860b73c8
svchost.exe
1420
480
10
146
2023-02-20
19:01:22 UTC+OOOO
Ox860ba030 taskhost
exe
1428
480
205
2023-02-20
19:01:22 UTC+OOOO
0x861321c8
dwm . exe
1576
868
2023-02-20
19:01:23 UTC+OOOO
0x8613c030
explorer
exe
1596
1540
29
842
2023-02-20
19:01:23 UTC+OOOO
0x841d7500 VGAuthService
1636
480
3
84
0
2023-02-20
19:01:23 UTC+OOOO
0x86189d20
vmtoolsd
exe
1736
1596
179
2023-02-20
19:01:23 UTC+OOOO
0x8619dd20
vm3dservice
ex
1848
480
60
0
2023-02-20
19:01:24 UTC+OOOO
0x861a9030
vmtoolsd .exe
1884
480
13
290
2023-02-20
19:01:24 UTC+OOOO
0x861b5360 vm3dservice
ex
1908
1848
2023-02-20
19:01:24 UTC+OOOO
Ox861fc700 svchost.exe
580
480
6
288
0
2023-02-20
19:01:25
UTC+OOOO
0x86261030
WmiPrvSE
exe
1748
632
10
2023-02-20
19:01:25 UTC+OOOO
0x86251bf0 dllhost.exe
400
480
15
196
2023-02-20
19:01:26 UTC+OOOO
 DeaoCa
E7eo
Woc
Ece5
Cnn
Toc7
57
WTC LCCcn]


And to find the total of the proccess, we need to use `wc -l` command and the result must be substracted by 2 because we don't need to count the header


[Image extracted text: daffainfo@dapos:
$
vol.py
~f
/home/daffainfo/forensic/memdump.raw
-profile-Win7SPlx86_23418 pslist
WC
-1
Volatility Foundation Volatility
Framework
2.6.1
49]


```
47
```