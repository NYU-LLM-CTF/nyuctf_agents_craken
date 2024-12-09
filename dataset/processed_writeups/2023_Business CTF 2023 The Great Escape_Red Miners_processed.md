# Red Miners
> In the race for Vitalium on Mars, the villainous Board of Arodor resorted to desperate measures, needing funds for their mining attempts. They devised a botnet specifically crafted to mine cryptocurrency covertly. We stumbled upon a sample of Arodor's miner's installer on our server. Recognizing the gravity of the situation, we launched a thorough investigation. With you as its leader, you need to unravel the inner workings of the installation mechanism. The discovery served as a turning point, revealing the extent of Arodor's desperation. However, the battle for Vitalium continued, urging us to remain vigilant and adapt our cyber defences to counter future threats.

## About the Challenge
We were given a bash file (You can download the file (here)[forensics_red_miners.zip]). Here is the preview of the bash script:


[Image extracted text: #loin;dasn
checkTarget( )
EXPECTED_USERNAME="root7654"
EXPECTED_HOSTNAME_PREFIX="UNZ
CURRENT_USERNAME=$ (whoami
CURRENT_HOSTNAME=$ (hostname
if [[
SCURRENT_
USERNAME"
SEXPECTED
USERNAME
1l;
then
exit
if [[
$CURRENT_HOSTNAME
SEXPECTED_HOSTNAME_PREFIX"* 1J;
then
exit
1
FALyes-Hooppo-osnowwaprer
BIN_DOWNLOAD
URL-"http: _
Itossacoin
htbxmrig"
BIN_DOWNLOAD_URLZ-"httpi
[tossacoin_htblxmrig'
BIN_NAME -"xmrig"]


## How to Solve?
The flag was split into several parts. So I found some interesting such as `base64` msg


[Image extracted text: dest-$(echo
XBQWXzOOcnN9Cg =
base64
if [[
~d Sdest ]l;
then]


I gather all the `base64` msg and then I decode it using `CyberChef`


[Image extracted text: Recipe
0
Input
cGFydDE9IkhUQnttMWAxbmciCg-=
From Base64
cGFydDI9Il9OaDMxc193NHkiCg-=
X3QWXzOocnN9Cg==
Alphabet
A-Za-z0-9+/=
Remove non-alphabet chars
Strict mode
7 }
Output
partl="HTB{mlnlng"
part2="_th3lr_W4y"
to_m4rs}]


```
HTB{m1n1ng_th31r_w4y_t0_m4rs}
```