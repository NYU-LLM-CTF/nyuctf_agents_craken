# Matryoshka
> : I think we should have a matryoshka challenge..

> : Sure! Go ahead.

> : Let's make it different this time. HEhe!

> : *-+

## About the Challenge
We were given a txt file containing a base64 encoded message

## How to Solve?
First we need to decode the encoded text with some steps:
* Base64
* Hex
* Decimal
* Hex


[Image extracted text: Recipe
Input
MzcgMzAgMjAgMzcgMzAgMjAgMzMgMz IgMjAgMz YgMzggMjAgMzUgMz YgMj Agl
File details
From Base64
Alphabet
A-Za-z0-9+/=
Remove non-alphabet chars
Strict mode
From Hex
Name:
matryoshka.txt
Size:
24,406,292 bytes
Delimiter
Type:
unknown
Auto
Loaded:
100%
AbC
24406292
F
TT
Raw Bytes
LF
From Decimal
Delimiter
Output
0J
Space
Support signed values
From Hex
Delimiter
Auto
Render Image
Input format
Raw
STEP
BAKEI
Auto Bake
AbC
1121ms
Raw
Bvtes]


And we got an image! Now, I tried to upload the image to Aperisolve and used `foremost` to extract a file inside the image. And we got 3 files here:

* The original image
* Another png file
* A zip file

When I opened the zip file, it turns out this file is useless.


