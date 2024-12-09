# EnableMe
> You've received a confidential document! Follow the instructions to unlock it.

> Note: This is not malware

## About the Challenge
We got a document file called `invoice.docm` (You can download the file [here](invoice.docm)) and when we attempted to open it, an alert appeared stating that our device has been hacked


[Image extracted text: Cul
Fino
A 4"
Aa
Replace
aste
B I W - 4 * * &7 - A -
38a
Change
Format Painter
Styles
Selec
Clipboard
Font
Paragraph
Styles
Editing
Please click enable content to see your full document @
Microsoft Word
YOU HAVE BEEN HACKEDI Just kidding :)
Ok
0
Copy]


## How to Solve?
Detect the file first using `oleid`. Here is the command

```bash
oleid invoice.docm
```


[Image extracted text: Filename:
invoice
docm
WARNING
For
now ,
VBA
stomping
cannot
be
detected
for
files
in memory
Indicator
[Value
Risk
Description
File
format
MS Word
2007+
Macro-
info
Enabled
Document
(.docm)
Container
format
OpenXML
info
(Container
type
Encrypted
False
none
The
file
is
not encrypted
VBA Macros
Yes
Medium
This
file
contains
VBA
macros
No
suspicious
keyword
was
found
Use
Iolevba
and
mraptor
for
more
info _
XLM
Macros
No
none
This
file
does
not
contain
Excel
L/XLM
macros
External
none
External relationships
Relationships
such
as
remote
templates ,
remote
OLE
objects,
etc]


Hmm, there's a VBA Macros script? Let's extract it using `olevba` command:

```
olevba invoice.docm
```


[Image extracted text: Sub AutoOpen( )
Dim
V6
As
Variant,
v7
As
Variant
V6
Array(98 ,
120 ,
113,
99 ,
116 ,
99 ,
113,
108 ,
115 ,
39 ,
116 ,
111
72 ,
113 ,
38 ,
123 ,
36 ,
34 ,
72 ,
116 ,
35 
121,
72 ,
101,
98 ,
121,
72 ,
116 ,
39
115 ,
114,
72 ,
99
39 ,
39 ,
39 ,
106 )
v7
Array(44 ,
32 ,
51,
84 ,
43 ,
53 ,
48 ,
62 ,
68 ,
114,
38 ,
61,
17 ,
70
121,
45 ,
112 ,
126 ,
26 ,
39 ,
21,
78 ,
21,
7 ,
6 ,
26 ,
127 ,
8 ,
89 ,
0 ,
1, 54,
26 ,
87 ,
16 ,
10 ,
84 )
Dim
v8
As Integer:
v8
23
Dim
v9
As
String,
V10
As
String,
v4
As
String,
1
As Integer
v9
For
To
UBound (V6 )
v9
v9
&
Chr(v6(i)
Xor
Asc (Mid(Chr(v8) ,
(i
Mod
Len(Chr(v8) ) )
1,
1) ) )
Next
V10
For
To
UBound (v7 )
V10
V10
&
Chr(v7(i)
Xor
Asc (Mid(v9 ,
(i
Mod
Len(v9 ) )
1,
1) ) )
Next
MsgBox
V10
End
Sub
VBA
MACRO
Modulel.bas
in
file:
word/vbaProject.bin
OLE
stream:
VBA
Modulel
empty
macro)
4
Type
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
Chr
May
attempt
to
obfuscate
specific strings
(use
option
~~deobf
to
deobfuscate)
Suspicious
Xor
May
attempt
to
obfuscate specific strings
(use option
~~deobf
to
deobfuscate)]


Change the `MsgBox v10` to `MsgBox v9` to print the flag or you can run this Python code (I asked ChatGPT to convert the VBA script to python :D)

```python
def auto_open():
    v6 = [98, 120, 113, 99, 116, 99, 113, 108, 115, 39, 116, 111, 72, 113, 38, 123, 36, 34, 72, 116, 35, 121, 72, 101, 98, 121, 72, 116, 39, 115, 114, 72, 99, 39, 39, 39, 106]
    v7 = [44, 32, 51, 84, 43, 53, 48, 62, 68, 114, 38, 61, 17, 70, 121, 45, 112, 126, 26, 39, 21, 78, 21, 7, 6, 26, 127, 8, 89, 0, 1, 54, 26, 87, 16, 10, 84]

    v8 = 23

    v9 = ""
    for i in range(len(v6)):
        v9 += chr(v6[i] ^ ord((chr(v8)[(i % len(chr(v8)))]) ))

    v10 = ""
    for i in range(len(v7)):
        v10 += chr(v7[i] ^ ord((v9[(i % len(v9))])))

    print(v9)

# Call the function
auto_open()
```

## Flag
```
uoftctf{d0cx_f1l35_c4n_run_c0de_t000}
```