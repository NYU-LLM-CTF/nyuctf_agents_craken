# pemanasan

> Is that a `qrcode`? why is it so big?

## About the Challenge
We were given a rar file (You can downlod the file [here](pemanasan.rar)). Inside the file, there were 2 files which is `whatistheDIFFerent` (Contain the diff between the new qr and old qr image) and we got `qr.new`. If we parse the qr new we got `Lorem ipsum ....` string


[Image extracted text: Recipe
Input
PNGS
Render Image
File details
SUB
NUL
NUL
NUL
RIHDR
NUL
NUL
ENQ
NUL
ACK
ACK
NUL
NUL
DC?
I
NUL
NUL
F?iCCPICC
Profile
NUL
NUL
Input format
H'
W
XSE
DLE
NUL
RBh
SOH
X ETB
AFH =
STX
DCZ
C
@Et kea VODU
A
Raw
ERQ
E
DC4
V 
i
ERQ
e]
7)
exol6}si*y96
ETX
NUL
iSW,1C5
NUL
E
ETB
NAK
JaA-
CAN
ESO
CAN
xS
NUL
ENQ
ETX
4aAa
NAK
Yttq
NUL
Uauioi:o vAQ oipyj
IA
SOH
NUL
$saf
Parse QR Code
SOH
ac
NUL
tx
DLE
NUL
ab
EOT
&
jB
IRa]
IPa}r-Ax6A_
NUL
q1
NUL
0; f(aeAR6>
El
NUL
SUB
ETX
byuue | -6!>beeuf
t2p}
1Eafc
aAla}
DCZ
DLE
cqsp agk
ak ZIs<^6gX'
Dca
#eXea QFt#Az
DLE
DLE
oap
Normalise image
DLE
f lix
A
5a
ai
Aile
DLE
oGfv |F{0 
ETX
1| !e
DC4
a!
b}
Bocz
>
%oa tD?L
Yafq%, 2X+Y1I,#bel
SOH
Go 
ET8
9 ' {@L'02H*
St:AN
ENQ 1
J
AuieA
4^. i%Af
QX B
+E
E+yKo
ACK
cemf
SYN
rc g@avb_
c>X
va+i
I
ENQ
e
DLE
XI
NQ sak C
DC4
sC
DI
J 
aA
xAx "f
Uuaz 40
Name:
Screenshot 2023-
#{AQ
xB
1
DC4
ETB
ESxoA
5
t" |de
12-18 at 21.17.48.
AO
NUL
)1
E
SOH
Aopu^xye
ENQ
SOH
Y@
NUL
fa
DC4
y
DC3
@1o
DC?
SOH
CAN
SUB
png
ETB
Si
b
GG')i
ENQ
0
I
BEL
~Ka EDCN- AcE
ESC
2
Ci7o:
152 R55 hitec
ABC
152855
97
TT
Raw Bytes
LF
Output
LLorem
ipsum
dolor
sit
amet_
consectetur adipiscing
elit. Quisque
nec risus
nec
urna
feugiat
pharetra _
Phasellus
sollicitudin
consectetur
commodo .
Ut
lacinia
risus
vitae
euismod
tincidunt_
Mauris porta
metus
id
libero ullamcorper venenatis_
Phasellus posuere
interdum
ipsum
vel
dictum.
Integer
ac
ipsum sollicitudin,
dapibus
elit
nec,
hendrerit
arcu.
In tincidunt
dolor
sit
amet
ornare fermentum.
Vivamus
varius
lacinia velit,
nec
ornare
erat egestas
vitae.
Quisque aliquet
felis
ut
mi
malesuada_
ut
accumsan
tellus tempor.
Praesent
tincidunt
massa
in
dolor aliquam
aliquam.
Etiam
at magna
commodo ,
venenatis turpis sed, porta
lorem.
3cl--
npSAF]


## How to Solve?
Use `patch` command and then parse the QR code again to obtain the flag

```bash
$ patch qr.new -i whatistheDIFFerent 
patching file qr.new
Reversed (or previously applied) patch detected!  Assume -R? [y] y
```

[Image extracted text: Recipe
Input
PNGS
Render Image
File details
SUB
NUL
NUL
NUL
RIHDR
NUL
NUL
ENQ
NUL
NUL
ACK
SUB
ACK
NUL
NUL
yy.2
F?iCCPICC Profile=
NUL
Input format
H'
W
XSE
DLE Q
NUL
RBh
SOH
X ETB
AFH
STX
DCZ
C
'@Et k
ET8
VPDU
A
Raw
E
DC4
Va
1
ERQ
e],0.7)
ex0l6}si y96
ETX
iSW,iC5
NUL
E
NAK
JaA-
CAN
ESO
CAN
xS
NUL
ENQ
ETX
4aAa
Yttq
NUL
Uauioi:o vAq{6ipyj
IA
SOH
NUL
$ saf
Parse QR Code
SOH
ac
NUL
a
<tn
DLE
NUL
4
ab
EOT
&
jB
IRa]
iPa}r Ax6A-
NUL
q1
NUL
0; f(aeAR6>_
Eli
SUB
ETX
byuie | *6!zbeuf
t2p}
1Eafs
aAla}
DCZ
DLE
cqsp aok
ak'ZIs<^6gX 
Dca
#eXea QFt#AZ
DLE
DLE
oap
Normalise image
DLE
f
lix
A
5a
af
.Ai
DLE
oGfv |F{0.
ETX
1| !e
DC4
a!
b}
ETB
3
DCZ
% bca
a
tDeL
Yafq%o, 2X+Y1I,#bel
SOH
Go 
ET8
g ' {@L'@2H.
St:AN
ENQ
J
AuieA
4^. i%An
STX
QX-B
+E
E+yKoy
ACK
cemf
SYN
rc g@avb_
c>X
%a+i
I
ENQ
DLE
XI-
~NQesay-C
DC4
sC
DI
J 
aA
xAx "f-Uuaa 40
Name:
Screenshot 2023-
#{AQ
ETB
xB
1
DC4
ESxoA-s _
t" |de
12-18 at 21.20.33.
AO
NUL
)1
SOH
Aopu^xye
ENQ
SOH
Y@
NUL
fa
DC4
y"
DC3
@1o
DC?
SOH
CAN
SUB
png
ETB
Si
NAK
E
b
NAK
GG )i-
ENQ
0
I
BEL
~Ka EDCN- AcE
ESC
2
BEL
Size:
172 FRR hutec
ABC
172668
209
TT
Raw Bytes
LF
Output
Lorem
ipsum dolor
sit amet,
consectetur adipiscing
elit. Quisque
nec
risus
nec
urna
feugiat pharetra_
Phasellus
sollicitudin consectetur
commodo .
Ut
lacinia risus
vitae
euismod
tincidunt_
Mauris porta
metus
id
libero ullamcorper
venenatis.
Phasellus posuere
interdum
ipsum
dictum. Integer
ac
ipsum
sollicitud-
dapibus
elit
nec,
hendrerit
arcu.
In tincidunt
dolor
sit
amet
ornare fermentum_
Vivamus
varius
lacinia velit,
nec
ornare
erat egestas
vitae
Quisque aliquet
felis
ut
mi
malesuada _
ut
accumsan
tellus
tempor.
Praesent
tincidunt
massa
in dolor aliquam
aliquam.
Etiam
at magna  commodo,
venenaSTS23{really_big_qr_isnt_It}
3cl-
npSAF
vel
in,]


```
STS23{really_big_qr_isnt_it}
```