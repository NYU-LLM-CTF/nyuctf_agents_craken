# Black Pandora
> Duncan just traded-off a device with a very promising price at a shop near the town. The seller is even more generous that he offers a program that can give Duncan a huge amount of money. Welp, Duncan is not really aware of the device's security so he just did what the seller tell him to do, and now there's an **annoying popup** that always get opened once he would like to **open a file directory**.

> Can you investigate what's happening on his device?

> Important Notes: Ignore the bitcoin stuff (like Kleopatra/GPG/bitcoin app/related files) as it's not related to the challenge.

## About the Challenge
We were given an image forensic challenge (on a memory). Additionally, we have received 5 questions that we need to answer correctly in order to obtain the flag.

## How to Solve?
In this case, im using Volatility 2 to do forensic on a memory. First, im gonna use `imageinfo` first to find the correct profile for this image. Here is the command I used to find the correct profile:

```shell
vol.py -f OdysseyVM-ded1be8a.vmem imageinfo
```


[Image extracted text: Volatility
Foundation Volatility
Framework 2.6.1
INFO
volatility.debug
Determining profile
based
on
KDBG search
Suggested Profile(s)
Win7SP1x64
Win7SPOx64
Win2oo8R2SPOx64 ,
Win2oo8R2SPlx64_24000
Win2oo8R2SPlx64_23418
Win2oO8R2SPlx64
WinTSP1x64_24000
WinTSPlx64_23418
AS Layerl
WindowsAMD6UPagedMemory (Kernel AS)
AS Layer2
FileAddressSpace
(/home/daffainfo/forensic/OdysseyVM-dedlbe8a . vmem)
PAE type
No
PAE
DTB
0x187000L
KDBG
Oxf8o0029fdOaOL
Number of Processors
Image Type
(Service Pack)
KPCR for
CPU
Oxfffff80002gfedooL
KUSER_SHARED_DATA
Oxfffff78OOOOOOOOOL
Image
date
and
time
2023-06-21
13:22.11 UTC+OOOO
Image Local
date
and time
2023-06-21
20:22:11
+0700]


As you can see, there are a lot of suggested profiles that you can use, but in this case im gonna use `Win7SP1x64`.  First im using `psxview` module to find hidden process, here is the output and the command when i used `psxview` module

```shell
vol.py -f OdysseyVM-ded1be8a.vmem --profile=Win7SP1x64 psxview
```


[Image extracted text: Ox000000007cc92650 ipconfig
exe
2956
True
True
False
True
False
True
False
2023-06-21
13.22.11 UTC+0OOO
0x000000007fb82060
cmd
exe
2948
True
True
False
True
False
True
False
2023-06-21
13.22.11
UTC+0000
0x000000007e7f4b30
csrsS
exe
360
True
True
True
True
False
True
True
Oxooooooo07dbb5b3o
csrss
exe
420
True
True
True
True
False
True
True
0x000000007fa036f0
conhost
exe
2916
True
True
False
True
False
True
False
2023-06-21
13.22.11
UTC+OOOO
0x000000007ff6d890
System
True
True
True
True
False False
False
0x00000000163e1310
smss
exe
268
True
True
True
True
False False
False
0x000000007d43c340
clickheretoget
328
False
True
False
False
False False
False
2023-06-21
13.21:57
UTC+0000]


Hmmm there is a proccess called `clickheretoget....`. It looks like the name program has been truncated. Let's see the full name using `filescan` module. Here is the command I used to find the full name of the suspicious program

```shell
vol.py -f OdysseyVM-ded1be8a.vmem --profile=Win7SP1x64 filescan | grep "clickhere"
```


[Image extracted text: daffainfo@dapos
Iforensic$ vol
~f
OdysseyVM-dedlbe8a
vmem
profile-WinZSPlx6u filescan
grep
"clickhere"
Volatility
Foundation Volatility
Framework
2.6.1
0x000000007d0765b0
R-~r-d
IDevice| HarddiskVolumell Users| USER| Desktoplclickheretogetmoney
exe
daffainfo@dapos
forensic$]


The file name is `clickheretogetmoney.exe` and now we need to dump it. But I failed when I want to dump the proccess. So, the next thing I want to do is print list of loaded dlls for each process (Especially clickheretogetmoney process). So im using `dlllist` module just hoping there is `clickheretogetmoney` proccess

```
vol.py -f OdysseyVM-ded1be8a.vmem --profile=Win7SP1x64 dlllist | grep "Money"
```


