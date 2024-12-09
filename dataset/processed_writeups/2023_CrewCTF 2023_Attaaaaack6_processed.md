# Attaaaaack6
> Q6. What is the full path (including executable name) of the hidden executable?

> example : crew{C:\Windows\System32\abc.exe}

## About the Challenge
We got `raw` image and we need to find the location of the hidden executable

## How to Solve?
To solve this, we need to find the list of the file using `filescan` plugin. And then use `grep` command to find `runddl`. Here is the command I used

```
vol.py -f /path/to/memdump.raw --profile=Win7SP1x86_23418 filescan | grep "runddl"
```


[Image extracted text: daffainfo@dapos
dumpdir$
vol.py
~f
/home/daffainfo/forensic/memdump
raw
-profile-Win7SPlx86_23418 filescan
grep "runddl"
Volatility Foundation
Volatility
Framework
2.6.1
0x0000000024534f80
R--r-d
IDevice| HarddiskVolumel |Users|OXSHZR~1 | AppData |Local | Temp| MSDcSCIrunddl32.exe
Ox000000003ea44038
RWD
IDevice| HarddiskVolumel |Users|OXSHZR~1 | AppData |Local | Temp| MSDcSC |runddl32_
exe]


There is another way to solve this chall by using `dlllist` plugin or you can use `strings` and `grep` command to find the location path in the `300.dmp` file


[Image extracted text: daffainfoddapos:
dumpdir$ strings
~el
300
grep
runddl
C:lUsers
OXSH3R~1 | AppData|Local | Temp | MSDcsC| runddl32 . EN . DLL
C:lUsers
OXSH3R~1 | AppDatalLocal | Temp | MSDcSC runddl32
EN . DLL
C:lUsers
OXSHZR~1 | AppData |Local | Temp| MSDcSC|runddl32
EN
C:lUsers
OXSHZR~1 | AppData |Local | Temp| MSDCSC
runddl32
exe
"C:lUsers
OXSHZR~1 | AppData |Local | Temp| MSDCSC
runddl32
exe
C:lUsers
OXSHZR~1 | AppData |Local | Temp| MSDcsC|runddl32
exe
C:lUsers
OXSHZR~1 | AppData |Local | Temp| MSDcsC|runddl32
exe
C:lUsers
OXSHZR~1 | AppData|Local | Temp | MSDCSC| runddl32
exe
runddl32
runddl32
cvCTfMICurrontcontrc]cetlCorvicoe 1dantracing
nundd13)
0v9
dmp]


```
crew{C:\Users\0XSH3R~1\AppData\Local\Temp\MSDCSC\runddl32.exe}
```