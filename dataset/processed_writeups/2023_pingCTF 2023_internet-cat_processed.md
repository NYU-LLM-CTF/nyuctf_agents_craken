# internet-cat
> I heard that there are is no official nc for windows and I love this OS! Fortunately, my black hat hacker colleague has sent me his forged copy that he intercepted from other hackers which have intercepted it from others and that from others... I don't know how many times it was intercepted but it works! I have tested it on my Windows 10 and it works like a charm!

## About the Challenge
We were given a file called `80295df3cfa79de08064ddffed0deff5.zip` (You can download the file [here](880295df3cfa79de08064ddffed0deff5.zip)). Here is the preview of the program

## How to Solve?
If you upload the file to an online malware sandbox (in this case, I am using https://www.hybrid-analysis.com/), you will receive a base64 string.


[Image extracted text: 1
"6"
ILDI
AIl Strings (246)
Interesting (131)
ncexe
(198)
ncexe:1428 (43)
screen_Ipng (3)
screen_Opng (2)
JJv_RegisterClasses
AddressFamily
G.hi lLno ps:tuvwz
AFNOSUPPORT
aHROcHM6Ly9naXNOLmdpdGhYnVzZXJjbZSOZWSOLmNvbS9ObZlIlazc2NjcvOTIzOTNhNTkyMDdkOTEzNzlmOWVIODcANTgBOGISOGlvcmF3LzNiNTMINzJjMzQONTYOZjMyMTESNjASMm
MzMzg2MZEzODVjMTMZMZQvZZIzdGZpbGUxLnRAdA==
API-MS-Win-Security-SDDL-LI-1-O.dll
Can't get socket
Can't
%s:%d with bind
Can't parse %s as an IP address
ade:g_
grab]


Decode it using `base64` encoding and you'll get a GitHub gist

```
https://gist.github.com/tomek7667/92393a59207d91379f9ee8785878b98b/e3dc6bb2fed39c0f9d3a74b30af09394174ef78c
```

If you open the GitHub gist, you'll see `Nothing to see here, move along.` msg. But there are 2 revisions here, open the first revision and you'll get a list of numbers


[Image extracted text: tomek7667 / gist:92393a59207d91379f9ee8785878b98b
Secret
Subscribe
Star
8 Fork
Last active 13 hours ago
Report abuse
Code
0
Revisions
2
Embed
<script src-"https://
Download ZIP
Only magicians can decipher this
gistfilel.txt
Raw
1
116
2
124
3
105
4
147
5
116
6
104
7
131
8
147
9
116
10
152
11
111
12
147
13
116
14
104
15
143
16
147
17
116]


And then upload to cyberchef and then use this options:
* Octal
* Base64
* Hex
* Base58
* Render Image
* Parse QR Code

And you'll get another URL


[Image extracted text: Recipe
Input
A-La-Zu-Y
116
File details
124
Remove non-alphabet chars
Strict mode
105
147
116
104
From Hex
131
147
Delimiter
116
Auto
152
Name:
gistfile1.txt
111
Size:
92,462 bytes
From Base58
147
Type:
unknown
116
Loaded: 100%
Alphabet
104
123456789ABCDEFGHJKLMNPQRSTUVWXYZ
143
AbC
92462
23140
TT
Raw Bytes
Remove non-alphabet chars
Output
0J
https: / /privatebin. io/?
Render Image
1cSga5beffe3a844#FHZGExP62PJVJGdZTBku77R16TsWpGzshD8ULzVaSfUm
Input format
Raw
Parse QR Code
Normalise image]


Open the URL and you got another string

```
UEsDBBQACQBjABpciVcFV6wiRQAAACcAAAAIAAsAZmxhZy50eHQBmQcAAQBBRQMIAOqNoUX0Z5cij1J6uViuJOT+jLbo0Tibnbs0x++zz1pfItBmkkebOjEsVMVAxWFcUO8yYdA4CXgjEECKzi+mBqdI+rjACFBLBwgFV6wiRQAAACcAAABQSwECHwAUAAkAYwAaXIlXBVesIkUAAAAnAAAACAAvAAAAAAAAACAIAAAAAAAAZmxhZy50eHQKACAAAAAAAAEAGAATmwIRiyraARObAhGLKtoBNqEVIIcq2gEBmQcAAQBBRQMIAFBLBQYAAAAAAQABAGUAAACGAAAAAAA=
```

Decode it again using `base64` encoding and you will receive a password-protected zip file. Crack it using john


[Image extracted text: Using
default
input encoding:
UTF-8
Loaded
1 password
hash
(ZIP ,
Winzip
[PBKDF2-SHA1
128/128
ASIMD
4x] )
Cost
(HMAC
size)
is
41
for
all
loaded
hashes
Will
run
8
OpenMP
threads
Press
'q
or
Ctrl-C
to
abort,
almost
any
other key
for
status
billabong
download
zip/
txt)
1g
0:00:00:00
DONE
(2023-12-10
12:03)
7.142g/s 58514p/$
58514c/s
58514C/s 123456
whitetiger
Use
the
~~show
option
to
display
all
of
the
cracked passwords reliably
Session completed _
flag]


Enter the password and voilà!

```
ping{u_w4nt3d_f0r3n51C5_4nD_y0u_g0t_17}
```