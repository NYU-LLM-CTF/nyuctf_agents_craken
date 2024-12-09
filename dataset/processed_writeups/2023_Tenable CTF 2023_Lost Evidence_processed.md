# Lost Evidence
> Someone hacked into our system and deleted most of the evidence we have against a certain group. All we have left is this seemingly random dump of garbage. See if you can uncover any secrets it may contain.

## About the Challenge
We were given a file called `lost_evidence` and we need to find the flag in this file

## How to Solve?
Initially, my team and I didn't know what this file was about. As I began searching for a specific string using the regex pattern `_.*_.*_` since flags typically involve underscore characters. I came across a peculiar text like this

```bash
strings lost_evidence | grep -E _.*_.*_
```


[Image extracted text: U_D_I]
k"yelsto"s{:0"
{ytep:"L"kuzs
"k"yes
zi"e6:
Ha""f{:t"py"e":ulsk"1"
tsirep"s4:00
Oh"sa"h":hs2a65}
raae
II MI
{ytep:"r"wa,
0"ffes"t":2367"8"
isez
"2"8540"8" , nercpyitno
"a"sex-stp-alniu6, "k"yes_zi"e6:}4" ,dk"f{:t"py"e":raog2ndi, "t"mi"e9:
emomyr
"018475, 6c"up"s4:
astl:"2"DoFZziJOfoBr6PIIWWFfnNTaoLztoiKqF6TrEvEGUD"=}} , }t"kone"s{: ,}s"geemtn"s{:0"
{ytep:"c"yrtp_
0"ffes"t":61772761
s"zi"e" :ydanim"c" , vit_ewka:"0"
"e"
cnyrtpoi"n" :ea-stx-slpia6n"4"
estcros_
zi"el:90}6, }d"gisest
MI MI
{"0{
t"py"e":bpdk2f , "k"yelsto"s[:0"]"", esmgnest
["0,Jh"sa"h"
hs2a65
"i"etaritno"52:9245,8s"La"t" : sFHil8xQAxhdTb/kkgCMTxBqSp
1BHZsVJqr/1DbhRg-k, "d"gise"t":u3GZJRFQjS995m/mVPRMTu0p92/cgncTcDzktzQtxw-o}
}c"noif"g{:j"os_nisez:"1"2288, "k"yelsto_sis
ez : "1"764444"8} }
k"yelsto"s{
0"
{ytep:"L"ku2s
"k"yes
zi"e6:
Ha""f{:t"py"e":ulsk"1"
tsirep"s4:00
Oh"sa"h":hs2a65}
raae
II M1
{ytep:"r"wa,
0"ffes"t"
2367"8"
isez
"2"8540"8" , nercpyitno
'a"sex-stp-alni46, "k"yes
zi"e6:}4" ,dk"f{:t"py"e":raog2ndi
"t"mi"e9:
emomyr
"018475, 6c"up"s4
astl:"2"DoFZziJOfoBr6PlIWWFfnNTaoLztoikqF6TrEvEGUD"=}} , }t"kone"s{: ,}s"geemtn"s{:0"
{ytep:
"c
"yrtp
0"ffes"t":61772761
s"zi"e" :ydanim"c"
vit_ewka
"0
"e"
cnyrtpoi"n" :ea-stx-slpia6n"4"
estcros_
zi"el:90}6, }d"gisest
{"0{
t"py"e":bpdk2f , "k"yelsto"s[:0"]"" , esmgnest
["0,Jh"sa"h"
hs2a65
"i"etaritno"52:9245,8s"La"t" : sFHil8xQAxhdTb/kkgCMTxBqSp
1BHZsVJqr/ DbhRg-k, "d"gise"t" :U3GZJRFQjS995m/mVPRMTuOp92/cgncTcDzKt3Qtxw-o}
}c"noif"g{:j"os_nisez:"1"2288, "k"yelsto_sis
ez : "1"764444"8} }]


What is this? It appears that the problem setter flipped every byte in this file. When we attempted to read the string, we found an interesting substring: `"type":"luks2"`. Based on this, we assumed that this forensic challenge involved a LUKS file and that we needed to recover it. Consequently, one of the team members created a Python code to flip every byte:

```python
with open("lost_evidence", "rb") as f:
	rawfile = f.read()

newfile = b""
print(len(rawfile))
with open("new_lost_evidence", "wb") as f:
    for i in range(0, len(rawfile), 2):
        newtwobytes = (rawfile[i+1].to_bytes(1, "big") + rawfile[i].to_bytes(1, "big"))
        f.write(newtwobytes)
```

And then we need to manually append `01` byte in the file (because the program wasn't perfect). And then use binwalk to find where is the LUKS file is


[Image extracted text: DECIMAL
HEXADECIMAL
DESCRIPTION
228746401
OxDA264A1
MySQL
MISAM index
file
268435841
Ox10000181
LUKS_MAGIC sha256
303324663
0x12145DF7
Nagra Constant_KEY
IDE]


The LUKS file located in `0x100000181`. In this case im gonna use binwalk again to extract the file

```bash
binwalk --dd='.*' new_lost_evidence
```


[Image extracted text: daffainfo@dapos
foren/
new_lost_evidence. extracted$
head
10000181
'D/OtBPkDe Ol>?mez{"keyslots"
{"0"
{"type
luks2"
size"
64
af": {"type
luksl"
stripes
4000 , "hash"
sha256"}
rea
{"type
raw
offset
32768
size
258048
'encryption
'aes-xts-plain64y"
size
'kdf"
{"type
argon2i
time"
'memory
1048576
cpus
'salt"
ZoDZFizOJofrBP6IlWwfFNnaTLo+zioqK6FrTvEGEDU="}}}
"tokens
{}
'segments" : {"
0"
{"type
crypt
offset
'16777216
size"
dynamic"
iv_tweak
'encryption"
aes-xts-plain6y"
'sector
size"
4096
}}
digests": {"0"
{"type
pbkdf2"
keyslots
["0"]
'segments
["0"]
hash"
sha256
iterations
229548
salt":"FsiH81q
xxAdhbTk/gkMCxTqBpSB1ZHVsqJ/rDlhbgRk="
digest
'3uZGRJQFSj99mSm/PVMRuTPO29c/ng cDcKz3ttQwxo="}} _
config" : {"json_Size"
12288"
'keyslots_size
'16744448
} } SKULo D@Dsha256eoDoM9ooNc}0o0
wX HDIJeemeDdoMo3Wa; evoDleeoB|ReoHezoABoFAec2ee7631-19d8
~409a-a3fe-ca35db8847a5@0Spoo
40<!'0
6o D/]eoOcepoDoI{"keyslots": {"0": {"type"
Luks2"
size"
64
'af": {"type"
'Luksl" , "stripes
4000 , "hash" :"sha256"}
ar
ea
{"type
raw
offset
32768
size
258048
'encryption
'aes-xts-plain6u"
size
64} , "kdf"
{"type
argon2id
time
'memory
1048576
cpus
'salt"
ZoDZFizOJofrBP6IlWwfFNnaTLotzioqK6FrTvEGEDU=" } }}
"tokens
{}
'segments
{"0
{"type
crypt
'offset
'16777216
size
'dynamic
iv_tweak
'encryption
'aes-xts-piain64"
'sector_Size
4096}
'digests" : {"0"
{"type
pbkdf2"
keyslots"
["0"], "segments" : ["0"]_
'hash"
sha256"
iterations
229548
salt":"FsiH8lQx
xAdhbTk/gkMCxTqBpSB1ZHVsqJ/rDlhbgRk=
'digest
3uZGRJQFSj99mSm/ PVMRuTPO29c/ng7cDcKz3ttQwxo="}},
config
{"json_size
key_
64}
key_
key_
key]


Okay we can recover the LUKS file, and then what? We need to find the master key of the LUKS file, in this case im gonna use `photorec`

```bash
photorec new_lost_evidence
```


[Image extracted text: daffainfoddapos
/foren/recup_dir.1$
cat
f0262144.txt
LUkS
header
information
for secrets
Cipher
name
aes
Cipher mode:
xts-plain6u
Payload offset:
32768
UUID:
c2ee7631-19d8-409a-a3fe-ca35db8847a5
MK bits
512
MK dump
6f f6 57
34 c4 c8 be
d1
14
ee
35
19 14 la 9
11
91
f8 75 2e
35
73
05 b6
94
a6 dc
ae
df c2
2f 0d
a3
4e 17
96
72
Of 2c ad
2d
le d8 Tc 16 b4
c4 Od
a5 97 ba
03
77
62 6b 80 24 Se be 81
4b 55 28
9a]


And luckily we found the master key, now we are gonna change the key into a file by running this command

```bash
print "6f f6 57 34 c4 c8 be d1 14 ee 35 19 14 1a 9b 11 91 f8 75 2e 35 73 05 b6 94 a6 dc ae df c2 2f 0d a3 4e 17 96 72 0f 2c ad 2d 1e d8 7c 16 b4 c4 0d a5 97 ba 03 77 62 6b 80 24 5e be 81 4b 55 28 9a" | tr -d ' ' | xxd -r -ps > key.bin
```

And then we need to set our custom password by running this command

```bash
sudo cryptsetup luksAddKey --master-key-file=key.bin new_file
```

And then mount the LUKS using `losetup` command

```bash
sudo losetup /dev/loop8 new_file
```

And in then open the LUKS using `luksOpen` command

```bash
sudo cryptsetup luksOpen /dev/loop8 new_file
```

Now open the mounted drive and open `flag.txt`

```
flag{d0_y0u_f33l_luksy?}
```