[Image extracted text: daffainfo@dapos:
Iforensic$
vol.py
OdysseyVM-dedlbe8a
vmem
~profile-Win7SPIx64 dlllist
grep
"Money"
Volatility Foundation
Volatility Framework 2.6.1
0x000007fef7580000
Oxibooo
Ox1
2023-06-21
13.21.57 UTC+OOOO
C:|Windous| System32"
Money
UwU. dll
daffainfo@dapos:~/forensic$]


But hey, there is a DLL file called `Money_UwU.dll`? Interesting, lets try to dump the dll file using `dumpfiles` module

```
vol.py -f OdysseyVM-ded1be8a.vmem --profile=Win7SP1x64 dumpfiles -r money -i --dump-dir dumpdir/
```


[Image extracted text: daffainfo@dapos:~/forensic$ vol.py
~f OdysseyVM-dedlbe8a _
vmem
profile-WinSPIx6u dumpfiles
~T money
dump-dir dumpdir/
Volatility
Foundation Volatility
Framework
2.6.1
ImageSectionobject
Oxfffffa80043cd070
1776
IDevice| HarddiskVolumell Windows| System32 | Money_UwU.dll
DataSectionObject
Oxfffffa80043cd070
1776
IDevice| HarddiskVolumel
Windows| System32
Money
UwU. dll]


And now, upload the file into `tria.ge`


[Image extracted text: epot
Unregister,
abl_ UseCompr 
Zeus Shop Offer
Thank you for purchasing the laptop from Zeus Shopl we also have some great
reward for you: Please launch clickheretogetmoney exe
your Desktop: This
program will transfer 500 dollars to
registered bank account and it's freel
Hid ,
Exportmp .
itgp SaveUnpro 
Your]


The popup title is `Zeus Shop Offer`


[Image extracted text: 1
What
is the
title of
the
popup message
that
appear when
the
user
opens
File Explorer?
Format
Message
Title
Ex:
This Is
The
Title
>>:
Zeus Shop Offer
Correct!]


For question number 2, we already got the answer by using `psxview` and `filescan` module before


[Image extracted text: 2
Duncan
said
he
double-clicked
the
file
before
the strange
popup
in his
device
appear
when
he
tries
to
open
the
file
irectory
Do
you know
the
name
of
that
executable file?
How
many timeCs)
did
he
execute
it?
Format
name
exe_thetotalofexecution
Ex: spiderverse.exe_14
>>:
clickheretogetmoney.exe_1
Correct!]


For question number 3, we can use `pstree` module to find the PID and the parent PID. Here is the command I used to obtain the pid and ppid

```shell
vol.py -f OdysseyVM-ded1be8a.vmem --profile=Win7SP1x64 psscan
```


[Image extracted text: 0x000000007d423340 taskhost
exe
1212
512
OxOOOOOE
0x000000007d42bb3o
svchost
exe
704
512
OxOOOOOE
0x000000007d43c340 clickheretoget
328
1776
Oxoooooe
0x000000007d46ab30
svchost
exe
756
512
Oxoooooe
Oxooo000007d4bflfo
VGAuthService
1320
512
OxOOOOOE
Ox000000007d4cd350
dwm
exe
1764
844
OxOOOOOE]


The PID is 328 and the PPID is 1776


[Image extracted text: 3 .
What
the
PID
PPID
of
the malicious
executable respectively?
Format
PID_PPID
Ex:
2256_1141
>>
328_1776
Correct!]


For question number 4, has been answered by one of the team member, he debug the dll file and find the actual MD5 hash


[Image extracted text: There
malicious
code
execution
which generally
known
as
shellcode
However it
was
encrypted _
Please provide
the **decrypted** shellcode (excluding the padding
after the decryption)
in
MDS
hash!
Ex:
e5433ad8e560ec4fd18ef28168b2c6ff
>>:
966c4ccd355c25eb79973303865a65fa
Correct]


For question number 5, im using dynamic analysis approach, so I upload the DLL code into Virustotal, and you can find the attacker's IP and port on the behaviour menu


[Image extracted text: Network Communication
IP Traffic
13.37.73.137:4269 (TCP)
8.253.133.248.80 (TCP)]


The IP and the port is `13.37.73.137:4269`


[Image extracted text: 5 .
Related
to
the previous question
there
reverse
shell attempt
Although
the
attacker
host
is already
down
can
you provide
the information
about which
IPv4 and
the port
does
the
att
acker
use?
Format
ip.ip.ip.ip:port
Ex:
192.168.1.23
2564
>>
13.37.73.137.4269
Correct!]


And voilà, you obtain the flag


[Image extracted text: I hope you
didn't
brute
force
the
last question
>:u
anyway
you
re
so good !
Here
s your
flag{th3_pUndOr4_!s_finully_clOsed_
pepega:}
^C
flag]


```
flag{th3_p4nd0r4_!s_f1n4lly_cl0sed_:pepega:}
```