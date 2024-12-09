# The Path to Victory
> A elite team of marine biologists have been working to genetically modify mantis shrimp into the ultimate killing machines. Your mission is to exploit vulnerabilities in the enemies website and retrieve session keys (the flag) in order to help bring the organization down.

## About the Challenge
We were given a simple website that contains an information about shrimp


[Image extracted text: < >
C
Not secure
18.216.238.24.1003/webpageffiles/dir/indexhtml
1 * & * = d
HOME
INFO
CONTACT
18.216.238.24.1003/webpageffiles/dirfindex html#
1 ^ NITIC
CiIDI ^D]


## How to Solve?
If you see the URL in the preview (http://18.216.238.24:1003/webpage/files/dir/index.html) you will notice this website have a lot of directories right? So to find useful information, I tried to access http://18.216.238.24:1003/webpage/


[Image extracted text: 6 7
Not secure
18.216.238.24.1003/webpage/
Index of /webpagel
filesL
12-Apr-2023
00:38
session
keys_txt
12-Apr-2023
00:37]


There is a file called `sessions_keys.txt`. Open that file to obtain the flag


[Image extracted text: 2 >
C
Not secure
18.216.238.24.1003/webpage/session_keystxt
texsaw{Th3
B3s7_Cru574c34n}]


```
texsaw{Th3_B3s7_Cru574c34n}
```