[Image extracted text: [bash-3 .2$
cd
zip/
[bash-3 .2$
1s
00001323
zip
readme
txt
[bash-3.2$
cat
readme
txt
This
text
file
is completely useless _
bash-3 .2$]


And then i tried to analyze the `.png` file, after using `binwalk`, `foremost`, `LSB steganography`, etc. sadly I got nothing here. But when I used `Extract RGBA` options (CyberChef), we got another image again!


[Image extracted text: Recipe
Input
PNGS
Extract RGBA
File details
SUB
NUL
GRIHDR
NUL
NUL
SOH
X
NUL
NUL
SOH
1
STX
NUL
u". U
NUL
SOH
NUL
NUL
IDATx
IA
Delimiter
Include
AtmU mUzcU mUImUIm#
162D
NUL
Rb
b
NUL
NUL
NUL
NUL
NUL
NUL
A
Alpha
NUL
A@@@@@A@@@AAAA
DLE
DLE
PPe
DLE
POdOPDpD
po
POHEH
Ed
NUL
A.AAA
A
DLE
DLE
8s D+D
y3 i~
NUL
D
DLE
NUL
D@ `DAia
NUL
NUL
DLE
@@
EOT
F stx
From Decimal
ACK
SOH
47F
F
EOT
STX
STX
STX
Delimiter
Comma
Support signed values
FFF eor
EOT
cr
NUL
L
STX
'A(
Nda  [
DC4
NUL
QDO-B,
p"to
fHAi
IR
IEU-
Idio7f.
ETX
NUL
uB
DC?
NUL
ayM-A
i
NUL
@@@  AA@AaA@
@A
NUL
@A
Name:
00000653.png
H
E'D. (L
ACK
aA
SOH
ENQ
CR
BY
ETX
+hsij
eA
NUL
0A
'A
NUL
Size:
343,402 bytes
NUL
Odp-.}okdc/
Render Image
Type:
imagelpng
@C
'NQY-WD
)x~
C?
NUL
eXg^Ag~& -
ENQ
gkabaN- 6D `E
EOT
ce
DC2
todi_>YY
100%
Loaded:
Input format
{""bhczan1
STX
nohu
'AiIthRf
0~3
VFFaaca_M
{An
Gks?
SYN k FS
AbC
343402
1214
TT
Raw Bytes
LF
Raw
Output
3
STEP
BAKEI
Auto Bake]


I uploaded the image to Aperisolve and there's a zip archive file inside the image


[Image extracted text: Binwalk
DECIMAL
HEXADECIMAL
DESCRIPTION
Ox0
JPEG image data,
JFIF
standard
1.01
Zip archive data,
at least
V1.0
to
extract,
compressed
size :
5120 ,
338750
0x52B3E
uncompressed
size :
5120 ,
name :
arc.tar.gz
344018
0x53FD2
End
of Zip archive,
footer length:
22
DOWNLOAD FILES]


Inside the zip file, there is a file called `arc.tar.gz` and if you `gunzip` it, you got a compiled binary file


[Image extracted text: [bash-3.2$
file
exec
exec:
ELF
64-bit
LSB pie executable ,
X86-64 ,
version
1 (SYSV) ,
dynamically linked ,
interpreter
Ilib64/ld-linux-x86-64.s0.2 ,
BuildID[ shal]-b971909fb51050afbe423bf2db272c280040371f ,
for
GNU/ Linux
3.2.0,
ot
stripped
bash-3.2$]


Reverse engineer the code and there's a hex code inside of it


[Image extracted text: VZu8
compizer
V200
'input1
2f6c616e672f4f626465637436295a0a001d001e07001f0c00200021010015646176612f7574696c2f436f6c6c656374696f6e7301000773687566666c65010013284c6a6176612f7574696c2f469737436295607
v192
'inputz
cafebabe0000003d008e0a000200030700040c000500060100106a6176612f6c616e672f4f62646563740100063c696e69743e010003282956070008010013646176612f7574696c2f41727261794c6973740a0007
~V184
"input3
"17272617901000428295b4300001100120700130c00140015010013606176612f6c616e672f43686172616374657201000776616c75654f660100182843294c606176612f6c616e672f4368617261637465723b0b0
_V176
"input4
76612f6c616e672f537472696e674275696c6465720a002f00030b002a00330c0034002e01000c6765744f7244656661756c740a001100360c003700380100096368617256616c75650100032829430a002f003a0c
v168
"input5
'f76650100152849294c6a6176612f6c616e672f4f6264656374360b002a002607002c0c002d002e01000d6a6176612f7574696c2f4d6170010003707574010038284c6a6176612f6c616e672f4f6264656374364c6
V160
"input6
4e010011606176612f6c616e672f496e74656765720100087061727365496e74010016284c6a6176612f6c616e672f537472696e673649294908005001001636383664366435663663333437393333373233353566
v152
"input7
73244c6f6f6b757007008c01001e6a6176612f6c616e672f696e766f66652f4d6574686f6448616e646c65730100064c6f6f6b75700021005e0002000000000004000100050006000100740000001d000100010000
v144
'input8
b0a002f003e0c003f0040010008746f537472696e6701001428294c6a6176612f6c616e672f537472696e67360a000600420c004300440100066c656e6774680100032829490a000b00460c0047004801000973756
vV136
'input9
5363937343635376233313566363833340800560100163566363433303663366333353566366533303737356608005801001633303636356636633331363633333566363936373764120000005a0c0056005c01001
v128
'input1o
67364c6a6176612f6c616e672f537472696e67364c6a6176612f6c616e672f537472696e67364c6a6176612f6c616e672f537472696e67364c6a6176612f6c616e672f537472696e6736294c6a6176612f6c616e6
vV120
'input11
"98284c6a6176612f6c616e672f696e766f66652f4d6574686f6448616e646c6573244c6f6f6b7570364c6a6176612f6c616e672f537472696e67364c6a6176612f6c616e672f696e766f6b652f4d6574686f64547
~V112
"input1z
0c005b00620a006f00700700710c00720073010013646176612f696f2f5072696e7453747265616d0100077072696e746c6e010015284c6a6176612f6c616e672f537472696e67362956010004436f646501000f-
vV104
"input13
"96e010016285b4c6a6176612f6c616e672f537472696e6736295601000a536f7572636546696c650100096e6974652e6a617661010010426f6f7473747261704d6574686f64730f06007f0a008000810700820c5
vV96
input14
0c0bb000759b700094cZabbodda4d2cbe3e03360415041da200162c15043436052615056b80010690016020057840401a7ffe52bb8001cbb002259b700244d2ab6o0da4e2dbe360403360515051504a200252d15053
v88
input15
"176612f6c616e672f696e766f66652f43616c6c53697465360800850100050101010101080087010025315f683474335f737472316e675f6d346e3170756c343731306e5f316e5f6a6176613a200101000c496e6e6
v80
input16
a6176612f6c616e672f537472696e6736294c6a6176612f6c616e672f537472696e673b0a005e00640c0065006201000d636f6e76657274537472696e6709006700680700690c006a00660100106a6176612f6c61
_v72
input17
4125734052d2c1904261905ba00590000b8005d3a061906b8006330076200661907ba006c0000b6006eb1000000010075000000260009000000260003002c0006002d0009002e000d002f00110030002200310029
vV64
input18
a00b5001800bb001d00760000004a0006ff0013000507000607001707007701010000f8001dff0017000607000607001707002a07007701010000f80028ff0015000707000b07001707002a07002f0700770101
_v56
'input19
2alc1c0560b600454e2d1010b8004936042615049266003957840202a7ffdc2bb6003db00000000200750000001e00070000002100080022001200230016002400230025002600220031002700760000000-
000
V48
inputzo
041904be360503360615061505a2002f190415063436072c150768001015076800106900320300c0001166003536082d150866003957840601a7ffd02db6003db00000000200750000003e000foo0b00a0008000
V40
print("Do you know what files always start with CAFE
BABE?" ) In
_v32
str
inputz+input3+inputl+inputS+input4+input8+inputb+inputg+inputlO+inputl6+inputlZ+inputl3+inputll+inputlS+input7+inputl4+input2o+inputl8+inputl9+inputl7in
'print(str)In'
FUN_00101020(_v208_
V200)
FUN_00101020(_v208_
V192);
00101o)0
49n0
04
~V24]


Assemble the hex data then insert them into CyberChef and you got a `class` file


[Image extracted text: Recipe
Input
kcafebabe0000003d008e0a000200030700040c000500060100106a6176612f6c616e672f4f626a6563
From Hex
740100063c696e69743e0100032829560700080100136a6176612f7574696c2f41727261794c697374
0a000700030a000b000c07o00d0c00de000f0100106a6176612f6c616e672f537472696e6701000b74
Delimiter
6f436861724172726179010004282956430a001100120700130c001400150100136a6176612f6c616e
Auto
672f43686172616374657201000776616c75654f660100182843294c6a6176612f6c616e672f436861
726163746572360b001700180700190c001a001601000e6a6176612f7574696c2f4c69737401000361
6464010015284c6a6176612f6c616e672f4f626a6563743b295a0a001d001e07001f0c002000210100
156a6176612f7574696c2f436f6c6c656374696f6e7301000773687566666c65010013284c6a617661
2f7574696c2f4c6973743629560700230100116a6176612f7574696c2f486173684d61700a00220003
0b001700260c0027002801000672656d6f76650100152849294c6a6176612f6c616e672f4f626a6563
743b0b002a002b07002c0c002d002e01000d6a6176612f7574696c2f4d617001000370757401003828
4c6a6176612f6c616e672f4f626a6563743b4c6a6176612f6c616e672f4f626a65637436294c6a6176
612f6c616e672f4f626a656374360700300100176a6176612f6c616e672f537472696e674275696c64
65720a002f00030b002a00330c0034002e01000c6765744f7244656661756c740a001100360c003700
30010000236061725616c7565m1mm03282043mamm2fmm3amcmm3hmm3c01mmm6617m7m656p64m1m01
EJava Class file detected
TT
Raw Bytes
Output
0J
Epea
NUL
NUL
NUL
NUL
NUL
STX
ETX
EOT
F
NUL
ERQ
NUL
ACK
SOH
NUL
DLE
java/ lang/Object
SOH
NUL
ACK
<init>
SOH
NUL
ETX
(V
NUL
SOH
NUL
DcJ
java/util/ArrayList
NUL
ETX
NUL
VT
NUL
F
NUL
SRF
NUL
NUL
SOH
NUL
DLE
java/lang/String
SOH
NUL
vtoCharArray
SOH
NUL
EOT
[C
NUL
NUL
DCZ
NUL
DC?
F
NUL
DC4
NUL
NAK
SOH
NUL
DC?
java/ lang/Character
SOH
NUL
valueof
SOH
CAN
(C)Ljava/ Lang/Character;
NUL
ETB
NUL
CAN
BEL
NUL
F
NUL
SUB
NUL
SOH
NUL
javalutil/List
SOH
NUL
ETX
add
SOH
NUL
NAK
(Ljava/ lang/Object;)z
NUL
F
NUL
NUL
SOH
NUL
javalutil/Collections
SOH
NUL
shuffle
SOH
NUL
DcJ
(Ljava/util/List;)V
NUL
#
SOH
NUL
javalutil/HashMap
NUL
NUL
ETX
V_
NUL
NUL
F
NUL
NUL
SOH
NUL
ACK
remove
SOH
NUL
NAX
I)Ljava/ lang/Object
NUL
*
NUL
BEL
NUL
F
NUL
SOH
NUL
CR]


Decompile the file, and you got this java program

```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;

public class nite {
   public static String convertString(String var0) {
      ArrayList var1 = new ArrayList();
      char[] var2 = var0.toCharArray();
      int var3 = var2.length;

      int var4;
      for(var4 = 0; var4 < var3; ++var4) {
         char var5 = var2[var4];
         var1.add(var5);
      }

      Collections.shuffle(var1);
      HashMap var9 = new HashMap();
      char[] var10 = var0.toCharArray();
      var4 = var10.length;

      int var13;
      for(var13 = 0; var13 < var4; ++var13) {
         char var6 = var10[var13];
         var9.put(var6, (Character)var1.remove(0));
      }

      StringBuilder var11 = new StringBuilder();
      char[] var12 = var0.toCharArray();
      var13 = var12.length;

      for(int var14 = 0; var14 < var13; ++var14) {
         char var7 = var12[var14];
         char var8 = (Character)var9.getOrDefault(var7, var7);
         var11.append(var8);
      }

      return var11.toString();
   }

   private static String convert(String var0) {
      StringBuilder var1 = new StringBuilder();

      for(int var2 = 0; var2 < var0.length(); var2 += 2) {
         String var3 = var0.substring(var2, var2 + 2);
         int var4 = Integer.parseInt(var3, 16);
         var1.append((char)var4);
      }

      return var1.toString();
   }

   public static void main(String[] var0) {
      String var1 = "686d6d5f6c34793372355f";
      String var2 = "76335f7734795f3730305f6d346e79";
      String var3 = "6e6974657b315f6834";
      String var4 = "5f64306c6c355f6e30775f";
      String var5 = "30665f6c3166335f69677d";
      String var6 = convert(var3 + var2 + var4 + var1 + var5);
      String var7 = convertString(var6);
      System.out.println("1_h4t3_str1ng_m4n1pul4710n_1n_java: " + var7);
   }
}
```

Remove the `convert()` and `convertString()` command and you got the final hex code


[Image extracted text: Main:java
0.
Run
Output
Clear
38
return
var11.toString();
java
cp
tmp/h7bIPmAIen nite
39
1_h4t3_strIng_m4n1pul471On_In_java:
40
6e6974657b315f683476335f7734795f3730305f6d346e795f64306c6c355f6e30775f686d6d
41
private static String convert(String varo)
{
5f6c34793372355f30665f6c3166335f69677d
42
StringBuilder
var1
new
StringBuilder() ;
43
44
for(int
var2
0;
var2
var0. length() ;
var2
+=
2) {
45
String var3
var0.substring(var2,
var2
+
2) ;
46
int
var4
Integer .parseInt(var3 ,
16) ;
47
var1
append( (char)var4) ;
48
49
50
return
var1
toString();
51
52
53
public static
void main(String[] varo)
{
54
String var1
"686d6d5f6c34793372355f"
55
String var2
"76335f7734795f3730305f6d346e79"_
56
String var3
"6e69746576315f6834" ;
57
String var4
"5f64306c6c355f6e30775f" =
58
String var5
"30665f6c3166335f69677d" ;
59
String var6
var3
var2
var4
var1
var5;]



[Image extracted text: Recipe
Input
Jbe69746576315f683476335f7734795f3730305f6d346e795f64306c6c355f6e30775f686d6d5f6c347
From Hex
93372355f30665f6c3166335f69677d
Delimiter
None
AbC
114
5
TT
Raw Bytes
LF
Output
hite{1_h4v3_W4y_700_m4ny_dOllS_nOw_
hmm_l4y3r5_0f_11f3_ig}]


```
nite{1_h4v3_w4y_700_m4ny_d0ll5_n0w_hmm_l4y3r5_0f_l1f3_ig}
```