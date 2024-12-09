# gaining insight
`kristen@kristenchavis.com` Gain some insight on the target by looking at their resume and maybe you get some flags.

## About the Challenge
We are given an email (kristen@kristenchavis.com) and we need to find a resume

## How to Solve?
One of the team member found the resume in github repository (You can access the resume [here](https://github.com/kristenchavis01/resume/blob/main/resume.tex))


[Image extracted text: Email
Ihref{mailto:kristen@kristenchavis _
com} {mail@website.com} | |
bile
+1
223-994-9882
V I]


And then if we check the commit named `Added profile.jpg` (You can access the commit [here](https://github.com/kristenchavis01/resume/commit/f8545cbb1cfdb244956345e4a1a4d098bce3c59c)). There is a new Overleaf link and we if access that link. We will get a profile photo


[Image extracted text: Menu
Kristen Chavis Resume
Share
Layout
profile-jpg
Recompile
Download
Sofluam' Euginett
Ocl 2016
Aeu
resume.tex
Jensorion:
sorklon
QULM
4T=
~W
library for Qucrical cotputaliou
data llow graphs;
primarily Isexl or training dexp lcaruing mocek:.
Apache Bea:
Apachc: Bc i:
utiliec modlel for delining lxothi mtch ad lreatning dala-parallcl procxssing
pipelincs.
well ;S
scL ol laugunge-~peilic: SDKs for construeting pipelines and
FIMCI
Coursera
Mountain View, CA
OF IUuI-
Sofla"(T' Eulgitutt
2014
Ocl 2016
Notilications: Service for >udling
push ad in-ipp uotificalious   Iuvolvexl iu fcalures such #s delivery tite
oplitnizatio; Lracking
queuitg arcl A/B testing. Built an inlernal app
balch (HAMLA [S
Mirkcliug ec.
Nostos: Bulk
[TOCZL
injection scrvic [rot Hadoop
Cas atra atel provitks
Lhin REST layer On
for srving olllize: €puted dala onlite: .
Workllows: Dataluct
OpCH ~urct: workllow (raucwork
creale #d] [aage data pipxlines keveraging
reusiu
paltcrus Lo
explite teveloper productivily.
Data Collection: Desiguecl te intcrual
surtC
crowd surcing platowI which alloxeal for
creating various
Lask: for crowa sourding
culxxkling surveys
A-m
Lhc: ( ourscra plat[Or:
Dev Environen:
Analytic > envirotcnt bascxl OL dockcr
AWS
stauiarclizex the python ajd R
clepclencic.
Wrota Lhe: cre: libraric: thal arc sharet] by all data scicntists.
Data Warchousing: Sclup; schcta desigu and  [Uagctqt o Amau Rcxlshilt.
Built ;LL intcrual app for
{L
Lhic tlala
web imtcrlace.
Dalacluct integralion for dlaily ETL injection into Rexlshill_
RecOHendations:
for all rxomndalion syStems al COurstSil
LITCMLI
#Sl on Ahc: HOtepage
ncl
LhrougHut Lc COnten discovery
Wrl(
Workexl Ou txth olllitc
training atcl onlize: scrving.
ICTF{NOT_A_FLAG}
Conent Discovery:
[Hprral
COlent ciscovery by
Luildling
MW
onlxxrdling
CCri[L
COUAC
Lhi:
pGrilizc
Lhic *rch auc[
browso
expericne
Also workexl On ranking and inlexing iprOvements
Course Dashboards: Iuslruclor dashlsoaruls
ITIT
surveying Lools
whict helped instructor
ucir class
belter by providling data on Assiguments
L
Activity
Lucena Research
Atlanta. GA
Dala Sciewlisl
Sutntiut 2012 und 2013
Fortlolio ManagCtcnt:
Crealer model: for portlolio hexlging, portlolic plitiztion ad
forecisting- Also
crealing
stralegy backtesting Gginue uscxl for sitnulating
backtesting strategies:
Quant Desk: Eythou backenc for
Wae
applicution
MS
by hetlgc: [Iuudl LI;LIIgCNS
porllolio Iat1ag IICIL .
PROIECTS
QuantSoltware Toolkit: O[X'IL sourCe python library [or linaucial dala analysi:
Qiu-hine Icaruiug for fitancx:
Github Visualization: Data Visualization ol Gil
data using D%
ALIMLIYZC
ruk
[rMl
over lic.
Recommendation Systet: Music: and Movic re(xenaler systeIs
collaborative: liltering
pubslic: datasts.
PROGRAMMING SKILLS
Languages: Scala; Python_
JJavascript.
C++. SQL, JJava
Technologies: AWS
Play. React .
Kafka, GCE
File outline
LaTeX help
Ig
VELJ
Ual
Wp'
Iiug
Cor
~rvit
Uxlug "
prica
adl
Lo8
Wing]


Download the profile picture first and then doing bruteforce steganography on the picture that we have download earlier (In this case im using [stegseek](https://github.com/RickdeJager/stegseek))


[Image extracted text: (kaliokali)-[~]
stegseek Desktop/profile|
I(11). jpg /usr/share/wordlists/rockyou
txt
StegSeek
0.6
https: //github
com/ Rie
ckdeJager/StegSeek
[1]
Found passphrase:
prettywoman
[i] Original filename
'flag.txt
[i] Extracting
profile (1) . Jpg.out"]


If we open the result of stegseek, we will retrieve the flag

```
ictf{av01d_th3_z1p_b0mb_87ad2th}
```