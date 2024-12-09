# Attaaaaack3
> Q3. i think the user left note on the machine. can you find it ?

> flag format : crew{}

## About the Challenge
We got `raw` image and we need to find the note

## How to Solve?
To solve this, we need to find the note using `clipboard` plugin. Here is the command I used

```
vol.py -f /path/to/memdump.raw --profile=Win7SP1x86_23418 clipboard
```


[Image extracted text: daffainfo@dapos
$
vol .py
~f
/home/daffainfolforensic/memdump
raw
~profile-Win7SP1x86_23418 clipboard
Volatility
Foundation Volatility
Framework
2.6
Session
WindowStation
Format
Handle Object
Data
1 WinStao
CF
UNICODETEXT
OxaO0d9 Oxfe897838 1_LOv3_M3mOry_FOr3nslcs_SO_muchhhhhhhhh
1 WinStao
OxOL
Oxlo
1 WinStao
Ox2OOOL
Oxo
1 WinStao
OxOL
Ox3000
Oxla02a9 Oxfe670a68
Ox100067
Oxffbab4u8]


Or if you check the the list of the process using `pslist`, you will see there is a notepad process (PID: 2556). Dump it using `memdump` plugin and then set the pid to 300. Here is the command I used to dump the notepad memory

```
vol.py -f /home/daffainfo/forensic/memdump.raw --profile=Win7SP1x86_23418 memdump -p 300 --dump-dir .
```

And then because the format of the flag usually like this `this_is_random_text`. So I tried to grep the string that have a lot of underscore character, here is the command I used to grep the flag

```
strings -e l 2556.dmp | grep -E "(.*?)_(.*?)_"
```


[Image extracted text: ##"!%$' '82)(++*)-,//.-10332154776598;
9-<??>-AQCCBAEL
040515ADSREV
00
PCII VEN_1SADSDEV
O405GSUBSYS_
040515ADSREV
TERMINAL
CII VEN_1SADSDEV_
04058CC_0300
DEV_
04058CC_
030000
PCII VEN_
15ADGDEV
04058CC_0300
1_lOv3_M3mOry_FOr3nslcs_SO_muchhhhhhhhh
EN_1SADGDEV_04058CC_
0300
1??1HID#VID_OEOFGPID
OOO3GMI_
00#88167f267s080000# {378del
1?2| IDE#CdRomNECVMWar_VMware_SATA_CDO1_
1
22 Uto#vtd
OforCdtD
Ooocmt
01#8go)6fuk56Gogoooot{278d6]


```
crew{1_l0v3_M3m0ry_F0r3ns1cs_S0_muchhhhhhhhh}
```