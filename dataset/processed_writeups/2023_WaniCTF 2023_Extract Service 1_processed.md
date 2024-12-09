# Extract Service 1
> We have released a summary service for document files! Please feel free to use the sample document file in the "sample" folder of the distribution file for trial purposes.

> The secret information is written in the /flag file on the server, but it should be safe, right...? Let's see what kind of HTTP request is sent!

## About the Challenge
We were given a website and a source code (You can download the file [here](web-extract1.zip)). This website can read the docx, xlsx, and pptx files that we have uploaded


[Image extracted text: Extract Service
Choose file
Choose file.
No file uploaded
Choose file type
docx
Submit]


## How to Solve?
If you check the source code especially on `main.go` file, there is a function called `ExtractContent` where this function can read any file by using `os.ReadFile` function

```go
func ExtractContent(baseDir, extractTarget string) (string, error) {
	raw, err := os.ReadFile(filepath.Join(baseDir, extractTarget))
	if err != nil {
		return "", err
	}

	removeXmlTag := regexp.MustCompile("<.*?>")
	resultXmlTagRemoved := removeXmlTag.ReplaceAllString(string(raw), "")
	removeNewLine := regexp.MustCompile(`\r?\n`)
	resultNewLineRemoved := removeNewLine.ReplaceAllString(resultXmlTagRemoved, "")
	return resultNewLineRemoved, nil
}
```

And because of there is no filter in the `extractTarget` variable (You can check this in line 38 - 44)

```go
		extractTarget := c.PostForm("target")
		if extractTarget == "" {
			c.HTML(http.StatusOK, "index.html", gin.H{
				"result": "Error : target is required",
			})
			return
		}
```

This website is vulnerable to directory traversal attack. To obtain the flag we need to change the value of the `target` parameter to `../../../../../../flag`


[Image extracted text: {Va"Y{Vu' g7AEO,jodo,jodo,JEij hoaj poaj hoaed'{1j poej pavsezjr5
<bucton type
subnic
class
'bucton
is-link
0zjrS02]
5o2r"U-h"U-p"U-1J0 O0
dad0
0<o
0adpOBUr
DEUE
DEUE* ED < ]
Subnit
7eDuloylu?DalOn
</button>
lxzQeap'nu+igios;
ode'
'#Fi
uaz"1o+i
zkWoa*del-u(-YOl) "10
divz
gzon"yo: "OUHAtijo[U_jj jy:
div?
Si8 OOuOd ( SyifH: peHf  De@o:Oxjv7EE
eBifbFad {TqluuQU; UcES3]-1OITY
</formj
~/sc
chnAry271uloz7eInaL
6 2 SOUAO-EX-OIS AIDS ;Lr &: @EDhOzUZG
Gect
on>
+0-uzmhaffo
ca[it3eqevoCe"lerka-l
oxE ; upOCnS+-G10E/*exoio<faU-0
section
class=
container Px-5
ODONuIL-NAp '1ica
(Di P]oaerO;66201-r5
oUepbx_beaboDzo
6i-yue? ~u
<div
class
Jnt _
99+0
DF dvaoylo_LYYyPE !ptx
docProps / app
Xl
DPID: IrudiDu [ POUHQJYOzEil !Dcyhi<eDPOOI ( EO
~QAadelt}h-BefHFhAUD
FLAG (ex7r427_15
br Ok: 3n_by_b4d_P41 4n 38 3rs}
Ood[+0_pO01t;-AgcHuno}: 0+10" ORONTI
EVD
<(p=
WoouVDj }ilYewVz4Dei
cxDh"teONq~DyUV^U] tvanco-j""y" @Nec-G;
Qesi
<fdiv>
Dg--EdooDui
L0?51"
70
~section>
OnaBFZ
IDo047 (YOgNo "DIEti]ADY" 'pouzBAF
DIJI; >
elil-"21
UD]Ja Du' +H-TIHoDI-0ol (-*oOxalou_DcD
71
<script>
jil
BOUu_DOgOD"P[iyyYyPK-!BROIZ
const
fileInput
docuhent
querySelector
[Content_
Types]
xnlPE-!0
1l10_rels/
relsPr-
Od'Qol uord/
rels/doc
ffile-Js-
example
input [twpezfile]
luenc
xll- relsPK-!I Joyoevord/docuent
XhlPK - !U301U<
fileInput . onchange
word/thene/thenel
xnlPK -
40*1
u;word/settings
rElPI =
ell (udocPro
75
1f
fileInput
files-length
ps /core
PF -
/OSuord/ fontTable
xhlPF- !i
76
const
file]ale
docuent
querySelector
IT~
ffile-Js-erample
file-nane
word/vebSettings
xhLPE- !bE ) >BuD
word/styles
XhlPK - !px
Dn-docPr
fil-lane
ercContent
fileInput
files[0]
nane
ops / app
xnlPEADO
78
28657062493776496405402089583
79
Content
osit
on:
forn-daca;
nae
arget
script>
</body>
/flag
28657062493776496405402089583-_
htnl>
Szorcni
matches
Seorcn 
0 matche
Done
(72:
IDEi
xhl
Disp]


```
FLAG{ex7r4c7_1s_br0k3n_by_b4d_p4r4m3t3rs}
```