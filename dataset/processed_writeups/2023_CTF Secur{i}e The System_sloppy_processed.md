# sloppy

> So, I found an USB in my class, I took it and I put it in my laptop. Then i found interesting anime (the anime is in mp4) and rar file and I copied it on my laptop. When i tried to open the file it showed pop up that my computer has been comprimized and my laptop restared after 1 minutes and I immediately remove all file that've been copied to my computer. As an engineer i always capture usb traffic using wireshark. Please help me to figure out what's happening in my laptop.

> [download](https://drive.google.com/file/d/1JFQ2p1tRGp_s1rrHWX6glHP2r4nftjR7/view?usp=sharing)

> wrap your flag with STS23{`<value>`}

## About the Challenge
We were given a pcapng file (You can download the file using the link above), and we need to find the flag inside the packet capture file


[Image extracted text: Time
Source
Destination
Protocol
Length| Leftover Capt | Info
9J
Luzj-11-Zo
V0;J4; 1J,ZJ/IU
IIUS L
L.21
UJD
UnD
DULN
LII
94
2023-11-26 06:54:15
291732
2.2.1
host
USBMS
40
SCSI: Response
LUN:
Ox0o
(CDB: Oxa2)
(Check Condition)
95
2023-11-26 06:54:15.291734
host
2.2.2
USBMS
58
SCSI:
Request Sense LUN: Ox0o
96
2023-11-26 06:54.15.291757
2.2.2
host
USB
27
URB_BULK out
97
2023-11-26 06:54:15.291758
host
2.2.1
USB
27
URB_BULK
in
98
2023-11-26 06:54:15
291804
2.2.1
host
USBMS
45
SCSI:
Data
In LUN: Ox00 (Request Sense Response Data)
99
2023-11-26 06:54:15.291805
host
2.2.1
USB
27
URB_BULK
in
100
2023-11-26 06:54:15.291857
2.2.1
host
USBMS
40
SCSI: Response LUN:
Ox00 (Request Sense)
(Good)
101
2023-11-26 06:54:15
291899
host
2.2.2
USBMS
58
SCSI: Inquiry
LUN:
0x00
102
2023-11-26 06:54:15.291921
2.2.2
host
USB
27
URBBULK out
103
2023-11-26 06:54.15.291923
host
2.2.1
USB
27
URBBULK
in
104
2023-11-26 06:54:15.291973
2.2.1
host
USBMS
63
SCSI:
Data
In LUN:
Oxoo (Inquiry Response Data)
[SCSI transfer limited due to alloca
105
2023-11-26 06:54.15.291973
host
2.2.1
USB
27
URBBULK
in
106
2023-11-26 06:54:15.292027
2.2.1
host
USBMS
40
SCSI:
Response LUN:
Ox00 (Inquiry)
(Good)
107
2023-11-26 06:54:15.292038
host
2.2.2
USBMS
58
SCSI Command:
0x23 LUN: Ox00
108
2023-11-26 06:54:15.292057
2.2.2
host
USB
27
URB
BULK out
109
2023-11-26 06:54:15.292058
host
2.2.1
USB
27
URBBULK
in
110
2023-11-26 06:54:15.292383
2.2.1
host
USB
27
URBBULK
in
111
2023-11-26 06:54:15.292392
host
2.2.1
USB
27
URB_FUNCTION_SYNC_RESETPIPE
AND_CLEAR_STALL
112
2023-11-26 06:54:15
292582
2.2.1
host
USB
27
URB_FUNCTION_SYNC_RESETPIPE_AND_CLEAR_STALL
113
2023-11-26 06:54:15.292584
host
2.2.1
USB
27
URB_BULK
in
114
2023-11-26 06:54.15.292603
2.2.1
host
USBMS
40
SCSI:
Response LUN:
Ox00 (CDB: 0x23)
(Check Condition)
115
2023-11-26 06:54:15.292604
host
2.2.2
USBMS
58
SCSI:
Request Sense
LUN: 0x0o
116
2023-11-26 06:54:15
292628
2.2.2
host
USB
27
URB_BULK out
117
2023-11-26 06:54:15.292629
host
2.2.1
USB
27
URB_BULK
in
118
2023-11-26 06:54:15.292682
2.2.1
host
USBMS
45
SCSI:
Data
In LUN:
Oxoo (Request Sense Response Data)
119
2023-11-26 06:54:15.292683
host
2.2.1
USB
27
URBBULK
in
120
2023-11-26 06:54:15.292731
2.2.1
host
USBMS
40
SCSI: Response
LUN:
Ox00 (Request Sense)
(Good)
Frame 1:
36
bvtes
on wire
(288 bits)
36 bvtes
captured
(288
bits)
on
interface
L  USBPcanz
id]


As you can see, there are USB and USBMS protocol in the packet capture file

## How to Solve?
As we can see, there are a loot of usbms protocol and the author mention about "rar" file. So im using this command to extract every file and then put it into a JSON file

```bash
tshark -T json -x -Y usbms -r chall.pcapng > usbms.json
```

And then I tried to find a rar file using `grep` command (Rar! == 52617221)

```bash
cat usbms.json | grep '"52617221'
```

Okay we found it, and then I submitted the hex code into CyberChef


[Image extracted text: Recipe
Input
526172211a070100f3e182eb0b0105070006010180808000d066d8084302030bdb0404d60e20de2641f
From Hex
4800300276578616d5f616e73776572732e747874202f6578616d5f616e73776572732e747874202e62
61740a0302a010cf7a0c1fda01cec157023064433333f46054f7a05e0e430151686208895fb80102d8c
Delimiter
416465d160703968a185028d272615d49851c945bel3ba5a34b8f4929949575393883f068eeee661cd3
None
a91e41b874e9d3bf9cdccfb33d7ee27fdfe7a3267ecf3f9bd8d68c5c59f97270f7c316f42e34d7362e2
c199313dbc56aff2511928cb18cced485be88ebe335f6b289f73f1e92618cfefeb8d4770015c4911f5e
9f77d3f75cb7532bf36002a0fb7e2c486d073c7c9cblfca3f68ab2d2d7b7caeea302e3cc8af25860191
el3b7ab3bl7e97dc734791aa520bc817a6045258d53a434d50556f9426c29795470a62995a14944ee92
929efdcd131db070eb5932d87ff80e9f9b5abc7a41f3cc1078fb6c272a16259a837064adddeee529eSb
aa463f4839b82ce9dc433c764fba01f3fdf5b2f8836b93709e843447d1e0a66eeee6314ecf576e870d7
77619cf2072e38aa4cf9fa06a892a7c34aff323380e83c0f84010844056eaf050d7cae6aee83c0f8401
08548c6036c62eae603220be295bf85096525e67d63e17f1635c0ab0d19596fd5e62451266c7f15409f
78e4a68d9c02c08c7f36569e5468b612alec77d5a55d4fa91489d857a26a58030dd13e3c358a9ef1383
baa775898ac3725a69359d9ed4f588da089546635c3c7a855f7d35df1f51af291a5e4c103807a9db5d5
8fd5162c7264aa0529d15ce62eddb04ff1c55be55293db44d34f6ced3635ed3f930653d367802a98b76
ca491797b6afd929ad8f291985c8fb6clff557ee76b77b6ecSaf23899df1b377d93d28e24e892d8d5ba
3ca77c9210e2debSdf9aee993d644d6bc90ac7d0eb117d9369aab48983864dd7eea108cf89094f2d020
abC
2048
5
TT
Raw
Bytes
LF
Output
Rar!
SUB
NUL
6a-ev
SOH
ENQ
BEL
NUL
ACK
SOH
SOH
NUL
Dfe
C sx
Erx VU
EOT
EOT
PGAo
ETX
NUL
exam
answers.txt
Iexam_answers.txt
bat
STX
DLE
izF
U
SOH
IAw
STX
0dC336 ` T+
C
SOH
Qh 2
SOH
BA
SYN
K]
SYN
ETX
CAN
P(ort]i:
[a;YEK-I)
u98 dhiif
0@
A,teoz Ufa_~a BcES~f?-p-|Yurp-A
SYN
6 . 4x6 .
DC?
UAjys
+'I0.4 ea5o2
+2
a
pp, Ow
NUL
NAK
A
wO+|
S+6
U~ , Hm B < |
tufo. 20x Eifsaf 
oX
DC3
<;
ETB
e}C4y sY 4
2
E%" Sn40
ENQ
VuBL)yTp} ) =
IDi
yi
DC?
peyze-
ZzA6f
DLE
xul' *
SYN
%
pd Yia) 39.co-
1
A3cdd
?6 [/+;17
eCD}
fiic
DC4
iovepxwa -
0
8aLuu
SAJy23*e<
ENQ
n
ENQ
eleji Ag@-
DLE
HE
Ubea
ETX
"va' 1
esa}ca
SYN
SAk?
YoOasqcl
xa {
STX
A
'6V-Thl
DCZ
iwor]o@
DC4
@WcjX
ETX
RN-<5-.f8; awXe-7%}
YUiOx
TfSAc"U+0]no
SUB
YaA
ETX
2
po-6
SYN
rda
ENQ
)NIa. %?OfA [aR-UDOOli65i? 'SOg
x
lx
y{jy
Aa
730
6pLR
HM
ACK]


As you can see, there is a file with a `.bat` extension—hmm, weird. If you analyze the RAR file, this is the payload for `CVE-2023-38831`. And then I extracted the bat file and submitted into a sandbox malware online platform


[Image extracted text: Processes
C:IWindowslsystem32lcmd.exe
cmd
Ic
"C: |Users| Admin| AppData |Local | Temp | exam_answers
txt
bat
C:IWindowslsystem32lreg exe
reg
add
HKCU | SoftwarelMicrosoft
Windows | CurrentVersion| Run
Iv
whatisthis"
It
REG_SZ
Id
COmPremIzed_d3sktop_h3h3
If
C:IWindowslsystem32lshutdown exe
shutdown
Fr
-t
60]


```
STS23{C0mPrem1zed_d3sktop_h3h3}
```
