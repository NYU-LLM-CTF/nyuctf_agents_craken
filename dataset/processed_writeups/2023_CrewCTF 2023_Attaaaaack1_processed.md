# Attaaaaack1
> One of our employees at the company complained about suspicious behavior on the machine, our IR team took a memory dump from the machine and we need to investigate it.

> Q1. What is the best profile for the the machine?

> example : crew{Profile}

## About the Challenge
We got `raw` image and we need to find the profile using Volatility2

## How to Solve?
To solve this, we need to find the best profile using `imageinfo` plugin. Here is the command I used

```
vol.py -f /path/to/memdump.raw imageinfo
```


[Image extracted text: daffainfo@dapOs:~$ vol.py
~f
/home/daffainfo/forensic/memdump
raw
imageinfo
Volatility Foundation Volatility
Framework
2.6 _
INFO
volatility debug
Determining profile
based
on
KDBG search
Suggested Profile(s)
Win7SP1x86_23418
Win7SPOx86
Win7SP1x86_24000
Win7SPlx86
AS Layerl
IA32PagedMemoryPae
(Kernel
As)
AS Layer2
FileAddressSpace
(/home/daffainfo/forensic/memdump.raw)
PAE
type
PAE
DTB
Ox185000L
KDBG
Ox82b7ab78L
Number of
Processors
Image Type
(Service
Pack)
KPCR for
CPU
Ox8ob96000L
KUSER_SHARED_DATA
OxffdfooooL
Image
date
and
time
2023-02-20 19:10:54 UTC+OOOO
Image
local
date and time
2023-02-20 21:10:54 +0200]


```
crew{Win7SP1x86_23418}
```