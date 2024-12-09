# Encrypt10n
> We made a memory dump on the criminal machine after entering the crime scene. Our investigator thought he was using encryption software to hide the secret. can you help me to detect it?

> Q1 : crew{password}

## About the Challenge
We got `raw` image and we need to find the password of an encrypted file

## How to Solve?
To solve this, we need to find the best volatility profile first using `imageinfo` plugin. Here is the command I used to find the profile

```
vol.py -f /path/to/dump.raw imageinfo
```


[Image extracted text: daffainfo@dapos:
dumpdir$
vol .py
~f
/home/daffainfo/forensic/dump
raw
imageinfo
Volatility Foundation Volatility
Framework
INFO
volatility.debug
Determining profile
based
on
KDBG search
Suggested Profile(s)
Win7SP1x86_23418
Win7SPOx86
Win7SP1x86_24000 _
Win7SPlx86
AS Layerl
IA32PagedMemoryPae
(Kernel
As)
AS Layer2
FileAddressSpace
(/home/daffainfo/forensic/dump.raw)
PAE
type
PAE
DTB
Ox185000L
KDBG
0x82b3db78L
Number of
Processors
Image Type
(Service
Pack)
KPCR for CPU
0x839a5000L
KUSER_SHARED_DATA
OxffdfooooL
Image date
and
time
2023-02-16
12:03:16 UTC+OOOO
Image
local
date
and
time
2023-02-16 14:03:16 +0200]


Now we need to check the process list first using `pslist` plugin. Here is the command I used to check the process list

```
vol.py -f /path/to/dump.raw --profile=Win7SP1x86_23418 pslist
```


[Image extracted text: 0x85bc5398 wmpnetwk
exe
2632
496
11
212
2023-02-16 12:01.16 UTC+OOOO
Ox85bba030
WmiPrvSE
exe
2860
624
15
319
2023-02-16 12:01:25 UTC+OOOO
0x85c53030 WmiApSrv
exe
3004
496
112
2023-02-16
12:01:30 UTC+OOOO
Ox85c596c0 TrueCrypt
exe
3196
1384
67
2023-02-16
12:02:07 UTC+OOOO
0x84d54d20 sppsvc
exe
3736
496
6
154
2023-02-16
12:03:05 UTC+OOOO
0x84d567f0 svchost
exe
3776
496
15
353
2023-02-16 12:03:05
UTC+OOOO]


You will notice there is a process called `TrueCrypt.exe`. TrueCrypt is a disk encryption software. Now, we know the encryption software, and we need to find the password. Luckily there is a plugin called `truecryptpassphrase` to find the TrueCrypt password. Here is the command I used to get the TrueCrypt password


[Image extracted text: daffainfo@dapos
dumpdir$ vol.py
~f
/home/daffainfo/forensic
dump
raw
'~profile-WinTSPlx86_23418 truecryptpassphrase
Volatility
Foundation Volatility
Framework 2.6.1
Found
at
0x8d23de44 Length
20: Strooooong_Passwword]


```
crew{Strooooong_Passwword}
```