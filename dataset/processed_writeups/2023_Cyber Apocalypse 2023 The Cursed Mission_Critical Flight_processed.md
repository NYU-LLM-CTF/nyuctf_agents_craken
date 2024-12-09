# Critical Flight
> Your team has assigned you to a mission to investigate the production files of Printed Circuit Boards for irregularities. This is in response to the deployment of nonfunctional DIY drones that keep falling out of the sky. The team had used a slightly modified version of an open-source flight controller in order to save time, but it appears that someone had sabotaged the design before production. Can you help identify any suspicious alterations made to the boards?

## About the Challenge
We were given a zip file and if we extract the file, we will see 13 files with `gbr` extension


[Image extracted text: Vame
HadesMicro-B_Cu.gbr
HadesMicro-B
rab,gor
HadesMicro-B_Maskgbr
HadesMicro-B_Paste gbr
HadesMicro-B_Silkscreen gbr
HadesMicro-Edge_Cutsgbr
HadesMicro-=
Cu.gbr
HadesMicro-=
Fab gbr
HadesMicro-=
Maskgbr
HadesMicro -
Paste.gbr
HadesMicro-=
Silkscreen gbr
HadesMicro-In1_Cu.gbr
HadesMicro-In2_Cu.gbr]


## How to Solve?
To solve this chall, I'm using [Gerber Viewer Online](https://www.pcbway.com/project/OnlineGerberViewer.html) and upload all with `gbr` extension files there.


[Image extracted text: Gerber view
HadesMicro-
layers
bottom
top
0
QDJ
@D
copper
HadesMicro-F
Cu.gbr
soldermask
HadesMicro-F_Mask.gbr
silkscreen
HadesMicro-F_Silkscreen.gbr
0
solderpaste
HadesMicro-F_Paste.gbr
bottom
copper
HadesMicro-B_
Cu.gbr
soldermask
HadesMicro-B_Mask.gbr
|
silkscreen
HadesMicro-B_Silkscreen.gbr
solderpaste
HadesMicro-B_Paste.gbr
L0f_313c720n1c5#S0}
inner
copper
HadesMicro-Inl
Cu.gbr
9
copper
HadesMicro-In2
Cu.gbr
8
mechanical
Hide filenames
hanks to Mike
ousins tor
COE
great]


You can see the flags in the `HadesMicro-B_Cu.gbr` and `HadesMicro-In1_Cu.gbr` files

```
HTB{533_7h3_1nn32_w02k1n95_0f_313c720n1c5#$@}
```