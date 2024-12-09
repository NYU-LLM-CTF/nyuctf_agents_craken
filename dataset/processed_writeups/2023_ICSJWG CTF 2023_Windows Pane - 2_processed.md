# Windows Pane - 2
> Due to this logon behavior, Jubilife would like to perform additional forensics on Abigail's machine. The attached prefetch data was extracted from their machine and Jubilife would like your assistance to find any evidence of a malicious executable.

> What is the full directory path of the malicious backdoor executable?

> Flag format: full directory path of malicious executable. Example: C:\Users\User\Desktop\Path.exe

> Note: A Windows machine or Windows VM is recommended for solving this challenge.

## About the Challenge
We were given a zip file that contains prefetch files (You can download the file [here](Prefetch.zip)). We need to find the full directory path of malicious executable 

## How to Solve?
Unzip the zip file first, and you will see a lot of prefetch files. But there is 1 file called `B@CKD00R.EXE-7CB4E6DE.pf` that has caught my attention

So to parse the `pf` file, you can use [PECmd](https://github.com/EricZimmerman/PECmd) tools or `Prefetch Explorer Command Line`. And here is the command I used to parse the `B@CKD00R.EXE-7CB4E6DE.pf`

```
.\PECmd.exe -f '\Prefetch\Prefetch\B@CKD00R.EXE-7CB4E6DE.pf'
```


[Image extracted text: 08
IVOLUME{01d926fadbedfla6-68dc08d5}
WINDOWS | SYSTEM32
WOW64CON
DLL
09
IVOLUME{01d926fadbedfla6-68dc08d5}
WINDOWS | SYSTEM32 | KERNEL32
DLL
10
IVOLUME{01d926fadbedfla6-68dc08d5}
WINDOWS | SYSWOW64
KERNEL32
DLL
11
IVOLUME{01d926fadbedfla6-68dc08d5}
WINDOWS"
SYSTEM32 |USER32
DLL
12
IVOLUME{01d926fadbedfla6-68dc08d5}
WINDOWS | SYSTEM32
WOW64CPU . DLL
13
IVOLUME{01d926fadbedfla6-68dc08d5}
WINDOWS | SYSWOW64
NTDLL
DLL
14
IVOLUME{01d926fadbedfla6-68dc08d5}
WINDOWS | SYSWOW64 | KERNELBASE
DLL
15
IVOLUME{01d926fadbedfla6-68dc08d5}
WINDOWS"
SYSTEM32ILOCALE
NLS
16
IVOLUME {01d926fadbedfla6-68dc08d5} | USERS |ABIGAIL_FORBES | DESKTOP | SECRETI B@CKDOOR. EXE (Executable
True)
17
IVOLUME{01d926fadbedfla6-68dc08d5}
WINDOWS | SYSWON64 | MSVCRT
DLL
18
IVOLUME{01d926fadbedfla6-68dc08d5}
WINDOWS | SYSWOW64 | ADVAPI32
DLL
19
IVOLUME{01d926fadbedfla6-68dc08d5}
WINDOWS
SYSWOW64
SECHOST
DLL
20
IVOLUME{01d926fadbedfla6-68dc08d5}
WINDOWS | SYSWOW64
RPCRT4
DLL
21
IVOLUME{01d926fadbedfla6-68dc08d5}
WINDOWS
SYSWOW64
WS2_32
DLL
22
IVOLUME{01d926fadbedfla6-68dc08d5}
WINDOWS'
SYSWOW64
WSOCK32
DLL
A
T
An
Ini]


As you can see in the result of the tool, there was location of malicious executable

```
\VOLUME{01d926fadbedf1a6-68dc08d5}\USERS\ABIGAIL_FORBES\DESKTOP\SECRET\B@CKD00R.EXE
```